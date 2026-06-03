import os

filepath = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/3_paginas_finales/Momentos/Momento Evaluativo2.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Let's find the start of v-pills-settings tab pane
start_marker = '<div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-settings"'
start_idx = html.find(start_marker)

if start_idx == -1:
    print("Could not find v-pills-settings in HTML!")
    exit(1)

# Keep everything before v-pills-settings
header = html[:start_idx]

# Write the new v-pills-settings tab pane and the closing section
new_settings = """<div class="tab-pane fade shadow rounded bg-white p-5" id="v-pills-settings"
                        role="tabpanel" aria-labelledby="v-pills-settings-tab">
                        <h4 class="mb-4">Contenido de los Entregables 3, 4 y 5</h4>
                        <div>
                            <ul class="nav nav-tabs" id="myTab" role="tablist">
                                <li class="nav-item">
                                    <a class="nav-link active" id="semana6-tab" data-toggle="tab" href="#semana6" role="tab"
                                        aria-controls="semana6" aria-selected="true">Semana 6
                                        <small class="d-block" style="text-align: center;">Avance 3</small></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" id="semana7-tab" data-toggle="tab" href="#semana7" role="tab"
                                        aria-controls="semana7" aria-selected="false" tabindex="-1">Semana 7
                                        <small class="d-block" style="text-align: center;">Avance 3</small></a>
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
                                        <p style="text-align: justify;">Continuamos a la <strong>Unidad 3 – medidas estadísticas univariantes con el entregable 3 – Análisis de datos</strong>.<br><br>Deberá entregar un informe en formato PDF donde se consolide el desarrollo de las actividades propuestas en la plantilla <strong>Entregable_3. Análisis de datos</strong>.<br><br><strong>Actividad 1: Organizador gráfico</strong><br><br>Resuma en un mapa conceptual las medidas estadísticas univariantes (medidas de tendencia central, medidas de posición, medidas de dispersión, medidas de asimetría y apuntamiento), detallando cada una de ellas.<br><br>Se recomienda realizar una revisión de los recursos:</p><br><br>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Universidad Abierta y a Distancia de México. (s.f.) Unidad 2. Medidas de tendencia central y dispersión.<br><strong><a href="https://dmd.unadmexico.mx/contenidos/TRONCO_COMUN/EBA/U2/descargables/EBA_U2_Contenidos.pdf" target="_blank" rel="noreferrer noopener">https://dmd.unadmexico.mx/contenidos/TRONCO_COMUN/EBA/U2/descargables/EBA_U2_Contenidos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 7. Medidas de tendencia central. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 72 - 85).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noreferrer noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 8. Medidas de posición. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 86 - 95).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noreferrer noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 9. Medidas de dispersión. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 96 - 107).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noreferrer noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Posada, G. (2016). Capítulo 10. Medidas de forma. En: Elementos básicos de estadística descriptiva para el análisis de datos. Fundación Universitaria Luis Amigó. Fondo Editorial Luis Amigó. Medellín (pp. 108 - 115).<br><strong><a href="https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf" target="_blank" rel="noreferrer noopener">https://www.funlam.edu.co/uploads/fondoeditorial/120_Ebook-elementos_basicos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Suarez. M. (2025). Capítulo 1. Medidas de tendencia central. En: Estadística descriptiva para todos: Fundamentos y aplicaciones – Volumen II. (pp.12 –35).<br><strong><a href="https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I" target="_blank" rel="noreferrer noopener">https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Suarez. M. (2025). Capítulo 2. Medidas de posición. En: Estadística descriptiva para todos: Fundamentos y aplicaciones – Volumen II. (pp.36 – 60).<br><strong><a href="https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I" target="_blank" rel="noreferrer noopener">https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Suarez. M. (2025). Capítulo 3. Medidas de dispersión. En: Estadística descriptiva para todos: Fundamentos y aplicaciones – Volumen II. (pp.61 – 95).<br><strong><a href="https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I" target="_blank" rel="noreferrer noopener">https://www.researchgate.net/publication/391908519_ESTADISTICA_DESCRIPTIVA_PARA_TODOS_FUNDAMENTOS_Y_APLICACIONES_VOLUMEN_I</a></strong>.</li>
                                        </ul><br><br>
                                        <p style="text-align: justify;">Para la elaboración del organizador gráfico puede realizarlo en plataformas como: Miro, Mindmeister, Canva, Genially, Lucidchart, Creately, etc. Debe adjuntar directamente el cuadro sinóptico. Evitar adjuntar enlaces donde se haya creado el recurso ya que la mayoría de las veces solicitan acceso. En caso de adjuntarlo y si no se logra su visualización se calificará teniendo en cuenta los criterios de la rúbrica de evaluación.<br><br>Las actividades 2 y 3 se pueden realizar utilizando Excel (Office) o el software Estadístico Infostat.<br><br>Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar para el desarrollo de las actividades 2 y 3:</p><br><br>
                                        <ul>
                                            <li style="margin-bottom: 10px;"><strong>Tarjetas didácticas medidas de tendencia central y de dispersión</strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Tarjetas didácticas medidas de posición y medidas de forma</strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Presentación caza del tesoro de las medidas estadísticas</strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Presentación tablas de frecuencias</strong>.</li>
                                        </ul><br><br>
                                        <p style="text-align: justify;"><strong>Actividad 2: Medidas univariantes - variable discreta</strong><br><br>Para el desarrollo de la actividad puede consultar los recursos sugeridos en la actividad 1 y adicionalmente la referencia:</p><br><br>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Montero, J. M. (2007). Características de Una Distribución de Frecuencias. Statistical Descriptive. Cengage Learning Paraninfo, S.A. (pp 17 – 61).<br><strong><a href="https://link.gale.com/apps/doc/CX4052100008/GVRL?u=unad&sid=GVRL&xid=d49ed557" target="_blank" rel="noreferrer noopener">https://link.gale.com/apps/doc/CX4052100008/GVRL?u=unad&sid=GVRL&xid=d49ed557</a></strong>.</li>
                                        </ul><br><br>
                                        <p style="text-align: justify;">Con base en el <strong>Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</strong> seleccione una variable CUANTITATIVA DISCRETA.<br><br><strong>Determine los siguientes elementos:</strong><br><br>a. <strong>Tabla de frecuencia datos no agrupados.</strong> diseñar una tabla de frecuencia para datos no agrupados de la variable elegida, a partir de ella elaborar un diagrama de barras y un diagrama de líneas o de puntos.<br><br><strong>b. Medidas de tendencias central y de posición:</strong> para la variable cuantitativa discreta elegida, deberá calcular las medidas de tendencia central (media, mediana y moda), medidas de posición: cuartiles 1, 2 y 3, percentil 30 y 90, determinar el tipo de asimetría y curtosis, interpretar los resultados, sacar conclusiones de los parámetros hallados y asociarlos con la problemática de estudio indicadores de accidentalidad vial en algunos departamentos de Colombia.<br><br><strong>c. Medidas de dispersión:</strong> para la variable cuantitativa discreta elegida calcular: rango, varianza, desviación típica o estándar, coeficiente de variación, posteriormente interpretar los resultados, sacar conclusiones de los parámetros hallados y asociarlos con la problemática de estudio indicadores de accidentalidad vial en algunos departamentos de Colombia.<br><br>Se deben presentar los resultados teniendo en cuenta la tabla consignada en la plantilla del entregable.</p>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana7" role="tabpanel" aria-labelledby="semana7-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">Reciban la más cordial bienvenida a la semana siete de este proceso académico. Iniciamos el momento evaluativo II de producto y la recta final del desarrollo del curso.<br><br>A través de su proceso de enseñanza - aprendizaje y de la apropiación del conocimiento, enfoque su aprendizaje en la actividad 3.<br><br><strong>Actividad 3: Medidas univariantes - variable continua</strong><br><br>Para el desarrollo de la actividad puede consultar los recursos sugeridos en la actividad 1 y 2.<br><br>Con base en el <strong>Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</strong> seleccione una variable CUANTITATIVA CONTINUA.<br><br><strong>Determine los siguientes elementos:</strong><br><br>a. <strong>Tabla de frecuencia datos agrupados.</strong> Con la variable cuantitativa continua elegida, diseñar una tabla de frecuencias para datos agrupados, identificando rango, número de intervalos, amplitud y a partir de ella elaborar un histograma de frecuencias y un polígono de frecuencias. Finalmente, interpretar los resultados de la tabla, de los gráficos estadísticos y asociarlos con la problemática <strong>indicadores de accidentalidad vial en algunos departamentos de Colombia.</strong><br><br>Debe realizar las tablas en Excel teniendo en cuenta el diseño consignado en la plantilla en su hoja de cálculo para la presentación de los resultados.<br><br><strong>b. Medidas de tendencias central y de posición:</strong> Para la variable cuantitativa continua elegida, deberá calcular las medidas de tendencia central (media, mediana, moda), medidas de posición: cuartiles 1, 2 y 3, percentil 15, 55 y 90, determinar el tipo de asimetría y curtosis e interpretar los resultados, sacar conclusiones de los parámetros hallados y asociarlos con la problemática <strong>indicadores de accidentalidad vial en algunos departamentos de Colombia.</strong><br><br><strong>c. Medidas de dispersión:</strong> Para la variable cuantitativa continua elegida calcular: rango, varianza, desviación típica o estándar, coeficiente de variación, posteriormente interpretar los resultados, sacar conclusiones de los parámetros hallados y asociarlos con la problemática <strong>indicadores de accidentalidad vial en algunos departamentos de Colombia.</strong><br><br>Se deben presentar los resultados teniendo en cuenta la tabla consignada en la plantilla del entregable.<br><br>A través de su proceso de enseñanza - aprendizaje y de la apropiación del conocimiento, enfoque su aprendizaje en la actividad 4.<br><br><strong>Actividad 4: Relación de la situación problema con los ODS (Objetivos de Desarrollo Sostenible)</strong><br><br>Diseñe una infografía en la cual pueda presentar como mejorar los <strong>indicadores de accidentalidad vial en algunos departamentos de Colombia</strong> podría contribuir a los <strong>ODS (Objetivos de Desarrollo Sostenible)</strong> y con cuáles específicamente se podría relacionar.<br><br><strong>Tener en cuenta los siguientes parámetros de presentación:</strong><br><br>Busque fuentes de información confiables para el desarrollo de la infografía.<br><br>Debe incluir gráficos, diagramas, esquemas o imágenes.<br><br>El texto que se incluya dentro de la infografía debe ser en inglés.<br><br>Debe tener un diseño creativo.<br><br>Puede crearlo en cualquier plataforma de preferencia personal.<br><br>Debe adjuntar directamente la imagen de la infografía.<br><br>Evitar adjuntar enlaces donde se haya creado, ya que la mayoría de las veces solicitan acceso. En caso de adjuntarlo y si no se logra su visualización se calificará teniendo en cuenta los criterios de la rúbrica de evaluación.<br><br>Realice la entrega del entregable en la plataforma. Una vez realizada la calificación recuerde tener en cuenta los comentarios de retroalimentación para los próximos entregables.</p>
                                        <br><br>
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
                                        <p style="text-align: justify;">Exploraremos la <strong>Unidad 4 – Medidas estadísticas bivariantes con el entregable 4 – interpretación de resultados</strong>.<br><br>Deberá entregar un informe en formato PDF donde se consolide el desarrollo de las actividades propuestas en la plantilla <strong>Entregable_4. Interpretación de resultados</strong>.<br><br><strong>Actividad 1: Organizador gráfico</strong><br><br>Resuma en un diagrama de araña las medidas estadísticas bivariantes de regresión y correlación.<br><br>Para el desarrollo de la actividad puede consultar los recursos:</p><br><br>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Talagala, P. (2020). Chapter 10 Correlation and Regression.<br><strong><a href="https://pridiltal.github.io/CM1110/correlation-and-regression.html" target="_blank" rel="noreferrer noopener">https://pridiltal.github.io/CM1110/correlation-and-regression.html</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Universidad Abierta y a Distancia de México. (s.f.) Unidad 3. Correlación y regresión lineal simple.<br><strong><a href="https://dmd.unadmexico.mx/contenidos/TRONCO_COMUN/EBA/U3/descargables/EBA_U3_Contenidos.pdf" target="_blank" rel="noreferrer noopener">https://dmd.unadmexico.mx/contenidos/TRONCO_COMUN/EBA/U3/descargables/EBA_U3_Contenidos.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Elias, J. (2019). Análisis bivariante.<br><strong><a href="https://openaccess.uoc.edu/bitstream/10609/148455/1/AnalisisBivariante.pdf" target="_blank" rel="noreferrer noopener">https://openaccess.uoc.edu/bitstream/10609/148455/1/AnalisisBivariante.pdf</a></strong>.</li>
                                            <li style="margin-bottom: 10px;">Torres, L. Ariza, L y Blanco, D (2016). Cinética de adsorción de 2-Nitrofenol desde disolución acuosa sobre carbón activado.<br><strong><a href="https://revistaciencias.univalle.edu.co/index.php/revista_de_ciencias/article/view/4674/6855" target="_blank" rel="noreferrer noopener">https://revistaciencias.univalle.edu.co/index.php/revista_de_ciencias/article/view/4674/6855</a></strong>.</li>
                                        </ul><br><br>
                                        <p style="text-align: justify;">Para la elaboración del organizador gráfico puede realizarlo en plataformas como: Miro, Mindmeister, Canva, Genially, Lucidchart, Creately, etc. Debe adjuntar directamente el diagrama de araña. Evitar adjuntar enlaces donde se haya creado el recurso ya que la mayoría de las veces solicitan acceso. En caso de adjuntarlo y si no se logra su visualización se calificará teniendo en cuenta los criterios de la rúbrica de evaluación.<br><br><strong>Actividad 2: Aplicación de regresión y correlación</strong><br><br>Realice la consulta de un artículo nacional o internacional (académico o científico relacionado con su carrera profesional como futuro ingeniero de software o una temática de su interés), en el cual se haya implementado un modelo de regresión o análisis de correlación.<br><br>Para tal fin podrá consultar en la biblioteca en línea de la UDES a través del siguiente enlace:<br><br><strong><a href="https://udes.edu.co/biblioteca/servicios" target="_blank" rel="noreferrer noopener">https://udes.edu.co/biblioteca/servicios</a></strong><br><br>Posterior a su lectura y revisión deberá realizar un breve resumen compuesto por mínimo 250 palabras en inglés, donde destaque: <strong>título, autores, objetivos, resultados y conclusiones del artículo</strong>. No se admite presentar el mismo resumen que viene en el artículo en caso de presentar el mismo se calificará teniendo en cuenta la rúbrica de evaluación.<br><br>Como ejemplo puede consultar el recurso: Torres, L. Ariza, L y Blanco, D (2016). Cinética de adsorción de 2-Nitrofenol desde disolución acuosa sobre carbón activado (el cual se encuentra en las referencias al inicio de la semana).<br><br>Es indispensable que dentro del artículo de su elección efectivamente se haya realizado la aplicación de un modelo de regresión y correlación lineal de lo contrario el artículo no podrá servirle para el desarrollo efectivo de la actividad.<br><br>Las actividades 3, 4 y 5 se pueden realizar utilizando Excel (Office) o el software Estadístico Infostat. Complemente su proceso de enseñanza aprendizaje con el estudio de los recursos educativos Digitales RED, elaborados por el experto disciplinar para el desarrollo de las actividades 3, 4 y 5:</p><br><br>
                                        <ul>
                                            <li style="margin-bottom: 10px;"><strong>Tarjetas didácticas medidas estadísticas bivariantes</strong>.</li>
                                            <li style="margin-bottom: 10px;"><strong>Presentación Unidad 4 – Medidas bivariantes</strong>.</li>
                                        </ul><br><br>
                                        <p style="text-align: justify;"><strong>Actividad 3: Ejercicio de aplicación</strong><br><br>Con base a la tabla que se encuentra en la plantilla en la cual se ilustran 8 valores anuales de ganancias de una empresa colombiana en miles de millones en el eje (y), y la inversión en miles de millones de dicha empresa en el eje (x).<br><br>Calcule los siguientes parámetros:<br><br>a. Realice el diagrama de dispersión y determine el tipo de asociación entre las variables.<br><br>b. Encuentre el coeficiente de determinación y correlación.<br><br>c. Determine el modelo matemático que permite predecir el efecto de una variable sobre la otra. ¿Es confiable?<br><br>d. Determine el grado de relación de las dos variables.</p>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana9" role="tabpanel" aria-labelledby="semana9-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;">A través de su proceso de enseñanza - aprendizaje y de la apropiación del conocimiento, enfoque su aprendizaje en la actividad 4 y 5.<br><br><strong>Actividad 4. Regresión y correlación lineal simple</strong><br><br>Para el desarrollo de la actividad 4 y 5 puede apoyarse en los referentes sugeridos de la actividad 1.<br><br>Con base en el <strong>Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</strong> presente los siguientes parámetros:<br><br>a. Identificar dos variables cuantitativas de la situación estudiada que puedan estar relacionadas e identificar cuál podría ser la variable dependiente e independiente.<br><br>b. Realizar el diagrama de dispersión de dichas variables y determinar el tipo de relación entre las variables.<br><br>c. Determine al coeficiente de determinación y de correlación de las dos variables. Interprete los resultados.<br><br>d. Encuentre el modelo matemático que permite predecir el efecto de una variable sobre la otra. ¿Es confiable?<br><br>e. Presente un análisis general de los resultados obtenidos de acuerdo con la problemática de estudio. Copie y pegue el diagrama de dispersión que realizó desde Excel o desde Infostat. Recuerde que debe aparecer directamente la imagen y no adjuntar enlaces de ningún tipo.<br><br><strong>Actividad 5. Regresión y correlación múltiple</strong><br><br>Se sugerirá revisar el recurso adicional:</p><br><br>
                                        <ul>
                                            <li style="margin-bottom: 10px;">Barón, F. (2022). Capítulo 7 Regresión lineal múltiple. En: Apuntes de Estadística.<br><strong><a href="https://www.bioestadistica.uma.es/apuntesMaster/regresi%C3%B3n-lineal-m%C3%BAltiple.html" target="_blank" rel="noreferrer noopener">https://www.bioestadistica.uma.es/apuntesMaster/regresi%C3%B3n-lineal-m%C3%BAltiple.html</a></strong>.</li>
                                        </ul><br><br>
                                        <p style="text-align: justify;">Con base en el <strong>Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</strong> presente los siguientes parámetros:<br><br>a. Identificar una variable cuantitativa dependiente y varias variables cuantitativas independientes del estudio de investigación.<br><br>b. Realizar el diagrama de dispersión de dichas variables y determinar el tipo de relación entre las variables.<br><br>c. Determine al coeficiente de determinación y de correlación para probar estadísticamente su relación.<br><br>d. Encuentre el modelo de regresión lineal múltiple.<br><br>e. Presente un análisis general de los resultados obtenidos de acuerdo con la problemática de estudio. Copie y pegue el diagrama de dispersión que realizó desde Excel o desde Infostat. Recuerde que debe aparecer directamente la imagen y no adjuntar enlaces de ningún tipo.<br><br>Realice la entrega del entregable en la LMS. Una vez realizada la calificación recuerde tener en cuenta los comentarios de retroalimentación para los próximos entregables.</p>
                                        <br><br>
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
                                        <p style="text-align: justify;">Culminamos el curso con el entregable 5 el cual se debe entregar de manera grupal en caso de realizar la entrega de manera individual tenga en cuenta que se tendrá en cuenta los criterios de la rúbrica para su evaluación.<br><br>Deberá entregar un informe en formato PDF donde se consolide el desarrollo de las actividades propuestas en la plantilla <strong>Entregable_5. Presentación de resultados</strong>.<br><br>Las actividades se pueden realizar utilizando Excel (Office) o el software Estadístico Infostat.<br><br><strong>Ajuste de datos</strong><br><br>Para iniciar su trabajo, el grupo deberá ajustar la base de datos: <strong><a href="@@PLUGINFILE@@/Anexo1_Base_de_datos.xlsx" target="_blank" rel="noopener">Anexo 1. Base de datos indicadores de accidentalidad vial en algunos departamentos de Colombia</a></strong> trabajada a lo largo del curso, el grupo dejará sólo los primeros 100 datos en cada una de las variables y procederá a procesarlos como una muestra de la base original.<br><br>Una vez ajustada la base de datos, el grupo deberá tomar mínimo seis variables (al menos dos cualitativas, dos cuantitativas discretas y dos cuantitativas continuas) y procesará para cada variable la información solicitada a continuación:<br><br>Para el desarrollo de esta actividad puede apoyarse en los recursos bibliográficos que fueron trabajados en la Unidad 1,2,3 y 4.<br><br><strong>Actividad 1. Variable cualitativa</strong><br><br>-Caracterizar una de las variables cualitativas elegidas presentando: tabla de frecuencias, diagrama de barras y circular, moda, tabla de contingencias y conclusiones.<br><br>-Realizar una tabla de contingencias con las dos variables cualitativas seleccionadas.<br><br><strong>Actividad 2. Variable cuantitativa discreta</strong><br><br>Para una de las variables discreta elegida, se deberán calcular las medidas univariantes de tendencia central: media, mediana, moda y todos los cuartiles. Así mismo deberán calcular las medidas univariantes de dispersión: rango, varianza, desviación típica y coeficiente de variación.</p>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana11" role="tabpanel" aria-labelledby="semana11-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;"><strong>Actividad 3. Variable cuantitativa continua</strong><br><br>Para una de las variables continua elegida, se deberán calcular las medidas univariantes de tendencia central: media, mediana, moda y todos los cuartiles. Así mismo deberán calcular las medidas univariantes de dispersión: rango, varianza, desviación típica y coeficiente de variación.</p>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="semana12" role="tabpanel" aria-labelledby="semana12-tab">
                                    <div class="card-body">
                                        <p style="text-align: justify;"><strong>Actividad 4. Regresión y correlación entre variables cuantitativas</strong><br><br>Identificar las dos variables <strong>cuantitativas discreta y continua que no se hayan trabajado en la actividad 2 y 3</strong> de las 6 que se eligieron inicialmente y calcular los siguientes parámetros:</p><br><br>
                                        <ol>
                                            <li style="margin-bottom: 10px;">Realizar el diagrama de dispersión de dichas variables y determinar el tipo de asociación entre las variables.</li>
                                            <li style="margin-bottom: 10px;">Encontrar el modelo matemático que permite predecir el efecto de una variable sobre la otra. ¿Es confiable?</li>
                                            <li style="margin-bottom: 10px;">Determinar el grado de relación de las dos variables.</li>
                                            <li style="margin-bottom: 10px;">Relacionar la información obtenida con el problema.</li>
                                        </ol><br><br>
                                        <p style="text-align: justify;"><strong>Actividad 5. Análisis y propuesta de solución a la problemática</strong><br><br>Finalmente, el grupo deberá responder a la pregunta: <strong>¿Qué alternativa de solución plantea para la problemática estudiada?,</strong> dicha respuesta deberá estar justificada descriptivamente, es decir para ello (utilizará tablas, gráficos, medidas, diagramas, entre otros) que fueron realizados en las actividades 1,2 y 3.<br><br><strong>Describir:</strong> es explicar, representar, definir con detalle, las cualidades características o las circunstancias de algo o de alguien.<br><br><strong>Por ejemplo:</strong><br><br>Del diagrama estadístico “XX" se desprende que.... De la tabla "XX" podemos concluir que.... A partir del valor de las medidas univariantes o de dispersión …Podemos afirmar que…. y… por esto consideramos necesario realizar……. Para ello es necesario disponer de …. (ver tabla XX) y se propone realizar.<br><br>Realice la entrega del entregable en la plataforma.</p>
                                        <br><br>
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
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

with open(filepath, "w", encoding="utf-8") as f:
    f.write(header + new_settings)

print("Updated Momento Evaluativo2.html successfully!")
