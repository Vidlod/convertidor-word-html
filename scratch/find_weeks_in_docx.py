import re

html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Let's search for lines containing "Semana 1", "Semana 2", etc.
for w in range(1, 13):
    pattern = rf'(?:[^\n]+\n){0,3}[^\n]*Semana\s+{w}\b[^\n]*(?:\n[^\n]+){0,3}'
    print(f"\n=== MATCHES FOR SEMANA {w} ===")
    matches = re.findall(pattern, html, re.IGNORECASE)
    for m in matches[:3]: # show first 3 matches
        clean_match = re.sub(r'<[^>]+>', ' ', m)
        print(" ".join(clean_match.split()))
        print("-" * 30)
