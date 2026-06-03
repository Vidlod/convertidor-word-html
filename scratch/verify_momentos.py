import re
from html.parser import HTMLParser
import sys

class validator(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.errors = []
        self.tag_stack = []
        self.in_li = False
        self.current_li_text = ""
        self.li_attrs = {}

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append((tag, attrs))
        attrs_dict = dict(attrs)
        
        if tag == 'li':
            self.in_li = True
            self.current_li_text = ""
            self.li_attrs = attrs_dict
            
        if tag == 'p' and self.in_li:
            self.errors.append(f"Nested <p> inside <li> tag found.")
            
        if tag == 'em':
            self.errors.append(f"Forbidden italic tag <em> found.")
            
        if tag == 'i':
            pass
            
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
            is_nav = 'nav-item' in self.li_attrs.get('class', '')
            if not is_nav:
                for ptag, pattrs in self.tag_stack:
                    pattrs_dict = dict(pattrs)
                    if 'nav' in pattrs_dict.get('class', ''):
                        is_nav = True
                        break
            
            if not is_nav:
                text = self.current_li_text.strip()
                clean_text = re.sub(r'<[^>]*>', '', text).strip()
                if clean_text:
                    if not clean_text.endswith('.') and not clean_text.endswith('?') and not clean_text.endswith(':'):
                        self.errors.append(f"<li> element text does not end with a period/question mark: {repr(clean_text[:40])}...")

    def handle_data(self, data):
        if self.in_li:
            self.current_li_text += data
            
        if self.tag_stack and self.tag_stack[-1][0] == 'i':
            if data.strip():
                self.errors.append(f"Forbidden italic text inside <i> tag: {repr(data.strip())}")

        lines = data.split('\n')
        for line in lines:
            line_str = line.strip()
            if '   ' in line_str: # 3 or more spaces
                self.errors.append(f"More than 2 consecutive spaces in text: {repr(line_str)}")

def validate_file(path):
    print(f"\n========================================\nValidating: {path}\n========================================")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    errors = []
    
    # 1. Check for italic inline style
    if 'font-style: italic' in content or 'font-style:italic' in content:
        errors.append("Forbidden font-style: italic style found.")
        
    # 2. Check for modulo/módulo (case insensitive, word boundary)
    modulos = re.findall(r'\bmódulo[s]?\b|\bmodulo[s]?\b', content, re.IGNORECASE)
    if modulos:
        errors.append(f"Found forbidden terminology (módulo/modulo): {modulos}")
        
    # 3. Check for "tablero de anotaciones" (case insensitive)
    anotaciones = re.findall(r'tablero de anotaciones', content, re.IGNORECASE)
    if anotaciones:
        errors.append(f"Found forbidden reference to 'tablero de anotaciones': {anotaciones}")
        
    # 4. Check for Avance 5
    avance5 = re.findall(r'Avance 5', content, re.IGNORECASE)
    if avance5:
        errors.append(f"Found 'Avance 5' instead of 'Producto Final': {avance5}")

    # 4b. Check for unlinked key documents in paragraphs (Formato/Forma Rule)
    # Database: "Anexo 1" (excluding already-linked mentions)
    db_matches = re.finditer(r'Anexo\s*1\b', content, re.IGNORECASE)
    for match in db_matches:
        idx = match.start()
        surrounding = content[max(0, idx - 500):idx + len(match.group()) + 500]
        if 'href="@@PLUGINFILE@@/' not in surrounding:
            snippet = content[max(0, idx - 40):idx + len(match.group()) + 40]
            errors.append(f"Potential unlinked database reference '{match.group()}' around: ...{snippet.strip()}...")

    # Templates: "plantilla" (excluding "plantilla del entregable" if already linked, and typical phrases)
    template_matches = re.finditer(r'\bplantilla\b', content, re.IGNORECASE)
    for match in template_matches:
        idx = match.start()
        surrounding = content[max(0, idx - 500):idx + len(match.group()) + 500]
        if 'href="@@PLUGINFILE@@/' not in surrounding:
            snippet = content[max(0, idx - 40):idx + len(match.group()) + 40]
            errors.append(f"Potential unlinked template reference '{match.group()}' around: ...{snippet.strip()}...")

    # Syllabus/Rubric (excluding bibliography or button containers)
    doc_matches = re.finditer(r'\bsyllabus\b|\brúbrica\b', content, re.IGNORECASE)
    for match in doc_matches:
        idx = match.start()
        surrounding = content[max(0, idx - 500):idx + len(match.group()) + 500]
        # Ignore if part of a button or bibliography URL or if already linked
        if 'href="@@PLUGINFILE@@/' not in surrounding and '<button' not in surrounding and '</button>' not in surrounding:
            snippet = content[max(0, idx - 40):idx + len(match.group()) + 40]
            errors.append(f"Potential unlinked document reference '{match.group()}' around: ...{snippet.strip()}...")

    # 5. Check consecutive br
    br_matches = re.findall(r'<br\s*/?>\s*<br\s*/?>\s*<br\s*/?>', content, re.IGNORECASE)
    if br_matches:
        errors.append(f"Found more than 2 consecutive <br> tags: {len(br_matches)} instances.")
        
    # 5c. Check for inter-block br tags (double spacing in Moodle)
    inter_block_br = re.findall(r'</(p|ul|ol|h[1-6]|div|table|li)>\s*<br\s*/?>(\s*<br\s*/?>)*\s*<(p|ul|ol|h[1-6]|div|table|li)\b', content, re.IGNORECASE)
    if inter_block_br:
        errors.append(f"Found {len(inter_block_br)} inter-block <br> tags (e.g. between closing and opening block tags).")
        
    # 6. Check trailing br inside list elements or close elements
    trailing_br = re.findall(r'<br\s*/?>\s*</(li|ul|ol|p|div|tr|td)>', content, re.IGNORECASE)
    if trailing_br:
        errors.append(f"Found trailing <br> immediately before closing tag: {trailing_br}")

    # 7. Check buttons text and periods for weekly buttons only
    buttons = re.findall(r'<button[^>]*>(.*?)</button>', content, re.DOTALL)
    for btn in buttons:
        btn_clean = re.sub(r'<[^>]*>', '', btn).strip()
        btn_collapsed = " ".join(btn_clean.split())
        # Weekly button check (starts with Enviar and ends with Avance/Producto Final)
        if btn_collapsed.startswith("Enviar") and not btn_collapsed.startswith("Enviar Entregable Avance"):
            if not btn_collapsed.endswith('.'):
                errors.append(f"Delivery button text does not end with a period: {repr(btn_collapsed)}")

    # 7.5. Check for forbidden use of "formato" (Formato vs Forma rule)
    text_content = re.sub(r'<[^>]*>', ' ', content)
    for match in re.finditer(r'\bformato[s]?\b', text_content, re.IGNORECASE):
        idx = match.start()
        test_str = text_content[idx:idx+50].strip()
        test_str_collapsed = " ".join(test_str.split())
        valid_pattern = r'^formato[s]?\s+(pdf|word|mp4|doc|docx|xls|xlsx|zip|rar|audio|video|de\s+(audio|video|archivo))\b'
        if not re.match(valid_pattern, test_str_collapsed, re.IGNORECASE):
            snippet = text_content[max(0, idx - 30):idx + 50]
            snippet_clean = " ".join(snippet.split())
            errors.append(f"Forbidden use of word 'formato' (must use 'forma' unless specifying file extensions like PDF/Word) around: ...{snippet_clean}...")

    # 7.8. Check that paragraph breaks (puntos apartes) from AAA are respected in Momentos descriptions
    if "Momento Evaluativo1.html" in path:
        if "Al finalizar cada informe" not in content:
            errors.append("Missing paragraph 'Al finalizar cada informe...' in Momento 1 description.")
        
        checks = [
            ("entregar dos informes en formato PDF donde se consolide el desarrollo de todas las actividades propuestas.", "Los informes deben cumplir con las siguientes condiciones"),
            ("de la problemática de estudio.", "La problemática de estudio que le fue asignada"),
            ("de cada entregable.", "No es casualidad que cada uno de los entregables"),
            ("utilizando Excel (Office) o el software Estadístico Infostat.", "Complemente su proceso de enseñanza"),
            ("Video Tutorial para la descarga del software Infostat.", "Enlace para la descarga del Infostat")
        ]
        for p1, p2 in checks:
            idx1 = content.find(p1)
            idx2 = content.find(p2)
            if idx1 != -1 and idx2 != -1:
                between = content[idx1 + len(p1):idx2]
                if "</p>" not in between and "<br" not in between:
                    errors.append(f"Punto aparte not respected in Momento 1: '{p1[:30]}...' and '{p2[:30]}...' are merged in the same paragraph.")

    if "Momento Evaluativo2.html" in path:
        checks = [
            ("utilizando Excel (Office) o el software Estadístico Infostat.", "Complemente su proceso de enseñanza"),
            ("Video Tutorial para la descarga del software Infostat.", "Enlace para la descarga del Infostat")
        ]
        for p1, p2 in checks:
            idx1 = content.find(p1)
            idx2 = content.find(p2)
            if idx1 != -1 and idx2 != -1:
                between = content[idx1 + len(p1):idx2]
                if "</p>" not in between and "<br" not in between:
                    errors.append(f"Punto aparte not respected in Momento 2: '{p1[:30]}...' and '{p2[:30]}...' are merged in the same paragraph.")

    # 8. Parser validation
    parser = validator(path)
    parser.feed(content)
    errors.extend(parser.errors)
    
    if not errors:
        print("SUCCESS: File is 100% compliant with rules.")
        return True
    else:
        print("ERRORS FOUND:")
        for err in errors:
            print(f"- {err}")
        return False

if __name__ == "__main__":
    p1 = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Momentos/Momento Evaluativo1.html"
    p2 = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Momentos/Momento Evaluativo2.html"
    
    v1 = validate_file(p1)
    v2 = validate_file(p2)
    
    if v1 and v2:
        print("\nALL MOMENTO FILES ARE COMPLIANT!")
        sys.exit(0)
    else:
        print("\nCOMPLIANCE FAILURE IN ONE OR MORE FILES.")
        sys.exit(1)
