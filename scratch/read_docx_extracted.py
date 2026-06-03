import re

html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Let's clean the HTML slightly for readability and print sections
# Let's replace tags to make it look like markdown and print first 4000 characters
clean = re.sub(r'</?(p|tr|div|table|td|tbody|thead)[^>]*>', '\n', html)
clean = re.sub(r'\n+', '\n', clean)
print("=== AAA-pregrado.docx Content Snippet ===")
print(clean[:5000])
