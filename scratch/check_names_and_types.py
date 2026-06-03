import os
import re
import unicodedata
from urllib.parse import unquote

html_dirs = [
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Momentos",
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Entregables",
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Introduccion al curso"
]

insumos_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen"

# Gather all physical files
physical_files = []
for root, dirs, files in os.walk(insumos_dir):
    for f in files:
        if f == ".DS_Store" or f.startswith("."):
            continue
        physical_files.append(f)

print("Physical files in 1_insumos_origen:")
for pf in sorted(physical_files):
    print(f"  - {pf}")

pluginfile_pattern = re.compile(r'href=["\']@@PLUGINFILE@@/([^"\']+)["\']', re.IGNORECASE)

print("\nScanning HTML files for @@PLUGINFILE@@ links...")
for html_dir in html_dirs:
    if not os.path.exists(html_dir):
        continue
    for f in os.listdir(html_dir):
        if not f.endswith(".html"):
            continue
        filepath = os.path.join(html_dir, f)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        matches = pluginfile_pattern.findall(content)
        if matches:
            print(f"\nIn file: {os.path.relpath(filepath, '/Users/buc-cvudes-medios1/Documents/GEO')}")
            for m in matches:
                decoded = unquote(m)
                # Check direct match
                direct_match = decoded in physical_files
                
                # Check NFC/NFD variants
                nfc_d = unicodedata.normalize('NFC', decoded)
                nfd_d = unicodedata.normalize('NFD', decoded)
                
                variant_match = False
                matched_phys_name = ""
                for pf in physical_files:
                    pf_nfc = unicodedata.normalize('NFC', pf)
                    pf_nfd = unicodedata.normalize('NFD', pf)
                    if pf in [decoded, nfc_d, nfd_d] or pf_nfc in [decoded, nfc_d, nfd_d] or pf_nfd in [decoded, nfc_d, nfd_d]:
                        variant_match = True
                        matched_phys_name = pf
                        break
                
                if direct_match:
                    print(f"  [OK] Link: '{decoded}' matches physical file exactly.")
                elif variant_match:
                    print(f"  [WARNING] Link: '{decoded}' matches physical file '{matched_phys_name}' but needs Unicode normalization normalization.")
                else:
                    print(f"  [ERROR] Link: '{decoded}' has NO matching physical file!")
