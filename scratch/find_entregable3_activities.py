from html.parser import HTMLParser

class ActivityParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = []
        self.current_tag = None
        self.tag_stack = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        self.current_tag = tag

    def handle_endtag(self, tag):
        if self.tag_stack:
            self.tag_stack.pop()
        self.current_tag = self.tag_stack[-1] if self.tag_stack else None

    def handle_data(self, data):
        cleaned = " ".join(data.split()).strip()
        if cleaned and self.current_tag in ['p', 'td', 'th', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.texts.append(cleaned)

parser = ActivityParser()
html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    parser.feed(f.read())

print("=== SEARCHING ENTREGABLE 3 CONTENT ===")
for idx, text in enumerate(parser.texts):
    if "entregable 3" in text.lower():
        # Print next 40 elements
        print(f"Found Entregable 3 at index {idx}: {text}")
        for j in range(idx, min(len(parser.texts), idx + 50)):
            print(f"  {j:3d}: {parser.texts[j]}")
        break
