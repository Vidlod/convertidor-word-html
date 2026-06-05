import os
import re

def clean_file(path):
    print(f"Cleaning: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. URL replacements (draftfile.php to @@PLUGINFILE@@)
    pattern = r'https://virtual\.udes\.edu\.co/draftfile\.php/[^\s\"<>]+/([^\s\"<>/]+\.[a-zA-Z0-9]+)'
    content, count = re.subn(pattern, r'@@PLUGINFILE@@/\1', content)
    print(f"Replaced {count} draftfile.php URLs in {os.path.basename(path)}")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    base_dir = "PLANTILLA_CURSO/3_paginas_finales"
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                clean_file(filepath)
