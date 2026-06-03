import os

def update_moment_urls(file_path):
    print(f"Updating URLs in: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements:
    # Avance 1: id=3844 -> id=3891
    # Avance 2: id=3874 -> id=3892
    # Avance 3: id=3877 -> id=3893
    # Avance 4: id=3878 -> id=3894
    # Avance 5: id=3879 -> id=3895
    replacements = {
        'id=3844': 'id=3891',
        'id=3874': 'id=3892',
        'id=3877': 'id=3893',
        'id=3878': 'id=3894',
        'id=3879': 'id=3895'
    }

    modified = False
    for old, new in replacements.items():
        if old in content:
            print(f"  Replacing '{old}' with '{new}'")
            content = content.replace(old, new)
            modified = True

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated {file_path}\n")
    else:
        print(f"No changes needed for {file_path}\n")

if __name__ == '__main__':
    moments = [
        '/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo1.html',
        '/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Momentos/Momento Evaluativo2.html'
    ]
    for m in moments:
        if os.path.exists(m):
            update_moment_urls(m)
        else:
            print(f"File not found: {m}")
