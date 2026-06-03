import os
import re
import sys

def preprocesar_archivo(file_path):
    print(f"\nProcesando: {os.path.basename(file_path)}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # 1. Regla 12 (Tablero de Anotaciones): Quitar "a través del tablero de anotaciones" y "en el tablero de anotaciones"
    content = re.sub(r'\ba\s+través\s+del\s+tablero\s+de\s+anotaciones\b', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\ben\s+el\s+tablero\s+de\s+anotaciones\b', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\ba\s+traves\s+del\s+tablero\s+de\s+anotaciones\b', '', content, flags=re.IGNORECASE)
    content = re.sub(r' +', ' ', content)
    
    # 2. Regla 10 (Trailing spaces/breaks): Quitar <br> antes de etiquetas de cierre de bloque
    # Esto busca uno o más tags <br> al final de párrafos, listas, celdas o divisiones y los elimina
    pattern = r'(?:<br\s*/?>\s*)+(\s*</(?:div|li|ul|ol|p)>)'
    content = re.sub(pattern, r'\1', content, flags=re.IGNORECASE)
    
    # 3. Quitar espacios excesivos consecutivos en el texto (más de 2 espacios) line-by-line
    # Preservando la indentación de la estructura HTML al principio de las líneas
    lines = content.splitlines()
    for idx, line in enumerate(lines):
        match = re.search(r'^(\s*)', line)
        indent = match.group(1) if match else ''
        text_part = line[len(indent):]
        # Reemplazar 3 o más espacios en el texto por exactamente 2 espacios
        cleaned_text = re.sub(r' {3,}', '  ', text_part)
        lines[idx] = indent + cleaned_text
    content = "\n".join(lines)
    
    # 4. Normalizar enlaces locales a formato portable Moodle (@@PLUGINFILE@@)
    # Convierte enlaces locales tipo href="Anexo1.pdf" a href="@@PLUGINFILE@@/Anexo1.pdf"
    def href_replacer(match):
        url = match.group(1)
        if url.startswith(('http', '#', 'mailto', 'tel', '@@PLUGINFILE@@')):
            return match.group(0)
        filename = os.path.basename(url)
        return f'href="@@PLUGINFILE@@/{filename}"'
        
    content = re.sub(r'href="([^"]+)"', href_replacer, content, flags=re.IGNORECASE)
    
    # 5. Desvincular recursos externos no locales (como OneDrive, SharePoint y Google Drive)
    # Reemplaza la etiqueta <a> por <strong>Text</strong> si apunta a nubes externas
    def drive_unlinker(match):
        url = match.group(1)
        text = match.group(2)
        if any(domain in url.lower() for domain in ['sharepoint.com', 'onedrive', 'drive.google.com']):
            # Quitar etiquetas strong redundantes dentro del texto
            clean_text = re.sub(r'</?strong>', '', text, flags=re.IGNORECASE)
            return f'<strong>{clean_text}</strong>'
        return match.group(0)
        
    content = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', drive_unlinker, content, flags=re.IGNORECASE | re.DOTALL)
    
    if content != original:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  [MODIFICADO] Guardado con éxito.")
    else:
        print("  [SIN CAMBIOS] El archivo ya cumple las normas.")

if __name__ == "__main__":
    # If a path is provided as argument, process it. Otherwise, search files in 3_paginas_finales/
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        # Default target path
        target = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../3_paginas_finales"))
        
    if os.path.isfile(target):
        preprocesar_archivo(target)
    elif os.path.isdir(target):
        print(f"Buscando archivos HTML en: {target}")
        for root, dirs, files in os.walk(target):
            for file in files:
                if file.endswith(".html"):
                    preprocesar_archivo(os.path.join(root, file))
    else:
        print(f"Ruta no válida: {target}")
