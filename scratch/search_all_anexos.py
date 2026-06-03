import re

with open("PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html", "r", encoding="utf-8") as f:
    text = f.read()

# Find all occurrences of "Anexo" in the text (with some context)
matches = re.finditer(r"Anexo\s+\d+[^<]*", text, re.IGNORECASE)
print("=== OCCURRENCES OF ANEXO ===")
for m in matches:
    print(m.group(0))

print("\n=== OCCURRENCES OF PLANTILLA ===")
matches2 = re.finditer(r"plantilla\s+\w+[^<]*", text, re.IGNORECASE)
for m in matches2:
    print(m.group(0))
