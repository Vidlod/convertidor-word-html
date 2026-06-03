import os
import re

def check_link_targets(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Regex to find <a> tags
    a_tag_pattern = re.compile(r'<a\s+([^>]*href=["\']([^"\']+)["\'][^>]*)>(.*?)</a>', re.DOTALL | re.IGNORECASE)
    
    issues = []
    for match in a_tag_pattern.finditer(content):
        attrs_str = match.group(1)
        href = match.group(2).strip()
        text = match.group(3).strip()
        
        # We only check real links (not internal anchors like #formato, #semana1, etc.)
        if href.startswith('#'):
            continue
            
        # Also skip empty links or javascript voids
        if not href or href.startswith('javascript:'):
            continue
            
        # Check if target="_blank" is in the attributes
        has_target_blank = 'target="_blank"' in attrs_str or "target='_blank'" in attrs_str
        
        if not has_target_blank:
            start = max(0, match.start() - 50)
            end = min(len(content), match.end() + 50)
            context = content[start:end].strip()
            issues.append({
                'tag': match.group(0),
                'href': href,
                'context': context
            })
            
    return issues

if __name__ == '__main__':
    search_dir = '/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales'
    all_files = []
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if file.endswith('.html'):
                all_files.append(os.path.join(root, file))
                
    print(f"Scanning {len(all_files)} HTML files for missing target='_blank'...\n")
    
    total_issues = 0
    for f_path in all_files:
        issues = check_link_targets(f_path)
        if issues:
            print(f"File: {os.path.relpath(f_path, search_dir)}")
            print(f"Found {len(issues)} links without target='_blank':")
            for idx, iss in enumerate(issues, 1):
                print(f"  {idx}. Href: {iss['href']}")
                print(f"     Tag:  {iss['tag']}")
                print(f"     Context: ... {iss['context']} ...")
            print("-" * 60)
            total_issues += len(issues)
            
    print(f"Total links missing target='_blank': {total_issues}")
