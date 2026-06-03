import re
from html.parser import HTMLParser

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_cell = False
        self.cell_tags = []
        self.rows = []
        self.current_row = []
        self.current_cell_content = []

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.in_table = True
        elif tag == 'tr' and self.in_table:
            self.current_row = []
        elif tag in ['td', 'th'] and self.in_table:
            self.in_cell = True
            self.current_cell_content = []
            self.cell_tags = [tag]
        elif self.in_cell:
            self.cell_tags.append(tag)
            attr_str = "".join([f' {k}="{v}"' for k, v in attrs])
            self.current_cell_content.append(f"<{tag}{attr_str}>")

    def handle_endtag(self, tag):
        if tag == 'table':
            self.in_table = False
        elif tag == 'tr' and self.in_table:
            self.rows.append(self.current_row)
        elif tag in ['td', 'th'] and self.in_table and self.in_cell:
            if self.cell_tags and self.cell_tags[-1] == tag:
                self.cell_tags.pop()
                if not self.cell_tags:
                    self.in_cell = False
                    cell_html = "".join(self.current_cell_content)
                    self.current_row.append(cell_html)
            else:
                self.current_cell_content.append(f"</{tag}>")
        elif self.in_cell:
            if self.cell_tags and self.cell_tags[-1] == tag:
                self.cell_tags.pop()
            self.current_cell_content.append(f"</{tag}>")

    def handle_data(self, data):
        if self.in_cell:
            self.current_cell_content.append(data)

parser = RawTableParser = TableParser()
html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    parser.feed(f.read())

for idx, r in enumerate(parser.rows):
    if len(r) > 0:
        first_col_text = " ".join(r[0].split()).strip()
        first_col_clean = re.sub(r'<[^>]+>', '', first_col_text).strip()
        if first_col_clean.isdigit() or first_col_clean.startswith("Semana") or "CIERRE" in first_col_clean:
            print(f"\n============================================================\nROW {idx} - WEEK: {first_col_clean}\n============================================================")
            for c_idx, cell in enumerate(r):
                print(f"Col {c_idx}:")
                # print a clean version
                print(cell)
                print()
