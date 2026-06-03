import sys
import re

if len(sys.argv) < 2:
    print("Usage: python3 view_row.py <row_number1> <row_number2> ...")
    sys.exit(1)

rows_to_find = sys.argv[1:]

with open("/Users/buc-cvudes-medios1/Documents/GEO/scratch/raw_weeks_output.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Split the content by "ROW " followed by a number
parts = re.split(r'(?=ROW \d+ - WEEK:)', content)

for r in rows_to_find:
    found = False
    prefix = f"ROW {r} - WEEK:"
    for p in parts:
        if p.strip().startswith(prefix):
            print(p.strip())
            print("\n" + "#" * 80 + "\n")
            found = True
            break
    if not found:
        print(f"Row {r} not found.")
