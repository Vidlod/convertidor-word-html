html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Introduccion al curso/Información del Curso botones.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    "Instrucciones_Generales_Estadistica_extracted.txt",
    "Instrucciones_Generales_Estadistica.pdf"
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Instructions link fixed successfully!")
