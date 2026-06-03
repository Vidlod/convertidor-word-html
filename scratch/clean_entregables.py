import os
import re

entregables_dir = "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Entregables CARJO"

html_files = [
    os.path.join(entregables_dir, f)
    for f in os.listdir(entregables_dir)
    if f.endswith(".html")
]

for file_path in html_files:
    print(f"\nProcessing: {os.path.basename(file_path)}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    
    # 1. Apply Rule 12 (remove "tablero de anotaciones" references)
    # We want to replace patterns like:
    # "a través del tablero de anotaciones en las fechas establecidas en el tablero de anotaciones" -> "en las fechas establecidas"
    # "a través del tablero de anotaciones de acuerdo" -> "de acuerdo"
    # "a través del tablero de anotaciones en las fechas establecidas" -> "en las fechas establecidas"
    # Let's use regex to handle any variations:
    content = re.sub(
        r'a través del\s+tablero de anotaciones\s+en\s+las\s+fechas\s+establecidas\s+en\s+el\s+tablero\s+de\s+anotaciones',
        'en las fechas establecidas',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'a través del\s+tablero de anotaciones\s+en\s+las\s+fechas\s+establecidas',
        'en las fechas establecidas',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'a través del\s+tablero de anotaciones\s+de\s+',
        'de ',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'a través del\s+tablero de anotaciones\s+en\s+',
        'en ',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'en\s+el\s+tablero\s+de\s+anotaciones\s+en\s+esta\s+semana\s+(\d+)',
        r'en esta semana \1',
        content,
        flags=re.IGNORECASE
    )
    
    # 2. Desvinculación de recursos (unlink fijos resources)
    # In Entregable avance 4:
    # <strong><a href="...Anexo3...">Anexo 3. las Crónicas...</a></strong> -> <strong>Anexo 2. las Crónicas de Enriq “noches de cocaína”.</strong>
    # (Note that it was Anexo 2, and the text has Anexo 3 in the old code)
    content = re.sub(
        r'<strong><a\s+[^>]*href="[^"]+Anexo3_Perfil_Ted_Bondy\.docx[^"]*"[^>]*>Anexo\s+3\.\s+las\s+Crónicas\s+de\s+Enriq\s+“noches\s+de\s+cocaína”\.</a></strong>',
        '<strong>Anexo 2. las Crónicas de Enriq “noches de cocaína”.</strong>',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    # In Entregable Avance 3:
    # <strong><a href="...Anexo3...">Anexo 3</a></strong> -> <strong>Anexo 3</strong>
    content = re.sub(
        r'<strong><a\s+[^>]*href="[^"]+Anexo3_Perfil_Ted_Bondy\.docx[^"]*"[^>]*>Anexo\s+3</a></strong>',
        '<strong>Anexo 3</strong>',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    # Remove any other draftfile / pluginfile docx/pdf links if they were somehow missed
    content = re.sub(
        r'<a\s+[^>]*href="[^"]+\.(?:docx|pdf)[^"]*"[^>]*>(.*?)</a>',
        r'\1',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # 3. Spacing corrections:
    # Fix nested linebreaks before </li>, </ul>, </ol>
    content = re.sub(r'(<br\s*/?>\s*)+</li>', '</li>', content, flags=re.IGNORECASE)
    content = re.sub(r'(<br\s*/?>\s*)+</ul>', '</ul>', content, flags=re.IGNORECASE)
    content = re.sub(r'(<br\s*/?>\s*)+</ol>', '</ol>', content, flags=re.IGNORECASE)
    
    # Ensure all tab-panes end with exactly one <br> before closing </div>
    # The tab pane pattern: <div class="tab-pane[^"]*"[^>]*>...</div>
    # Let's find each tab-pane card-body and adjust its trailing space.
    # We can match card-body contents: <div class="card-body">(.*?)</div>\s*</div>
    def card_body_replacer(match):
        prefix = match.group(1)
        body_content = match.group(2)
        suffix = match.group(3)
        
        # Clean up the end of the body content
        # Strip trailing whitespaces and br tags
        cleaned_body = re.sub(r'(?:\s*<br\s*/?>)*\s*$', '', body_content, flags=re.IGNORECASE)
        # Add exactly one <br> at the end
        return f'{prefix}{cleaned_body}\n                <br>\n            </div>\n        </div>'

    content = re.sub(
        r'(<div class="tab-pane\b[^>]*>\s*<div class="card-body">)(.*?)(</div>\s*</div>)',
        card_body_replacer,
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    # 4. Collapse inline tag whitespaces (spanning lines or multiple spaces)
    inline_tags = ["a", "strong", "span", "em", "i", "b", "u"]
    for tag in inline_tags:
        def inline_replacer(match):
            full_tag = match.group(0)
            if '\n' in full_tag:
                tag_open_match = re.match(rf'(<{tag}\b[^>]*>)(.*?)(</{tag}>)', full_tag, re.DOTALL | re.IGNORECASE)
                if tag_open_match:
                    open_part = tag_open_match.group(1)
                    inner_part = tag_open_match.group(2)
                    close_part = tag_open_match.group(3)
                    
                    clean_inner = re.sub(r'\s+', ' ', inner_part).strip()
                    clean_open = re.sub(r'\s+', ' ', open_part)
                    return f"{clean_open}{clean_inner}{close_part}"
            return full_tag
            
        content = re.sub(rf'<{tag}\b[^>]*>.*?</{tag}>', inline_replacer, content, flags=re.DOTALL | re.IGNORECASE)

    # 5. Fix double spaces in text
    lines = content.splitlines()
    new_lines = []
    for line in lines:
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]
        # Replace multiple spaces in the content part (3+ spaces, or 2+ spaces if not indents)
        # We replace 3+ spaces with 1 space
        clean_content = re.sub(r'(?<!\s) {3,}(?!\s)', ' ', stripped)
        new_lines.append(indent + clean_content)
    content = '\n'.join(new_lines)

    if content != original:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  Updated file successfully.")
    else:
        print("  No changes needed.")
