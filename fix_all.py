import glob

# 1. Subject name fix
for fpath in glob.glob('*.html'):
    with open(fpath, 'r') as f:
        content = f.read()
    
    # Replace any instance of "Theory of Computer Science"
    new_content = content.replace("Theory of Computer Science", "Theoretical Computer Science")
    
    # 2. Fix topnav in pyq files
    if 'TCS PYQ' in content and 'pbtn' in content:
        # standard topnav for pyq_2024, pyq_2023, pyq
        nav_html = """
        <div class="topnav-inner">
            <div class="brand">TCS PYQ</div>
            <button class="pbtn{{' active' if '2024' in fpath else ''}}" onclick="window.location.href='pyq_2024.html'">2024-25 Final/Re</button>
            <button class="pbtn{{' active' if '2023' in fpath else ''}}" onclick="window.location.href='pyq_2023.html'">2022-23 Final/Re</button>
            <button class="pbtn{{' active' if 'pyq.html' in fpath else ''}}" onclick="window.location.href='pyq.html'">2021-22 Re-Exam</button>
        </div>"""
        
        # generate specific nav html for the current file
        specific_nav = nav_html.replace("{{' active' if '2024' in fpath else ''}}", " active" if "pyq_2024" in fpath else "")
        specific_nav = specific_nav.replace("{{' active' if '2023' in fpath else ''}}", " active" if "pyq_2023" in fpath else "")
        specific_nav = specific_nav.replace("{{' active' if 'pyq.html' in fpath else ''}}", " active" if "pyq.html" in fpath else "")
        
        import re
        new_content = re.sub(r'<div class="topnav-inner">.*?</div>', specific_nav.strip(), new_content, flags=re.DOTALL)
        
    if new_content != content:
        with open(fpath, 'w') as f:
            f.write(new_content)
        print(f"Updated {fpath}")

print("All fixes applied")
