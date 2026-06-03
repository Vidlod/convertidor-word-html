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
* **Sin Negrita (Strong) y con Link Visible:** La cita bibliográfica no debe ir en negrita (`<strong>` ni `<b>`). Tampoco debe ir el enlace incrustado directamente en el texto de la cita. En su lugar, el texto de la cita va como texto plano normal, seguido de un salto de línea (`<br>`) y el enlace explícito visible como hipervínculo.
  * Formato: `Autor (Año). Título del libro...<br><a href="ENLACE_ELIBRO" target="_blank" rel="noopener">ENLACE_ELIBRO</a>`
* **Limpieza de textos adicionales:** La cita bibliográfica debe ir completamente sola en su viñeta. Se deben remover textos descriptivos que queden pegados como `"Lectura requerida."` o `"Lectura de ampliación temática."`.
* **Separación:** Las citas bibliográficas siempre deben ir separadas por viñetas (`<li>`).

---

## 3. Recursos Educativos Digitales (RED)
* **Preguntar por Enlaces:** Siempre que se haga referencia a un RED en el HTML, se debe preguntar al usuario por el enlace correspondiente.
* **Formato con Enlace:** Si el usuario proporciona el enlace, el título del RED debe ir en negrilla y enlazarse:
  * Formato: `<strong><a href="ENLACE_ONEDRIVE" target="_blank" rel="noopener">Título del RED</a></strong>`
* **Formato sin Enlace:** Si el enlace no está disponible ("no lo tengo"), el título del RED debe formatearse únicamente en negrilla normal:
  * Formato: `<strong>Título del RED</strong>`
* **Separación:** Cada RED siempre debe listarse en una viñeta independiente. En caso de recursos compuestos (ej. Parte I y Parte II), se deben separar en dos viñetas independientes con sus respectivos hipervínculos individuales.

---

## 4. Estructura, Viñetas y Espaciado
* **Espaciado entre ítems (margin-bottom):** 
  * Si en un grupo de viñetas (`<ul>` o `<ol>`), al menos **una viñeta tiene más de 3 renglones**, o bien **dos viñetas tienen 2 renglones**, se debe aplicar un espacio de separación entre cada ítem.
  * Implementación: Añadir `style="margin-bottom: 10px;"` a cada etiqueta `<li>` de ese grupo de viñetas.
  * Si los ítems tienen un solo renglón, se dejan pegados (sin margen).
* **Separación de bloques (doble salto de línea):**
  * Ningún grupo de viñetas (`<ul>` o `<ol>`) puede quedar pegado a un párrafo adyacente (al principio o al final) que no pertenezca a las viñetas.
  * Se deben insertar etiquetas de salto de línea dobles (`<br><br>`) justo antes de abrir la lista y justo después de cerrarla.

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
                <span class="spinner-grow spinner-grow-sm"></span> Enviar Producto Final.
            </button>
        </a>
    </div>
    ```
* **En la pestaña "Instrumento para Enviar Entregable" (Pestaña 4):**
  * Debe contener exactamente la cantidad de botones necesarios que representen el número de avances del momento correspondiente (especificado en el Word).
  * Ejemplo: Momentos con 3 avances deben tener exactamente 3 botones (Avance 3, Avance 4 y Producto Final).
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
  1. **Escribir en local usando el marcador:** Escribe todas las URLs en el HTML usando la estructura `href="@@PLUGINFILE@@/Nombre_Exacto_del_Archivo.ext"`.
  2. **Copiar y pegar el HTML:** Pega todo el código HTML en la vista de código fuente (`<>`) de Moodle.
  3. **Carga masiva de ficheros:** Haz clic en el icono **"Gestionar ficheros incrustados"** (el 6.º botón de la segunda fila en la barra de herramientas del editor, con forma de hoja de papel). En la ventana emergente que se abre, arrastra y suelta **todos los archivos del computador de una sola vez**.
  4. **Guardar:** Cierra la ventana emergente y guarda los cambios en Moodle. La plataforma enlazará todo automáticamente.





## 7. Anexos 
* Si se detecta que dentro del archivo suministrado que se hace referencia a algún anexo, me dices para darte el url y tú lo pones en negrilla y que al darle click al nombre del anexo lo lleve al enlace.

---

## 8. Regla del apartado "Documento"
* Si en el PDF suministrado el párrafo inicial del entregable no está precedido por la palabra `"Documento."` o `"Documento:"` de manera explícita en su estructura original:
  - No se coloca el apartado de cabecera `<h5>Documento: ...</h5>` en el HTML.
  - En su lugar, se toma ese primer párrafo del PDF y se inserta como el primer párrafo dentro de la pestaña **"Forma de entrega"**.
* Si el PDF sí contiene la palabra `"Documento."`, se mantiene la cabecera `<h5>Documento: ...</h5>` arriba de las pestañas.


## 8. REP 2

Si se encuentran alguna parte del html que hagan referecia a Syllabus, Rúbrica, la AAA y el documento de Instruciones generales, debes decime para darte el url y tú lo pones en negrilla y que al darle click al nombre del anexo lo lleve al enlace.
tenemos que localizar estos fracmentos ponerlos en negriña y cuando de click en la palabra me lleve al enlace que te suministre

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

## 13. Regla de Estructura de Entregables (Subtítulo de Entregable)
* **Subtítulo Descriptivo**: Debajo del título principal (`<h3>`) de cada entregable (ya sea Avance o Producto Final), se debe colocar obligatoriamente un subtítulo (`<h5>`) con la descripción del entregable extraída de la tabla de la AAA bajo la columna "Nombre del entregable". Esta descripción debe estructurarse de la forma: `<h5>Tipo de entregable: <span style="">Descripción...</span></h5><br>`.
* **Evitar Duplicados**: Se prohíbe duplicar o mantener este párrafo descriptivo del entregable dentro del cuerpo de la pestaña "Forma de entrega" (como ocurría anteriormente en el Producto Final).

---

## 14. Regla de Rúbricas en Botones de Introducción
* **Rúbrica Oficial a Enlazar:** En la página de `Información del Curso botones.html`, en el botón correspondiente a **Rúbricas**, se debe enlazar siempre y de forma exclusiva la **Rúbrica 1** (`RUBRICA1_NombreCurso.pdf`) del curso, la cual es la rúbrica inicial de proceso.