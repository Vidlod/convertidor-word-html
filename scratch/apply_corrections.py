import re

def apply_corrections(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    print("Original content length:", len(content))
    
    # 1. URL replacements (draftfile.php to @@PLUGINFILE@@)
    pattern = r'https://virtual\.udes\.edu\.co/draftfile\.php/[^\s\"<>]+/([^\s\"<>/]+\.[a-zA-Z0-9]+)'
    content, count = re.subn(pattern, r'@@PLUGINFILE@@/\1', content)
    print(f"Replaced {count} draftfile.php URLs")
    
    # 2. Fix typo "activdades" if it exists, but wait, the typo was in my replacement code.
    # In the original file it is "actividades" (line 133: "...actividades propuestas de cada entregable.")
    # Let's check if there is any "activdades" in the file now:
    content, count = re.subn(r'activdades', 'actividades', content)
    print(f"Fixed {count} instances of 'activdades'")
    
    # 3. Trailing periods on weekly buttons
    # Let's find the exact weekly buttons:
    # "Enviar Avance 1" and "Enviar Avance 2"
    # Semana 3 button (Avance 1):
    avance1_btn_old = """<button type="button" class="btn btn-outline-primary btn-lg"
                                                     aria-pressed="true" role="button">
                                                     <span class="spinner-grow spinner-grow-sm"></span> Enviar Avance 1
                                                 </button>"""
    avance1_btn_new = """<button type="button" class="btn btn-outline-primary btn-lg"
                                                     aria-pressed="true" role="button">
                                                     <span class="spinner-grow spinner-grow-sm"></span> Enviar Avance 1.
                                                 </button>"""
                                                 
    # Semana 5 button (Avance 2):
    avance2_btn_old = """<button type="button" class="btn btn-outline-primary btn-lg"
                                                     aria-pressed="true" role="button">
                                                     <span class="spinner-grow spinner-grow-sm"></span> Enviar Avance 2
                                                 </button>"""
    avance2_btn_new = """<button type="button" class="btn btn-outline-primary btn-lg"
                                                     aria-pressed="true" role="button">
                                                     <span class="spinner-grow spinner-grow-sm"></span> Enviar Avance 2.
                                                 </button>"""
                                                 
    if avance1_btn_old in content:
        content = content.replace(avance1_btn_old, avance1_btn_new)
        print("Added period to weekly button 1")
    else:
        # try standard spacing
        content, count = re.subn(r'Enviar Avance 1\s*\n\s*</button>', r'Enviar Avance 1.\n</button>', content)
        print(f"Regex added period to button 1: {count} matches")
        
    if avance2_btn_old in content:
        content = content.replace(avance2_btn_old, avance2_btn_new)
        print("Added period to weekly button 2")
    else:
        content, count = re.subn(r'Enviar Avance 2\s*\n\s*</button>', r'Enviar Avance 2.\n</button>', content)
        print(f"Regex added period to button 2: {count} matches")

    # 4. RED redundancy in Semana 1: remove Syllabus and Mapa mental from the list
    # We will look for the exact HTML block in Semana 1:
    red_list_old = """                                        <ul>
                                            <li style="margin-bottom: 10px;"><strong><a
                                                        href="@@PLUGINFILE@@/Mapa_Curso_Estadistica.pdf"
                                                        target="_blank" rel="noopener">Mapa mental Estadística
                                                        Descriptiva</a></strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong><a
                                                        href="@@PLUGINFILE@@/SYLLABUS_Estadistica_Descriptiva.pdf"
                                                        target="_blank" rel="noopener">Syllabus del curso Estadística
                                                        Descriptiva</a></strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Video de presentación y bienvenida
                                                    del curso Estadística Descriptiva</strong>.</li>
                                        </ul>"""
                                        
    # Let's normalize space to do string replace:
    # We will search for a simplified version of the list that is unique to semana 1:
    target_pattern = r'<ul>\s*<li[^>]*><strong><a\s+href="@@PLUGINFILE@@/Mapa_Curso_Estadistica\.pdf"[^>]*>Mapa mental Estadística\s+Descriptiva</a></strong>\.</li>\s*<li[^>]*><strong><a\s+href="@@PLUGINFILE@@/SYLLABUS_Estadistica_Descriptiva\.pdf"[^>]*>Syllabus del curso Estadística\s+Descriptiva</a></strong>\.</li>\s*<li[^>]*><strong>Video de presentación y bienvenida\s+del curso Estadística Descriptiva</strong>\.</li>\s*</ul>'
    match = re.search(target_pattern, content)
    if match:
        new_list = """<ul>
                                            <li style="margin-bottom: 10px;"><strong>Video de presentación y bienvenida del curso Estadística Descriptiva</strong>.</li>
                                        </ul>"""
        content = content.replace(match.group(), new_list)
        print("Removed redundant REDs from Semana 1 list (via regex)")
    else:
        # Try direct string replace with slightly flexible whitespaces
        print("WARNING: RED list pattern not matched, trying fallback replace")
        # Let's do a fallback regex replacing the exact block of text
        fallback_pattern = r'Mapa mental Estadística\s*Descriptiva.*?Syllabus del curso Estadística\s*Descriptiva.*?Video de presentación y bienvenida\s*del curso Estadística Descriptiva'
        # Let's find the <ul>...</ul> containing this
        ul_match = re.search(r'<ul>\s*<li[^>]*><strong><a[^>]*>Mapa mental.*?Video de presentación.*?</li>\s*</ul>', content, re.DOTALL)
        if ul_match:
            new_list = """<ul>
                                            <li style="margin-bottom: 10px;"><strong>Video de presentación y bienvenida del curso Estadística Descriptiva</strong>.</li>
                                        </ul>"""
            content = content.replace(ul_match.group(), new_list)
            print("Removed redundant REDs from Semana 1 list (via fallback regex)")
        else:
            print("ERROR: Fallback regex also failed!")
            
    # 5. Insert FLAG for the forum social
    content, count = re.subn(
        r'foro social',
        r'foro social <!-- FLAG: dato-faltante Falta enlace para "foro social" -->',
        content
    )
    print(f"Flagged {count} instances of 'foro social'")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Corrections applied successfully!")

if __name__ == '__main__':
    apply_corrections("PLANTILLA_CURSO/3_paginas_finales/Momentos/Momento Evaluativo1.html")
