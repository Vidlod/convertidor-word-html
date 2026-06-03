import os

html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Introduccion al curso/Información del Curso botones.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Files list from the folder
base_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/guias_pdf"
files = os.listdir(base_dir)

# Find the specific files
syllabus_file = [f for f in files if "SYLLABUS" in f][0]
rubrica_file = [f for f in files if "RUBRICA1" in f][0]
inst_file = [f for f in files if "Instrucciones_Generales" in f][0]

print(f"Syllabus file name: {repr(syllabus_file)}")
print(f"Rubrica 1 file name: {repr(rubrica_file)}")
print(f"Instructions file name: {repr(inst_file)}")

# Replace the links
# Instructions link:
content = content.replace(
    'href="https://virtual.udes.edu.co/pluginfile.php/7835/mod_resource/content/15/Instrucciones_Generales_Fisica_mecanica.pdf"\n                                        target="_blank" title="Instrucciones Generales"',
    f'href="@@PLUGINFILE@@/{inst_file}"\n                                        target="_blank" rel="noopener" title="Instrucciones Generales"'
)

# Syllabus link:
content = content.replace(
    'href="https://virtual.udes.edu.co/pluginfile.php/7836/mod_resource/content/18/Syllabus_Fisica_mecanica.pdf"\n                                        target="_blank" title="Syllabus"',
    f'href="@@PLUGINFILE@@/{syllabus_file}"\n                                        target="_blank" rel="noopener" title="Syllabus"'
)

# Rubricas link:
content = content.replace(
    'href="https://virtual.udes.edu.co/pluginfile.php/7817/mod_label/intro/Rubricas_Fisica_mecanica.pdf"\n                                        target="_blank" title="Rúbricas"',
    f'href="@@PLUGINFILE@@/{rubrica_file}"\n                                        target="_blank" rel="noopener" title="Rúbricas"'
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated buttons HTML successfully!")
