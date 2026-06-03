import os
import re

entregables_dir = "/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales/Entregables CARJO"

html_files = [
    os.path.join(entregables_dir, f)
    for f in os.listdir(entregables_dir)
    if f.endswith(".html")
]

for file_path in html_files:
    print(f"\nProcessing: {os.path.basename(file_path)}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    
    # We match: <div class="card-body"> ... [br tags] </div>
    # and remove the br tags at the end of the card-body content.
    def card_body_replacer(match):
        prefix = match.group(1)
        body_content = match.group(2)
        suffix = match.group(3)
        
        # Strip trailing whitespaces and br tags completely
        cleaned_body = re.sub(r'(?:\s*<br\s*/?>)*\s*$', '', body_content, flags=re.IGNORECASE)
        # End directly with no <br>
        return f'{prefix}{cleaned_body}\n            </div>\n        </div>'

    # The tab pane has structure:
    # <div class="tab-pane ...">
    #     <div class="card-body">
    #         ...
    #     </div>
    # </div>
    # We replace:
    content = re.sub(
        r'(<div class="tab-pane\b[^>]*>\s*<div class="card-body">)(.*?)(</div>\s*</div>)',
        card_body_replacer,
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    if content != original:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  Updated file successfully.")
    else:
        print("  No changes needed.")
