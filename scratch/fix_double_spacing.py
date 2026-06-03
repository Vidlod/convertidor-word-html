# -*- coding: utf-8 -*-
import os
import re

base_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Entregables"

files_to_fix = [
    os.path.join(base_dir, "Entregalbe Avance 1.html"),
    os.path.join(base_dir, "Entregalbe Avance 2.html"),
    os.path.join(base_dir, "Entregalbe Avance 3.html"),
    os.path.join(base_dir, "Entregalbe Avance 4.html"),
    os.path.join(base_dir, "Entregable Producto Fina (Entregalbe Avance 5).html")
]

pattern = re.compile(
    r'(</(?:p|ul|ol|h[1-6]|div|table|li)>)'                  # Group 1: closing tag
    r'(\s*)(?:<br\s*/?>\s*)+(\s*)'                           # Group 2 & 3: whitespace around <br>s
    r'(<(?:p|ul|ol|h[1-6]|div|table|li)\b)',                 # Group 4: opening tag
    re.IGNORECASE
)

def replacer(match):
    closing = match.group(1)
    ws_before = match.group(2)
    ws_after = match.group(3)
    opening = match.group(4)
    combined = ws_before + ws_after
    last_nl = combined.rfind('\n')
    if last_nl != -1:
        indent = combined[last_nl:]
    else:
        indent = '\n' + combined
    return f"{closing}{indent}{opening}"

for filepath in files_to_fix:
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    new_content, count = pattern.subn(replacer, content)
    print(f"Fixed {count} inter-block breaks in {os.path.basename(filepath)}")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

print("\nDone fixing all deliverable files.")
