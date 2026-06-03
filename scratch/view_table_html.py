html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

import re
# Find table containing RESUMEN DE ENTREGAS
matches = list(re.finditer(r'<table.*?>.*?RESUMEN DE ENTREGAS.*?</table>', html, re.DOTALL | re.IGNORECASE))
if matches:
    table_content = matches[0].group()
    # Let's print it line by line
    for line in table_content.split('\n'):
        if line.strip():
            # truncate base64 images if any
            clean_line = re.sub(r'data:image/[^"]+', 'IMAGE_DATA', line)
            print(clean_line)
else:
    print("Table not found!")
