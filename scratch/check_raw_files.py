import re
import os

html_files = [
    "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo1.html",
    "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo2.html"
]

file_pattern = re.compile(r'href=["\']([^"\']+\.(?:docx|pdf|PDF|xlsx|xls|docx\?|pdf\?)[^"\']*)["\']', re.IGNORECASE)

errors = 0
for file_path in html_files:
    print(f"\nAuditing document links in: {os.path.basename(file_path)}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    matches = file_pattern.findall(content)
    for m in matches:
        if not m.startswith("@@PLUGINFILE@@/"):
            print(f"  [WARNING] Link does NOT use @@PLUGINFILE@@: {m}")
            errors += 1
        else:
            print(f"  [OK] Link uses @@PLUGINFILE@@: {m}")

if errors == 0:
    print("\nSUCCESS: All document links are using the portable @@PLUGINFILE@@ format!")
else:
    print(f"\nWARNING: Found {errors} document links not using @@PLUGINFILE@@.")
