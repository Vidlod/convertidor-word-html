import re
import os

html_files = [
    "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo1.html",
    "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo2.html"
]

def collapse_whitespace(text):
    # Replace any sequence of whitespace (newlines, tabs, spaces) inside tags with a single space
    return re.sub(r'\s+', ' ', text)

for file_path in html_files:
    print(f"\nProcessing: {os.path.basename(file_path)}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # 1. Let's fix specific anchor tags that contain newlines and indentations.
    # We match <a ...> ... </a>
    # We use a non-greedy regex that matches anchor tags.
    def anchor_replacer(match):
        full_tag = match.group(0)
        # Check if there are newlines inside
        if '\n' in full_tag:
            # We want to keep the tag opening and closing, but collapse the inner text and tags
            # Let's extract the href, and other attributes, and the inner content.
            tag_open_match = re.match(r'(<a\s+[^>]*>)(.*)(</a>)', full_tag, re.DOTALL | re.IGNORECASE)
            if tag_open_match:
                open_part = tag_open_match.group(1)
                inner_part = tag_open_match.group(2)
                close_part = tag_open_match.group(3)
                
                # Clean up inner content: collapse multiple spaces and newlines
                clean_inner = collapse_whitespace(inner_part).strip()
                # Clean up open part: collapse newlines/tabs in attributes if any
                clean_open = re.sub(r'\s+', ' ', open_part)
                
                return f"{clean_open}{clean_inner}{close_part}"
        return full_tag

    content = re.sub(r'<a\s+[^>]*>.*?</a>', anchor_replacer, content, flags=re.DOTALL | re.IGNORECASE)

    # 2. Also fix <strong> tags containing newlines/indentations around anchors
    def strong_replacer(match):
        full_tag = match.group(0)
        if '\n' in full_tag:
            tag_open_match = re.match(r'(<strong\b[^>]*>)(.*)(</strong>)', full_tag, re.DOTALL | re.IGNORECASE)
            if tag_open_match:
                open_part = tag_open_match.group(1)
                inner_part = tag_open_match.group(2)
                close_part = tag_open_match.group(3)
                
                clean_inner = collapse_whitespace(inner_part).strip()
                clean_open = re.sub(r'\s+', ' ', open_part)
                
                return f"{clean_open}{clean_inner}{close_part}"
        return full_tag

    content = re.sub(r'<strong\b[^>]*>.*?</strong>', strong_replacer, content, flags=re.DOTALL | re.IGNORECASE)

    # 3. Let's fix specific double-spaces inside list items or paragraphs if any
    # (Checking if any double space exists that isn't leading indentation)
    lines = content.splitlines()
    new_lines = []
    for line in lines:
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]
        # Replace multiple spaces in the content part
        # but keep single or double spaces as allowed, collapse 3+ spaces to 1 space
        # (Though we shouldn't have 3+ spaces anyway)
        clean_content = re.sub(r'(?<!\s) {3,}(?!\s)', ' ', stripped)
        new_lines.append(indent + clean_content)
    
    content = '\n'.join(new_lines)

    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  Updated file successfully.")
    else:
        print("  No changes needed.")
