import re
from html.parser import HTMLParser

class Validator(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.errors = []
        self.tag_stack = []
        self.in_li = False

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        attrs_dict = dict(attrs)
        
        if tag == 'li':
            self.in_li = True
        
        if tag == 'p' and self.in_li:
            self.errors.append(f"Nested <p> inside <li> tag found.")
            
        if tag == 'a':
            href = attrs_dict.get('href', '')
            if href and not href.startswith('#'):
                target = attrs_dict.get('target', '')
                rel = attrs_dict.get('rel', '')
                if target != '_blank':
                    self.errors.append(f"Link to '{href}' does not have target='_blank' (target={repr(target)}).")
                if 'noopener' not in rel:
                    self.errors.append(f"Link to '{href}' does not have 'noopener' in rel (rel={repr(rel)}).")

    def handle_endtag(self, tag):
        if self.tag_stack:
            self.tag_stack.pop()
        if tag == 'li':
            self.in_li = False

    def handle_data(self, data):
        # Check consecutive spaces per line, ignoring leading/trailing indentations
        lines = data.split('\n')
        for line in lines:
            line_str = line.strip()
            if '   ' in line_str: # 3 or more spaces
                self.errors.append(f"More than 2 consecutive spaces in text: {repr(line_str)}")

def validate_file(path):
    print(f"\nValidating: {path}")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    errors = []
    
    # Check consecutive br
    br_matches = re.findall(r'<br\s*/?>\s*<br\s*/?>\s*<br\s*/?>', content, re.IGNORECASE)
    if br_matches:
        errors.append(f"Found more than 2 consecutive <br> tags: {len(br_matches)} instances.")
        
    # Check trailing br inside list elements or close elements
    trailing_br = re.findall(r'<br\s*/?>\s*</(li|ul|ol|p|div|tr|td)>', content, re.IGNORECASE)
    if trailing_br:
        errors.append(f"Found trailing <br> immediately before closing tag: {trailing_br}")

    # Parser validation
    parser = Validator(path)
    parser.feed(content)
    errors.extend(parser.errors)
    
    if not errors:
        print("SUCCESS: File is 100% compliant with rules.")
    else:
        print("ERRORS FOUND:")
        for err in errors:
            print(f"- {err}")
    return len(errors) == 0

if __name__ == "__main__":
    p1 = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Introduccion al curso/Introduccion al curso.html"
    p2 = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Introduccion al curso/Información del Curso botones.html"
    p3 = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Linea del tiempo/Lineadeltiempo.html"
    
    v1 = validate_file(p1)
    v2 = validate_file(p2)
    v3 = validate_file(p3)
    
    if v1 and v2 and v3:
        print("\nALL FILES ARE COMPLIANT!")
    else:
        print("\nCOMPLIANCE FAILURE IN ONE OR MORE FILES.")
