from html.parser import HTMLParser

class SectionParser(HTMLParser):
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
            # We associate the text with its parent tags hierarchy
            self.texts.append(("/".join(self.tag_stack), cleaned))

parser = SectionParser()
html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    parser.feed(f.read())

# Let's print the first 250 text items
print("=== FIRST 250 TEXTS IN DOCX ===")
for i, (path, text) in enumerate(parser.texts[:250]):
    print(f"{i:3d}: [{path}] -> {text}")
