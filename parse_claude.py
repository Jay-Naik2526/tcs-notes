import re
with open('/Users/JayNaik/Downloads/TCS/Code/claude.html', 'r') as f:
    html = f.read()

paper_sections = re.findall(r'<div class="psec[^>]*id="p1".*?<!-- =========================================================\s+PAPER 2', html, re.DOTALL)
if paper_sections:
    p1 = paper_sections[0]
    # we need to put it into a standalone html file similar to pyq.html
    print("Found paper 1. Size:", len(p1))
    
    # Save the paper 1 content into pyq_2024.html
