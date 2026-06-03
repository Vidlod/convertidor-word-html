import os
import re

def fix_link_targets(file_path):
    print(f"Processing: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find <a> tags
    # Group 1: '<a' and attributes before target/href
    # Group 2: the href attribute and value
    # Group 3: the rest of the attributes inside the opening tag
    # Group 4: the closing '>' and inner content + </a>
    a_tag_pattern = re.compile(
        r'(<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*)>(.*?)</a>',
        re.DOTALL | re.IGNORECASE
    )

    modified = False
    new_content = ""
    last_idx = 0

    for match in a_tag_pattern.finditer(content):
        start_idx = match.start()
        end_idx = match.end()
        
        full_opening_tag = match.group(1)
        href = match.group(2).strip()
        inner_content = match.group(3)

        new_content += content[last_idx:start_idx]
        last_idx = end_idx

        # Skip anchor links
        if href.startswith('#') or not href or href.startswith('javascript:'):
            new_content += match.group(0)
            continue

        # Check if target="_blank" is already there
        has_target_blank = 'target="_blank"' in full_opening_tag or "target='_blank'" in full_opening_tag

        if not has_target_blank:
            # We need to inject target="_blank"
            # Let's also check if it has a rel attribute. If not, let's add rel="noopener"
            has_rel = 'rel=' in full_opening_tag
            
            # Let's insert target="_blank" right after the "<a"
            tag_parts = full_opening_tag.split('<a', 1)
            new_opening = tag_parts[0] + '<a target="_blank"'
            if not has_rel:
                new_opening += ' rel="noopener"'
            new_opening += tag_parts[1]
            
            reconstructed_tag = f"{new_opening}>{inner_content}</a>"
            print(f"  Fixed link: {href}")
            print(f"    Original: {match.group(0)}")
            print(f"    New:      {reconstructed_tag}")
            new_content += reconstructed_tag
            modified = True
        else:
            new_content += match.group(0)

    new_content += content[last_idx:]

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated targets in {file_path}\n")
    else:
        print(f"No changes needed for {file_path}\n")

if __name__ == '__main__':
    search_dir = '/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales'
    all_files = []
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if file.endswith('.html'):
                all_files.append(os.path.join(root, file))
                
    for f in all_files:
        fix_link_targets(f)
