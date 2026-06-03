# Guía de Carga y Procesamiento de Cursos en la Plataforma Educativa

## Objetivo de la Guía
1. **Entender en orden los procesos** para enlistar/cargar cursos en la plataforma educativa Moodle.
2. **Agilizar el procesamiento** de forma precisa y estricta, siguiendo el estándar de maquetación HTML y las reglas de consistencia de contenido (sin inventar datos ni estructuras).

---

## 🛠️ Procesos Generales de Procesamiento y Maquetación

Antes de iniciar la carga en la plataforma, cada archivo HTML de las páginas finales (`paginas_finales/`) debe ser procesado de acuerdo con las siguientes directrices técnicas para asegurar la portabilidad y evitar errores visuales o lógicos en Moodle:

### 1. Revisión de Enlaces a Recursos Estáticos
* **Acción**: Reemplazar todos los enlaces (`<a>`) que dirigen a URLs externas de OneDrive/SharePoint o servidores temporales de `pluginfile.php` para documentos de lectura o plantillas (PDF, Word, Excel, etc.) por el formato portable `@@PLUGINFILE@@/Nombre_Exacto_Archivo.ext`.
* **Formato**: Todo enlace a un recurso estático (Syllabus, Rúbrica, anexos, guías) debe estar en negrita y abrir en pestaña nueva (`target="_blank" rel="noopener"`): `<strong><a href="@@PLUGINFILE@@/Nombre_Archivo.ext" target="_blank" rel="noopener">Nombre del Recurso</a></strong>`.
* **Excepción**: Los enlaces a actividades internas de la plataforma, como los botones de entrega (`mod/assign`) o el glosario del curso (`mod/glossary`), deben permanecer activos, funcionales y abrirse en nueva pestaña.

### 2. Eliminación de Referencias al "Tablero de Anotaciones"
* **Acción**: En las instrucciones de entrega y textos explicativos (ej. *"Envíe el documento... a través del tablero de anotaciones"*), se elimina por completo la mención *"a través del tablero de anotaciones"* o *"en el tablero de anotaciones"*.
* **Ejemplo de Corrección**:
  - *Antes*: `Envíe el documento en formato PDF a través del tablero de anotaciones en las fechas establecidas en el tablero de anotaciones.`
  - *Después*: `Envíe el documento en formato PDF en las fechas establecidas.`

### 3. Apertura de Enlaces en Nueva Pestaña
* **Acción**: Todo enlace HTML a páginas o recursos externos que deba abrirse en el navegador (como referencias a bibliotecas virtuales, el DLE de la RAE, eLibro, etc.) debe configurarse obligatoriamente para abrirse en una pestaña independiente.
* **Sintaxis**: Incluir los atributos `target="_blank" rel="noopener noreferrer"` en la etiqueta de anclaje:
  `Texto de la Cita<br><a href="URL" target="_blank" rel="noopener noreferrer">URL</a>`

### 3.1. Verificación de Enlaces Caídos
* **Acción**: Comprobar que los enlaces a bibliografías externas (eLibro, Dialnet, etc.) estén activos y funcionales antes de finalizar la maquetación.
* **Método de Prueba**: Para probar los enlaces con proxy institucional (`ezproxy.udes.edu.co`) sin estar logueado, se debe remover la porción de proxy del dominio de la URL de prueba para verificar si el recurso aún existe en el catálogo público de eLibro (ej. convertir `elibro-net.ezproxy.udes.edu.co` a `elibro.net`).
* **Estructura del Proxy eLibro**: El dominio oficial del proxy para eLibro de la UDES debe contener un guion medio: `elibro-net.ezproxy.udes.edu.co`. Si se escribe como `elibronet` (sin guion), el enlace fallará en la red institucional.
* **Resolución**: Si un enlace está definitivamente caído o el recurso ya no está disponible, se debe buscar un reemplazo fiable con el mismo título o temática y actualizarlo en el código HTML.

### 4. Directrices de Espaciado y Control de Saltos de Línea (Reglas 9 y 10)
* **Saltos de Línea Máximos**: Se permite un **máximo de 2 saltos de línea consecutivos (`<br><br>`)** en cualquier parte del documento. Nunca usar 3 o más.
* **Espacios Consecutivos**: Se prohíbe el uso de 3 o más espacios de caracteres consecutivos (`   `) dentro del cuerpo de texto (excepto por la indentación de código al inicio de las líneas).
* **Espaciado en Cierres Anidados**: Queda estrictamente prohibido insertar saltos de línea (`<br>`) inmediatamente antes de una etiqueta de cierre de ítem de lista (`</li>`) o cierre de lista (`</ul>`, `</ol>`). La lista debe cerrarse directamente para evitar brechas de espaciado excesivas acumuladas.
* **Cierre de Contenedor**: La estructura de texto al final del contenido (por ejemplo, antes de cerrar con `</div>` en los contenedores o pestañas) nunca debe llevar saltos de línea (`<br>` ni `<br><br>`) ni espacios vacíos adicionales. El contenido debe cerrarse de forma directa.

### 5. Carga de Archivos Portable y Agilizada (@@PLUGINFILE@@)
* **El Método**: Se utiliza el marcador `href="@@PLUGINFILE@@/Nombre_Exacto_del_Archivo.ext"` o `src="@@PLUGINFILE@@/Nombre_Exacto_del_Archivo.ext"` en el HTML.
* **Proceso**: 
  1. Escribir las rutas con el marcador en el HTML (incluyendo enlaces a PDFs, Word y rutas de reproductores `<audio>` de los podcasts).
  2. Pegar el código HTML en el editor de Moodle (`<>`).
  3. Hacer clic en el icono **"Gestionar ficheros incrustados"** (el botón de la hoja de papel doblada en la segunda fila de herramientas) y arrastrar todos los archivos locales en bloque (PDFs, Word y los audios `.mp3` de los podcasts. **Importante:** No use el micrófono del editor para intentar subir el archivo, ya que este último es para grabaciones locales en vivo).
  4. Guardar los cambios. Moodle traduce automáticamente el marcador portable a la URL definitiva de descarga del servidor (`/pluginfile.php/...`).


---

## 🗂️ Estructura de Carga por Grupos y Secciones

A continuación, se detalla el orden del flujo de trabajo y la configuración correspondiente para cada sección del curso en Moodle, estructurada por grupos:

### 📍 GRUPO 1: Sala de Encuentro Sincrónico / Secciones Principales
Esta sección representa la interfaz de navegación modular del curso mediante pestañas semanales y bloques iniciales.

1. **Recursos Generales**
   * *Descripción/Proceso*: Corresponde a la sección o pestaña inicial de inducción al módulo donde se colocan los recursos de soporte general del curso.
   * *Estado*: No hay información específica sobre configuraciones de salas de videoconferencias o enlaces sincrónicos en los insumos actuales.
2. **Información del Curso**
   * *Descripción/Proceso*: Se despliega mediante la estructura de `Introduccion al curso.html`. Ofrece una bienvenida y contextualización inicial.
   * *Enlaces*: Los recursos descargables generales (Instrucciones Generales, Syllabus y Rúbrica) deben estar enlazados utilizando el formato portable `@@PLUGINFILE@@/` con el nombre exacto de archivo en `Archivos E`, abriendo en pestaña nueva (`target="_blank" rel="noopener"`). El Glosario se mantiene enlazado a la herramienta de Moodle (`mod/glossary`). la informacion para llenar este apartado se obtiene de los archivos Rubrica para los creditos horas etc y del sylabus.docx para el resto de informacion
3. **Línea de Tiempo**
   * *Descripción/Proceso*: Recurso interactivo que organiza las semanas y entregables del curso.
   * *Enlaces*: Al dar clic sobre los títulos correspondientes a los avances (ej. "Avance 1", "Avance 2"), el usuario debe ser redirigido directamente a la respectiva pestaña o sección del entregable.
   * *Corrección*: Se debe eliminar la sección "CIERRE DE CURSO" del archivo HTML original de la línea de tiempo, ya que no corresponde al programa formativo.
4. **Momento Evaluativo I**
   * *Descripción/Proceso*: Bloque modular de aprendizaje I (abarca de la Semana 1 a la Semana 6).
   * *Maquetación*: Contiene pestañas para cada semana.
   * *Videos*: Se incrustan los videos correspondientes de YouTube usando la estructura de caja responsiva autocentrada (`max-width: 360px` y relación `56.25%`). Los videos incrustados son:
     - *Semana 2*: "Diapositivas en vídeo: objeto de la criminología", "Vídeo clase: métodos y técnicas de investigación en la criminología", y "Diapositivas en vídeo: escuelas de la criminología".
     - *Semana 4*: "Video corto: factores criminológicos".
   * *Botones*: Se agrega un botón de envío centrado al final de la última semana de este avance (Semana 3 para Avance 1) enlazado a la tarea de Moodle.
5. **Momento Evaluativo II**
   * *Descripción/Proceso*: Bloque modular de aprendizaje II (abarca de la Semana 7 a la Semana 14).
   * *Videos*: Se incrustan los videos responsivos de YouTube:
     - *Semana 7*: "Video con diapositivas: tipos de conductas y trastornos de personalidad".
     - *Semana 9*: "Vídeo clase: criminología y nuevas relaciones sociales: hacia una perspectiva digital y contextual".
   * *Botones*: Se configuran los botones de envío en la última semana de cada avance (Semana 8 para Avance 3, Semana 10 para Avance 4 y Semana 14 para Avance 5 / Producto Final). En la pestaña "Instrumento para Enviar Entregable", se muestran y configuran exactamente los botones correspondientes al número de avances del momento formativo.

---

### 📍 GRUPO 2: Rúbricas
1. **Rúbricas (Archivos PDF)**
   * *Descripción/Proceso*: La cantidad de rúbricas depende de las rúbricas evaluativas suministradas en los insumos.
   * *Carga y Orden*: Su asignación y orden se define según las guías AAA y el syllabus. Para este curso se procesan dos rúbricas principales:
     1. *Rúbrica Evaluativa de Avance 1 y 2* (Asociada al Momento I).
     2. *Rúbrica Evaluativa de Avance 3, 4 y 5* (Asociada al Momento II).
   * *Maquetación*: Los enlaces a estos PDFs se deben enlazar localmente en el HTML utilizando el formato portable `@@PLUGINFILE@@/Nombre_Archivo.ext` (con el nombre exacto de la carpeta `Archivos E`), siempre en negrita y abriendo en pestaña nueva (`target="_blank" rel="noopener"`).

---

### 📍 GRUPO 3: Entregables
Esta sección contiene la descripción y directrices de cada entrega que realiza el estudiante.

* **Reglas Específicas**:
  - Se remueve la frase "a través del tablero de anotaciones".
  - El documento AAA (Actividad de Aprendizaje Alternativa) no se enlaza en el HTML (se deja en negrita simple `<strong>AAA</strong>`).
  - Todos los enlaces a sitios externos deben configurarse para abrir en nueva pestaña (`target="_blank"`).
1. **Entregables**
   * *Descripción/Proceso*: La cantidad total de entregables está dictada por las especificaciones de las guías de actividades del curso (para este caso, 5 entregables en total).
   * *Último Entregable / Avance*: En el último momento evaluativo (Momento II), solo se cambia el nombre del avance en la última semana (Semana 14) a **Producto Final**. En las semanas previas (Semanas 11, 12 y 13) y demás referencias generales, se mantiene la denominación de **Avance 5**.
   * *Estructura HTML*: Se alojan en archivos individuales bajo una interfaz de dos pestañas: **Forma de entrega** (corregido del término "Formato de entrega") y **Tenga en cuenta**. No deben contener enlaces directos a OneDrive o SharePoint; los nombres de los formatos/anexos deben enlazarse localmente en el HTML mediante el formato portable `@@PLUGINFILE@@/Nombre_Archivo.ext` (con el nombre exacto de la carpeta `Archivos E`), siempre en negrita y abriendo en pestaña nueva.

---

### 📍 GRUPO 4: Repositorio
Esta sección agrupa los documentos y recursos troncales de apoyo y referencia para el curso.

1. **Mapa del Curso**
   * *Descripción/Proceso*: Corresponde al mapa conceptual de introducción al curso. Se enlaza o carga en formato PDF.
2. **Instrucciones Generales**
   * *Descripción/Proceso*: PDF que detalla las pautas iniciales del curso. Su contenido y archivo específico dependen del curso respectivo que se esté configurando.
3. **Syllabus**
   * *Descripción/Proceso*: Corresponde siempre al Syllabus de introducción del curso actual.
4. **Glosario**
   * *Descripción/Proceso*: Se construye con base en el archivo de rúbrica de Excel, extrayendo las definiciones oficiales del diccionario de la RAE de los verbos y dimensiones indicadas.
   * *Formateo e Importación*:
     - Cada verbo se genera como una tabla HTML sin estilos inline: `<table class="table table-striped table-bordered">`.
     - Se eliminan títulos duplicados internos en el HTML, ya que Moodle los genera de forma automatizada al crear el concepto.
     - Cada tabla debe concluir obligatoriamente con el bloque `<br>\n<p></p>`.
     - En Moodle, se introduce el verbo con mayúscula inicial en el campo "Concepto", el código limpio de la tabla en la pestaña HTML de "Definición", y se asocia la categoría correspondiente (`SER`, `SABER` o `HACER`).
     - **Regla de Capitalización en Fuentes**: En la columna FUENTE, no se deben usar mayúsculas sostenidas ni minúsculas sostenidas.
       - *Instituciones*: Solo la primera letra debe ir en mayúsculas (ej. *Bien*: `Real Academia Española` / *Mal*: `REAL ACADEMIA ESPAÑOLA`, `real academia española`).
       - *Nombres*: Solo la primera letra de nombres y apellidos en mayúscula (ej. *Bien*: `Omar Barbosa Santiago` / *Mal*: `OMAR BARBOSA SANTIAGO`, `omar barbosa santiago`).
