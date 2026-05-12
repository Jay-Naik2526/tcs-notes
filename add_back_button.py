import os
import glob

html_files = glob.glob('ch*.html')

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "← Back to Chapters" in content:
        continue
        
    target = '        <div class="nav-section">Contents</div>'
    replacement = '''        <a class="nav-item" href="index.html" style="margin-top: 15px; margin-bottom: 5px; font-weight: 800; color: var(--accent4); border-left: 2px solid var(--accent4);">← Back to Chapters</a>
        <div class="nav-section">Contents</div>'''
        
    if target in content:
        content = content.replace(target, replacement)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fpath}")
    else:
        print(f"Target not found in {fpath}")

