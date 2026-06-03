import os
import pypdf
import mammoth

def extract_docx(docx_path):
    print(f"\n=== EXTRACTING DOCX: {docx_path} ===")
    with open(docx_path, "rb") as f:
        result = mammoth.convert_to_html(f)
        html = result.value
        # Write to a text file in scratch
        out_path = docx_path.replace(".docx", "_extracted.html")
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(html)
        print(f"Extracted HTML written to: {out_path}")
        # Print first 1000 characters of clean text
        text = result.value[:1000]
        print("First 1000 chars of HTML:")
        print(text)

def extract_pdf(pdf_path):
    print(f"\n=== EXTRACTING PDF: {pdf_path} ===")
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        text += f"\n--- PAGE {i+1} ---\n{page_text}"
    
    out_path = pdf_path.replace(".pdf", "_extracted.txt")
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(text)
    print(f"Extracted text written to: {out_path}")
    print("First 1000 chars of text:")
    print(text[:1000])

if __name__ == "__main__":
    base_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen"
    docx_path = os.path.join(base_dir, "documentos_word/AAA-pregrado.docx")
    syllabus_path = os.path.join(base_dir, "guias_pdf/SYLLABUS_Estadística_Descriptiva.pdf")
    rubrica_path = os.path.join(base_dir, "guias_pdf/RUBRICA1_Estadística_Descriptiva.pdf")
    
    extract_docx(docx_path)
    extract_pdf(syllabus_path)
    extract_pdf(rubrica_path)
