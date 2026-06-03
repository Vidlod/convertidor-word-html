# Herramientas de Automatización del Curso

Este directorio contiene scripts desarrollados para optimizar el procesamiento y enlistamiento en Moodle.

## 🚀 1. Generador de Glosario XML (`generar_glosario_xml.py`)
Lee el archivo de Rúbricas en Excel, formatea cada verbo en tablas HTML y crea un único archivo XML.

### Uso:
```bash
python3 generar_glosario_xml.py ../../1_insumos_origen/glosario_excel/Rubrica.xlsx
```
* **Salida**: Genera `glosario_importar.xml` en la carpeta `3_paginas_finales/`.
* **Cómo usarlo en Moodle**: Ve a la actividad Glosario, haz clic en **Importar entradas** (en la rueda dentada/administración) y sube este archivo XML. Todos tus conceptos se cargarán en 5 segundos.

---

## 🧹 2. Limpiador y Portable de HTML (`preprocesar.py`)
Busca y limpia errores comunes de maquetación en todos tus archivos HTML:
- Quita el texto del tablero de anotaciones.
- Elimina los `<br>` y espacios no válidos al final de los contenedores (Regla 10).
- Normaliza las rutas físicas al formato portable `@@PLUGINFILE@@/`.
- Desvincula enlaces a SharePoint, OneDrive o Google Drive, convirtiéndolos en negrita simple.

### Uso:
```bash
# Procesar todos los archivos HTML de paginas_finales/
python3 preprocesar.py

# Procesar un archivo individual
python3 preprocesar.py ../../3_paginas_finales/Momentos/Momento_Evaluativo1.html
```
