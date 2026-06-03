import os
import re

def find_links_in_html(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # We want to find <a> tags
    # Let's use a regex to find all <a> tags and check their structure
    # Match: <a ... href="..." ...> ... </a>
    pattern = re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', re.DOTALL | re.IGNORECASE)
    matches = pattern.findall(content)
    
    results = []
    for full_match in pattern.finditer(content):
        href = full_match.group(1)
        text = full_match.group(2).strip()
        outer_start = max(0, full_match.start() - 50)
        outer_end = min(len(content), full_match.end() + 50)
        context = content[outer_start:outer_end].strip()
        
        # Check if the link contains elibro, ezproxy or is a bibliography link
        # Usually, bibliography links have the URL as the text or contain ezproxy/elibro
        is_bib_link = "ezproxy" in href or "elibro" in href or "login" in href or text.startswith("http")
        
        if is_bib_link:
            # Check if this link is bolded
            # A link is bolded if the <a> tag is inside <strong>/<b> or if the text inside <a> is inside <strong>/<b>
            # Let's check both
            is_bold = False
            # Check if text is wrapped in <strong> or <b>
            if text.startswith('<strong>') or text.startswith('<b>'):
                is_bold = True
            # Check if the outer context wraps the <a> tag in <strong>
            # e.g. <strong><a ...> or similar
            # Let's extract 20 characters before the match to check for <strong>
            before = content[max(0, full_match.start()-20):full_match.start()]
            after = content[full_match.end():min(len(content), full_match.end()+20)]
            if '<strong>' in before or '<b>' in before:
                is_bold = True
                
            results.append({
                'href': href,
                'text': text,
                'is_bold': is_bold,
                'context': context,
                'start': full_match.start(),
                'end': full_match.end()
            })
            
    return results

if __name__ == '__main__':
    search_dir = '/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales'
    all_files = []
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if file.endswith('.html'):
                all_files.append(os.path.join(root, file))
                
    print(f"Checking {len(all_files)} HTML files for bibliography links...\n")
    
    for f_path in all_files:
        links = find_links_in_html(f_path)
        # We filter links that are NOT bold
        not_bold = [l for l in links if not l['is_bold']]
        if not_bold:
            print(f"File: {os.path.relpath(f_path, search_dir)}")
            print(f"Found {len(not_bold)} links NOT in bold:")
            for idx, l in enumerate(not_bold, 1):
                print(f"  {idx}. Text: {l['text']}")
                print(f"     Href: {l['href']}")
                print(f"     Context: ... {l['context']} ...")
            print("-" * 60)
