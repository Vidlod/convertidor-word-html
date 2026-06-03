import os
import re

base_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales"

files_to_check = []
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            files_to_check.append(os.path.join(root, file))

for filepath in files_to_check:
    rel_path = os.path.relpath(filepath, base_dir)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find all `<br> number` and check if there's no `<br>` immediately before it
    # We can match `<br>[\s\n]*\d+[\.\)]`
    matches = re.finditer(r'(<br\s*/?>[\s\n]*\d+[\.\)])', content, re.IGNORECASE)
    for m in matches:
        start_idx = m.start()
        # Look at the text before the match
        before = content[max(0, start_idx - 15):start_idx]
        # Check if before contains a br tag
        if not re.search(r'<br\s*/?>\s*$', before, re.IGNORECASE):
            # It is a single <br>!
            context_start = max(0, start_idx - 40)
            context_end = min(len(content), m.end() + 40)
            context = content[context_start:context_end].replace('\n', ' ')
            print(f"[{rel_path}] Single <br> separation for list item in: {repr(context.strip())}")
