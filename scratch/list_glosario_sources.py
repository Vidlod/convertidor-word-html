import re

files = [
    "/Users/buc-cvudes-medios1/Documents/GEO/Contexto & reglas/tablas_glosario.txt",
    "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/glosario_para_copiar.html"
]

source_pattern = re.compile(r'<td>([^<]+)</td>|&lt;td&gt;([^&]+)&lt;/td&gt;')

unique_sources = set()

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We find all cells, but since the source is the 4th column, let's parse table rows.
    # A cleaner way is to parse <tr> blocks.
    rows = re.findall(r'<tr>(.*?)</tr>', content, re.DOTALL | re.IGNORECASE)
    for r in rows:
        cells = re.findall(r'<td>(.*?)</td>', r, re.DOTALL | re.IGNORECASE)
        if len(cells) >= 4:
            source_text = re.sub(r'<[^>]+>', '', cells[3]).strip()
            unique_sources.add(source_text)

    # Check for escaped td in HTML content area
    escaped_rows = re.findall(r'&lt;tr&gt;(.*?)&lt;/tr&gt;', content, re.DOTALL | re.IGNORECASE)
    for r in escaped_rows:
        cells = re.findall(r'&lt;td&gt;(.*?)&lt;/td&gt;', r, re.DOTALL | re.IGNORECASE)
        if len(cells) >= 4:
            source_text = re.sub(r'&lt;[^&]+&gt;', '', cells[3]).strip()
            # remove html tags if any
            source_text = re.sub(r'<[^>]+>', '', source_text).strip()
            unique_sources.add(source_text)

print("Found unique sources:")
for s in sorted(unique_sources):
    print(f" - {repr(s)}")
