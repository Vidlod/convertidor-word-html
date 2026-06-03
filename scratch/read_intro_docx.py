from html.parser import HTMLParser

class EarlyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = []
        self.tag_stack = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)

    def handle_endtag(self, tag):
        if self.tag_stack:
            self.tag_stack.pop()

    def handle_data(self, data):
        cleaned = " ".join(data.split())
        if cleaned:
            self.texts.append(("/".join(self.tag_stack), cleaned))

parser = EarlyParser()
html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    parser.feed(f.read())

print("=== DOCX TEXTS 0 - 80 ===")
for i in range(min(80, len(parser.texts))):
    path, text = parser.texts[i]
    if not text.startswith("data:image"):
        print(f"{i:2d}: [{path}] -> {text}")
