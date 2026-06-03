# Let's inspect rows 1 to 24 of AAA-pregrado table to see where the deliverables summary is
from html.parser import HTMLParser

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.rows = []
        self.current_row = []
        self.current_cell = []

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.in_table = True
        elif tag == 'tr':
            self.current_row = []
        elif tag in ['td', 'th']:
            self.current_cell = []

    def handle_endtag(self, tag):
        if tag == 'table':
            self.in_table = False
        elif tag == 'tr':
            self.rows.append(self.current_row)
        elif tag in ['td', 'th']:
            text = " ".join("".join(self.current_cell).split())
            self.current_row.append(text)

    def handle_data(self, data):
        if self.in_table:
            self.current_cell.append(data)

parser = TableParser()
html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    parser.feed(f.read())

print("=== INSPECTING FIRST 25 ROWS ===")
for idx, r in enumerate(parser.rows[:25]):
    print(f"Row {idx:2d}: {r}")
