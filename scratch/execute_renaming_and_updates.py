import os
import re
import unicodedata

# 1. Rename files in documentos_word
word_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word"
word_renames = {
    "Entregable1_Recolección de datos.docx": "Entregable1_Recoleccion_de_datos.docx",
    "Entregable2_Organización de datos.docx": "Entregable2_Organizacion_de_datos.docx",
    "Entregable3_Ánalisis de datos.docx": "Entregable3_Analisis_de_datos.docx",
    "Entregable4_Interpretación de resultados.docx": "Entregable4_Interpretacion_de_resultados.docx",
    "Entregable5_Presentación de resultados.docx": "Entregable5_Presentacion_de_resultados.docx"
}

# 2. Rename files in guias_pdf
pdf_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/guias_pdf"
pdf_renames = {
    "Rubrica1_Estadística_Descriptiva.pdf": "Rubrica1_Estadistica_Descriptiva.pdf",
    "Rubrica2Estadística_Descriptiva.pdf": "Rubrica2_Estadistica_Descriptiva.pdf",
    "SYLLABUS_Estadística_Descriptiva.pdf": "SYLLABUS_Estadistica_Descriptiva.pdf",
    "Mapa_Curso_Estadística.pdf": "Mapa_Curso_Estadistica.pdf"
}

def normalize_variants(name):
    # Returns NFC and NFD byte patterns of the string
    nfc = unicodedata.normalize('NFC', name)
    nfd = unicodedata.normalize('NFD', name)
    return list(set([name, nfc, nfd]))

def safe_rename(directory, mapping):
    print(f"\nRenaming files in: {os.path.basename(directory)}")
    available_files = os.listdir(directory)
    
    for old_name, new_name in mapping.items():
        variants = normalize_variants(old_name)
        found_name = None
        for v in variants:
            # check case-insensitive match on filesystem
            for f in available_files:
                if unicodedata.normalize('NFC', f) == unicodedata.normalize('NFC', v) or unicodedata.normalize('NFD', f) == unicodedata.normalize('NFD', v):
                    found_name = f
                    break
            if found_name:
                break
                
        if found_name:
            src = os.path.join(directory, found_name)
            dest = os.path.join(directory, new_name)
            if src != dest:
                if os.path.exists(dest):
                    os.remove(dest)
                os.rename(src, dest)
                print(f"  [RENAMED] '{found_name}' ➔ '{new_name}'")
            else:
                print(f"  [ALREADY OK] '{found_name}' is already '{new_name}'")
        else:
            print(f"  [NOT FOUND] Variant of '{old_name}' not found on filesystem!")

# Run physical renaming
safe_rename(word_dir, word_renames)
safe_rename(pdf_dir, pdf_renames)


# 3. Update HTML files content
html_dirs = [
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Momentos",
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Entregables",
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Introduccion al curso"
]

all_renames_mappings = {}
# Add word files renames
for k, v in word_renames.items():
    for var in normalize_variants(k):
        all_renames_mappings[var] = v

# Add PDF files renames
for k, v in pdf_renames.items():
    for var in normalize_variants(k):
        all_renames_mappings[var] = v

# Add special uppercase rubrica error
for var in normalize_variants("RUBRICA1_Estadística_Descriptiva.pdf"):
    all_renames_mappings[var] = "Rubrica1_Estadistica_Descriptiva.pdf"

print("\nUpdating references in HTML files...")
for html_dir in html_dirs:
    if not os.path.exists(html_dir):
        continue
    for f in os.listdir(html_dir):
        if not f.endswith(".html"):
            continue
        filepath = os.path.join(html_dir, f)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            
        original_content = content
        
        # Replace occurrences in @@PLUGINFILE@@/filename
        # We search specifically for the target names in hrefs
        for old_pattern, new_name in all_renames_mappings.items():
            # escape for regex
            escaped_pattern = re.escape(old_pattern)
            # Replaces exact matches in PLUGINFILE refs
            content = re.sub(
                r'@@PLUGINFILE@@/' + escaped_pattern,
                r'@@PLUGINFILE@@/' + new_name,
                content
            )
            
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"  [UPDATED] {os.path.relpath(filepath, '/Users/buc-cvudes-medios1/Documents/GEO')}")
        else:
            print(f"  [NO CHANGES] {os.path.relpath(filepath, '/Users/buc-cvudes-medios1/Documents/GEO')}")

print("\nDone!")
