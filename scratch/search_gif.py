import os
import zipfile
import re

def clean_xml_tags(xml_content):
    text = re.sub(r'<[^>]+>', '', xml_content)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def search_word_files(dir_path):
    print(f"Scanning directory: {dir_path}")
    scanned_files = []
    results = []
    
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_lower = file.lower()
            if (file_lower.endswith('.docx') or file_lower.endswith('.doc') or file_lower.endswith('.docm')) and not file.startswith('~$'):
                file_path = os.path.join(root, file)
                scanned_files.append(file_path)
                
                # If it's docx or docm, we can open it as zip
                if file_lower.endswith('.docx') or file_lower.endswith('.docm'):
                    try:
                        with zipfile.ZipFile(file_path, 'r') as zip_ref:
                            xml_files = [name for name in zip_ref.namelist() if name.endswith('.xml')]
                            for xml_file in xml_files:
                                content = zip_ref.read(xml_file).decode('utf-8', errors='ignore')
                                # Case-insensitive search for 'gif' with word boundary or specific term
                                # Let's search for case-insensitive 'gif'
                                matches = list(re.finditer(r'\bgif\b', content, re.IGNORECASE))
                                # Also check if it's part of a string like "gif" (without word boundary) but exclude base64 junk
                                if not matches:
                                    matches = list(re.finditer(r'gif', content, re.IGNORECASE))
                                
                                if matches:
                                    plain_text = clean_xml_tags(content)
                                    text_matches = list(re.finditer(r'gif', plain_text, re.IGNORECASE))
                                    contexts = []
                                    for m in text_matches:
                                        start = max(0, m.start() - 50)
                                        end = min(len(plain_text), m.end() + 50)
                                        contexts.append(plain_text[start:end].strip())
                                    
                                    # Filter contexts to make sure they are readable text (not base64 strings)
                                    readable_contexts = []
                                    for ctx in contexts:
                                        # Base64 string check: if there are no spaces in a long segment, it's likely base64
                                        if len(ctx.split()) > 2:
                                            readable_contexts.append(ctx)
                                            
                                    if readable_contexts:
                                        results.append({
                                            'file': file_path,
                                            'xml_file': xml_file,
                                            'contexts': readable_contexts
                                        })
                    except Exception as e:
                        print(f"Error reading zip structure of {file_path}: {e}")
                else:
                    # It's an old .doc format, binary file. Let's do a raw string/regex search
                    try:
                        with open(file_path, 'rb') as f:
                            raw_content = f.read().decode('utf-8', errors='ignore')
                            # Look for 'gif' in raw decoded string
                            matches = list(re.finditer(r'gif', raw_content, re.IGNORECASE))
                            if matches:
                                contexts = []
                                for m in matches:
                                    start = max(0, m.start() - 50)
                                    end = min(len(raw_content), m.end() + 50)
                                    # clean up binary noise
                                    snippet = re.sub(r'[\x00-\x1f\x7f-\xff]', ' ', raw_content[start:end])
                                    snippet = re.sub(r'\s+', ' ', snippet)
                                    contexts.append(snippet.strip())
                                results.append({
                                    'file': file_path,
                                    'xml_file': 'binary raw content',
                                    'contexts': contexts
                                })
                    except Exception as e:
                        print(f"Error reading binary doc {file_path}: {e}")
                        
    return scanned_files, results

if __name__ == '__main__':
    search_dir = '/Users/buc-cvudes-medios1/Documents/GEO/Archivos E'
    scanned, found_items = search_word_files(search_dir)
    
    print("\n--- Scanned Word Files ---")
    for f in scanned:
        print(f" - {f}")
        
    print(f"\n--- Search Results ({len(found_items)} matches found) ---")
    for idx, item in enumerate(found_items, 1):
        print(f"{idx}. File: {item['file']}")
        print(f"   Internal path: {item['xml_file']}")
        print("   Matches Context:")
        for ctx in item['contexts']:
            print(f"     - ... {ctx} ...")
        print("-" * 50)
