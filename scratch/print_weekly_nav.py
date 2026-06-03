html_path_1 = "/Users/buc-cvudes-medios1/Documents/GEO/Html Originales/Momentos/Momento evaluativo 1.html"
html_path_2 = "/Users/buc-cvudes-medios1/Documents/GEO/Html Originales/Momentos/momento evaluantivo 2.html"

with open(html_path_1, "r", encoding="utf-8") as f:
    html_1 = f.read()

with open(html_path_2, "r", encoding="utf-8") as f:
    html_2 = f.read()

import re

print("=== MOMENTO 1 WEEKLY NAV ===")
weekly_nav_1 = re.findall(r'<div class="dropdown-menu[^"]*">.*?</div>', html_1, re.DOTALL)
if weekly_nav_1:
    print(weekly_nav_1[0])

print("\n=== MOMENTO 2 WEEKLY NAV ===")
weekly_nav_2 = re.findall(r'<div class="dropdown-menu[^"]*">.*?</div>', html_2, re.DOTALL)
if weekly_nav_2:
    print(weekly_nav_2[0])
