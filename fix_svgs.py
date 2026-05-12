import re

with open('/Users/JayNaik/Downloads/TCS/Code/pyq_2024.html', 'r') as f:
    html = f.read()

def adjust_viewbox(match):
    prefix = match.group(1)
    min_x = int(match.group(2))
    min_y = int(match.group(3))
    w = int(match.group(4))
    h = int(match.group(5))
    
    # Adjust min-y by -50 and height by +80 to give plenty of padding top and bottom
    new_min_y = min_y - 50
    new_h = h + 80
    
    return f'{prefix}viewBox="{min_x} {new_min_y} {w} {new_h}"'

new_html = re.sub(r'(<svg[^>]*?)viewBox="(-?\d+)\s+(-?\d+)\s+(\d+)\s+(\d+)"', adjust_viewbox, html)

with open('/Users/JayNaik/Downloads/TCS/Code/pyq_2024.html', 'w') as f:
    f.write(new_html)

print("Adjusted SVGs in pyq_2024.html")
