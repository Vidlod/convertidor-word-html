import re

with open("/Users/buc-cvudes-medios1/Documents/GEO/scratch/weeks_raw_cells.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Let's split by double line separators
blocks = content.split("============================================================\n")

for b in blocks:
    if "ROW" in b:
        # get week header
        lines = b.split("\n")
        header = lines[0]
        # check which week
        print(f"\n=========================================\n{header}\n=========================================")
        # print first few lines of each column
        current_col = None
        col_lines = []
        for line in lines[1:]:
            if line.startswith("--- Col "):
                if current_col is not None:
                    col_text = "\n".join(col_lines).strip()
                    # print first 1000 chars of the column text
                    print(f"{current_col}:")
                    print(col_text[:1500])
                    print("...")
                current_col = line.strip()
                col_lines = []
            else:
                col_lines.append(line)
        if current_col is not None:
            col_text = "\n".join(col_lines).strip()
            print(f"{current_col}:")
            print(col_text[:1500])
            print("...")
