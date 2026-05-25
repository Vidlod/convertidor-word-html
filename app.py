import os
import re
import sys
import io
import mammoth
from flask import Flask, render_template, request, jsonify
from html.parser import HTMLParser

app = Flask(__name__)

# Note: We no longer need app.config['UPLOAD_FOLDER'] or os.makedirs because we process files 100% in-memory!

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
                "inner_html": inner_html
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
        
    if file and file.filename.endswith('.docx'):
        try:
            # Process the file completely in-memory using io.BytesIO
            file_bytes = file.read()
            docx_file_in_memory = io.BytesIO(file_bytes)
            
            # Convert DOCX to raw HTML
            result = mammoth.convert_to_html(docx_file_in_memory)
            raw_html = result.value
            
            # Segment HTML into blocks
            parser = BlockSegmenter()
            parser.feed(raw_html)
            blocks = parser.blocks
            
            # Clean up: format raw_html and inner_html for each block
            for block in blocks:
                block['html'] = format_html(block['html'])
                if block['inner_html']:
                    block['inner_html'] = format_html(block['inner_html'])
                    
            return jsonify({
                "filename": file.filename,
                "blocks": blocks,
                "warnings": [msg.message for msg in result.messages]
            })
        except Exception as e:
            return jsonify({"error": f"Fallo al procesar el archivo Word: {str(e)}"}), 500
    else:
        return jsonify({"error": "Tipo de archivo no permitido. Debe ser un archivo .docx"}), 400

if __name__ == '__main__':
    # Running locally on http://localhost:5000
    print("Iniciando servidor Flask local...")
    app.run(host='127.0.0.1', port=5000, debug=True)
