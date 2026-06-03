# -*- coding: utf-8 -*-
import os

html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Momentos/Momento Evaluativo1.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define Semana 3 block with correct suffix
semana3_old = """                                <div class="tab-pane fade" id="semana3" role="tabpanel" aria-labelledby="semana3-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">A través de su proceso de enseñanza - aprendizaje y de la apropiación del conocimiento, enfoque su aprendizaje en la actividad 3 y 4.<br><br><strong>Actividad 3: Clasificación de variables</strong><br><br>Para el desarrollo de esta actividad se puede apoyar de los recursos:<br><br>Posada, G. (2016). Capítulo 1. Conceptos generales sobre estadística. En: Elementos básicos de estadística descriptiva para el análisis de datos. <br><br>Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar:<br><br>Infografía de variables.<br><br>Clasifique todas las variables del <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> en cualitativas (nominales, ordinales) y cuantitativas (discretas o continuas) teniendo en cuenta la tabla que se encuentra en la <strong><a href="@@PLUGINFILE@@/Entregable1_Recoleccion_de_datos.docx" target="_blank" rel="noopener">plantilla</a></strong>.<br><br><strong>Actividad 4. Muestreo</strong><br><br>Revise los siguientes recursos para el desarrollo de esta actividad:<br><br>Posada, G. (2016). Capítulo 2. Introducción a los tipos de muestreo. En: Elementos básicos de estadística descriptiva para el análisis de datos. <br><br>Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar:<br><br>Presentación cálculo del tamaño muestral.<br><br>Dado que la base de datos suministrada <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> corresponde a una muestra ya definida, es important reconocer que, en algunas ocasiones, la muestra se debe calcular. Realice los dos ejercicios que se presentan a continuación: <br><br>1. Si se desea establecer una muestra representativa para estudiar la problemática de <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> a través del muestreo aleatorio simple con un nivel de confianza del 90%, un error estimado del 5% y una población de 2920 defunciones, ¿Cuál sería el tamaño de la muestra?<br>2. Si se desea establecer una muestra representativa para estudiar el problema de <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> a través del muestreo aleatorio simple, con un nivel de confianza del 91%, un error estimado del 5%, pero se desconoce el total de la población constituida mayormente por peatones, ¿Cuál sería el tamaño de la muestra?<br><br>Se debe presentar no solo el resultado sino los procedimientos o cálculos realizados para llegar a las respuestas.</p><br><br>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 1. Conceptos generales sobre estadística. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín. (pp. 11 – 21).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong><a href="@@PLUGINFILE@@/VARIABLES.pdf" target="_blank" rel="noopener">Infografía de variables</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 2. Introducción a los tipos de muestreo. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 23 -32).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Cálculo del tamaño muestral [Presentación]</strong>.</li>
                                        </ul><br><br>
                                        <p style="text-align: justify;">Realice la entrega del entregable en la plataforma. Una vez realizada la calificación recuerde tener en cuenta los comentarios de retroalimentación para los próximos entregables.</p>"""

# Wait, let's verify if the word 'importante' was correctly typed as 'importante' in the old text.
# In semana3_old from view_file: "es importante reconocer que"
# In my semana3_old variable: "es important reconocer que" -- Oh, there was a typo "important"!
# Let's fix that typo in semana3_old first.

semana3_old = semana3_old.replace("es important reconocer", "es importante reconocer")

semana3_new = """                                <div class="tab-pane fade" id="semana3" role="tabpanel" aria-labelledby="semana3-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">A través de su proceso de enseñanza - aprendizaje y de la apropiación del conocimiento, enfoque su aprendizaje en la actividad 3 y 4.<br><br><strong>Actividad 3: Clasificación de variables</strong><br><br>Para el desarrollo de esta actividad se puede apoyar de los recursos:</p><br><br>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 1. Conceptos generales sobre estadística. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín. (pp. 11 – 21).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                        </ul><br><br>
                                        <p style="text-align: justify;">Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar:</p><br><br>
                                        <ul>
                                            <li style="margin-bottom: 10px;"><strong><a href="@@PLUGINFILE@@/VARIABLES.pdf" target="_blank" rel="noopener">Infografía de variables</a></strong>.</li>
                                        </ul><br><br>
                                        <p style="text-align: justify;">Clasifique todas las variables del <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> en cualitativas (nominales, ordinales) y cuantitativas (discretas o continuas) teniendo en cuenta la tabla que se encuentra en la <strong><a href="@@PLUGINFILE@@/Entregable1_Recoleccion_de_datos.docx" target="_blank" rel="noopener">plantilla</a></strong>.<br><br><strong>Actividad 4. Muestreo</strong><br><br>Revise los siguientes recursos para el desarrollo de esta actividad:</p><br><br>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 2. Introducción a los tipos de muestreo. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 23 -32).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                        </ul><br><br>
                                        <p style="text-align: justify;">Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar:</p><br><br>
                                        <ul>
                                            <li style="margin-bottom: 10px;"><strong>Cálculo del tamaño muestral [Presentación]</strong>.</li>
                                        </ul><br><br>
                                        <p style="text-align: justify;">Dado que la base de datos suministrada <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> corresponde a una muestra ya definida, es importante reconocer que, en algunas ocasiones, la muestra se debe calcular. Realice los dos ejercicios que se presentan a continuación:<br><br>
                                        1. Si se desea establecer una muestra representativa para estudiar la problemática de <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> a través del muestreo aleatorio simple con un nivel de confianza del 90%, un error estimado del 5% y una población de 2920 defunciones, ¿Cuál sería el tamaño de la muestra?<br><br>
                                        2. Si se desea establecer una muestra representativa para estudiar el problema de <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> a través del muestreo aleatorio simple, con un nivel de confianza del 91%, un error estimado del 5%, pero se desconoce el total de la población constituida mayormente por peatones, ¿Cuál sería el tamaño de la muestra?<br><br>
                                        Se debe presentar no solo el resultado sino los procedimientos o cálculos realizados para llegar a las respuestas.</p><br><br>
                                        <p style="text-align: justify;">Realice la entrega del entregable en la plataforma. Una vez realizada la calificación recuerde tener en cuenta los comentarios de retroalimentación para los próximos entregables.</p>"""

replaced = False
if semana3_old in content:
    content = content.replace(semana3_old, semana3_new)
    replaced = True
else:
    # Try alt format (Windows carriage returns)
    semana3_old_alt = semana3_old.replace('\n', '\r\n')
    semana3_new_alt = semana3_new.replace('\n', '\r\n')
    if semana3_old_alt in content:
        content = content.replace(semana3_old_alt, semana3_new_alt)
        replaced = True

print("Semana 3 Replaced:", replaced)

if replaced:
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Momento Evaluativo 1 successfully updated with Semana 3!")
else:
    print("No updates applied.")
