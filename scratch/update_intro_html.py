import os
import re

html_path = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Introduccion al curso/Introduccion al curso.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Tab 1 replacement: Resultado de Aprendizaje y Dimensiones
pattern_tab1 = r'<div class="card-body p-lg-5 rounded bg-light" style="border-width: 0px;">.*?</div>\s*</div>'
replacement_tab1 = """<div class="card-body p-lg-5 rounded bg-light" style="border-width: 0px;">
                                        <h3 class="h5">Resultado de Aprendizaje</h3>
                                        <p align="justify">Resuelve problemas relacionados con el análisis e interpretación de datos para apoyar la toma de decisiones teniendo en cuenta los fundamentos y técnicas de la estadística descriptiva.</p>
                                        <h3 class="h5">Dimensiones del resultado de aprendizaje</h3>
                                        <ul>
                                            <li style="margin-bottom: 10px;">
                                                <div align="justify"><strong>Cognitiva (saber): </strong>expone planteamientos estadísticos formales de una situación problema.</div>
                                            </li>
                                            <li style="margin-bottom: 10px;">
                                                <div align="justify"><strong>Actitudinal (ser): </strong>analiza variables relacionadas con un problema estadístico.</div>
                                            </li>
                                            <li>
                                                <div align="justify"><strong>Procedimental (hacer): </strong>propone soluciones basadas en el análisis de datos y representaciones de estos.</div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>"""

content, count = re.subn(pattern_tab1, replacement_tab1, content, flags=re.DOTALL)
print(f"Tab 1 replaced: {count} times")

# Tab 1 image replacement: Alt text and make it portable or set clean alt
pattern_img = r'<img\s+src="https://virtual\.udes\.edu\.co/draftfile\.php/7655/user/draft/179301487/Imagen-general-del-curso%20%281%29\.jpg"\s+alt="[^"]*"\s+width="866"\s+height="1300"\s+style="[^"]*"\s+class="[^"]*">'
replacement_img = '<img src="@@PLUGINFILE@@/Imagen-general-del-curso.jpg" alt="Estadística Descriptiva" width="866" height="1300" style="border-radius:0.5rem; transform: rotate(3deg);" class="img-fluid atto_image_button_text-bottom">'

content, count = re.subn(pattern_img, replacement_img, content)
print(f"Tab 1 image replaced: {count} times")

# Tab 2 replacement: Detalles del Curso table
pattern_tab2 = r'<table class="table table-bordered">.*?</table>'
# We want to replace the first table in v-pills-profile
# Let's locate the tab pane for profile
profile_start = content.find('id="v-pills-profile"')
if profile_start != -1:
    # find table within it
    table_match = re.search(r'<table class="table table-bordered">.*?</table>', content[profile_start:], re.DOTALL)
    if table_match:
        table_old = table_match.group()
        table_new = """<table class="table table-bordered">
                                <tbody>
                                    <tr>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">Número de Créditos Académicos</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">Horas de Trabajo con Acompañamiento Docente</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">Duración del Curso</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">Total de Horas</th>
                                    </tr>
                                    <tr>
                                        <td style="text-align: center;">3</td>
                                        <td style="text-align: center;">36</td>
                                        <td style="text-align: center;">12 Semanas</td>
                                        <td style="text-align: center;">144</td>
                                    </tr>
                                </tbody>
                            </table>"""
        content = content.replace(table_old, table_new, 1)
        print("Tab 2 table replaced successfully!")
    else:
        print("Tab 2 table match failed!")
else:
    print("Profile tab start failed!")

# Tab 3 replacement: Justificación
pattern_tab3 = r'(<div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-profile2" role="tabpanel"\s+aria-labelledby="v-pills-profile2-tab">.*?<h4 class="mb-4">Justificación</h4>).*?(</div>)'
replacement_tab3 = r"""\1
                        <p align="justify">La comprensión de los principios estadísticos es indispensable para llevar a cabo investigaciones en el campo de la ingeniería de software, desde el diseño de experimentos hasta la interpretación de los resultados. El curso de Estadística Descriptiva pretende fortalecer en el estudiante, conocimientos, conceptos, categorías y métodos, que le permitan analizar, comprobar y comparar resultados entre lo teórico y lo real. Además de promover el uso de herramientas tecnológicas y el uso de software estadístico especializado. Hoy en día su importancia es tal, que muchos de los trabajos y de las conclusiones procedentes de la investigación, o de una actividad profesional concreta, se debe refrendar estadísticamente antes de su aceptación definitiva.</p>
                        <p align="justify">Al finalizar el curso de Estadística Descriptiva el estudiante de Ingeniería de software estará en la capacidad de comprender, analizar y actuar frente al comportamiento de un conjunto de datos con base a la problemática o situación problema planteada. Lo que le permitirá en el futuro aplicar el conocimiento en su contexto real para tomar decisiones acertadas en un entorno cada vez más impulsado por los datos y para un desempeño exitoso en el ámbito académico, profesional y social.</p>
                    \2"""
content, count = re.subn(pattern_tab3, replacement_tab3, content, flags=re.DOTALL)
print(f"Tab 3 replaced: {count} times")

# Tab 4 replacement: Problemas
pattern_tab4 = r'(<div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-messages" role="tabpanel"\s+aria-labelledby="v-pills-messages-tab">.*?<h4 class="mb-4">Problemas que se abordarán en el Curso</h4>).*?(</div>)'
replacement_tab4 = r"""\1
                        <p align="justify">Con el fin de aportar al desarrollo de la competencia, con este curso se proyecta dar solución con argumentos al siguiente problema.</p>
                        <p align="justify">Resuelve problemas con base al análisis de indicadores en diversos sectores como salud, seguridad, educación, medio ambiente y otras temáticas de orden político, social y económico que le permitan tomar decisiones a través del uso de métodos, técnicas y herramientas de la estadística descriptiva y proponer soluciones innovadoras que contribuyan a los ODS en el territorio colombiano.</p>
                    \2"""
content, count = re.subn(pattern_tab4, replacement_tab4, content, flags=re.DOTALL)
print(f"Tab 4 replaced: {count} times")

# Tab 5 replacement: Temas
pattern_tab5 = r'(<div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-messages1" role="tabpanel"\s+aria-labelledby="v-pills-messages1-tab">.*?<h4 class="mb-4">Temas a Trabajar en el Curso</h4>).*?(</div>)'
replacement_tab5 = r"""\1
                        <strong>Unidad 1: Investigación estadística</strong>
                        <ul>
                            <li>Etapas de una investigación estadística.</li>
                            <li>Conceptos básicos.</li>
                            <li>Muestreo poblacional.</li>
                        </ul><br>
                        <strong>Unidad 2: Fundamentos de estadística</strong>
                        <ul>
                            <li>Variables y atributos.</li>
                            <li>Caracterización de variables cualitativas.</li>
                            <li>Distribuciones de frecuencias.</li>
                            <li>Tablas de contingencia.</li>
                            <li>Diagramas estadísticos.</li>
                        </ul><br>
                        <strong>Unidad 3: Medidas estadísticas univariantes</strong>
                        <ul>
                            <li>Medidas de tendencia Central.</li>
                            <li>Medidas de posición.</li>
                            <li>Medidas de dispersión.</li>
                            <li>Medidas de asimetría y apuntamiento.</li>
                        </ul><br>
                        <strong>Unidad 4: Medidas estadísticas bivariantes</strong>
                        <ul>
                            <li>Regresión y correlación.</li>
                            <li>Regresión lineal simple.</li>
                            <li>Diagramas de dispersión.</li>
                            <li>Coeficientes de determinación.</li>
                            <li>Coeficientes de Correlación.</li>
                        </ul>
                    \2"""
content, count = re.subn(pattern_tab5, replacement_tab5, content, flags=re.DOTALL)
print(f"Tab 5 replaced: {count} times")

# Tab 6 replacement: Palabras Claves
pattern_tab6 = r'(<div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-messages2" role="tabpanel"\s+aria-labelledby="v-pills-messages2-tab">.*?<h4 class="mb-4">Palabras Claves</h4>).*?(</div>)'
replacement_tab6 = r"""\1
                        <ul>
                            <li>Variables cuantitativas y cualitativas.</li>
                            <li>Tablas de contingencia.</li>
                            <li>Diagramas estadísticos.</li>
                            <li>Distribución de frecuencias.</li>
                            <li>Medidas univariantes y bivariantes.</li>
                        </ul>
                    \2"""
content, count = re.subn(pattern_tab6, replacement_tab6, content, flags=re.DOTALL)
print(f"Tab 6 replaced: {count} times")

# Tab 7 replacement: Resumen de Entregas Table
# We want to replace the table in the settings tab
settings_start = content.find('id="v-pills-settings"')
if settings_start != -1:
    table_match = re.search(r'<table class="table table-bordered">.*?</table>', content[settings_start:], re.DOTALL)
    if table_match:
        table_old = table_match.group()
        table_new = """<table class="table table-bordered">
                                <tbody>
                                    <tr>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">Momento Evaluativo</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">Duración Semanas</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">Entregable / Cuestionario</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;" nowrap="">Peso %</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">Semana de Entrega</th>
                                    </tr>
                                    <tr>
                                        <td rowspan="4" style="vertical-align: middle; text-align: center;">I<br>40%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">1 - 3</td>
                                        <td><strong>Avance 1.</strong> Recolección de datos – Informe con la elaboración de un mapa mental, respuesta a las preguntas orientadoras del contexto de la problemática, clasificación de variables y ejercicio de muestreo.</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">3</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Cuestionario de evaluación –</strong> Unidad 1 - Investigación estadística</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">4 - 5</td>
                                        <td><strong>Avance 2.</strong> Organización de datos – Informe con la construcción de un cuadro sinóptico, caracterización de variables cualitativas, diagramas estadísticos, tabla de contingencia de doble entrada y aplicaciones de la estadística en la Ingeniería de software.</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">5</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Cuestionario de evaluación -</strong> Unidad 2 – Fundamentos de Estadística</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="6" style="vertical-align: middle; text-align: center;">II<br>60%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">6 - 7</td>
                                        <td><strong>Avance 3.</strong> Análisis de datos – Informe con el diseño de un mapa conceptual, medidas univariantes - Variable Discreta, medidas Univariantes - variable continua y relación de la situación problema con los ODS (Objetivos de Desarrollo Sostenible).</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">7</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Cuestionario de evaluación -</strong> Unidad 3 – medidas estadísticas univariantes</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">8 - 9</td>
                                        <td><strong>Avance 4.</strong> Interpretación de resultados – Informe con la creación de un diagrama de araña, aplicación de regresión y correlación, ejercicio de aplicación, regresión y correlación lineal simple y regresión y correlación múltiple.</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">9</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Cuestionario de evaluación -</strong> Unidad 4 – Medidas estadísticas bivariantes</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">10 - 12</td>
                                        <td><strong>Producto Final.</strong> Presentación de resultados – Informe variable cualitativa, variable cuantitativa discreta, variable cuantitativa continua, regresión y correlación entre variables cuantitativas y análisis y propuesta de solución a la problemática.</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">12</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Cuestionario de evaluación final</strong></td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                    </tr>
                                </tbody>
                            </table>"""
        content = content.replace(table_old, table_new, 1)
        print("Tab 7 table replaced successfully!")
    else:
        print("Tab 7 table match failed!")
else:
    print("Settings tab start failed!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Update of Introduccion al curso.html completed!")
