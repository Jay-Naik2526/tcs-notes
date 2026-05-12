import os
import glob

html_files = glob.glob("*.html")
count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "Theory of Computation" in content:
        new_content = content.replace("Theory of Computation", "Theoretical Computer Science")
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
        count += 1

print(f"Total files updated: {count}")
