import re

with open('/Users/JayNaik/Downloads/TCS/Code/claude.html', 'r') as f:
    claude = f.read()

with open('/Users/JayNaik/Downloads/TCS/Code/pyq.html', 'r') as f:
    pyq = f.read()

# Extract p1 from claude
p1_match = re.search(r'<div class="psec[^>]*id="p1".*?>(.*?)<!-- =========================================================\s+PAPER 2', claude, re.DOTALL)
if p1_match:
    p1_content = p1_match.group(1).strip()
    
    # We need to wrap it inside the main div
    # In pyq.html, the structure is:
    # <div class="main">
    #     <div class="ph">...</div>
    #     ...
    # </div>
    # So we replace the content inside <div class="main"> in pyq.html with p1_content
    # wait, pyq.html has a <footer> inside the body.
    
    pyq_head = pyq.split('<div class="main">')[0] + '<div class="main">\n'
    pyq_tail = '\n    </div> <!-- end main -->\n' + pyq.split('</div> <!-- end main -->')[1]
    
    new_html = pyq_head + p1_content + pyq_tail
    
    with open('/Users/JayNaik/Downloads/TCS/Code/pyq_2024.html', 'w') as f:
        f.write(new_html)
        
    print("pyq_2024.html created.")
else:
    print("Could not find p1 content.")

