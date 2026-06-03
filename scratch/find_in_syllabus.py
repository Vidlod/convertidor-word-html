with open("/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/guias_pdf/SYLLABUS_Estadística_Descriptiva_extracted.txt", "r") as f:
    text = f.read()

import re
print("=== Matches for 'problema' ===")
for match in re.finditer(r'(?:[^\n]+\n){0,2}[^\n]*problema[^\n]*(?:\n[^\n]+){0,2}', text, re.IGNORECASE):
    print(match.group())
    print("-" * 50)
