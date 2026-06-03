import re
from html.parser import HTMLParser

class WeekParser(HTMLParser):
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

parser = WeekParser()
html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    parser.feed(f.read())

print("=== SEARCHING WEEKS IN DOCX TEXT ===")
# Let's find occurrences of weeks
for idx, text in enumerate(parser.texts):
    # If text is a number 1 to 12
    # in the AAA table, the first column might just be the week number
    if text in [str(i) for i in range(1, 13)] or "Semana" in text:
        # Print this text and the next 5 text elements
        print(f"\n--- MATCH AT INDEX {idx}: {text} ---")
        for j in range(max(0, idx - 1), min(len(parser.texts), idx + 8)):
            prefix = ">>> " if j == idx else "    "
            print(f"{prefix}{j:3d}: {parser.texts[j]}")
