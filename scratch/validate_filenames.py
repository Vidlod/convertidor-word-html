import os
import re
import unicodedata
from urllib.parse import unquote

html_files = [
    "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo1.html",
    "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo2.html"
]

base_dir = "/Users/buc-cvudes-medios1/Documents/GEO/Archivos E/Archivos con nombre y tamaño corregido "
anexos_dir = os.path.join(base_dir, "Anexos")

# List all files in both directories, normalized NFC and NFD
available_files = {}
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f == ".DS_Store":
            continue
        path = os.path.join(root, f)
        rel_path = os.path.relpath(path, base_dir)
        
        # We store normalized versions
        nfc_name = unicodedata.normalize('NFC', f)
        nfd_name = unicodedata.normalize('NFD', f)
        
        available_files[nfc_name] = rel_path
        available_files[nfd_name] = rel_path
        # also URL encoded just in case
        available_files[f] = rel_path

pluginfile_pattern = re.compile(r'href=["\']@@PLUGINFILE@@/([^"\']+)["\']', re.IGNORECASE)

print("Checking files...")
errors = 0
for html_path in html_files:
    print(f"\nAnalyzing: {os.path.basename(html_path)}")
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = pluginfile_pattern.findall(content)
    for m in matches:
        # Decode URL representation
        decoded_name = unquote(m)
        nfc_decoded = unicodedata.normalize('NFC', decoded_name)
        nfd_decoded = unicodedata.normalize('NFD', decoded_name)
        
        found = False
        match_rel_path = ""
        for name_variant in [decoded_name, nfc_decoded, nfd_decoded]:
            if name_variant in available_files:
                found = True
                match_rel_path = available_files[name_variant]
                break
                
        if found:
            print(f"  [OK] Link to '{decoded_name}' -> matches physical file '{match_rel_path}'")
        else:
            print(f"  [ERROR] Link to '{decoded_name}' NOT found in physical files!")
            errors += 1

if errors == 0:
    print("\nSUCCESS: All @@PLUGINFILE@@ links match physical files!")
else:
    print(f"\nFAILED: Found {errors} broken @@PLUGINFILE@@ links.")
