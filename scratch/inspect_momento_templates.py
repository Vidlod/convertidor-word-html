from html.parser import HTMLParser

class StructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.nav_links = []
        self.tab_panes = []
        self.current_pane = None
        self.pane_headings = {}

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'a' and 'nav-link' in attrs_dict.get('class', ''):
            self.nav_links.append(attrs_dict.get('href', ''))
        elif tag == 'div' and 'tab-pane' in attrs_dict.get('class', ''):
            pane_id = attrs_dict.get('id', '')
            self.tab_panes.append(pane_id)
            self.current_pane = pane_id
            self.pane_headings[pane_id] = []
        elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] and self.current_pane:
            self.pane_headings[self.current_pane].append(tag)

    def handle_endtag(self, tag):
        if tag == 'div' and self.current_pane:
            # We don't track nesting closely, but this is fine for a quick check
            pass

    def handle_data(self, data):
        pass

def inspect_file(path):
    print(f"\n=== INSPECTING TEMPLATE: {path} ===")
    parser = StructureParser()
    with open(path, "r", encoding="utf-8") as f:
        parser.feed(f.read())
    print("Nav links (hrefs):", parser.nav_links)
    print("Tab panes (ids):  ", parser.tab_panes)
    print("Pane headings:")
    for pane, headings in parser.pane_headings.items():
        print(f"  {pane}: {headings}")

inspect_file("/Users/buc-cvudes-medios1/Documents/GEO/Html Originales/Momentos/Momento evaluativo 1.html")
inspect_file("/Users/buc-cvudes-medios1/Documents/GEO/Html Originales/Momentos/momento evaluantivo 2.html")
