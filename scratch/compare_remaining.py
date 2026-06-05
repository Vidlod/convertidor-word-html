import re

def print_activities(txt_path):
    print(f"\n=== Activities in {txt_path} ===")
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    acts = re.findall(r'Actividad\s+\d+[:\.]\s+.*', content)
    for act in acts:
        print("  -", act)

if __name__ == '__main__':
    print_activities("scratch/Entregable3_Analisis_de_datos_text.txt")
    print_activities("scratch/Entregable4_Interpretacion_de_resultados_text.txt")
    print_activities("scratch/Entregable5_Presentacion_de_resultados_text.txt")
