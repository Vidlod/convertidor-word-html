import os

files_to_fix = [
    "/Users/buc-cvudes-medios1/Documents/GEO/Contexto & reglas/tablas_glosario.txt",
    "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/glosario_para_copiar.html",
    "/Users/buc-cvudes-medios1/Documents/GEO/Contexto & reglas/Glosario estructura.text"
]

replacements = {
    "Real academia española": "Real Academia Española",
    "real academia española": "Real Academia Española",
    "REAL ACADEMIA ESPAÑOLA": "Real Academia Española",
    "Maria Moliner": "María Moliner",
    "maria moliner": "María Moliner",
    "MARIA MOLINER": "María Moliner"
}

for fpath in files_to_fix:
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        continue
        
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Corrected capitalization in: {os.path.basename(fpath)}")
    else:
        print(f"No changes needed in: {os.path.basename(fpath)}")
