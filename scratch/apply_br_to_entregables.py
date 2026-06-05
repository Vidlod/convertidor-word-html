# -*- coding: utf-8 -*-
import os
import re

def add_br_to_lists(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # Target <ul> or <ol> elements that do not have class="nav" or "nav-tabs" or similar
    pattern = r'<(ul|ol)(?![^>]*class="[^"]*nav)([^>]*)>(.*?)</\1>'
    
    def replace_list(match):
        tag_name = match.group(1)
        attrs = match.group(2)
        inner_content = match.group(3)
        
        # Clean any existing <br> elements inside the list to avoid duplication
        # e.g., if there are already <br> tags between <li> tags, let's strip them
        inner_content_clean = re.sub(r'\s*<br\s*/?>\s*', '\n', inner_content, flags=re.IGNORECASE)
        
        # Find all <li>...</li> blocks
        li_pattern = r'<li([^>]*)>(.*?)</li>'
        li_matches = list(re.finditer(li_pattern, inner_content_clean, re.DOTALL))
        
        if not li_matches:
            return match.group(0) # No list items, return original
            
        new_inner = "\n                                            <br>\n"
        for li_match in li_matches:
            li_attrs = li_match.group(1).strip()
            li_text = li_match.group(2).strip()
            
            li_tag = f"<li {li_attrs}>" if li_attrs else "<li>"
            
            new_inner += f"                                            {li_tag}{li_text}</li>\n"
            new_inner += "                                            <br>\n"
            
        # Format the block neatly
        return f"<{tag_name}{attrs}>\n{new_inner}                                        </{tag_name}>"
        
    content = re.sub(pattern, replace_list, content, flags=re.DOTALL | re.IGNORECASE)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully added list <br> spacing to: {filepath}")
        return True
    else:
        print(f"No changes made in: {filepath}")
        return False

# Base directory for the course
base_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Entregables"
files = [
    "Entregalbe Avance 1.html",
    "Entregalbe Avance 2.html",
    "Entregalbe Avance 3.html",
    "Entregalbe Avance 4.html",
    "Entregable Producto Fina (Entregalbe Avance 5).html"
]

for filename in files:
    path = os.path.join(base_dir, filename)
    add_br_to_lists(path)

print("\n--- List spacing modification complete ---")
