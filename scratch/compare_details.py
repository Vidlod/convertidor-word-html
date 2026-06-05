import re

def search_text_in_file(filepath, pattern):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return re.findall(pattern, content, re.IGNORECASE)

if __name__ == '__main__':
    # Let's inspect specific items
    # 1. Check questions in Entregable 1 vs AAA
    e1_path = "scratch/Entregable1_Recoleccion_de_datos_text.txt"
    aaa_path = "scratch/AAA-pregrado_text.txt"
    
    with open(e1_path, 'r', encoding='utf-8') as f:
        e1_content = f.read()
        
    with open(aaa_path, 'r', encoding='utf-8') as f:
        aaa_content = f.read()
        
    print("=== CHECKING ENTREGABLE 1 QUESTIONS ===")
    e1_questions = re.findall(r'\d+\)\s+.*', e1_content)
    aaa_questions = re.findall(r'\d+\)\s+.*', aaa_content)
    
    print("Questions in Entregable 1 DOCX:")
    for q in e1_questions:
        print("  -", q)
        
    print("\nQuestions in AAA DOCX:")
    for q in aaa_questions:
        print("  -", q)
        
    # Let's check calculations or exercises in Entregable 1
    print("\n=== CHECKING ENTREGABLE 1 SAMPLING EXERCISES ===")
    e1_exercises = re.findall(r'\b(?:muestra|población|peatones|defunciones)\b', e1_content)
    print("Found key sampling terms in Entregable 1:", set(e1_exercises))
    
    # 2. Check if there are differences in Entregable 2 activities
    print("\n=== CHECKING ENTREGABLE 2 ACTIVITIES ===")
    e2_path = "scratch/Entregable2_Organizacion_de_datos_text.txt"
    with open(e2_path, 'r', encoding='utf-8') as f:
        e2_content = f.read()
    
    # Check what activities are in Entregable 2
    e2_acts = re.findall(r'Actividad\s+\d+[:\.]\s+.*', e2_content)
    print("Activities in Entregable 2 DOCX:")
    for act in e2_acts:
        print("  -", act)
        
    # Compare with AAA activities for Entregable 2
    # In AAA we have Weeks 4 and 5 which are for Entregable 2.
    aaa_e2_acts = re.findall(r'Actividad\s+\d+[:\.]\s+.*', aaa_content)
    print("\nAll Activities in AAA:")
    for act in aaa_e2_acts:
        print("  -", act)
