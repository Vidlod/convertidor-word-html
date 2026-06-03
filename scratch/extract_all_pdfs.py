import os
import pypdf

def extract_pdf(pdf_path):
    print(f"Extracting PDF: {pdf_path}")
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        text += f"\n--- PAGE {i+1} ---\n{page_text}"
    
    out_path = pdf_path.replace(".pdf", "_extracted.txt")
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(text)
    print(f"Extracted text written to: {out_path}")

if __name__ == "__main__":
    base_dir = "/Users/buc-cvudes-medios1/Documents/GEO/PLANTILLA_CURSO/1_insumos_origen/guias_pdf"
    for filename in os.listdir(base_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(base_dir, filename)
            extract_pdf(pdf_path)
