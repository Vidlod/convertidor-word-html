import json

# Let's read from the parsed rows directly
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

with open("/Users/buc-cvudes-medios1/Documents/GEO/scratch/weeks_extracted_content.txt", "w", encoding="utf-8") as f:
    for idx, r in enumerate(parser.rows):
        if len(r) > 0:
            first = r[0].strip()
            if first.isdigit() or first.startswith("Semana") or "CIERRE" in first:
                f.write(f"=========================================\n")
                f.write(f"ROW {idx} - FIRST COL (WEEK): {first}\n")
                f.write(f"=========================================\n")
                for col_idx, col in enumerate(r):
                    f.write(f"Col {col_idx}:\n{col}\n\n")

print("Dumped weeks text to scratch/weeks_extracted_content.txt")
