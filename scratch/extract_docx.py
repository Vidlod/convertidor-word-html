import os
import re
import html.parser
import mammoth

class HTMLToText(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    def handle_starttag(self, tag, attrs):
        if tag in ['p', 'tr', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'br']:
            self.text.append('\n')
        elif tag == 'td':
            self.text.append(' | ')
    def handle_endtag(self, tag):
        if tag in ['p', 'tr', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']:
            self.text.append('\n')
    def handle_data(self, data):
        self.text.append(data)
    def get_text(self):
        return ''.join(self.text)

def extract_docx_to_text(docx_path, output_txt_path):
    print(f"Extracting {docx_path}...")
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html_content = result.value
        
    parser = HTMLToText()
    parser.feed(html_content)
    text = parser.get_text()
    
    lines = []
    for line in text.split('\n'):
        l = line.strip()
        if l:
            lines.append(l)
    clean_text = '\n'.join(lines)
    
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(clean_text)
    print(f"Saved to {output_txt_path}")

if __name__ == '__main__':
    word_dir = "PLANTILLA_CURSO/1_insumos_origen/documentos_word"
    scratch_dir = "scratch"
    os.makedirs(scratch_dir, exist_ok=True)
    
    for filename in os.listdir(word_dir):
        if filename.endswith(".docx"):
            docx_path = os.path.join(word_dir, filename)
            txt_filename = filename.replace(".docx", "_text.txt")
            txt_path = os.path.join(scratch_dir, txt_filename)
            extract_docx_to_text(docx_path, txt_path)
