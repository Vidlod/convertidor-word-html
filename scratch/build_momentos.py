# -*- coding: utf-8 -*-
import os

filepath_m1 = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Momentos/Momento Evaluativo1.html"
filepath_m2 = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Momentos/Momento Evaluativo2.html"

# Load the file content
with open(filepath_m1, "r", encoding="utf-8") as f:
    html_m1 = f.read()

with open(filepath_m2, "r", encoding="utf-8") as f:
    html_m2 = f.read()

# Helper to find the start of v-pills-tabContent
def get_header(html):
    marker = '<div class="tab-content" id="v-pills-tabContent">'
    idx = html.find(marker)
    if idx == -1:
        raise ValueError("Could not find tabContent marker!")
    return html[:idx + len(marker)]

header_m1 = get_header(html_m1)
header_m2 = get_header(html_m2)

# Ensure left nav label of Momento 2 is updated to 3, 4 y 5
header_m2 = header_m2.replace("CONTENIDO DE LOS ENTREGABLES 1 Y 2", "CONTENIDO DE LOS ENTREGABLES 3, 4 Y 5")

# Common footer
footer = """
                </div>
            </div>
        </div>
    </div>
</section>
"""

# Tab content for Momento 1
tab_home_m1 = """
                    <div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-home" role="tabpanel"
                        aria-labelledby="v-pills-home-tab">
                        <h4 class="mb-4">Resumen de Entregas</h4>
                        <div style="text-align: center;">
                            <table class="table table-bordered">
                                <tbody>
                                    <tr>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">
                                            Momento Evaluativo</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">
                                            Duración Semana</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">
                                            Entregable</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;"
                                            nowrap="">Peso %</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">Semana
                                            de Entrega</th>
                                    </tr>
                                    <tr>
                                        <td rowspan="4" style="vertical-align: middle; text-align: center;">I <br>
                                            40%
                                        </td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">1 - 3</td>
                                        <td style="text-align: left; vertical-align: middle;"><strong>Avance 1. Recolección de datos:</strong> Informe con la elaboración de un mapa mental, respuesta a las preguntas orientadoras del contexto de la problemática, clasificación de variables y ejercicio de muestreo.</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">3</td>
                                    </tr>
                                    <tr>
                                        <td style="text-align: left; vertical-align: middle;"><strong>Cuestionario de evaluación – Unidad 1 - Investigación estadística</strong></td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">4 - 5</td>
                                        <td style="text-align: left; vertical-align: middle;"><strong>Avance 2. Organización de datos:</strong> Informe con la construcción de un cuadro sinóptico, caracterización de variables cualitativas, diagramas estadísticos, tabla de contingencia de doble entrada y aplicaciones de la estadística en la Ingeniería de software.</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">5</td>
                                    </tr>
                                    <tr>
                                        <td style="text-align: left; vertical-align: middle;"><strong>Cuestionario de evaluación - Unidad 2 – Fundamentos de Estadística</strong></td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>"""

tab_profile_m1 = """
                    <div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-profile" role="tabpanel"
                        aria-labelledby="v-pills-profile-tab">
                        <h4 class="mb-4">Descripción General</h4>
                        <p style="text-align: justify;">Durante el desarrollo del avance 1 y 2 deberá entregar dos informes en formato PDF donde se consolide el desarrollo de todas las actividades propuestas.</p>
                        <p style="text-align: justify;"><strong>Los informes deben cumplir con las siguientes condiciones formales de entrega:</strong></p>
                        <ul>
                            <li style="margin-bottom: 10px;">Portada.</li>
                            <li style="margin-bottom: 10px;">Introducción.</li>
                            <li style="margin-bottom: 10px;">Justificación.</li>
                            <li style="margin-bottom: 10px;">Objetivos.</li>
                            <li style="margin-bottom: 10px;">Conclusiones (relacionadas con los métodos estadísticos aplicados y la problemática estudiada).</li>
                            <li style="margin-bottom: 10px;">Referencias bibliográficas.</li>
                        </ul>
                        <p style="text-align: justify;">Al finalizar cada informe deberá adjuntar evidencias del desarrollo de las actividades como pantallazos o compartir el enlace directo de la hoja de cálculo donde realizo los procedimientos correspondientes. Verifique en la configuración que cualquier persona con el enlace pueda ver el archivo y asegúrese de que el enlace abra correctamente.</p>
                        <p style="text-align: justify;"><strong>Tenga en cuenta la siguiente situación hipotética:</strong></p>
                        <p style="text-align: justify;">Usted ha sido contratado como ingeniero de software en la Agencia Nacional de Seguridad Vial (ANSV) y debe apoyar el área del observatorio nacional y entre sus funciones debe recopilar estudios, informes, investigaciones y documentos técnicos relacionados con las áreas de acción del sistema seguro y seguridad vial. Dentro de su labor deberá realizar análisis de datos, gráficos y presentar informes con los resultados parciales de la problemática de estudio.</p>
                        <p style="text-align: justify;">La problemática de estudio que le fue asignada es analizar la accidentalidad vial en algunos departamentos de Colombia para el primer semestre del 2024 por lo tanto deberá trabajar siempre con el <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> para el desarrollo de las actividades propuestas de cada entregable.</p>
                        <p style="text-align: justify;">No es casualidad que cada uno de los entregables tenga el nombre de las etapas de una investigación estadística, ya que en cada uno de los informes o entregables se espera que pueda ir desarrollando las competencias esperadas y de esta manera logre avanzar de manera progresiva hasta alcanzar el nivel relacional más alto en las dimensiones ser, saber y hacer para lograr la aprobación del curso.</p>
                        <p style="text-align: justify;">El desarrollo de las actividades se puede realizar utilizando Excel (Office) o el software Estadístico Infostat.</p>
                        <p style="text-align: justify;">Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar: Video Tutorial para la descarga del software Infostat.</p>
                        <p style="text-align: justify;">Enlace para la descarga del Infostat: <strong><a href="http://www.infostat.com.ar" target="_blank" rel="noreferrer noopener">www.infostat.com.ar</a></strong>.</p>
                        <h4 class="mb-4"><br>Condiciones Particulares de Entrega</h4>
                        <p style="text-align: justify;">Desarrolle el entregable siguiendo las indicaciones de la forma <strong><a href="@@PLUGINFILE@@/Entregable1_Recolección de datos.docx" target="_blank" rel="noopener">Entregable 1 Recolección de datos</a></strong> suministrado para su estructuración. Lea con atención las instrucciones para su correcto diligenciamiento. No modifique ni elimine elementos de la forma.<br><br>Así mismo, desarrolle el entregable siguiendo las indicaciones de la forma <strong><a href="@@PLUGINFILE@@/Entregable2_Organización de datos.docx" target="_blank" rel="noopener">Entregable 2 Organización de datos</a></strong> suministrado para su estructuración. Lea con atención las instrucciones para su correcto diligenciamiento. No modifique ni elimine elementos de la forma.</p>
                    </div>"""


tab_profile1_m1 = """
                    <div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-profile1" role="tabpanel"
                        aria-labelledby="v-pills-profile1-tab">
                        <h4 class="mb-4">Instrumento de Evaluación</h4><strong><a
                                href="@@PLUGINFILE@@/Rubrica1_Estadística_Descriptiva.pdf"
                                target="_blank" rel="noopener"><button type="button"
                                    class="btn btn-outline-primary btn-lg" aria-pressed="true" role="button"> <i
                                        class="fa fa fa-file-pdf-o fa-lg"></i> Rúbrica</button></a></strong>
                    </div>"""

tab_profile2_m1 = """
                    <div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-profile2" role="tabpanel"
                        aria-labelledby="v-pills-profile2-tab">
                        <h4 class="mb-4">Instrumento para Enviar Entregable</h4>
                        <a target="_blank" href="https://virtual.udes.edu.co/mod/assign/view.php?id=3940"
                            rel="noopener"><button type="button" class="btn btn-outline-primary btn-lg"
                                aria-pressed="true" role="button"><span class="spinner-grow spinner-grow-sm"></span>
                                Enviar Entregable
                                Avance 1</button></a>
                        <p>
                        </p>
                        <a target="_blank" href="https://virtual.udes.edu.co/mod/assign/view.php?id=3950"
                            rel="noopener"><button type="button" class="btn btn-outline-primary btn-lg"
                                aria-pressed="true" role="button"><span class="spinner-grow spinner-grow-sm"></span>
                                Enviar Entregable
                                Avance 2</button></a>
                    </div>"""

tab_settings_m1 = """
                    <div class="tab-pane fade shadow rounded bg-white p-5 active show" id="v-pills-settings"
                        role="tabpanel" aria-labelledby="v-pills-settings-tab">
                        <h4 class="mb-4">Contenido de los Entregables 1 y 2</h4>
                        <div>
                            <ul class="nav nav-tabs" id="myTab" role="tablist">
                                <li class="nav-item">
                                    <a class="nav-link active" id="semana1-tab" data-toggle="tab" href="#semana1" role="tab"
                                        aria-controls="semana1" aria-selected="true">Semana 1 <small
                                            class="d-block" style="text-align: center;">Avance 1</small></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="semana2-tab" data-toggle="tab" href="#semana2" role="tab"
                                        aria-controls="semana2" aria-selected="false" tabindex="-1">Semana 2 <small
                                            class="d-block" style="text-align: center;">Avance 1</small></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="semana3-tab" data-toggle="tab" href="#semana3" role="tab"
                                        aria-controls="semana3" aria-selected="false" tabindex="-1">Semana 3 <small
                                            class="d-block" style="text-align: center;">Avance 1</small></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="semana4-tab" data-toggle="tab" href="#semana4" role="tab"
                                        aria-controls="semana4" aria-selected="false" tabindex="-1">Semana 4 <small
                                            class="d-block" style="text-align: center;">Avance 2</small></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="semana5-tab" data-toggle="tab" href="#semana5" role="tab"
                                        aria-controls="semana5" aria-selected="false" tabindex="-1">Semana 5 <small
                                            class="d-block" style="text-align: center;">Avance 2</small></a>
                                </li>
                            </ul>
                            <div class="tab-content" id="myTabContent">
                                <div class="tab-pane fade active show" id="semana1" role="tabpanel" aria-labelledby="semana1-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">Cordial saludo.<br><br>Bienvenido(a) al curso de estadística descriptiva. Inicie su proceso académico, revisando el <strong><a href="@@PLUGINFILE@@/SYLLABUS_Estadística_Descriptiva.pdf" target="_blank" rel="noopener">syllabus</a></strong>, el video de bienvenida y presentación del curso, la <strong><a href="@@PLUGINFILE@@/Rubrica1_Estadística_Descriptiva.pdf" target="_blank" rel="noopener">rúbrica</a></strong>, así como el <strong><a href="@@PLUGINFILE@@/Mapa_Curso_Estadística.pdf" target="_blank" rel="noopener">mapa conceptual</a></strong> para que pueda identificar la información general y detallada del curso, además de la organización y secuencia de las temáticas y contenidos propuestos, las estrategias de enseñanza – aprendizaje. Así mismo es importante realizar la exploración de los recursos educativos sugeridos para el desarrollo exitoso de las actividades propuestas.<br><br>Se realizarán encuentros sincrónicos para abordar aspectos y contenidos relacionados con las temáticas del curso. También se resolverán inquietudes que surjan en la construcción de los entregables e igualmente es importante que pueda participar e interactuar a través del foro social para que intercambien expectativas e intereses individuales que tengan del curso.</p>
<ul>
                                            <li style="margin-bottom: 10px;"><strong><a href="@@PLUGINFILE@@/Mapa_Curso_Estadística.pdf" target="_blank" rel="noopener">Mapa mental Estadística Descriptiva</a></strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong><a href="@@PLUGINFILE@@/SYLLABUS_Estadística_Descriptiva.pdf" target="_blank" rel="noopener">Syllabus del curso Estadística Descriptiva</a></strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Video de presentación y bienvenida del curso Estadística Descriptiva</strong>.</li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana2" role="tabpanel" aria-labelledby="semana2-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">Iniciamos la <strong>Unidad 1 - Investigación estadística</strong> con el entregable 1 - Recolección de datos.<br><br>Deberá entregar un informe en formato PDF donde se consolide el desarrollo de las actividades propuestas en la plantilla <strong><a href="@@PLUGINFILE@@/Entregable1_Recolección de datos.docx" target="_blank" rel="noopener">Entregable 1 Recolección de datos</a></strong>.<br><br><strong>Actividad 1: Organizador gráfico</strong><br><br>Resumir mediante un organizador gráfico las etapas para el inicio de una investigación estadística (planeación, recolección, organización, análisis y presentación de resultados) describiendo cada una de ellas. Para el desarrollo de este podrá seleccionar de manera libre el organizador gráfico de su preferencia (cuadro sinóptico, mapa conceptual, mapa mental, mentefacto, etc.). Se sugiere explorar los siguientes recursos para que pueda revisar diferentes alternativas y tener en cuenta los aspectos fundamentales para el diseño y la presentación:</p>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Dirección General de Educación Tecnológica Agropecuaria y Ciencias del Mar (2025). Organizadores gráficos.<br><strong><a href="https://dgetaycm.sep.gob.mx/storage/recursos/2025/01/Wj9GE11AYO-Organizadores%20gr%C3%A1ficos.pdf" target="_blank" rel="noopener">https://dgetaycm.sep.gob.mx/storage/recursos/2025/01/Wj9GE11AYO-Organizadores%20gr%C3%A1ficos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Orientación Andújar (2015). Organizadores gráficos.<br><strong><a href="https://www.orientacionandujar.es/wp-content/uploads/2015/07/OrganizadoresGraficos.pdf" target="_blank" rel="noopener">https://www.orientacionandujar.es/wp-content/uploads/2015/07/OrganizadoresGraficos.pdf</a></strong>.</li>
                                        </ul>
                                        <p style="text-align: justify;">Para el desarrollo del organizador gráfico teniendo en cuenta la temática propuesta puede revisar los referentes:</p>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Martínez, C. (2013). Capítulo 1. Conceptos generales. En: Estadística y muestreo, 13a ed. [Online] Bogotá: Ecoe Ediciones. (pp. 10– 33).<br><strong><a href="http://ies-booklick.s3.amazonaws.com/1626728222781-Estadistica-MuestreoCiro1-198.pdf" target="_blank" rel="noopener">http://ies-booklick.s3.amazonaws.com/1626728222781-Estadistica-MuestreoCiro1-198.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Fernández, D., y Guitart. M. (s.f.) Estadística Descriptiva y análisis de datos.<br><strong><a href="http://www1.frm.utn.edu.ar/estadistica/documentos/ed&ad.pdf" target="_blank" rel="noopener">http://www1.frm.utn.edu.ar/estadistica/documentos/ed&ad.pdf</a></strong>.</li>
                                        </ul>
                                        <p style="text-align: justify;">Para la elaboración del organizador gráfico puede realizarlo en plataformas como: Miro, Mindmeister, Canva, Genially, Lucidchart, Creately, etc. Debe adjuntar directamente la imagen del organizador gráfico. Evitar adjuntar enlaces donde se haya creado el organizador gráfico ya que la mayoría de las veces solicitan acceso. En caso de adjuntarlo y si no se logra su visualización se calificará teniendo en cuenta los criterios de la <strong><a href="@@PLUGINFILE@@/Rubrica1_Estadística_Descriptiva.pdf" target="_blank" rel="noopener">rúbrica de evaluación</a></strong>.<br><br><strong>Actividad 2: Contexto de la problemática</strong><br><br>Responda las siguientes preguntas orientadoras para que pueda contextualizarse con la problemática de estudio:<br><br>1) ¿Cuáles son las causas o factores que ocasionan los accidentes de tránsito en las vías?<br>2) ¿Qué impacto podría tener el estado de ánimo del conductor, en un accidente de tránsito?<br>3) ¿Cómo influye el estado y las condiciones de las vías de los accidentes reportados en algunos departamentos en Colombia?<br>4) ¿Quiénes son más responsables a la hora de conducir los hombres o las mujeres?<br>5) ¿Cuáles considera son los accidentes de tránsito más frecuentes en Bogotá?<br>6) ¿Qué es un anuario de siniestralidad?<br><br>Para el desarrollo de esta actividad se recomienda explorar los recursos:</p>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Concejo de Bogotá (2025). En los últimos 7 años, los lesionados por siniestros viales han disminuido en el país, pero las muertes han aumentado.<br><strong><a href="https://concejodebogota.gov.co/en-los-ultimos-7-anos-los-lesionados-por-siniestros-viales-han/cbogota/2025-03-25/102637.php" target="_blank" rel="noopener">https://concejodebogota.gov.co/en-los-ultimos-7-anos-los-lesionados-por-siniestros-viales-han/cbogota/2025-03-25/102637.php</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Alcaldía de Bogotá (2025). 47,3 % de las víctimas fatales en accidentes de tránsito fueron motociclistas.<br><strong><a href="https://bogota.gov.co/mi-ciudad/movilidad/47-de-victimas-en-accidentes-transito-en-bogota-fueron-moticiclistas" target="_blank" rel="noopener">https://bogota.gov.co/mi-ciudad/movilidad/47-de-victimas-en-accidentes-transito-en-bogota-fueron-moticiclistas</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Observatorio de salud de Bogotá (2025). Mortalidad por accidentes de tránsito en Bogotá D.C.<br><strong><a href="https://saludata.saludcapital.gov.co/osb/indicadores/mortalidad-de-accidentes-de-transito/" target="_blank" rel="noopener">https://saludata.saludcapital.gov.co/osb/indicadores/mortalidad-de-accidentes-de-transito/</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Gómez, L. (2025). Muertes por accidentes de tránsito en Colombia disminuyeron en enero de 2025: este es el panorama por ciudades.<br><strong><a href="https://www.infobae.com/colombia/2025/02/16/muertes-por-accidentes-de-transito-en-colombia-disminuyeron-en-enero-de-2025-este-es-el-panorama-por-ciudades/" target="_blank" rel="noopener">https://www.infobae.com/colombia/2025/02/16/muertes-por-accidentes-de-transito-en-colombia-disminuyeron-en-enero-de-2025-este-es-el-panorama-por-ciudades/</a></strong>.</li>
                                        </ul>
                                        <p style="text-align: justify;">No obstante, puede dirigirse a otras fuentes de información. Responda las preguntas planteadas no solo desde su opinión, sino también debe argumentar y justificar su respuesta teniendo en cuenta cifras y datos estadísticos.</p>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana3" role="tabpanel" aria-labelledby="semana3-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">A través de su proceso de enseñanza - aprendizaje y de la apropiación del conocimiento, enfoque su aprendizaje en la actividad 3 y 4.<br><br><strong>Actividad 3: Clasificación de variables</strong><br><br>Para el desarrollo de esta actividad se puede apoyar de los recursos:</p>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 1. Conceptos generales sobre estadística. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín. (pp. 11 – 21).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                        </ul>
                                        <p style="text-align: justify;">Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar:</p>
                                        <ul>
                                            <li style="margin-bottom: 10px;"><strong><a href="@@PLUGINFILE@@/VARIABLES.pdf" target="_blank" rel="noopener">Infografía de variables</a></strong>.</li>
                                        </ul>
                                        <p style="text-align: justify;">Clasifique todas las variables del <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> en cualitativas (nominales, ordinales) y cuantitativas (discretas o continuas) teniendo en cuenta la tabla que se encuentra en la <strong><a href="@@PLUGINFILE@@/Entregable1_Recolección de datos.docx" target="_blank" rel="noopener">plantilla</a></strong>.<br><br><strong>Actividad 4. Muestreo</strong><br><br>Revise los siguientes recursos para el desarrollo de esta actividad:</p>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 2. Introducción a los tipos de muestreo. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 23 -32).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                        </ul>
                                        <p style="text-align: justify;">Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar:</p>
                                        <ul>
                                            <li style="margin-bottom: 10px;"><strong>Cálculo del tamaño muestral [Presentación]</strong>.</li>
                                        </ul>
                                        <p style="text-align: justify;">Dado que la base de datos suministrada <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> corresponde a una muestra ya definida, es importante reconocer que, en algunas ocasiones, la muestra se debe calcular. Realice los dos ejercicios que se presentan a continuación: <br><br>1. Si se desea establecer una muestra representativa para estudiar la problemática de <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> a través del muestreo aleatorio simple con un nivel de confianza del 90%, un error estimado del 5% y una población de 2920 defunciones, ¿Cuál sería el tamaño de la muestra?<br>2. Si se desea establecer una muestra representativa para estudiar el problema de <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> a través del muestreo aleatorio simple, con un nivel de confianza del 91%, un error estimado del 5%, pero se desconoce el total de la población constituida mayormente por peatones, ¿Cuál sería el tamaño de la muestra?<br><br>Se debe presentar no solo el resultado sino los procedimientos o cálculos realizados para llegar a las respuestas.<br><br>Realice la entrega del entregable en la plataforma. Una vez realizada la calificación recuerde tener en cuenta los comentarios de retroalimentación para los próximos entregables.</p>
                                        <div style="text-align: center;">
                                            <a href="https://virtual.udes.edu.co/mod/assign/view.php?id=3940" target="_blank" rel="noopener">
                                                <button type="button" class="btn btn-outline-primary btn-lg" aria-pressed="true" role="button">
                                                    <span class="spinner-grow spinner-grow-sm"></span> Enviar Avance 1.
                                                </button>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana4" role="tabpanel" aria-labelledby="semana4-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">Avanzamos a la <strong>Unidad 2 – Fundamentos de Estadística con el entregable 2 - Organización de datos</strong>.<br><br>Deberá entregar un informe en formato PDF donde se consolide el desarrollo de las actividades propuestas en la plantilla <strong><a href="@@PLUGINFILE@@/Entregable2_Organización de datos.docx" target="_blank" rel="noopener">Entregable 2 Organización de datos</a></strong>.<br><br><strong>Actividad 1: Organizador gráfico</strong><br><br>Diseñar un cuadro sinóptico donde se recopile lo relacionado con la tabulación de datos estadísticos, distribución de frecuencias y tipos de gráficas y diagramas. Para el desarrollo de la actividad puede consultar los recursos:</p>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 3. Tabulación de datos estadísticos. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 34 -43).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 4. Distribución de frecuencias. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 44 -51).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 5. Gráficas y Diagramas. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 52 - 63).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Suarez. M. (2025). Capítulo 2. Tablas estadísticas. En: Estadística descriptiva para todos: Fundamentos y aplicaciones – Volumen I. (pp.52 – 69).<br><strong><a href="https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I" target="_blank" rel="noopener">https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Suarez. M. (2025). Capítulo 3. Distribución de frecuencias. En: Estadística descriptiva para todos: Fundamentos y aplicaciones – Volumen I. (pp.70 – 108).<br><strong><a href="https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I" target="_blank" rel="noopener">https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I</a></strong>.</li>
                                        </ul>
                                        <p style="text-align: justify;">Para la elaboración del organizador gráfico puede realizarlo en plataformas como: Miro, Mindmeister, Canva, Genially, Lucidchart, Creately, etc. Debe adjuntar directamente el cuadro sinóptico. Evitar adjuntar enlaces donde se haya creado el recurso ya que la mayoría de las veces solicitan acceso. En caso de adjuntarlo y si no se logra su visualización se calificará teniendo en cuenta los criterios de la <strong><a href="@@PLUGINFILE@@/Rubrica1_Estadística_Descriptiva.pdf" target="_blank" rel="noopener">rúbrica de evaluación</a></strong>. Las actividades 2, 3 y 4 se pueden realizar utilizando Excel (Office) o el software Estadístico Infostat. Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar para el desarrollo de las actividades 2, 3 y 4:</p>
                                        <ul>
                                            <li style="margin-bottom: 10px;"><strong>Fundamentos de estadística [Presentación]</strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Tablas de frecuencias [Presentación]</strong>.</li>
                                        </ul>
                                        <p style="text-align: justify;"><strong>Actividad 2: Caracterización de Variables cualitativas tabla de frecuencias</strong><br><br>Se sugerirá revisar los siguientes referentes para una mayor comprensión de la temática propuesta:</p>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Martínez, C. (2013). Capítulo 2. Distribuciones de frecuencia. En: Estadística y muestreo, 13a ed. [Online] Bogotá: Ecoe Ediciones. (pp 43 – 89).<br><strong><a href="http://ies-booklick.s3.amazonaws.com/1626728222781-Estadistica-MuestreoCiro1-198.pdf" target="_blank" rel="noopener">http://ies-booklick.s3.amazonaws.com/1626728222781-Estadistica-MuestreoCiro1-198.pdf</a></strong>.</li>
                                        </ul>
                                        <p style="text-align: justify;">Teniendo en cuenta el <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> seleccione una variable cualitativa.<br><br>a) Calcule la frecuencia absoluta, frecuencia relativa y frecuencia porcentual de la variable cualitativa elegida y reporte los valores en la tabla de frecuencias consignada en la <strong><a href="@@PLUGINFILE@@/Entregable2_Organización de datos.docx" target="_blank" rel="noopener">plantilla</a></strong>.</p>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana5" role="tabpanel" aria-labelledby="semana5-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">A través de su proceso de enseñanza - aprendizaje y de la apropiación del conocimiento, enfoque su aprendizaje en la actividad 3 y 4.<br><br><strong>Actividad 3: Diagramas estadísticos</strong><br><br>Representar la información de la tabla de datos realizada en la actividad 2 (variable vs frecuencia absoluta) por medio de (diagrama de barras y diagrama circular). Posteriormente determine cuál es la moda de la variable cualitativa. Realizar un análisis estadístico asociado con la situación objeto de estudio en este caso indicadores de accidentalidad vial en algunos departamentos de Colombia. El análisis debe ser coherente de acuerdo con las gráficas realizadas y la moda. Copie y pegue las gráficas realizadas en Excel o en el software de Infostat. Evite adjuntar enlaces de hojas de cálculo. Deben presentarse directamente las imágenes de los diagramas estadísticos. En caso de adjuntarlo y si no se logra su visualización se calificará teniendo en cuenta los criterios de la <strong><a href="@@PLUGINFILE@@/Rubrica1_Estadística_Descriptiva.pdf" target="_blank" rel="noopener">rúbrica de evaluación</a></strong>.<br><br><strong>Actividad 4: Tabla de contingencia de doble entrada</strong><br><br>Realizar una tabla de contingencias o de doble entrada, con dos variables cualitativas, las cuales usted considere podrían estar relacionadas. (Representarla gráficamente) y realizar un análisis asociado con la situación objeto de estudio en este caso indicadores de accidentalidad vial en algunos departamentos de Colombia. Puede emplear la misma variable que usó en las actividades anteriores junto con otra variable de su preferencia o puede escoger una variable distinta a la que seleccionó inicialmente lo importante es analizar y establecer si existe alguna relación entre dos variables. Recuerde que las variables deben ser únicamente de tipo cualitativo.<br><br>Continúe su proceso de enseñanza - aprendizaje con el desarrollo de la actividad 5.<br><br><strong>Actividad 5: Aplicaciones de la estadística en la Ingeniería de software</strong><br><br>Realice un video (de máximo 3 a 5 minutos), subirlo a un canal como YouTube o similares (se sugiere publicar en modo oculto); y compartir el enlace. El video debe presentarse teniendo en cuenta los siguientes parámetros:<br><br>Debe realizar su presentación personal (nombre, edad, con quién vive, lugar de residencia, hobby o pasatiempos). Debe responder a la pregunta ¿Por qué es importante aprender estadística descriptiva para su formación profesional como futuro ingeniero de software o qué aplicaciones podría darle en su vida cotidiana, académica o laboral? Puede emplear diapositivas o presentación con las respuestas o las ideas que quiera expresar y puede acompañarla de imágenes o fotografías. Debe compartir la pantalla en caso de tener una presentación de apoyo y debe activarse la cámara durante todo el transcurso de la presentación. Es importante tener en cuenta aspectos como buena iluminación, sonido, presentación personal. Verificar que el enlace del video se pueda visualizar correctamente y no solicite ningún tipo de permiso. Copiar el enlace del video.</p>
<p style="text-align: justify;">Realice la entrega del entregable en la plataforma. Una vez realizada la calificación recuerde tener en cuenta los comentarios de retroalimentación para los próximos entregables.</p>
                                        <div style="text-align: center;">
                                            <a href="https://virtual.udes.edu.co/mod/assign/view.php?id=3950" target="_blank" rel="noopener">
                                                <button type="button" class="btn btn-outline-primary btn-lg" aria-pressed="true" role="button">
                                                    <span class="spinner-grow spinner-grow-sm"></span> Enviar Avance 2.
                                                </button>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>"""

# Tab content for Momento 2
tab_home_m2 = """
                    <div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-home" role="tabpanel"
                        aria-labelledby="v-pills-home-tab">
                        <h4 class="mb-4">Resumen de Entregas</h4>
                        <div style="text-align: center;">
                            <table class="table table-bordered">
                                <tbody>
                                    <tr>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">
                                            Momento Evaluativo</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">
                                            Duración Semana</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">
                                            Entregable</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;"
                                            nowrap="">Peso %</th>
                                        <th bgcolor="#F9F9F9" style="vertical-align: middle; text-align: center;">Semana
                                            de Entrega</th>
                                    </tr>
                                    <tr>
                                        <td rowspan="6" style="vertical-align: middle; text-align: center;">II <br>
                                            60%
                                        </td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">6 - 7</td>
                                        <td style="text-align: left; vertical-align: middle;"><strong>Avance 3. Análisis de datos:</strong> Informe con el diseño de un mapa conceptual, medidas univariantes - Variable Discreta, medidas Univariantes - variable continua y relación de la situación problema con los ODS (Objetivos de Desarrollo Sostenible).</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">7</td>
                                    </tr>
                                    <tr>
                                        <td style="text-align: left; vertical-align: middle;"><strong>Cuestionario de evaluación - Unidad 3 – medidas estadísticas univariantes</strong></td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">8 - 9</td>
                                        <td style="text-align: left; vertical-align: middle;"><strong>Avance 4. Interpretación de resultados:</strong> Informe con la creación de un diagrama de araña, aplicación de regresión y correlación, ejercicio de aplicación, regresión y correlación lineal simple y regresión y correlación múltiple.</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">9</td>
                                    </tr>
                                    <tr>
                                        <td style="text-align: left; vertical-align: middle;"><strong>Cuestionario de evaluación - Unidad 4 – Medidas estadísticas bivariantes</strong></td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">10 - 12</td>
                                        <td style="text-align: left; vertical-align: middle;"><strong>Producto Final. Presentación de resultados:</strong> Informe variable cualitativa, variable cuantitativa discreta, variable cuantitativa continua, regresión y correlación entre variables cuantitativas y análisis y propuesta de solución a la problemática.</td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                        <td rowspan="2" style="vertical-align: middle; text-align: center;">12</td>
                                    </tr>
                                    <tr>
                                        <td style="text-align: left; vertical-align: middle;"><strong>Cuestionario de evaluación final</strong></td>
                                        <td style="vertical-align: middle; text-align: center;">10%</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>"""

tab_profile_m2 = """
                    <div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-profile" role="tabpanel"
                        aria-labelledby="v-pills-profile-tab">
                        <h4 class="mb-4">Descripción General</h4>
                        <p style="text-align: justify;">Durante el desarrollo del avance 3, 4 y el producto final deberá entregar tres informes en formato PDF donde se consolide el desarrollo de todas las actividades propuestas.</p>
                        <p style="text-align: justify;"><strong>Los informes deben cumplir con las siguientes condiciones formales de entrega:</strong></p>
                        <ul>
                            <li style="margin-bottom: 10px;">Portada.</li>
                            <li style="margin-bottom: 10px;">Introducción.</li>
                            <li style="margin-bottom: 10px;">Justificación.</li>
                            <li style="margin-bottom: 10px;">Objetivos.</li>
                            <li style="margin-bottom: 10px;">Conclusiones (relacionadas con los métodos estadísticos aplicados y la problemática estudiada).</li>
                            <li style="margin-bottom: 10px;">Referencias Bibliográficas.</li>
                        </ul>
                        <p style="text-align: justify;">Al finalizar cada informe deberá adjuntar evidencias del desarrollo de las actividades como pantallazos o compartir el enlace directo de la hoja de cálculo donde realizo los procedimientos correspondientes. Verifique en la configuración que cualquier persona con el enlace pueda ver el archivo y asegúrese de que el enlace abra correctamente.</p>
                        <p style="text-align: justify;">Recuerde que deberá seguir trabajando con la problemática de estudio que le fue asignada “accidentalidad vial en algunos departamentos de Colombia para el primer semestre del 2024” y los datos del <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong>.</p>
                        <p style="text-align: justify;">El desarrollo de las actividades se puede realizar utilizando Excel (Office) o el software Estadístico Infostat.</p>
                        <p style="text-align: justify;">Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar: Video Tutorial para la descarga del software Infostat.</p>
                        <p style="text-align: justify;">Enlace para la descarga del Infostat: <strong><a href="http://www.infostat.com.ar" target="_blank" rel="noreferrer noopener">www.infostat.com.ar</a></strong>.</p>
                        <h4 class="mb-4"><br>Condiciones Particulares de Entrega</h4>
                        <p style="text-align: justify;">Desarrolle el entregable siguiendo las indicaciones de la forma <strong><a href="@@PLUGINFILE@@/Entregable3_Ánalisis de datos.docx" target="_blank" rel="noopener">Entregable 3 Análisis de datos</a></strong> suministrado para su estructuración. Lea con atención las instrucciones para su correcto diligenciamiento. No modifique ni elimine elementos de la forma.<br><br>Así mismo, desarrolle el entregable siguiendo las indicaciones de la forma <strong><a href="@@PLUGINFILE@@/Entregable4_Interpretación de resultados.docx" target="_blank" rel="noopener">Entregable 4 Interpretación de resultados</a></strong> suministrado para su estructuración. Lea con atención las instrucciones para su correcto diligenciamiento. No modifique ni elimine elementos de la forma.<br><br>De igual manera, desarrolle el entregable siguiendo las indicaciones de la forma <strong><a href="@@PLUGINFILE@@/Entregable5_Presentación de resultados.docx" target="_blank" rel="noopener">Entregable 5 Presentación de resultados</a></strong> suministrado para su estructuración. Lea con atención las instrucciones para su correcto diligenciamiento. No modifique ni elimine elementos de la forma.</p>
                    </div>"""

tab_profile1_m2 = """
                    <div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-profile1" role="tabpanel"
                        aria-labelledby="v-pills-profile1-tab">
                        <h4 class="mb-4">Instrumento de Evaluación</h4><strong><a
                                href="@@PLUGINFILE@@/Rubrica2Estadística_Descriptiva.pdf"
                                target="_blank" rel="noopener"><button type="button"
                                    class="btn btn-outline-primary btn-lg" aria-pressed="true" role="button"> <i
                                        class="fa fa fa-file-pdf-o fa-lg"></i> Rúbrica</button></a></strong>
                    </div>"""

tab_profile2_m2 = """
                    <div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-profile2" role="tabpanel"
                        aria-labelledby="v-pills-profile2-tab">
                        <h4 class="mb-4">Instrumento para Enviar Entregable</h4>
                        <a target="_blank" href="https://virtual.udes.edu.co/mod/assign/view.php?id=3951"
                            rel="noopener"><button type="button" class="btn btn-outline-primary btn-lg"
                                aria-pressed="true" role="button"><span class="spinner-grow spinner-grow-sm"></span>
                                Enviar Entregable
                                Avance 3</button></a>
                        <p>
                        </p>
                        <a target="_blank" href="https://virtual.udes.edu.co/mod/assign/view.php?id=3952"
                            rel="noopener"><button type="button" class="btn btn-outline-primary btn-lg"
                                aria-pressed="true" role="button"><span class="spinner-grow spinner-grow-sm"></span>
                                Enviar Entregable
                                Avance 4</button></a>
                        <p>
                        </p>
                        <a target="_blank" href="https://virtual.udes.edu.co/mod/assign/view.php?id=3953"
                            rel="noopener"><button type="button" class="btn btn-outline-primary btn-lg"
                                aria-pressed="true" role="button"><span class="spinner-grow spinner-grow-sm"></span>
                                Enviar Producto Final.</button></a>
                    </div>"""

tab_settings_m2 = """
                    <div class="tab-pane fade shadow rounded bg-white p-5 active show" id="v-pills-settings"
                        role="tabpanel" aria-labelledby="v-pills-settings-tab">
                        <h4 class="mb-4">Contenido de los Entregables 3, 4 y 5</h4>
                        <div>
                            <ul class="nav nav-tabs" id="myTab" role="tablist">
                                <li class="nav-item">
                                    <a class="nav-link active" id="semana6-tab" data-toggle="tab" href="#semana6" role="tab"
                                        aria-controls="semana6" aria-selected="true">Semana 6 <small
                                            class="d-block" style="text-align: center;">Avance 3</small></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="semana7-tab" data-toggle="tab" href="#semana7" role="tab"
                                        aria-controls="semana7" aria-selected="false" tabindex="-1">Semana 7 <small
                                            class="d-block" style="text-align: center;">Avance 3</small></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="semana8-tab" data-toggle="tab" href="#semana8" role="tab"
                                        aria-controls="semana8" aria-selected="false" tabindex="-1">Semana 8 <small
                                            class="d-block" style="text-align: center;">Avance 4</small></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="semana9-tab" data-toggle="tab" href="#semana9" role="tab"
                                        aria-controls="semana9" aria-selected="false" tabindex="-1">Semana 9 <small
                                            class="d-block" style="text-align: center;">Avance 4</small></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="semana10-tab" data-toggle="tab" href="#semana10" role="tab"
                                        aria-controls="semana10" aria-selected="false" tabindex="-1">Semana 10 <small
                                            class="d-block" style="text-align: center;">Producto Final</small></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="semana11-tab" data-toggle="tab" href="#semana11" role="tab"
                                        aria-controls="semana11" aria-selected="false" tabindex="-1">Semana 11 <small
                                            class="d-block" style="text-align: center;">Producto Final</small></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="semana12-tab" data-toggle="tab" href="#semana12" role="tab"
                                        aria-controls="semana12" aria-selected="false" tabindex="-1">Semana 12 <small
                                            class="d-block" style="text-align: center;">Producto Final</small></a>
                                </li>
                            </ul>
                            <div class="tab-content" id="myTabContent">
                                <div class="tab-pane fade active show" id="semana6" role="tabpanel" aria-labelledby="semana6-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">Continuamos a la <strong>Unidad 3 – medidas estadísticas univariantes con el entregable 3 – Análisis de datos</strong>.<br><br>Deberá entregar un informe en formato PDF donde se consolide el desarrollo de las actividades propuestas en la plantilla <strong><a href="@@PLUGINFILE@@/Entregable3_Ánalisis de datos.docx" target="_blank" rel="noopener">Entregable 3. Análisis de datos</a></strong>.<br><br><strong>Actividad 1: Organizador gráfico</strong><br><br>Resuma en un mapa conceptual las medidas estadísticas univariantes (medidas de tendencia central, medidas de posición, medidas de dispersión, medidas de asimetría y apuntamiento), detallando cada una de ellas.<br><br>Se recomienda realizar una revisión de los recursos:</p>
<ul>
                                            <li style="margin-bottom: 10px;">Universidad Abierta y a Distancia de México. (s.f.) Unidad 2. Medidas de tendencia central y dispersión.<br><strong><a href="https://dmd.unadmexico.mx/contenidos/TRONCO_COMUN/EBA/U2/descargables/EBA_U2_Contenidos.pdf" target="_blank" rel="noreferrer noopener">https://dmd.unadmexico.mx/contenidos/TRONCO_COMUN/EBA/U2/descargables/EBA_U2_Contenidos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 7. Medidas de tendencia central. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 72 - 85).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noreferrer noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 8. Medidas de posición. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 86 - 95).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noreferrer noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 9. Medidas de dispersión. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 96 - 107).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noreferrer noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 10. Medidas de forma. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 108 - 115).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noreferrer noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Suarez. M. (2025). Capítulo 1. Medidas de tendencia central. En: Estadística descriptiva para todos: Fundamentos y aplicaciones – Volumen II. (pp.12 –35).<br><strong><a href="https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I" target="_blank" rel="noreferrer noopener">https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Suarez. M. (2025). Capítulo 2. Medidas de posición. En: Estadística descriptiva para todos: Fundamentos y aplicaciones – Volumen II. (pp.36 – 60).<br><strong><a href="https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I" target="_blank" rel="noreferrer noopener">https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Suarez. M. (2025). Capítulo 3. Medidas de dispersión. En: Estadística descriptiva para todos: Fundamentos y aplicaciones – Volumen II. (pp.61 – 95).<br><strong><a href="https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I" target="_blank" rel="noreferrer noopener">https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I</a></strong>.</li>
                                        </ul>
<p style="text-align: justify;">Para la elaboración del organizador gráfico puede realizarlo en plataformas como: Miro, Mindmeister, Canva, Genially, Lucidchart, Creately, etc. Debe adjuntar directamente el cuadro sinóptico. Evitar adjuntar enlaces donde se haya creado el recurso ya que la mayoría de las veces solicitan acceso. En caso de adjuntarlo y si no se logra su visualización se calificará teniendo en cuenta los criterios de la <strong><a href="@@PLUGINFILE@@/Rubrica2Estadística_Descriptiva.pdf" target="_blank" rel="noopener">rúbrica de evaluación</a></strong>.<br><br>Las actividades 2 y 3 se pueden realizar utilizando Excel (Office) o el software Estadístico Infostat.<br><br>Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar para el desarrollo de las actividades 2 y 3:</p>
<ul>
                                            <li style="margin-bottom: 10px;"><strong>Tarjetas didácticas medidas de tendencia central y de dispersión</strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Tarjetas didácticas medidas de posición y medidas de forma</strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Presentación caza del tesoro de las medidas estadísticas</strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Presentación tablas de frecuencias</strong>.</li>
                                        </ul>
<p style="text-align: justify;"><strong>Actividad 2: Medidas univariantes - variable discreta</strong><br><br>Para el desarrollo de la actividad puede consultar los recursos sugeridos en la actividad 1 y adicionalmente la referencia:</p>
<ul>
                                            <li style="margin-bottom: 10px;">Montero, J. M. (2007). Características de Una Distribución de Frecuencias. Statistical Descriptive. Cengage Learning Paraninfo, S.A. (pp 17 – 61).<br><strong><a href="https://link.gale.com/apps/doc/CX4052100008/GVRL?u=unad&sid=GVRL&xid=d49ed557" target="_blank" rel="noreferrer noopener">https://link.gale.com/apps/doc/CX4052100008/GVRL?u=unad&sid=GVRL&xid=d49ed557</a></strong>.</li>
                                        </ul>
<p style="text-align: justify;">Con base en el <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> seleccione una variable CUANTITATIVA DISCRETA.<br><br><strong>Determine los siguientes elementos:</strong><br><br><strong>a. Tabla de frecuencia datos no agrupados.</strong> diseñar una tabla de frecuencia para datos no agrupados de la variable elegida, a partir de ella elaborar un diagrama de barras y un diagrama de líneas o de puntos.<br><br><strong>b. Medidas de tendencias central y de posición:</strong> para la variable cuantitativa discreta elegida, deberá calcular las medidas de tendencia central (media, mediana y moda), medidas de posición: cuartiles 1, 2 y 3, percentil 30 y 90, determinar el tipo de asimetría y curtosis, interpretar los resultados, sacar conclusiones de los parámetros hallados y asociarlos con la problemática de estudio indicadores de accidentalidad vial en algunos departamentos de Colombia.<br><br><strong>c. Medidas de dispersión:</strong> para la variable cuantitativa discreta elegida calcular: rango, varianza, desviación típica o estándar, coeficiente de variación, posteriormente interpretar los resultados, sacar conclusiones de los parámetros hallados y asociarlos con la problemática de estudio indicadores de accidentalidad vial en algunos departamentos de Colombia.<br><br>Se deben presentar los resultados teniendo en cuenta la tabla consignada en la <strong><a href="@@PLUGINFILE@@/Entregable3_Ánalisis de datos.docx" target="_blank" rel="noopener">plantilla del entregable</a></strong>.</p>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana7" role="tabpanel" aria-labelledby="semana7-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">Reciban la más cordial bienvenida a la semana siete de este proceso académico. Iniciamos el momento evaluativo II de producto y la recta final del desarrollo del curso.<br><br>A través de su proceso de enseñanza - aprendizaje y de la apropiación del conocimiento, enfoque su aprendizaje en la actividad 3.<br><br><strong>Actividad 3: Medidas univariantes - variable continua</strong><br><br>Para el desarrollo de la actividad puede consultar los recursos sugeridos en la actividad 1 y 2.<br><br>Con base en el <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> seleccione una variable CUANTITATIVA CONTINUA.<br><br><strong>Determine los siguientes elementos:</strong><br><br><strong>a. Tabla de frecuencia datos agrupados.</strong> Con la variable cuantitativa continua elegida, diseñar una tabla de frecuencias para datos agrupados, identificando rango, número de intervalos, amplitud y a partir de ella elaborar un histograma de frecuencias y un polígono de frecuencias. Finalmente, interpretar los resultados de la tabla, de los gráficos estadísticos y asociarlos con la problemática <strong>indicadores de accidentalidad vial en algunos departamentos de Colombia.</strong><br><br>Debe realizar las tablas en Excel teniendo en cuenta el diseño consignado en la <strong><a href="@@PLUGINFILE@@/Entregable3_Ánalisis de datos.docx" target="_blank" rel="noopener">plantilla</a></strong> en su hoja de cálculo para la presentación de los resultados.<br><br><strong>b. Medidas de tendencias central y de posición:</strong> Para la variable cuantitativa continua elegida, deberá calcular las medidas de tendencia central (media, mediana, moda), medidas de posición: cuartiles 1, 2 y 3, percentil 15, 55 y 90, determinar el tipo de asimetría y curtosis e interpretar los resultados, sacar conclusiones de los parámetros hallados y asociarlos con la problemática <strong>indicadores de accidentalidad vial en algunos departamentos de Colombia.</strong><br><br><strong>c. Medidas de dispersión:</strong> Para la variable cuantitativa continua elegida calcular: rango, varianza, desviación típica o estándar, coeficiente de variación, posteriormente interpretar los resultados, sacar conclusiones de los parámetros hallados y asociarlos con la problemática <strong>indicadores de accidentalidad vial en algunos departamentos de Colombia.</strong><br><br>Se deben presentar los resultados teniendo en cuenta la tabla consignada en la <strong><a href="@@PLUGINFILE@@/Entregable3_Ánalisis de datos.docx" target="_blank" rel="noopener">plantilla del entregable</a></strong>.<br><br>A través de su proceso de enseñanza - aprendizaje y de la apropiación del conocimiento, enfoque su aprendizaje en la actividad 4.<br><br><strong>Actividad 4: Relación de la situación problema con los ODS (Objetivos de Desarrollo Sostenible)</strong><br><br>Diseñe una infografía en la cual pueda presentar como mejorar los <strong>indicadores de accidentalidad vial en algunos departamentos de Colombia</strong> podría contribuir a los <strong>ODS (Objetivos de Desarrollo Sostenible)</strong> y con cuáles específicamente se podría relacionar.</p>
                                        <p style="text-align: justify;"><strong>Tener en cuenta los siguientes parámetros de presentación:</strong></p>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Busque fuentes de información confiables para el desarrollo de la infografía.</li>
                                            <li style="margin-bottom: 10px;">Debe incluir gráficos, diagramas, esquemas o imágenes.</li>
                                            <li style="margin-bottom: 10px;">El texto que se incluya dentro de la infografía debe ser en inglés.</li>
                                            <li style="margin-bottom: 10px;">Debe tener un diseño creativo.</li>
                                            <li style="margin-bottom: 10px;">Puede crearlo en cualquier plataforma de preferencia personal.</li>
                                            <li style="margin-bottom: 10px;">Debe adjuntar directamente la imagen de la infografía.</li>
                                            <li style="margin-bottom: 10px;">Evitar adjuntar enlaces donde se haya creado, ya que la mayoría de las veces solicitan acceso. En caso de adjuntarlo y si no se logra su visualización se calificará teniendo en cuenta los criterios de la <strong><a href="@@PLUGINFILE@@/Rubrica2Estadística_Descriptiva.pdf" target="_blank" rel="noopener">rúbrica de evaluación</a></strong>.</li>
                                        </ul>
                                        <p style="text-align: justify;">Realice la entrega del entregable en la plataforma. Una vez realizada la calificación recuerde tener en cuenta los comentarios de retroalimentación para los próximos entregables.</p>
                                        <div style="text-align: center;">
                                            <a href="https://virtual.udes.edu.co/mod/assign/view.php?id=3951" target="_blank" rel="noopener">
                                                <button type="button" class="btn btn-outline-primary btn-lg" aria-pressed="true" role="button">
                                                    <span class="spinner-grow spinner-grow-sm"></span> Enviar Avance 3.
                                                </button>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana8" role="tabpanel" aria-labelledby="semana8-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">Exploraremos la <strong>Unidad 4 – Medidas estadísticas bivariantes con el entregable 4 – interpretación de resultados</strong>.<br><br>Deberá entregar un informe en formato PDF donde se consolide el desarrollo de las actividades propuestas en la plantilla <strong><a href="@@PLUGINFILE@@/Entregable4_Interpretación de resultados.docx" target="_blank" rel="noopener">Entregable 4. Interpretación de resultados</a></strong>.<br><br><strong>Actividad 1: Organizador gráfico</strong><br><br>Resuma en un diagrama de araña las medidas estadísticas bivariantes de regresión y correlación.<br><br>Para el desarrollo de la actividad puede consultar los recursos:</p>
<ul>
                                            <li style="margin-bottom: 10px;">Talagala, P. (2020). Chapter 10 Correlation and Regression.<br><strong><a href="https://pridiltal.github.io/CM1110/correlation-and-regression.html" target="_blank" rel="noreferrer noopener">https://pridiltal.github.io/CM1110/correlation-and-regression.html</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Universidad Abierta y a Distancia de México. (s.f.) Unidad 3. Correlación y regresión lineal simple.<br><strong><a href="https://dmd.unadmexico.mx/contenidos/TRONCO_COMUN/EBA/U3/descargables/EBA_U3_Contenidos.pdf" target="_blank" rel="noreferrer noopener">https://dmd.unadmexico.mx/contenidos/TRONCO_COMUN/EBA/U3/descargables/EBA_U3_Contenidos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Elias, J. (2019). Análisis bivariante.<br><strong><a href="https://openaccess.uoc.edu/bitstream/10609/148455/1/AnalisisBivariante.pdf" target="_blank" rel="noreferrer noopener">https://openaccess.uoc.edu/bitstream/10609/148455/1/AnalisisBivariante.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Torres, L. Ariza, L y Blanco, D (2016). Cinética de adsorción de 2-Nitrofenol desde disolución acuosa sobre carbón activado.<br><strong><a href="https://revistaciencias.univalle.edu.co/index.php/revista_de_ciencias/article/view/4674/6855" target="_blank" rel="noreferrer noopener">https://revistaciencias.univalle.edu.co/index.php/revista_de_ciencias/article/view/4674/6855</a></strong>.</li>
                                        </ul>
<p style="text-align: justify;">Para la elaboración del organizador gráfico puede realizarlo en plataformas como: Miro, Mindmeister, Canva, Genially, Lucidchart, Creately, etc. Debe adjuntar directamente el diagrama de araña. Evitar adjuntar enlaces donde se haya creado el recurso ya que la mayoría de las veces solicitan acceso. En caso de adjuntarlo y si no se logra su visualización se calificará teniendo en cuenta los criterios de la <strong><a href="@@PLUGINFILE@@/Rubrica2Estadística_Descriptiva.pdf" target="_blank" rel="noopener">rúbrica de evaluación</a></strong>.<br><br><strong>Actividad 2: Aplicación de regresión y correlación</strong><br><br>Realice la consulta de un artículo nacional o internacional (académico o científico relacionado con su carrera profesional como futuro ingeniero de software o una temática de su interés), en el cual se haya implementado un modelo de regresión o análisis de correlación.<br><br>Para tal fin podrá consultar en la biblioteca en línea de la UDES a través del siguiente enlace:<br><br><strong><a href="https://udes.edu.co/biblioteca/servicios" target="_blank" rel="noreferrer noopener">https://udes.edu.co/biblioteca/servicios</a></strong><br><br>Posterior a su lectura y revisión deberá realizar un breve resumen compuesto por mínimo 250 palabras en inglés, donde destaque: <strong>título, autores, objetivos, resultados y conclusiones del artículo</strong>. No se admite presentar el mismo resumen que viene en el artículo en caso de presentar el mismo se calificará teniendo en cuenta la <strong><a href="@@PLUGINFILE@@/Rubrica2Estadística_Descriptiva.pdf" target="_blank" rel="noopener">rúbrica de evaluación</a></strong>.<br><br>Como ejemplo puede consultar el recurso: Torres, L. Ariza, L y Blanco, D (2016). Cinética de adsorción de 2-Nitrofenol desde disolución acuosa sobre carbón activado (el cual se encuentra en las referencias al inicio de la semana).<br><br>Es indispensable que dentro del artículo de su elección efectivamente se haya realizado la aplicación de un modelo de regresión y correlación lineal de lo contrario el artículo no podrá servirle para el desarrollo efectivo de la actividad.<br><br>Las actividades 3, 4 y 5 se pueden realizar utilizando Excel (Office) o el software Estadístico Infostat. Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar para el desarrollo de las actividades 3, 4 y 5:</p>
<ul>
                                            <li style="margin-bottom: 10px;"><strong>Tarjetas didácticas medidas estadísticas bivariantes</strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Presentación Unidad 4 – Medidas bivariantes</strong>.</li>
                                        </ul>
<p style="text-align: justify;"><strong>Actividad 3: Ejercicio de aplicación</strong><br><br>Con base a la tabla que se encuentra en la <strong><a href="@@PLUGINFILE@@/Entregable4_Interpretación de resultados.docx" target="_blank" rel="noopener">plantilla</a></strong> en la cual se ilustran 8 valores anuales de ganancias de una empresa colombiana en miles de millones en el eje (<span>y</span>), y la inversión en miles de millones de dicha empresa en el eje (<span>x</span>).<br><br>Calcule los siguientes parámetros:<br><br>a. Realice el diagrama de dispersión y determine el tipo de asociación entre las variables.<br><br>b. Encuentre el coeficiente de determinación y correlación.<br><br>c. Determine el modelo matemático que permite predecir el efecto de una variable sobre la otra. ¿Es confiable?<br><br>d. Determine el grado de relación de las dos variables.</p>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana9" role="tabpanel" aria-labelledby="semana9-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">A través de su proceso de enseñanza - aprendizaje y de la apropiación del conocimiento, enfoque su aprendizaje en la actividad 4 y 5.<br><br><strong>Actividad 4. Regresión y correlación lineal simple</strong><br><br>Para el desarrollo de la actividad 4 y 5 puede apoyarse en los referentes sugeridos de la actividad 1.<br><br>Con base en el <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> presente los siguientes parámetros:<br><br>a. Identificar dos variables cuantitativas de la situación estudiada que puedan estar relacionadas e identificar cuál podría ser la variable dependiente e independiente.<br><br>b. Realizar el diagrama de dispersión de dichas variables y determinar el tipo de relación entre las variables.<br><br>c. Determine al coeficiente de determinación y de correlación de las dos variables. Interprete los resultados.<br><br>d. Encuentre el modelo matemático que permite predecir el efecto de una variable sobre la otra. ¿Es confiable?<br><br>e. Presente un análisis general de los resultados obtenidos de acuerdo con la problemática de estudio. Copie y pegue el diagrama de dispersión que realizó desde Excel o desde Infostat. Recuerde que debe aparecer directamente la imagen y no adjuntar enlaces de ningún tipo.<br><br><strong>Actividad 5. Regresión y correlación múltiple</strong><br><br>Se sugerirá revisar el recurso adicional:</p>
<ul>
                                            <li style="margin-bottom: 10px;">Barón, F. (2022). Capítulo 7 Regresión lineal múltiple. En: Apuntes de Estadística.<br><strong><a href="https://www.bioestadistica.uma.es/apuntesMaster/regresi%C3%B3n-lineal-m%C3%BAltiple.html" target="_blank" rel="noreferrer noopener">https://www.bioestadistica.uma.es/apuntesMaster/regresi%C3%B3n-lineal-m%C3%BAltiple.html</a></strong>.</li>
                                        </ul>
<p style="text-align: justify;">Con base en el <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> presente los siguientes parámetros:<br><br>a. Identificar una variable cuantitativa dependiente y varias variables cuantitativas independientes del estudio de investigación.<br><br>b. Realizar el diagrama de dispersión de dichas variables y determinar el tipo de relación entre las variables.<br><br>c. Determine al coeficiente de determinación y de correlación para probar estadísticamente su relación.<br><br>d. Encuentre el modelo de regresión lineal múltiple.<br><br>e. Presente un análisis general de los resultados obtenidos de acuerdo con la problemática de estudio. Copie y pegue el diagrama de dispersión que realizó desde Excel o desde Infostat. Recuerde que debe aparecer directamente la imagen y no adjuntar enlaces de ningún tipo.<br><br>Realice la entrega del entregable en la LMS. Una vez realizada la calificación recuerde tener en cuenta los comentarios de retroalimentación para los próximos entregables.</p>
                                        <div style="text-align: center;">
                                            <a href="https://virtual.udes.edu.co/mod/assign/view.php?id=3952" target="_blank" rel="noopener">
                                                <button type="button" class="btn btn-outline-primary btn-lg" aria-pressed="true" role="button">
                                                    <span class="spinner-grow spinner-grow-sm"></span> Enviar Avance 4.
                                                </button>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana10" role="tabpanel" aria-labelledby="semana10-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">Culminamos el curso con el entregable 5 el cual se debe entregar de manera grupal en caso de realizar la entrega de manera individual tenga en cuenta que se tendrá en cuenta los criterios de la <strong><a href="@@PLUGINFILE@@/Rubrica2Estadística_Descriptiva.pdf" target="_blank" rel="noopener">rúbrica</a></strong> para su evaluación.<br><br>Deberá entregar un informe en formato PDF donde se consolide el desarrollo de las actividades propuestas en la plantilla <strong><a href="@@PLUGINFILE@@/Entregable5_Presentación de resultados.docx" target="_blank" rel="noopener">Entregable 5. Presentación de resultados</a></strong>.<br><br>Las actividades se pueden realizar utilizando Excel (Office) o el software Estadístico Infostat.<br><br><strong>Ajuste de datos</strong><br><br>Para iniciar su trabajo, el grupo deberá ajustar la base de datos: <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> trabajada a lo largo del curso, el grupo dejará sólo los primeros 100 datos en cada una de las variables y procederá a procesarlos como una muestra de la base original.<br><br>Una vez ajustada la base de datos, el grupo deberá tomar mínimo seis variables (al menos dos cualitativas, dos cuantitativas discretas y dos cuantitativas continuas) y procesará para cada variable la información solicitada a continuación:<br><br>Para el desarrollo de esta actividad puede apoyarse en los recursos bibliográficos que fueron trabajados en la Unidad 1, 2, 3 y 4.<br><br><strong>Actividad 1. Variable cualitativa</strong><br><br>-Caracterizar una de las variables cualitativas elegidas presentando: tabla de frecuencias, diagrama de barras y circular, moda, tabla de contingencias y conclusiones.<br><br>-Realizar una tabla de contingencias con las dos variables cualitativas seleccionadas.<br><br><strong>Actividad 2. Variable cuantitativa discreta</strong><br><br>Para una de las variables discreta elegida, se deberán calcular las medidas univariantes de tendencia central: media, mediana, moda y todos los cuartiles. Así mismo deberán calcular las medidas univariantes de dispersión: rango, varianza, desviación típica y coeficiente de variación.</p>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana11" role="tabpanel" aria-labelledby="semana11-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;"><strong>Actividad 3. Variable cuantitativa continua</strong><br><br>Para una de las variables continua elegida, se deberán calcular las medidas univariantes de tendencia central: media, mediana, moda y todos los cuartiles. Así mismo deberán calcular las medidas univariantes de dispersión: rango, varianza, desviación típica y coeficiente de variación.</p>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana12" role="tabpanel" aria-labelledby="semana12-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;"><strong>Actividad 4. Regresión y correlación entre variables cuantitativas</strong><br><br>Identificar las dos variables <strong>cuantitativas discreta y continua que no se hayan trabajado en la actividad 2 y 3</strong> de las 6 que se eligieron inicialmente y calcular los siguientes parámetros:</p>
<ol>
                                            <li style="margin-bottom: 10px;">Realizar el diagrama de dispersión de dichas variables y determinar el tipo de asociación entre las variables.</li>
                                            <li style="margin-bottom: 10px;">Encontrar el modelo matemático que permite predecir el efecto de una variable sobre la otra. ¿Es confiable?</li>
                                            <li style="margin-bottom: 10px;">Determinar el grado de relación de las dos variables.</li>
                                            <li style="margin-bottom: 10px;">Relacionar la información obtenida con el problema.</li>
                                        </ol>
<p style="text-align: justify;"><strong>Actividad 5. Análisis y propuesta de solución a la problemática</strong><br><br>Finalmente, el grupo deberá responder a la pregunta: <strong>¿Qué alternativa de solución plantea para la problemática estudiada?,</strong> dicha respuesta deberá estar justificada descriptivamente, es decir para ello (utilizará tablas, gráficos, medidas, diagramas, entre otros) que fueron realizados en las actividades 1, 2 y 3.<br><br><strong>Describir:</strong> es explicar, representar, definir con detalle, las cualidades características o las circunstancias de algo o de alguien.<br><br><strong>Por ejemplo:</strong><br><br>Del diagrama estadístico “XX" se desprende que.... De la tabla "XX" podemos concluir que.... A partir del valor de las medidas univariantes o de dispersión …Podemos afirmar que…. y… por esto consideramos necesario realizar……. Para ello es necesario disponer de …. (ver tabla XX) y se propone realizar.<br><br>Realice la entrega del entregable en la plataforma.</p>
                                        <div style="text-align: center;">
                                            <a href="https://virtual.udes.edu.co/mod/assign/view.php?id=3953" target="_blank" rel="noopener">
                                                <button type="button" class="btn btn-outline-primary btn-lg" aria-pressed="true" role="button">
                                                    <span class="spinner-grow spinner-grow-sm"></span> Enviar Producto Final.
                                                </button>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>"""

# Rebuild Momento 1 HTML
with open(filepath_m1, "w", encoding="utf-8") as f:
    f.write(header_m1 + tab_home_m1 + tab_profile_m1 + tab_profile1_m1 + tab_profile2_m1 + tab_settings_m1 + footer)
print("Rebuilt Momento Evaluativo1.html successfully!")

# Rebuild Momento 2 HTML
with open(filepath_m2, "w", encoding="utf-8") as f:
    f.write(header_m2 + tab_home_m2 + tab_profile_m2 + tab_profile1_m2 + tab_profile2_m2 + tab_settings_m2 + footer)
print("Rebuilt Momento Evaluativo2.html successfully!")

# Run automatic validation
print("\nRunning automatic post-build validation checks...")
import sys
sys.path.append(os.path.dirname(__file__))
from verify_momentos import validate_file

v1 = validate_file(filepath_m1)
v2 = validate_file(filepath_m2)
if not (v1 and v2):
    print("\n❌ BUILD WARNING: One or more files generated do not comply with the formatting rules!")
    sys.exit(1)
else:
    print("\n✅ BUILD SUCCESS: All generated files are 100% compliant with all rules!")
