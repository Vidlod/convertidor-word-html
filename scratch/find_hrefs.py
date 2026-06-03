import re

html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Introduccion al curso/Información del Curso botones.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

hrefs = re.findall(r'href="([^"]+)"', content)
print("=== HREFS FOUND ===")
for h in hrefs:
    print(h)
