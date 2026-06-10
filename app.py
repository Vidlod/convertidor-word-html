import os
import re
import sys
import io
import mammoth
import pymupdf4llm
import pypandoc
import markdown
from flask import Flask, render_template, request, jsonify
from html.parser import HTMLParser

app = Flask(__name__)

# Ensure pandoc is installed via pypandoc
try:
    pypandoc.ensure_pandoc_installed()
except Exception as e:
    print(f"Advertencia: No se pudo verificar o instalar Pandoc automáticamente: {e}", file=sys.stderr)

class BlockSegmenter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.current_tag = None
        self.current_attrs = []
        self.depth = 0
        self.current_block_html = []
        self.current_block_text = []

    def handle_starttag(self, tag, attrs):
        if self.depth == 0:
            self.current_tag = tag
            self.current_attrs = attrs
            self.current_block_html = []
            self.current_block_text = []
            
        attr_str = "".join(f' {k}="{v}"' for k, v in attrs)
        self.current_block_html.append(f"<{tag}{attr_str}>")
        self.depth += 1

    def handle_endtag(self, tag):
        self.depth -= 1
        self.current_block_html.append(f"</{tag}>")
        
        if self.depth == 0:
            html_content = "".join(self.current_block_html)
            text_content = " ".join(self.current_block_text).strip()
            
            # Determine tag category
            block_type = "párrafo"
            if self.current_tag in ['ul', 'ol']:
                block_type = "lista"
            elif self.current_tag == 'table':
                block_type = "tabla/cuadro"
            elif self.current_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                block_type = f"título ({self.current_tag.upper()})"
                
            # If it's a table (often used for boxes), extract inner td content
            inner_html = ""
            if self.current_tag == 'table':
                inner_html = self.extract_table_contents(html_content)
                
            self.blocks.append({
                "type": block_type,
                "html": html_content,
                "text": text_content,
                "inner_html": inner_html,
                "markdown": ""
            })
            self.current_tag = None

    def handle_data(self, data):
        if self.depth > 0:
            self.current_block_html.append(data)
            # Only append meaningful text
            stripped_data = data.strip()
            if stripped_data:
                self.current_block_text.append(stripped_data)

    def extract_table_contents(self, table_html):
        # Extract text/paragraphs from inside all cells <td>...</td>
        cells = re.findall(r'<td[^>]*>(.*?)</td>', table_html, re.DOTALL)
        return "\n".join(cells).strip()

def format_html(html_str):
    # Standardize spaces and newlines around block tags
    html_str = re.sub(r'</p>\s*<p>', '</p>\n<p>', html_str)
    html_str = re.sub(r'</p>\s*<ul', '</p>\n<ul', html_str)
    html_str = re.sub(r'</p>\s*<ol', '</p>\n<ol', html_str)
    html_str = re.sub(r'</ul>\s*<p>', '</ul>\n<p>', html_str)
    html_str = re.sub(r'</ol>\s*<p>', '</ol>\n<p>', html_str)
    html_str = re.sub(r'</ul>\s*<ul', '</ul>\n<ul', html_str)
    html_str = re.sub(r'</ol>\s*<ol', '</ol>\n<ol', html_str)
    
    # Put newlines around ul and ol tags
    html_str = re.sub(r'<ul([^>]*)>', r'\n<ul\1>\n', html_str)
    html_str = re.sub(r'</ul>', r'\n</ul>\n', html_str)
    html_str = re.sub(r'<ol([^>]*)>', r'\n<ol\1>\n', html_str)
    html_str = re.sub(r'</ol>', r'\n</ol>\n', html_str)
    
    # Add newlines after closing list items
    html_str = re.sub(r'</li>', r'</li>\n', html_str)
    
    # Handle nested lists inside list items: separate the text from the sub-list
    html_str = re.sub(r'(<li>.*?)(<ul|<ol)', r'\1\n\2', html_str)
    
    # Clean up empty lines and strip spacing
    lines = []
    for line in html_str.split('\n'):
        stripped = line.strip()
        if stripped:
            lines.append(stripped)
            
    # Build the indented result
    result = []
    indent_level = 0
    indent_char = "    " # 4 spaces
    
    for line in lines:
        if line.startswith('</ul>') or line.startswith('</ol>') or line == '</li>':
            indent_level = max(0, indent_level - 1)
            
        result.append((indent_char * indent_level) + line)
        
        if line.startswith('<ul') or line.startswith('<ol>') or (line.startswith('<li>') and not line.endswith('</li>')):
            indent_level += 1
            
    return '\n'.join(result)

def segment_markdown_to_blocks(md_text):
    # Standardize newlines
    md_text = md_text.replace('\r\n', '\n')
    
    # Pre-split by double newlines
    raw_parts = md_text.split('\n\n')
    blocks = []
    
    def is_list_line(l):
        l_strip = l.strip()
        return bool(re.match(r'^[-*+]\s+', l_strip)) or bool(re.match(r'^\d+\.\s+', l_strip))
        
    for part in raw_parts:
        part_text = part.strip()
        if not part_text:
            continue
            
        # If a block starts with a header but contains more lines, split the header from the rest
        lines = part_text.split('\n')
        if lines[0].strip().startswith('#') and len(lines) > 1:
            header_line = lines[0]
            rest = '\n'.join(lines[1:])
            blocks.append((header_line, "título (H" + str(len(re.match(r'^(#+)', header_line.strip()).group(1))) + ")"))
            part_text = rest.strip()
            lines = part_text.split('\n')
            
        first_line = lines[0].strip()
        if first_line.startswith('#'):
            h_match = re.match(r'^(#+)', first_line)
            level = len(h_match.group(1)) if h_match else 1
            blocks.append((part_text, f"título (H{level})"))
        elif first_line.startswith('|') or (len(lines) > 1 and lines[1].strip().startswith('|')):
            blocks.append((part_text, "tabla/cuadro"))
        elif is_list_line(first_line):
            blocks.append((part_text, "lista"))
        else:
            blocks.append((part_text, "párrafo"))
            
    segmented_blocks = []
    for block_md, block_type in blocks:
        # Convert markdown block to HTML (with tables support)
        block_html = markdown.markdown(block_md, extensions=['extra', 'tables'])
        
        # Clean text
        clean_text_lines = []
        for line in block_html.split('\n'):
            line_clean = re.sub(r'<[^>]*>', '', line).strip()
            if line_clean:
                clean_text_lines.append(line_clean)
        clean_text = ' '.join(clean_text_lines)
        
        segmented_blocks.append({
            "type": block_type,
            "html": block_html,
            "text": clean_text or block_md,
            "markdown": block_md,
            "inner_html": ""
        })
        
    return segmented_blocks

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No se subió ningún archivo"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Nombre de archivo no válido"}), 400
        
    engine = request.form.get('engine', 'mammoth') # 'mammoth', 'pandoc' or 'pymupdf4llm'
    filename = file.filename
    ext = os.path.splitext(filename)[1].lower()
    
    if ext == '.pdf':
        engine = 'pymupdf4llm'
    elif ext == '.docx':
        if engine not in ['mammoth', 'pandoc']:
            engine = 'mammoth'
    else:
        return jsonify({"error": "Tipo de archivo no permitido. Debe ser .docx o .pdf"}), 400

    if engine == 'mammoth':
        try:
            file_bytes = file.read()
            docx_file_in_memory = io.BytesIO(file_bytes)
            
            result = mammoth.convert_to_html(docx_file_in_memory)
            raw_html = result.value
            
            parser = BlockSegmenter()
            parser.feed(raw_html)
            blocks = parser.blocks
            
            for block in blocks:
                block['html'] = format_html(block['html'])
                if block['inner_html']:
                    block['inner_html'] = format_html(block['inner_html'])
                block['markdown'] = ""
                
            return jsonify({
                "filename": filename,
                "engine": engine,
                "blocks": blocks,
                "warnings": [msg.message for msg in result.messages]
            })
        except Exception as e:
            return jsonify({"error": f"Fallo al procesar con Mammoth: {str(e)}"}), 500
    else:
        # Pandoc or PyMuPDF4LLM
        upload_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
        os.makedirs(upload_dir, exist_ok=True)
        temp_path = os.path.join(upload_dir, filename)
        
        try:
            file.save(temp_path)
            
            if engine == 'pandoc':
                md_content = pypandoc.convert_file(temp_path, 'markdown')
            else:
                md_content = pymupdf4llm.to_markdown(temp_path)
                
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
            blocks = segment_markdown_to_blocks(md_content)
            
            for block in blocks:
                block['html'] = format_html(block['html'])
                
            return jsonify({
                "filename": filename,
                "engine": engine,
                "blocks": blocks,
                "warnings": []
            })
        except Exception as e:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return jsonify({"error": f"Fallo al procesar con {engine}: {str(e)}"}), 500

if __name__ == '__main__':
    print("Iniciando servidor Flask local...")
    app.run(host='127.0.0.1', port=5000, debug=True)

