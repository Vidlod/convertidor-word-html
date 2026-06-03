import re

input_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/documentos_word/AAA-pregrado_extracted.html"
output_path = "/Users/buc-cvudes-medios1/Documents/GEO/scratch/AAA-pregrado_readable.html"

with open(input_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's add newlines before block elements to make it readable
content = content.replace("<table>", "\n<table>\n")
content = content.replace("</table>", "\n</table>\n")
content = content.replace("<tr>", "\n  <tr>\n")
content = content.replace("</tr>", "\n  </tr>\n")
content = content.replace("<td>", "\n    <td>")
content = content.replace("</td>", "</td>\n")
content = content.replace("<p>", "\n      <p>")
content = content.replace("</p>", "</p>\n")
content = content.replace("<ul>", "\n      <ul>\n")
content = content.replace("</ul>", "\n      </ul>\n")
content = content.replace("<li>", "\n        <li>")
content = content.replace("</li>", "</li>\n")

# Remove multiple blank lines
content = re.sub(r'\n\s*\n', '\n', content)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Readable HTML written to {output_path}")
