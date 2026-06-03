from bs4 import BeautifulSoup

html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# Let's extract all tables and paragraphs
print("=== HEADINGS AND PARAGRAPHS ===")
for elem in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'td']):
    # get text and clean spacing
    text = " ".join(elem.get_text().split())
    if text:
        # Don't print long base64 image strings
        if len(text) > 200:
            print(f"[{elem.name}]: {text[:200]}...")
        else:
            print(f"[{elem.name}]: {text}")
