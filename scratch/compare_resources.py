import re

def extract_urls(file_path):
    urls = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex to find URLs
    url_pattern = re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')
    matches = url_pattern.findall(content)
    return set(matches)

def extract_citations(text_path):
    citations = []
    with open(text_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find lines that look like citations, e.g., containing author and year
    # e.g., Posada, G. (2016) or Martínez, C. (2013)
    citation_pattern = re.compile(r'\b[A-Za-z]+,\s*[A-Z]\.\s*(?:\s*[A-Z]\.)?\s*\(\d{4}\)')
    for line in lines:
        line = line.strip()
        if citation_pattern.search(line):
            citations.append(line)
    return set(citations)

if __name__ == '__main__':
    syllabus_path = "PLANTILLA_CURSO/1_insumos_origen/guias_pdf/SYLLABUS_Estadística_Descriptiva_extracted.txt"
    aaa_path = "scratch/AAA-pregrado_text.txt"
    
    syll_urls = extract_urls(syllabus_path)
    aaa_urls = extract_urls(aaa_path)
    
    print("=== URLS IN SYLLABUS BUT NOT IN AAA ===")
    for url in sorted(syll_urls - aaa_urls):
        print("-", url)
        
    print("\n=== URLS IN AAA BUT NOT IN SYLLABUS ===")
    for url in sorted(aaa_urls - syll_urls):
        print("-", url)
        
    syll_citations = extract_citations(syllabus_path)
    aaa_citations = extract_citations(aaa_path)
    
    print("\n=== CITATIONS IN SYLLABUS BUT NOT IN AAA ===")
    for cit in sorted(syll_citations - aaa_citations):
        print("-", cit)
        
    print("\n=== CITATIONS IN AAA BUT NOT IN SYLLABUS ===")
    for cit in sorted(aaa_citations - syll_citations):
        print("-", cit)
