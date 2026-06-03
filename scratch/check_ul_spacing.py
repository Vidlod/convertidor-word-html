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

    # Find all <ul> and <ol> tags
    # Check if they are preceded by double br if there is a paragraph/text before them
    # And followed by double br if there is a paragraph/text after them
    
    # We can search for the pattern <p>...</p>[not double br]<ul> or </ul>[not double br]<p>
    # Note that there might be text directly, or other elements.
    # Let's search for <ul> tags and print what's immediately before them.
    # Also </ul> tags and print what's immediately after them.
    
    # Let's find all occurrences of <ul> or <ol>
    matches_before = re.finditer(r'((?:.|\n){0,100})\s*<(?:ul|ol)\b', content, re.IGNORECASE)
    for m in matches_before:
        prefix = m.group(1)
        # Check if the prefix ends with <br><br> or <br/><br/> or similar, or if it is inside a card-body/tab-pane start
        # Wait, if the list is the very first element in card-body/tab-pane, it doesn't need <br><br> before it.
        # But if there's text/paragraph before it, it must have double br.
        prefix_clean = prefix.strip()
        if prefix_clean:
            # Check if there is some text or a paragraph close tag like </p>
            if '</p>' in prefix_clean or '</div>' in prefix_clean or not prefix_clean.endswith('>') or prefix_clean.endswith('</strong>'):
                # Check if it contains double br
                if not re.search(r'<br\s*/?>\s*<br\s*/?>$', prefix_clean, re.IGNORECASE):
                    # It's an issue if it doesn't end with double br and has text before it
                    # Let's check if the parent tag is nav-tabs (then it's a menu, not list content)
                    # We can check if it's class="nav..."
                    tag_start = content[m.end() - 3 : m.end() + 100]
                    if 'class="nav' not in tag_start and 'class="list-' not in tag_start:
                        # Let's print the line number
                        line_no = content[:m.start()].count('\n') + 1
                        print(f"[{rel_path} - Line {line_no}] Potential missing double <br> BEFORE list:")
                        print(f"  Prefix: {repr(prefix_clean[-60:])}")
                        print(f"  List tag: {repr(content[m.start():m.end() + 20])}")
                        
    matches_after = re.finditer(r'</(?:ul|ol)>\s*((?:.|\n){0,100})', content, re.IGNORECASE)
    for m in matches_after:
        suffix = m.group(1)
        suffix_clean = suffix.strip()
        if suffix_clean:
            # If there is content after the list
            if suffix_clean.startswith('<p') or suffix_clean.startswith('<div') or suffix_clean.startswith('<strong>') or not suffix_clean.startswith('<'):
                # Check if it starts with double br
                if not re.match(r'^\s*<br\s*/?>\s*<br\s*/?>', suffix_clean, re.IGNORECASE):
                    # Check if it's followed by a closing tag like </div> or nav tabs or button containers
                    if not (suffix_clean.startswith('</div>') or suffix_clean.startswith('</div') or 'nav' in suffix_clean):
                        line_no = content[:m.start()].count('\n') + 1
                        print(f"[{rel_path} - Line {line_no}] Potential missing double <br> AFTER list:")
                        print(f"  List end tag: {repr(content[m.start():m.end()])}")
                        print(f"  Suffix: {repr(suffix_clean[:60])}")
