# -*- coding: utf-8 -*-
import os
import re

def modify_file(path, replacements):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return False
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for target, replacement in replacements.items():
        content = content.replace(target, replacement)
    
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {path}")
        return True
    else:
        print(f"No changes needed: {path}")
        return False

# 1. Update instructions_especificas.md
instrucciones_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/4_soporte_y_reglas/instrucciones_especificas.md"
instrucciones_content = ""
if os.path.exists(instrucciones_path):
    with open(instrucciones_path, 'r', encoding='utf-8') as f:
        instrucciones_content = f.read()

    # Define the old section and new section
    old_section = """## 4. Estructura, Viñetas y Espaciado
* **Espaciado entre ítems (margin-bottom):** 
  * Si en un grupo de viñetas (`<ul>` o `<ol>`), al menos **una viñeta tiene más de 3 renglones**, o bien **dos viñetas tienen 2 renglones**, se debe aplicar un espacio de separación entre cada ítem.
  * Implementación: Añadir `style="margin-bottom: 10px;"` a cada etiqueta `<li>` de ese grupo de viñetas.
  * Si los ítems tienen un solo renglón, se dejan pegados (sin margen).
* **Separación de bloques (doble salto de línea):**
  * Ningún grupo de viñetas (`<ul>` o `<ol>`) puede quedar pegado a un párrafo adyacente (al principio o al final) que no pertenezca a las viñetas.
  * Se deben insertar etiquetas de salto de línea dobles (`<br><br>`) justo antes de abrir la lista y justo después de cerrarla."""

    new_section = """## 4. Estructura, Viñetas y Espaciado
* **Prohibición de Márgenes Inline para Separación**:
  * Queda estrictamente prohibido el uso de estilos de margen inline (`style="margin-bottom: ..."` o `style="margin-top: ..."`) en cualquier etiqueta HTML (`p`, `li`, `h4`, etc.) para forzar la separación visual.
  * Si es estrictamente necesario separar elementos de forma manual y no existe espaciado nativo, se debe utilizar únicamente la etiqueta `<br>`.
  * Los párrafos (`<p>`) ya cuentan con separación automática en Moodle, por lo que queda prohibido insertar etiquetas `<br>` o márgenes inline entre ellos.
* **Prohibición de saltos de línea inter-bloque (Prevención de Doble Espacio)**:
  * Queda estrictamente prohibido colocar etiquetas de salto de línea (`<br>` o `<br><br>`) directamente entre elementos de bloque HTML (por ejemplo, entre `</p>` y `<ul>`, o entre `</ul>` y `<p>`).
  * Las listas y párrafos deben limitarse a abrirse y cerrarse consecutivamente (ej. `</p><ul>` o `</ul><p>`). Moodle aplica márgenes por defecto a los bloques; colocar saltos de línea intermedios produce una separación visual excesiva."""

    # Normalize line endings to avoid issues
    instrucciones_content_norm = instrucciones_content.replace('\r\n', '\n')
    old_section_norm = old_section.replace('\r\n', '\n')
    new_section_norm = new_section.replace('\r\n', '\n')

    if old_section_norm in instrucciones_content_norm:
        instrucciones_content_norm = instrucciones_content_norm.replace(old_section_norm, new_section_norm)
        with open(instrucciones_path, 'w', encoding='utf-8') as f:
            f.write(instrucciones_content_norm)
        print("Updated instrucciones_especificas.md successfully!")
    else:
        # Try a flexible regex replacement
        pattern = r'## 4\. Estructura, Viñetas y Espaciado.*?## 5\. Botones de Envío de Entregables'
        match = re.search(pattern, instrucciones_content_norm, re.DOTALL)
        if match:
            replacement_text = new_section_norm + "\n\n---\n\n## 5. Botones de Envío de Entregables"
            # We want to replace everything from ## 4. to ## 5.
            instrucciones_content_norm = re.sub(pattern, replacement_text, instrucciones_content_norm, flags=re.DOTALL)
            with open(instrucciones_path, 'w', encoding='utf-8') as f:
                f.write(instrucciones_content_norm)
            print("Updated instrucciones_especificas.md via regex successfully!")
        else:
            print("Could not find section in instrucciones_especificas.md")

# 2. Update reglas-transversales.md in the four skill directories
skills = ['geo-entregable', 'geo-glosario', 'geo-linea-tiempo', 'geo-momento']
for skill in skills:
    path = f"/Users/buc-cvudes-medios1/Documents/GEO/.agent/skills/{skill}/references/reglas-transversales.md"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read().replace('\r\n', '\n')
        
        # Replace the list spacing rule
        old_rule = "- Si una viñeta supera 3 renglones, o dos viñetas tienen 2 renglones → `style=\"margin-bottom: 10px;\"`\n  en cada `<li>` del grupo. (Es visual: si dudas, emite FLAG en vez de adivinar.)"
        new_rule = "- Queda estrictamente prohibido usar estilos inline de margen (`style=\"margin-bottom: ...\"` o `style=\"margin-top: ...\"`) en cualquier etiqueta HTML (`p`, `li`, `h4`, etc.) para forzar la separación visual.\n- Para separación vertical manual donde sea estrictamente necesario y no exista separación nativa, usar únicamente la etiqueta `<br>`.\n- Los párrafos (`<p>`) ya cuentan con separación automática en Moodle, por lo que no deben separarse entre sí con etiquetas `<br>`."
        
        content = content.replace(old_rule, new_rule)
        
        # Clean inline margins from rules-transversales code examples
        content = content.replace('style="margin-bottom: 10px;"', '')
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated reglas-transversales.md for skill: {skill}")

# 3. Update verify.py with the new validation checks
verify_path = "/Users/buc-cvudes-medios1/Documents/GEO/verify.py"
if os.path.exists(verify_path):
    with open(verify_path, 'r', encoding='utf-8') as f:
        verify_content = f.read().replace('\r\n', '\n')
        
    # Check if we already added the rule
    if "Check for forbidden positive inline margins" not in verify_content:
        # Insert check after the italic inline style check
        target_check = """    # 1. Check for italic inline style
    if 'font-style: italic' in content or 'font-style:italic' in content:
        errors.append("Forbidden font-style: italic style found.")"""
        
        new_check = """    # 1. Check for italic inline style
    if 'font-style: italic' in content or 'font-style:italic' in content:
        errors.append("Forbidden font-style: italic style found.")
        
    # 1.5. Check for forbidden positive inline margins
    # Match any style attribute with margin-bottom, margin-top, margin-left, margin-right, or margin
    # having a positive value (e.g. 10px, 16px, 36px, 0.5rem, etc., excluding 0, 0px, 0rem)
    margin_matches = re.finditer(r'style="[^"]*margin(-(bottom|top|left|right))?\\s*:\\s*(?!(0\\b|0px\\b|0rem\\b))[^;"]+;?[^"]*"', content, re.IGNORECASE)
    for match in margin_matches:
        errors.append(f"Forbidden inline margin style found: {match.group()}")"""
        
        verify_content = verify_content.replace(target_check, new_check)
        with open(verify_path, 'w', encoding='utf-8') as f:
            f.write(verify_content)
        print("Updated verify.py successfully!")
    else:
        print("verify.py already contains margin check")

# 4. Clean margin styles from all HTML files
base_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales"
files_to_clean = [
    os.path.join(base_dir, "Introduccion al curso/Introduccion al curso.html"),
    os.path.join(base_dir, "Introduccion al curso/Información del Curso botones.html"),
    os.path.join(base_dir, "Linea del tiempo/Lineadeltiempo.html"),
    os.path.join(base_dir, "Momentos/Momento Evaluativo1.html"),
    os.path.join(base_dir, "Momentos/Momento Evaluativo2.html"),
    os.path.join(base_dir, "Entregables/Entregalbe Avance 1.html"),
    os.path.join(base_dir, "Entregables/Entregalbe Avance 2.html"),
    os.path.join(base_dir, "Entregables/Entregalbe Avance 3.html"),
    os.path.join(base_dir, "Entregables/Entregalbe Avance 4.html"),
    os.path.join(base_dir, "Entregables/Entregable Producto Fina (Entregalbe Avance 5).html")
]

for filepath in files_to_clean:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace inline margin declarations that are positive (e.g. margin-bottom: 10px; or margin-top: 16px;)
        # We target style="... margin-bottom: 10px; ..."
        # Specifically, we find any substring matching margin-bottom/top/etc.: value; inside style="..."
        # Let's match: \s*margin(-(bottom|top|left|right))?\s*:\s*(?!(0\b|0px\b|0rem\b))[^;"]+;?
        pattern = r'\s*margin(-(bottom|top|left|right))?\s*:\s*(?!(0\b|0px\b|0rem\b))[^;"]+;?'
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)
        
        # Clean up empty style attributes: style="" -> empty
        # Wait, if we have style="text-align: justify; " (with trailing spaces or semicolons), let's normalize
        content = re.sub(r'style="\s*;?\s*"', '', content, flags=re.IGNORECASE)
        # Normalize double spaces inside style attribute if any remain
        # E.g. style="text-align: justify;   font-weight: bold;"
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Cleaned margins in HTML: {filepath}")
        else:
            print(f"No positive margins found in: {filepath}")

print("\n--- Corrections Complete ---")
