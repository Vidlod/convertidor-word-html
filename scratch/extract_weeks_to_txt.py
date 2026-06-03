import re
from html.parser import HTMLParser

class Extractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.output = []
        self.current_tag = None
        self.tag_stack = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        self.current_tag = tag
        if tag in ['p', 'tr', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.output.append(f"<{tag}>")

    def handle_endtag(self, tag):
        if self.tag_stack:
            self.tag_stack.pop()
        self.current_tag = self.tag_stack[-1] if self.tag_stack else None
        if tag in ['p', 'tr', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.output.append(f"</{tag}>\n")

    def handle_data(self, data):
        cleaned = " ".join(data.split()).strip()
        if cleaned:
            self.output.append(data)

html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

parser = Extractor()
parser.feed(html_content)

out_text = "".join(parser.output)
# clean some spaces
out_text = re.sub(r' +', ' ', out_text)

with open("/Users/buc-cvudes-medios1/Documents/GEO/scratch/extracted_weeks_text.txt", "w", encoding="utf-8") as f:
    f.write(out_text)

print("Extraction completed. File size:", len(out_text))
