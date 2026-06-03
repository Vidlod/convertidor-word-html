import os

# Define files and replacements
replacements = {
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Momentos/Momento Evaluativo1.html": [
        (
            'condiciones formales de entrega:</p>\n                        <ul>',
            'condiciones formales de entrega:</p><br><br>\n                        <ul>'
        ),
        (
            '</ul>\n                        <p style="text-align: justify;">Tenga en cuenta la siguiente situación hipotética:',
            '</ul><br><br>\n                        <p style="text-align: justify;">Tenga en cuenta la siguiente situación hipotética:'
        )
    ],
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Momentos/Momento Evaluativo2.html": [
        (
            'condiciones formales de entrega:</p>\n                        <ul>',
            'condiciones formales de entrega:</p><br><br>\n                        <ul>'
        ),
        (
            '</ul>\n                        <p style="text-align: justify;">Al finalizar cada informe',
            '</ul><br><br>\n                        <p style="text-align: justify;">Al finalizar cada informe'
        )
    ],
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Entregables/Entregalbe Avance 1.html": [
        (
            'referencias bibliográficas con normas APA).</p>\n                <ul>',
            'referencias bibliográficas con normas APA).</p><br><br>\n                <ul>'
        )
    ],
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Entregables/Entregalbe Avance 2.html": [
        (
            'referencias bibliográficas con normas APA).</p>\n                <ul>',
            'referencias bibliográficas con normas APA).</p><br><br>\n                <ul>'
        )
    ],
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Entregables/Entregalbe Avance 3.html": [
        (
            'referencias bibliográficas con normas APA).</p>\n                <ul>',
            'referencias bibliográficas con normas APA).</p><br><br>\n                <ul>'
        )
    ],
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Entregables/Entregalbe Avance 4.html": [
        (
            'referencias bibliográficas con normas APA).</p>\n                <ul>',
            'referencias bibliográficas con normas APA).</p><br><br>\n                <ul>'
        )
    ],
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Entregables/Entregable Producto Fina (Entregalbe Avance 5).html": [
        (
            'referencias bibliográficas con normas APA).</p>\n                <ul>',
            'referencias bibliográficas con normas APA).</p><br><br>\n                <ul>'
        )
    ],
    "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Introduccion al curso/Introduccion al curso.html": [
        (
            '<strong>Unidad 1: Investigación estadística</strong>\n                        <ul>',
            '<strong>Unidad 1: Investigación estadística</strong><br><br>\n                        <ul>'
        ),
        (
            '</ul><br>\n                        <strong>Unidad 2: Fundamentos de estadística</strong>\n                        <ul>',
            '</ul><br><br>\n                        <strong>Unidad 2: Fundamentos de estadística</strong><br><br>\n                        <ul>'
        ),
        (
            '</ul><br>\n                        <strong>Unidad 3: Medidas estadísticas univariantes</strong>\n                        <ul>',
            '</ul><br><br>\n                        <strong>Unidad 3: Medidas estadísticas univariantes</strong><br><br>\n                        <ul>'
        ),
        (
            '</ul><br>\n                        <strong>Unidad 4: Medidas estadísticas bivariantes</strong>\n                        <ul>',
            '</ul><br><br>\n                        <strong>Unidad 4: Medidas estadísticas bivariantes</strong><br><br>\n                        <ul>'
        )
    ]
}

for path, pairs in replacements.items():
    print(f"Updating: {path}")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    original_len = len(content)
    for old, new in pairs:
        if old not in content:
            print(f"  WARNING: target content not found in {path}")
            # Try with single newline or carriage return if any
            old_alt = old.replace('\n', '\r\n')
            new_alt = new.replace('\n', '\r\n')
            if old_alt in content:
                content = content.replace(old_alt, new_alt)
            else:
                print("  ERROR: Alt replacement also not found.")
        else:
            content = content.replace(old, new)
            
    if len(content) != original_len:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  Successfully updated.")
    else:
        print("  No changes made.")
