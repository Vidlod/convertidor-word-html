import os
import re

def bold_links_in_file(file_path):
    print(f"Processing: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to match <a> tag
    # Group 1: opening part up to href
    # Group 2: the href URL itself
    # Group 3: the rest of the opening tag attributes
    # Group 4: the text content inside <a>
    a_tag_pattern = re.compile(
        r'(<a\s+[^>]*href=["\'])([^"\']+)(["\'][^>]*>)(.*?)(</a>)',
        re.DOTALL | re.IGNORECASE
    )

    modified = False
    new_content = ""
    last_idx = 0

    for match in a_tag_pattern.finditer(content):
        start_idx = match.start()
        end_idx = match.end()
        
        prefix = match.group(1)
        href = match.group(2)
        attr = match.group(3)
        inner_text = match.group(4)
        suffix = match.group(5)

        # Append preceding content
        new_content += content[last_idx:start_idx]
        last_idx = end_idx

        # Check if the link should be bolded (external references)
        is_ref_link = (
            "ezproxy" in href or 
            "elibro" in href or 
            "login" in href or 
            "dle.rae.es" in href or
            inner_text.strip().startswith("http")
        )

        if is_ref_link:
            # Check if already wrapped in <strong> or <b>
            # Let's inspect the characters immediately preceding the <a tag
            preceding_str = content[max(0, start_idx-20):start_idx].rstrip()
            following_str = content[end_idx:min(len(content), end_idx+20)].lstrip()

            already_bold = False
            if preceding_str.endswith('<strong>') and following_str.startswith('</strong>'):
                already_bold = True
            elif preceding_str.endswith('<b>') and following_str.startswith('</b>'):
                already_bold = True
            elif inner_text.strip().startswith('<strong>') and inner_text.strip().endswith('</strong>'):
                already_bold = True
            elif inner_text.strip().startswith('<b>') and inner_text.strip().endswith('</b>'):
                already_bold = True

            if not already_bold:
                # Wrap the <a> tag inside <strong>
                original_tag = match.group(0)
                wrapped_tag = f"<strong>{original_tag}</strong>"
                print(f"  Bolding link: {href}")
                print(f"    Original: {original_tag}")
                print(f"    New:      {wrapped_tag}")
                new_content += wrapped_tag
                modified = True
            else:
                new_content += match.group(0)
        else:
            new_content += match.group(0)

    new_content += content[last_idx:]

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated {file_path}\n")
    else:
        print(f"No changes needed for {file_path}\n")

if __name__ == '__main__':
    files_to_process = [
        '/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo1.html',
        '/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo2.html',
        '/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/glosario_para_copiar.html'
    ]
    
    for f in files_to_process:
        if os.path.exists(f):
            bold_links_in_file(f)
        else:
            print(f"File not found: {f}")
