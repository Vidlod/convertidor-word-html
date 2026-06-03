import os
import re

base_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales"

files_to_check = []
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            files_to_check.append(os.path.join(root, file))

print(f"Found {len(files_to_check)} HTML files to check.")

for filepath in files_to_check:
    rel_path = os.path.relpath(filepath, base_dir)
    print(f"\nChecking spacing rules in: {rel_path}")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. 3 or more consecutive spaces (ignoring leading indentation)
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        # Find 3 or more spaces in the stripped text
        matches = re.findall(r'\s{3,}', stripped)
        if matches:
            print(f"  [TRIPLE SPACE] Line {i}: Found {len(matches)} instance(s) of 3+ consecutive spaces in: {repr(stripped)}")
            
    # 2. More than 2 consecutive br tags
    consec_br = re.findall(r'<br\s*/?>\s*<br\s*/?>\s*<br\s*/?>', content, re.IGNORECASE)
    if consec_br:
        print(f"  [CONSECUTIVE BR] Found 3+ consecutive <br> tags: {len(consec_br)} times")
        
    # 3. Trailing br immediately before closing tag (li, ul, ol, p, div, tr, td)
    trailing_br = re.finditer(r'<br\s*/?>\s*</(li|ul|ol|p|div|tr|td)>', content, re.IGNORECASE)
    for match in trailing_br:
        start_idx = max(0, match.start() - 40)
        end_idx = min(len(content), match.end() + 40)
        snippet = content[start_idx:end_idx].strip()
        print(f"  [TRAILING BR] Found trailing <br> before closing tag: {repr(snippet)}")

    # 4. Spacing rules for list items
    # Check if we have <ul> or <ol> and we check if style="margin-bottom: 10px;" is used appropriately
    # We can list the items in <ul> and see if they have style="margin-bottom: 10px;"
    # Let's find all <ul> groups
    ul_groups = re.findall(r'<ul\b[^>]*>(.*?)</ul>', content, re.DOTALL | re.IGNORECASE)
    for group_idx, group in enumerate(ul_groups, 1):
        li_items = re.findall(r'<li\b[^>]*>(.*?)</li>', group, re.DOTALL | re.IGNORECASE)
        if not li_items:
            continue
        
        # Check if any li has margin-bottom
        has_margin = any('margin-bottom' in tag for tag in re.findall(r'<li\b([^>]*)>', group, re.IGNORECASE))
        # Let's count line length/word count for each li to see if they are long
        long_items = []
        for li_idx, li_content in enumerate(li_items, 1):
            clean_li = re.sub(r'<[^>]*>', '', li_content).strip()
            word_count = len(clean_li.split())
            if word_count > 15: # approximate for 2-3 lines
                long_items.append((li_idx, clean_li))
                
        if long_items and not has_margin:
            print(f"  [LIST MARGIN MISSING] Group {group_idx}: Has long items but missing style='margin-bottom: 10px;' on <li> elements.")
            for idx, text in long_items:
                print(f"    Item {idx}: {repr(text[:60])}...")
        elif not long_items and has_margin and len(li_items) > 1:
            # Let's check if all items are very short (e.g. less than 5 words)
            all_short = True
            for li_content in li_items:
                clean_li = re.sub(r'<[^>]*>', '', li_content).strip()
                if len(clean_li.split()) > 5:
                    all_short = False
                    break
            if all_short:
                # Short items having margin is okay, but rule says "cuando solo tengan un renglón las puedes dejar pegadas (sin margen)".
                # Let's just flag it for awareness, not necessarily an error, unless it is a strict requirement.
                pass
