import re

html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Introduccion al curso/Información del Curso botones.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's define the exact filenames (from the previous print we know they are):
syllabus_file = "SYLLABUS_Estadística_Descriptiva.pdf"
rubrica_file = "RUBRICA1_Estadística_Descriptiva.pdf"
inst_file = "Instrucciones_Generales_Estadistica.pdf"

# Replace Instructions link:
# Find: href="https://virtual.udes.edu.co/pluginfile.php/.../Instrucciones_Generales_Fisica_mecanica.pdf"
# And its associated target="_blank"
pattern_inst = r'href="https://virtual.udes.edu.co/pluginfile.php/[^"]+?/Instrucciones_Generales_Fisica_mecanica.pdf"\s+target="_blank"'
match_inst = re.search(pattern_inst, content)
if match_inst:
    print("Found instructions link!")
    content = re.sub(
        pattern_inst,
        f'href="@@PLUGINFILE@@/{inst_file}" target="_blank" rel="noopener"',
        content
    )
else:
    print("Instructions link NOT found by regex")

# Replace Syllabus link:
pattern_syll = r'href="https://virtual.udes.edu.co/pluginfile.php/[^"]+?/Syllabus_Fisica_mecanica.pdf"\s+target="_blank"'
match_syll = re.search(pattern_syll, content)
if match_syll:
    print("Found syllabus link!")
    content = re.sub(
        pattern_syll,
        f'href="@@PLUGINFILE@@/{syllabus_file}" target="_blank" rel="noopener"',
        content
    )
else:
    print("Syllabus link NOT found by regex")

# Replace Rubrica link:
pattern_rubr = r'href="https://virtual.udes.edu.co/pluginfile.php/[^"]+?/Rubricas_Fisica_mecanica.pdf"\s+target="_blank"'
match_rubr = re.search(pattern_rubr, content)
if match_rubr:
    print("Found rubrica link!")
    content = re.sub(
        pattern_rubr,
        f'href="@@PLUGINFILE@@/{rubrica_file}" target="_blank" rel="noopener"',
        content
    )
else:
    print("Rubrica link NOT found by regex")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Regex update done.")
