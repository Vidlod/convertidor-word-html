# Instrucciones y Pasos a Seguir para la Conversión de HTML

Este documento sirve como la guía oficial y fuente de verdad para el formateo, codificación y corrección de las páginas de los Momentos Evaluativos y otros entregables. Se detallan todas las reglas y directrices acordadas durante el desarrollo del proyecto.

---

## Estructura del Proyecto y Carpetas

El flujo de trabajo y la organización de archivos se estructuran en las siguientes carpetas:

1. **`Html Originales/`**: Contiene los archivos HTML de plantilla originales. Tienen la estructura visual e interactiva correcta (pestañas, tablas, clases CSS de Bootstrap), pero la **información y textos en su interior son incorrectos o antiguos**.
2. **`documentos_origen/`**: Contiene los archivos Word (`.docx` y sus conversiones `.html` limpias) que contienen la **información y textos correctos y actualizados** que deben insertarse en las plantillas.
3. **`paginas_finales/`**: Es la carpeta de destino donde se guardan los archivos HTML corregidos y finalizados (por ejemplo, `Momento Evaluativo1.html`, `Momento Evaluativo2.html`), listos para ser subidos a la plataforma virtual (Moodle).
4. **`Contexto & reglas/`**: Contiene los archivos de reglas, notas de contexto e instrucciones generales del proyecto.

---

## 1. Regla de Oro
* **No inventar nada, no parafrasear nada:** La información textual debe coincidir exactamente con los archivos de origen (Words, PDFs, etc.). 
* Si algún texto, instrucción o recurso no se encuentra en el archivo origen, se debe **detener y avisar al usuario** para que lo aclare, sin asumir ni inventar información.

---

## 2. Citas Bibliográficas
* **Sin cursiva:** Eliminar todas las etiquetas de cursiva (`<em>`, `<i>`, o estilos inline de cursiva) de las citas bibliográficas.
* **Sin Negrita (Strong) en el texto de la cita, y Link Visible y en Negrita:** La cita bibliográfica no debe ir en negrita (`<strong>` ni `<b>`). Tampoco debe ir el enlace incrustado directamente en el texto de la cita. En su lugar, el texto de la cita va como texto plano normal, seguido de un salto de línea (`<br>`) y el enlace explícito visible como hipervínculo envuelto siempre en negrita (`<strong>`).
  * Formato: `Autor (Año). Título del libro...<br><strong><a href="ENLACE_ELIBRO" target="_blank" rel="noopener">ENLACE_ELIBRO</a></strong>`
* **Limpieza de textos adicionales:** La cita bibliográfica debe ir completamente sola en su viñeta. Se deben remover textos descriptivos que queden pegados como `"Lectura requerida."` o `"Lectura de ampliación temática."`.
* **Separación:** Las citas bibliográficas siempre deben ir separadas por viñetas (`<li>`).

---

## 3. Recursos Educativos Digitales (RED)
* **Obligatoriedad de Viñetas (`<li>`)**: Todos los Recursos Educativos Digitales (RED) —incluyendo mapas conceptuales, infografías, cómics, podcasts y demás recursos— deben presentarse **siempre dentro de una viñeta o ítem de lista (`<li>`)**. Queda prohibido colocarlos sueltos o como párrafos independientes fuera de una lista.
* **Carga en local**: Los REDs que correspondan a archivos locales (tales como mapas conceptuales, infografías, cómics, etc.) deben enlazarse utilizando el formato portable `@@PLUGINFILE@@/Nombre_Archivo.ext` con el nombre exacto del archivo que se encuentra en la carpeta `Archivos E`.
* **Formato del Enlace**: El enlace debe estar en negrita y configurarse para abrirse en una pestaña nueva:
  * Formato: `<strong><a href="@@PLUGINFILE@@/Nombre_Archivo.ext" target="_blank" rel="noopener">Título del RED</a></strong>`
* **Sin Archivo/Enlace**: Si no hay un archivo local ni un enlace disponible, el título del RED se formatea únicamente en negrita simple:
  * Formato: `<strong>Título del RED</strong>`
* **Separación**: Cada RED siempre debe listarse en una viñeta independiente. En caso de recursos compuestos (ej. Parte I y Parte II), se deben separar en dos viñetas independientes con sus respectivos hipervínculos individuales.
* **Podcasts como RED**: Los podcasts son considerados Recursos Educativos Digitales (RED) y se integran mediante un reproductor de audio HTML5 nativo utilizando el formato de enlace portable.
  * Formato de código:
    ```html
    <li style="margin-bottom: 10px;"><strong>Podcast: Título del Podcast.</strong><br><br>
        <audio controls="true" title="Podcast: Título del Podcast">
            <source src="@@PLUGINFILE@@/Nombre_Archivo.mp3">@@PLUGINFILE@@/Nombre_Archivo.mp3
        </audio>
    </li>
    ```
    *(Nota: El elemento `<audio>` debe ubicarse siempre dentro del elemento de viñeta `<li>`, y no debe llevar saltos de línea `<br>` ni espacios al final, cerrándose de forma directa).*
  * **Revisión de Título por Escucha**: Siempre que haya un podcast en los recursos, se debe recordar al usuario que escuche el audio para verificar y ajustar el título del podcast en el HTML según corresponda a lo que dice el audio.

---

## 4. Estructura, Viñetas y Espaciado
* **Punto Final Obligatorio**: Al final del texto de cada viñeta (`<li>`), se debe colocar obligatoriamente un punto final (`.`).
* **Prohibición de Combinar `<li>` y `<p>`**: Queda estrictamente prohibido anidar etiquetas de párrafo (`<p>`) dentro de las etiquetas de lista o viñeta (`<li>`). El contenido o texto debe escribirse directamente dentro del elemento `<li>` (ej. `<li>Texto...</li>`), sin envolverlo en etiquetas `<p>`, para evitar distorsiones en los márgenes y en el renderizado del navegador.
* **Espaciado entre ítems (margin-bottom)**: 
  * Si en un grupo de viñetas (`<ul>` o `<ol>`), al menos **una viñeta tiene más de 3 renglones**, o bien **dos viñetas tienen 2 renglones**, se debe aplicar un espacio de separación entre cada ítem.
  * Implementación: Añadir `style="margin-bottom: 10px;"` a cada etiqueta `<li>` de ese grupo de viñetas.
  * Si los ítems tienen un solo renglón, se dejan pegados (sin margen).
* **Prohibición de saltos de línea inter-bloque (Prevención de Doble Espacio)**:
  * Queda estrictamente prohibido colocar etiquetas de salto de línea (`<br>` o `<br><br>`) directamente entre elementos de bloque HTML (por ejemplo, entre `</p>` y `<ul>`, o entre `</ul>` y `<p>`).
  * Moodle aplica márgenes CSS por defecto a los bloques. Colocar saltos de línea entre bloques acumula el margen con el salto de línea, produciendo una separación visual excesiva (doble renglón). Las listas y párrafos deben limitarse a abrirse y cerrarse consecutivamente (ej. `</p><ul>` o `</ul><p>`).

---

## 5. Botones de Envío de Entregables
* **En las pestañas semanales:**
  * Se agrega un botón de envío únicamente al final de la **última semana de cada Avance/Producto** (ej. Semana 3 para Avance 1, Semana 6 para Avance 2, Semana 8 para Avance 3, Semana 10 para Avance 4, Semana 14 para Producto Final).
  * El botón debe colocarse centrado dentro de un div:
    ```html
    <br><br>
    <div style="text-align: center;">
        <a href="ENLACE_MOODLE" rel="noopener">
            <button type="button" class="btn btn-outline-primary btn-lg" aria-pressed="true" role="button">
                <span class="spinner-grow spinner-grow-sm"></span> Enviar Entregable X.
            </button>
        </a>
    </div>
    ```
    *(Nota: Reemplazar `X` por el número de entregable correspondiente).*
* **En la pestaña "Instrumento para Enviar Entregable" (Pestaña 4):**
  * Debe contener exactamente la cantidad de botones necesarios que representen el número de avances del momento correspondiente (especificado en el Word).
  * Ejemplo: Momentos con 3 avances deben tener exactamente 3 botones (Avances 3, 4 y 5).
  * El formato de enlace y botón debe ser el estándar grande y preguntar al usuario por los enlaces correspondientes si no están definidos.

* **Nomenclatura del último Avance (Producto Final)**: Siempre que se mencione el último avance de la última semana (en este caso "Avance 5" del curso), este pasa a ser **Producto Final** de forma global en **todas** partes del HTML. Esto incluye la tabla resumen de entregas, las pestañas de navegación semanal, los botones de envío y los textos informativos. Queda prohibido usar la expresión "Avance 5" en cualquier parte del HTML de los momentos.
  - Ejemplo:
    - Tabla resumen, pestañas de navegación, botones de envío y textos informativos $\rightarrow$ **Producto Final**

---

## 6. Enlaces y Direcciones de Archivos en Moodle (Método Portable @@PLUGINFILE@@)
* **El Método Portable (`@@PLUGINFILE@@/`):**
  * Para evitar colocar enlaces absolutos que puedan caducar (como los enlaces `/draftfile.php/` temporales) y evitar la tarea manual de enlazar archivo por archivo, se utiliza el marcador oficial de Moodle: `@@PLUGINFILE@@/nombre_archivo.extension`.
  * **Cómo funciona la conversión automática:**
    1. En el código HTML local, se escribe la ruta de esta forma: `href="@@PLUGINFILE@@/Anexo1_Formato.docx"`.
    2. Al pegar el código en Moodle y subir el archivo físico, la plataforma traduce temporalmente el marcador a un enlace de sesión `/draftfile.php/...`.
    3. Al hacer clic en **Guardar cambios**, Moodle convierte de forma definitiva y automática el enlace a la ruta permanente del servidor: `/pluginfile.php/...`, asegurando que el archivo siempre esté disponible y no caduque.

* **Procedimiento para Carga Agilizada de Archivos en Bloque:**
  1. **Escribir en local usando el marcador:** Escribe todas las URLs de archivos y audios en el HTML usando la estructura `href="@@PLUGINFILE@@/Nombre_Exacto_del_Archivo.ext"` (o `src="@@PLUGINFILE@@/Nombre_Exacto_del_Archivo.ext"` para fuentes de reproductores).
  2. **Copiar y pegar el HTML:** Pega todo el código HTML en la vista de código fuente (`<>`) de Moodle.
  3. **Carga masiva de ficheros:** Haz clic en el icono **"Gestionar ficheros incrustados"** (el 6.º botón de la segunda fila en la barra de herramientas del editor, con forma de hoja de papel). En la ventana emergente que se abre, arrastra y suelta **todos los archivos locales en bloque de una sola vez** (esto incluye PDFs, documentos de Word y los archivos de audio `.mp3` de los podcasts. **Nota:** No utilice el icono del micrófono del editor de texto de Moodle para subir los podcasts, ya que ese botón está diseñado exclusivamente para realizar grabaciones de voz en vivo y no permite cargar ficheros pregrabados locales).
  4. **Guardar:** Cierra la ventana emergente de gestión de ficheros y guarda los cambios en Moodle. La plataforma enlazará todo automáticamente.





## 7. Anexos
* Los anexos y formatos mencionados en el contenido deben enlazarse localmente utilizando el formato portable `@@PLUGINFILE@@/Nombre_Archivo.ext` con el nombre exacto del archivo ubicado en la carpeta `Archivos E`.
* Deben formatearse en negrita y configurarse para abrirse en pestaña nueva (`target="_blank" rel="noopener"`).

---

## 8. Regla del apartado "Documento"
* Si en el PDF suministrado el párrafo inicial del entregable no está precedido por la palabra `"Documento."` o `"Documento:"` de manera explícita en su estructura original:
  - No se coloca el apartado de cabecera `<h5>Documento: ...</h5>` en el HTML.
  - En su lugar, se toma ese primer párrafo del PDF y se inserta como el primer párrafo dentro de la pestaña **"Forma de entrega"**.
* Si el PDF sí contiene la palabra `"Documento."`, se mantiene la cabecera `<h5>Documento: ...</h5>` arriba de las pestañas.


## 8. Enlaces a Syllabus, Rúbrica, AAA e Instrucciones Generales

* Cuando en el HTML se haga referencia al Syllabus, Rúbrica, la AAA o el documento de Instrucciones generales, se deben enlazar localmente en el HTML utilizando el formato portable `@@PLUGINFILE@@/Nombre_Archivo.ext` correspondiente a su archivo de la carpeta `Archivos E`.
* El enlace completo debe ir envuelto en negrita (`<strong><a href="@@PLUGINFILE@@/Nombre_Archivo.ext" target="_blank" rel="noopener">Syllabus</a></strong>`).

---

## 9. Regla de Espaciado Máximo (Saltos de Línea)
* Se permite un **máximo de 2 saltos de línea consecutivos (`<br><br>`)** en cualquier situación dentro del HTML. Queda prohibido el uso de 3 o más etiquetas `<br>` consecutivas o espaciados vacíos excesivos.

---

## 10. Regla de Espaciado Máximo (Caracteres de Espacio y Cierre de Contenido)
* Se permite un **máximo de 2 espacios consecutivos (`  `)** en cualquier parte del texto o contenido dentro del HTML. Queda prohibido el uso de 3 o más caracteres de espacio en secuencia, excepto para la indentación estándar al inicio de las líneas de código.
* La estructura de texto al final del contenido (por ejemplo, antes de cerrar con `</div>` en los contenedores o pestañas) nunca debe llevar saltos de línea (`<br>` ni `<br><br>`) ni espacios vacíos adicionales. El contenido debe cerrarse de forma directa.
* **Detección de Brechas de Espaciado por Cierre Anidado:** Queda prohibido insertar saltos de línea `<br>` o `<br><br>` inmediatamente antes de una etiqueta de cierre de ítem de lista (`</li>`) o de cierre de lista (`</ul>`, `</ol>`). Cuando una lista anidada termina, debe cerrarse directamente sin saltos intermedios. Colocar saltos antes de cerrar la viñeta y otros saltos después de cerrarla acumula de 3 a 4 saltos de línea visuales, lo cual deforma la estructura limpia del documento.
* **Espacios Indeseados por otros Elementos HTML:** Se deben tener muy en cuenta los espacios consecutivos en el renderizado final que pueden producir fragmentos de código o etiquetas inline distintas a `<br>`, `<li>`, `<div>`, `<ol>` (como por ejemplo las etiquetas de enlace `<a>`, `<strong>`, `<span>`, `<td>`, etc.). Se debe vigilar que la separación de etiquetas en el editor de código no introduzca espacios en blanco acumulados en el navegador.
* **Tener en cuenta los espacios que puede producir fragmentos del codigo que no sean Br, li, div, ol, para aplicar la regla de los espacios** (evitando saltos de línea e indentaciones excesivas dentro de etiquetas inline como `<a>`, `<strong>` y `<span>` que el navegador interpreta y renderiza como espacios en blanco visibles consecutivos).



---

## 11. Reglas y Procedimientos del Glosario de Verbos
* **Orden alfabético estricto**: Las tablas del glosario se ordenan alfabéticamente de la A a la Z por su verbo, sin importar la dimensión a la que pertenezcan.
* **Separación de responsabilidades en Moodle**:
  - El campo **Concepto** debe contener únicamente el nombre del verbo en mayúscula inicial (ej. `Adaptar`). No colocar títulos ni dimensiones aquí.
  - El campo **Definición** debe contener el código de la tabla limpia en modo HTML, sin títulos duplicados arriba ni textos planos ajenos.
  - El campo **Categorías** debe asociar el verbo a su dimensión (`SABER`, `SER`, `HACER`).
* **Estructura limpia de la Tabla**:
  - Usar la clase estándar `<table class="table table-striped table-bordered">` sin estilos inline en los `<td>` para que herede las directivas visuales nativas de Moodle.
  - Usar `<th style="text-align:center;">` para el centrado del encabezado.
  - El final de cada tabla debe incorporar exactamente la secuencia `<br>\n<p></p>`.
* **Seguridad en enlaces RAE**: Los hipervínculos al diccionario de la Real Academia Española deben usar los atributos `target="_blank" rel="noreferrer noopener"`.
* **Capitalización de Fuentes en el Glosario**: En el apartado de fuentes (columna FUENTE de la tabla del glosario), se debe aplicar la siguiente regla de mayúsculas y minúsculas:
  - **Estructura con Instituciones**: Solo la primera letra de las palabras principales debe ir en mayúsculas (capitalización de nombres propios), evitando textos completamente en mayúsculas o completamente en minúsculas.
    - *Mal*: `REAL ACADEMIA ESPAÑOLA` o `real academia española`
    - *Bien*: `Real Academia Española`
  - **Estructura con Nombres**: Solo la primera letra de cada nombre y apellido debe ir en mayúscula, evitando textos completamente en mayúsculas o completamente en minúsculas.
    - *Mal*: `OMAR BARBOSA SANTIAGO` o `omar barbosa santiago`
    - *Bien*: `Omar Barbosa Santiago`

---

## 12. Regla de Eliminación de Referencias al "Tablero de Anotaciones"
* **Eliminación Obligatoria**: Queda prohibida la inclusión de las frases "a través del tablero de anotaciones" o "en el tablero de anotaciones" en cualquiera de los textos e instrucciones de los archivos HTML.
* **Sustitución**: Se debe omitir la frase de forma directa para simplificar la redacción. Por ejemplo:
  * *Incorrecto*: `Envíe el documento en formato PDF a través del tablero de anotaciones en las fechas establecidas.`
  * *Correcto*: `Envíe el documento en formato PDF en las fechas establecidas.`

---

## 13. Reglas de la Línea del Tiempo (Timeline)
* **Títulos simplificados**: Los títulos de los avances y enlaces dentro de la línea del tiempo deben utilizar estrictamente la estructura simplificada `"Avance (Número)"`, sin añadir ninguna descripción o subtítulo adicional.
  * *Correcto*: `Avance 1`, `Avance 2`, `Avance 3`, `Avance 4`.
  * *Incorrecto*: `Avance 1. Documento`, `Avance 4. Vídeo creativo`.
* **Regla del último Avance (Producto Final)**: Siempre que se mencione el último avance de la última semana (en este caso "Avance 5" del curso), este pasa a ser `"Producto Final"` de forma global (tanto el texto visible como el atributo `title` de los enlaces).
  - *Correcto*: `Producto Final`
  - *Incorrecto*: `Avance 5. Informe criminológico básico`

---

## 14. Regla de Destino de Enlaces (target="_blank")
* **Apertura en nueva pestaña**: Todos los hipervínculos (`<a>`), ya sean a páginas web externas, enlaces de Moodle (incluidos botones de envío), o archivos físicos/locales (como PDFs o documentos Word), deben abrirse obligatoriamente en una nueva página o pestaña del navegador.
  * **Atributos requeridos**: Deben llevar siempre el atributo `target="_blank"`.
  * **Seguridad (rel)**: Deben incluir el atributo `rel="noopener"` (o `rel="noreferrer noopener"` para enlaces externos que lo requieran como RAE) para evitar riesgos de seguridad.
  * *Excepción única*: Se excluyen únicamente los enlaces de anclaje internos (aquellos cuyo `href` comienza con `#`, por ejemplo: `#formato`, `#tengaencuenta`, etc.).

---

## 15. Verificación de Enlaces Externos Caídos
* **Obligatoriedad de comprobación**: Antes de cargar o dar por finalizado cualquier HTML, se deben verificar todos los enlaces a bibliografías o páginas web externas (eLibro, RAE, Dialnet, etc.) para descartar enlaces caídos o inexistentes.
* **Procedimiento para Enlaces eLibro con Proxy**: Dado que los enlaces de eLibro suelen incluir el prefijo de proxy institucional de la UDES (`ezproxy.udes.edu.co`), para comprobarlos de forma externa se debe remover la porción del dominio del proxy y testear la URL limpia directamente en el navegador o mediante script (ej. convertir `https://elibro-net.ezproxy.udes.edu.co/es/ereader/...` a `https://elibro.net/es/ereader/...`).
* **Ortografía correcta del Proxy eLibro**: Se debe validar que los enlaces utilicen el dominio oficial del proxy con un guion medio: `https://elibro-net.ezproxy.udes.edu.co/`. Si se omite el guion medio (ej. `elibronet`), el enlace fallará en la red institucional para los estudiantes.
* **Acción ante Enlaces Rotos**: Si se detecta un libro o recurso que ha sido retirado de la plataforma eLibro o cuyo enlace está caído:
  - Se debe detener el procesamiento y buscar un reemplazo bibliográfico equivalente y activo, o reportarlo al equipo encargado para recibir una referencia alternativa.

---

## 16. Regla para la Extracción de Créditos Académicos (Introducción al Curso)
* **Fuente de verdad para créditos y horas**: En el apartado de "Detalles del Curso" de la Introducción al Curso (así como en cualquier otro documento donde se listen los créditos o la intensidad horaria), los datos relativos al **número de créditos académicos**, **horas de trabajo con acompañamiento docente** y **total de horas** se deben extraer de forma obligatoria y estricta de la **Rúbrica 1** (`Rúbrica1_Introducción_criminología.pdf`), garantizando así que no haya inconsistencias con la planificación académica del curso.

---

## 17. Regla de Respeto a la Puntuación Original (Puntos Seguidos y Puntos Aparte)
* **Consistencia en Puntuación y Párrafos**: Todos los puntos seguidos y puntos aparte (párrafos y saltos de línea) presentes en los documentos de origen (Words, PDFs, etc.) se deben respetar y trasladar de forma estricta al HTML. Queda prohibido eliminar o alterar estos signos de puntuación, garantizando que el texto mantenga la misma estructura argumentativa del documento fuente.

---

## 18. Regla de Reemplazo de Terminología ("módulo" por "curso")
* **Nomenclatura Unificada**: Siempre que se encuentre la palabra **"módulo"** (o sus variantes: *Módulo*, *módulos*, *Módulos*) en los textos de origen o en las plantillas HTML, se debe cambiar y reemplazar por la palabra **"curso"** (o *cursos*), manteniéndose en **minúscula** (ej. *curso*), a no ser que las reglas ortográficas y de redacción exijan explícitamente el uso de mayúscula inicial (por ejemplo, al inicio de una oración, en un título o como nombre propio).

---

## 19. Regla de Ubicación del Párrafo de Instrucción de Envío
* **Orden de Párrafos Finales**: El párrafo que indica explícitamente la acción de entregar el documento (ej. *"Envíe el documento en formato PDF en las fechas establecidas."*) debe posicionarse obligatoriamente como el **último párrafo** del cuerpo de texto de la pestaña semanal o sección correspondiente, situándose justo encima del botón de entrega o del final del contenedor. Cualquier otro párrafo descriptivo (como el bloque de *"Exposiciones orales"*) debe colocarse antes (arriba) de este.

---

## 20. Regla de Estructura de Entregables (Subtítulo de Entregable)
* **Subtítulo Descriptivo**: Debajo del título principal (`<h3>`) de cada entregable (ya sea Avance o Producto Final), se debe colocar obligatoriamente un subtítulo (`<h5>`) con la descripción del entregable extraída de la tabla de la AAA bajo la columna "Nombre del entregable". Esta descripción debe estructurarse de la forma: `<h5>Tipo de entregable: <span style="">Descripción...</span></h5><br>`.
* **Evitar Duplicados**: Se prohíbe duplicar o mantener este párrafo descriptivo del entregable dentro del cuerpo de la pestaña "Forma de entrega" (como ocurría anteriormente en el Producto Final).

---

## 21. Regla de Rúbricas en Botones de Introducción
* **Rúbrica Oficial a Enlazar:** En la página de `Información del Curso botones.html`, en el botón correspondiente a **Rúbricas**, se debe enlazar siempre y de forma exclusiva la **Rúbrica 1** (`RUBRICA1_NombreCurso.pdf`) del curso, la cual es la rúbrica inicial de proceso.

---

## 22. Regla de Fusión de Filas en Resumen de Entregas
* **Fusión de Semanas y Fechas en Tablas:** En la tabla de Resumen de Entregas (tanto de la Introducción al curso como de los Momentos Evaluativos), queda prohibido repetir de manera separada filas independientes con la misma duración semanal y la misma semana de entrega para el entregable de avance y su cuestionario respectivo. En su lugar, se deben fusionar estas filas en las columnas "Duración Semana" (o "Duración Semanas") y "Semana de Entrega" utilizando el atributo `rowspan="2"` (o el número de filas correspondiente) para agruparlas de manera visual y ordenada.

---

## 23. Regla de Fusión de Semanas en Pestañas de Contenido (Contenido de los Entregables)
* **Pestañas Agrupadas por Rango de Semanas:** En las pestañas de "Contenido de los Entregables" de ambos Momentos Evaluativos, queda prohibido tener pestañas de navegación superior (`nav-tabs`) separadas para cada semana individual si estas corresponden al mismo entregable o avance. En su lugar, se deben fusionar en una única pestaña agrupada que abarque el rango de semanas correspondiente (ej. "Semanas 1 - 3", "Semanas 4 - 5" para el Momento 1; "Semanas 6 - 7", "Semanas 8 - 9", "Semanas 10 - 12" para el Momento 2). Todo el contenido visual e instructivo de esas semanas debe consolidarse en un único panel de contenido (`tab-pane`) correspondiente a la pestaña agrupada.

---

## 24. Regla de Formateo Único de Recursos (Alineamiento con Momento 2)
* **Eliminación de Redundancias:** Todos los recursos bibliográficos y de ampliación temática deben ser listados una única vez en el lugar donde son presentados (debajo del párrafo de la actividad correspondiente). Queda estrictamente prohibido duplicar los recursos bibliográficos al final de las pestañas semanales (como una lista redundante general).
* **Formateo al Primer Uso:** Siempre que se haga referencia a recursos en el texto (ej. "Para el desarrollo de la actividad puede consultar los recursos:"), se debe colocar inmediatamente la estructura correcta del recurso. Se usarán viñetas (`<ul>` y `<li>`) únicamente si el recurso mencionado tiene un link en el word (con la cita completa y link visible en negrita). Los recursos (RED) se dejan igual en negrita y con el @@plugin si corresponde.
* **No Duplicidad:** Si un recurso ya fue listado en su respectiva actividad al primer uso, no se debe volver a incluir en ninguna otra lista general o posterior de esa semana.

---

## 25. Regla de Separación de Listas de Texto (Cuestionarios y Ejercicios)
* **Doble Salto de Línea en Listas de Texto:** Siempre que se presente una lista basada en texto plano en la cual los elementos estén numerados (por ejemplo: `1)`, `2)`, `3)...` o `1.`, `2.`, `3....`), se debe asegurar que cada elemento se separe del siguiente utilizando exactamente un doble salto de línea (`<br><br>`), de manera que visualmente quede una línea en blanco de separación y no queden agrupados consecutivamente sin espacio vertical.
* **Control de Límites de Saltos:** Al aplicar esta separación, se debe respetar rigurosamente la regla de no superar el límite de 2 saltos de línea consecutivos (`<br><br>`) en total, y no dejar saltos de línea vacíos al final de los contenedores o de las etiquetas de cierre.

---

## 26. Prevención de Emoticonos Automáticos en Moodle
* **Bypass de Filtro de Emoticonos:** Moodle cuenta con filtros automáticos que convierten combinaciones de caracteres como `(y)` o `(x)` en emoticonos (por ejemplo, `(y)` se convierte en el emoji de pulgar arriba 👍). Para evitar esta conversión automática sin alterar visualmente el texto del curso, se debe envolver el carácter interior en una etiqueta `<span>` (ej. `(<span>y</span>)` o `(<span>x</span>)`), lo cual rompe la expresión regular del filtro de emoticonos de Moodle mientras se renderiza correctamente para el usuario final.

---

## 27. Consistencia en Marcadores de Listas de Texto (Negritas)
* **Ubicación del Marcador:** Cuando se tengan listas de texto plano marcadas con letras o números (por ejemplo: `a.`, `b.`, `c.` o `1.`, `2.`, `3.`) y los títulos de los elementos lleven negrita (`<strong>`), el marcador (la letra o número) debe ir de manera consistente **dentro** del tag de negrita para todos los elementos (ej. `<strong>a. Título.</strong>`). Se prohíbe mezclar formatos donde algunos marcadores queden fuera y otros dentro del tag `<strong>`.

---

## 28. Regla de Espaciado de Botones de Envío
* **Separación de Botones:** Todos los botones de envío (tanto los de las pestañas semanales como los de la pestaña "Instrumento para Enviar Entregable") deben ir colocados exactamente un renglón después del último párrafo o elemento que los antecede.
* **Prohibición de Elementos Intermedios:** Queda estrictamente prohibido usar saltos de línea (`<br>` o `<br><br>`) o párrafos vacíos redundantes en medio. La separación debe lograrse a través del margen inferior nativo del elemento anterior.
* **Separador de Botones Múltiples:** Únicamente se permite usar un párrafo vacío (`<p></p>`) entre botones de envío consecutivos en la pestaña de envíos múltiples para asegurar su separación visual sin acumular espacios en blanco innecesarios.