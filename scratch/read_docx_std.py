from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current_tag = None
        self.texts = []

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag

    def handle_endtag(self, tag):
        if tag == self.current_tag:
            self.current_tag = None

    def handle_data(self, data):
        if self.current_tag in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'td', 'th']:
            text = " ".join(data.split())
            if text and not text.startswith("data:image"):
                self.texts.append((self.current_tag, text))

parser = MyHTMLParser()
html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    parser.feed(f.read())

print("=== DOCX TEXT ELEMENTS ===")
for tag, text in parser.texts:
    if len(text) > 200:
        print(f"[{tag}]: {text[:200]}...")
    else:
        print(f"[{tag}]: {text}")
