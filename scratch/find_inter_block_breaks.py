import re
import os

base_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales"
files = [
    os.path.join(base_dir, "Introduccion al curso/Introduccion al curso.html"),
    os.path.join(base_dir, "Introduccion al curso/Información del Curso botones.html"),
    os.path.join(base_dir, "Linea del tiempo/Lineadeltiempo.html"),
    os.path.join(base_dir, "Momentos/Momento Evaluativo1.html"),
    os.path.join(base_dir, "Momentos/Momento Evaluativo2.html"),
    os.path.join(base_dir, "Entregables/Entregalbe Avance 1.html"),
    os.path.join(base_dir, "Entregables/Entregalbe Avance 2.html"),
    os.path.join(base_dir, "Entregables/Entregalbe Avance 3.html"),
    os.path.join(base_dir, "Entregables/Entregalbe Avance 4.html"),
    os.path.join(base_dir, "Entregables/Entregable Producto Fina (Entregalbe Avance 5).html")
]

# Find breaks between block tags: </(p|ul|ol|h[1-6]|table|div|li)>\s*(<br\s*/?>\s*)+\s*<(p|ul|ol|h[1-6]|table|div|li)
pattern = re.compile(r'(</(p|ul|ol|h[1-6]|table|div|li)>\s*(?:<br\s*/?>\s*)+\s*<(p|ul|ol|h[1-6]|table|div|li[^>]*>))', re.IGNORECASE)

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = pattern.findall(content)
    if matches:
        print(f"\nFile: {os.path.basename(filepath)} - Found {len(matches)} occurrences:")
        for m in matches[:10]: # Print first 10
            print(f"  {repr(m[0])}")
