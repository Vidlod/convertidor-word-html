# Guía de Procesamiento de Documentos para IA (DOCX-Pandoc y PDF-PyMuPDF4LLM)

Esta guía documenta el funcionamiento, configuración y uso del nuevo motor de procesamiento de archivos del proyecto, diseñado para extraer de manera literal e íntegra el contenido y estructura de archivos Word (`.docx`) y PDF (`.pdf`), previniendo alucinaciones y parafraseos por parte de los agentes de IA.

---

## 1. Arquitectura y Tecnologías
Para garantizar que la estructura del documento original (viñetas, párrafos, tablas y saltos) se conserve exactamente igual, se implementan dos motores deterministas:

*   **PDF ➡️ Markdown:** Utiliza **`pymupdf4llm`**, que agrupa las líneas de texto según su cercanía visual en el PDF en lugar de extraer caracteres sueltos en vertical. Las tablas se extraen directamente en formato de tablas de Markdown (`| columna |`).
*   **DOCX ➡️ Markdown:** Utiliza **`pypandoc`** (Pandoc), un compilador de documentos clásico y robusto que mapea la estructura interna del archivo XML de Word a formato Markdown sin alterar el texto.
*   **DOCX ➡️ HTML (Clásico):** Se conserva **`mammoth`** para la previsualización y conversión tradicional a HTML5 estructurado.

---

## 2. Instalación y Requisitos

### Dependencias de Python
Las dependencias se encuentran especificadas en el archivo `requirements.txt`. Para instalarlas en el entorno virtual local, ejecuta:
```bash
./venv/bin/pip install -r requirements.txt
```

### Binario de Pandoc (macOS Intel)
El paquete `pypandoc` cuenta con un sistema de auto-detección y descarga. Al iniciar la aplicación web o el script por primera vez, intentará descargar automáticamente la versión de Pandoc compatible con el sistema:
*   En equipos **macOS Intel CPU (x86_64)**, descargará el paquete nativo para arquitectura Intel (`pandoc-[version]-macOS.pkg`) y lo instalará de forma aislada en la carpeta del usuario:
    `~/Library/Application Support/pypandoc/pandoc`
*   Si la red o los permisos bloquearan esta descarga, puedes instalar Pandoc manualmente mediante el paquete oficial de macOS Intel descargándolo directamente de las [releases de GitHub de Pandoc](https://github.com/jgm/pandoc/releases).

---

## 3. Uso mediante Consola (CLI)
El script `convert.py` ha sido actualizado para procesar de forma automática y versátil tus archivos:

### Conversión Automática
Si no especificas ningún archivo, el convertidor buscará el primer `.docx` o `.pdf` que encuentre en la raíz o en los directorios de insumos del proyecto (`PLANTILLA_CURSO/1_insumos_origen/`):
```bash
./venv/bin/python3 convert.py
```

### Conversión de un Archivo Específico
Puedes pasarle la ruta de cualquier archivo Word o PDF como argumento:
```bash
./venv/bin/python3 convert.py ruta/a/mi_guia.pdf
./venv/bin/python3 convert.py ruta/a/mi_avance.docx
```

### Resultados Generados:
*   **Si procesa un PDF:** Generará un archivo `.md` (Markdown) con el mismo nombre en el mismo directorio.
*   **Si procesa un DOCX:** Generará **ambos**: un archivo `index.html` (vía Mammoth) y un archivo `.md` (vía Pandoc).

---

## 4. Uso de la Aplicación Web Interactiva
El backend `app.py` y el frontend `templates/index.html` admiten ahora el flujo completo para ambos tipos de archivos:

1.  **Iniciar Servidor:**
    ```bash
    ./venv/bin/python3 app.py
    ```
2.  **Acceder a la Interfaz:** Visita [http://localhost:5000](http://localhost:5000) en tu navegador.
3.  **Carga del Archivo:** Arrastra y suelta un archivo `.docx` o `.pdf` en la zona punteada.
4.  **Selección de Motor (Solo para DOCX):**
    *   **Mammoth (HTML):** Genera código HTML directo, ideal para tablas de una celda / recuadros de Moodle.
    *   **Pandoc (Markdown):** Genera Markdown estructurado para que la IA lo interprete de forma óptima.
    *(Al cargar un PDF, se activa por defecto el motor PyMuPDF4LLM).*
5.  **Toma por Bloques:** El panel izquierdo mostrará las tarjetas segmentadas del documento. Puedes activar o desactivar las casillas para generar dinámicamente tu resultado combinado.
6.  **Pestañas de Resultado (Markdown / HTML / Previsualización):**
    *   Copia o descarga el Markdown crudo desde la nueva pestaña **Código Markdown**.
    *   Copia o descarga el código HTML equivalente desde la pestaña **Código HTML**.

---

## 5. Directrices Críticas para Agentes y Modelos de IA
Esta sección contiene instrucciones específicas sobre **cómo debe actuar un agente de IA** al recibir un archivo Markdown extraído con estos métodos para transformarlo al HTML de Moodle (GEO/UDES):

### 🚫 REGLA DE ORO: Copia Literal Completa
*   **Prohibición de parafraseo:** Queda terminantemente prohibido reescribir, abreviar, resumir, corregir la ortografía (salvo acentos rotos obvios) o simplificar el texto original del Markdown.
*   **Estructura literal:** Cada punto seguido, punto aparte y salto de párrafo del archivo Markdown debe mapearse exactamente a su equivalente en HTML (ej. envolviendo cada párrafo en su respectivo `<p>...</p>` o viñeta `<li>...</li>`).

### 📋 Mapeo de Viñetas e Ítems de Listas
*   Las líneas que inicien con `-`, `*` o `1.` en el Markdown representan elementos de lista.
*   Deben traducirse a etiquetas `<ul><li>...</li></ul>` o `<ol><li>...</li></ol>`.
*   **Regla de puntuación de listas (Linter `verify.py`):** Asegúrate de que el texto dentro del `<li>` termine en un punto final (`.`), signo de interrogación (`?`) o dos puntos (`:`), a menos que sea un elemento de navegación o menú de pestañas.

### 📊 Conservación y Mapeo de Tablas
*   Las tablas representadas en Markdown con barras verticales (`|`) deben conservarse tal cual, transformándolas a etiquetas `<table>`, `<tr>`, `<td>` de HTML. No omitas filas ni cambies el texto de los encabezados.

### 🔍 Proceso de Validación
Después de que la IA genere o edite una página HTML basada en el Markdown:
1.  **Ejecutar el validador local:**
    ```bash
    python verify.py
    ```
2.  **Corrección inmediata:** El validador (`verify.py`) analiza que se cumplan las reglas estructurales (sin cursivas `<em>`, enlaces con `target="_blank"` y `rel="noopener"`, sin saltos `<br>` duplicados, etc.). Si reporta fallos, deben corregirse antes de dar la tarea por finalizada.
