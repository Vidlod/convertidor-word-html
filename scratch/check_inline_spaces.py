import re

html_files = [
    "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo1.html",
    "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo2.html"
]

inline_tags = ["a", "strong", "span", "em", "i", "b", "u"]

for html_path in html_files:
    print(f"\nAnalyzing inline tags in: {html_path}")
    with open(html_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines, 1):
        # Find if line contains open inline tags that are not closed on the same line,
        # or if the tags contain multi-line text.
        # We can also check if a line has trailing spaces or spaces before/after inline elements.
        for tag in inline_tags:
            # Check for tags spanning multiple lines (starts with tag but doesn't close on the same line)
            open_pattern = re.compile(rf'<{tag}\b[^>]*>[^<]*$', re.IGNORECASE)
            if open_pattern.search(line):
                print(f"  [SPANNING] Line {i}: <{tag}> tag starts but does not close on this line.")
                # print snippet
                print(f"    {repr(line.strip())}")
                
            # Check for multiple spaces or spaces around tag boundaries
            double_space_pattern = re.compile(r'\s{2,}')
            # We ignore indentation spaces at start of line
            clean_line = line.lstrip()
            # If there's an inline tag and multiple spaces inside or around it
            if tag in clean_line:
                # check if there are 2 or more spaces in the text part
                # e.g. text between tags
                matches = list(re.finditer(r'>([^<]+)<', clean_line))
                for m in matches:
                    text = m.group(1)
                    if "  " in text:
                        print(f"  [DOUBLE SPACE IN TEXT] Line {i}: Double space inside tag content.")
                        print(f"    {repr(clean_line.strip())}")
                        
                # check for spaces inside inline tag attributes
                # e.g. href="@@PLUGINFILE@@/Anexo1_Formato_Cuadro comparativo.docx" has space in the filename!
                # Wait, spaces in filenames inside href should be URL encoded as %20 or NFD counterpart!
                href_matches = re.findall(r'href=["\']([^"\']+)["\']', clean_line)
                for h in href_matches:
                    if " " in h:
                        print(f"  [SPACE IN URL] Line {i}: URL contains raw space: {h}")
                        print(f"    {repr(clean_line.strip())}")
