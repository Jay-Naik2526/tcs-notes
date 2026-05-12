import re

with open('pyq_2024.html', 'r') as f:
    html = f.read()

# Remove white-space: pre-wrap from .grammar CSS
html = html.replace('.grammar { white-space: pre-wrap; background: var(--bg3);', '.grammar { background: var(--bg3);')

def format_grammar(match):
    inner = match.group(1)
    # Collapse all newlines and multiple spaces into a single space
    inner = re.sub(r'\s+', ' ', inner)
    
    # Now we insert <br> before every LHS.
    # LHS is either `<span class="nt">X</span> →` or `S →`
    # We shouldn't insert <br> at the very beginning.
    
    # Pattern to match LHS: (maybe space) ( <span class="nt">.*?</span> | [A-Za-z0-9_]+ ) \s* → 
    # But wait, in "where E1 →", "E1" is an LHS, but it's part of the same line! We don't want a <br> there.
    # Actually, looking at the previous output, new lines usually started right before `<span class="nt">A</span> → `
    # Let's just use manual replace since there are only 4 blocks, but wait, the Python script I wrote earlier already changed the spacing!
    
    return '<div class="grammar">' + inner + '</div>'

html = re.sub(r'<div class="grammar">(.*?)</div>', format_grammar, html, flags=re.DOTALL)

# Manual <br> insertions:
# Block 1:
html = html.replace('<span class="nt">A</span> → <span class="t">0</span>', '<br><span class="nt">A</span> → <span class="t">0</span>')

# Block 2:
html = html.replace('<span class="nt">A</span> → <span class="t">a</span><span class="nt">A</span>', '<br><span class="nt">A</span> → <span class="t">a</span><span class="nt">A</span>')
html = html.replace('<span class="nt">C</span> → <span class="t">a</span><span class="nt">C</span>', '<br><span class="nt">C</span> → <span class="t">a</span><span class="nt">C</span>')
html = html.replace('<span class="nt">D</span> → <span class="t">a</span><span class="nt">D</span>', '<br><span class="nt">D</span> → <span class="t">a</span><span class="nt">D</span>')

# Block 3:
html = html.replace('<span class="nt">A</span> → <span class="nt">Xa</span><span class="nt">Xb</span>', '<br><span class="nt">A</span> → <span class="nt">Xa</span><span class="nt">Xb</span>')
html = html.replace('<span class="nt">C</span> → <span class="nt">Xa</span><span class="nt">C</span>', '<br><span class="nt">C</span> → <span class="nt">Xa</span><span class="nt">C</span>')
html = html.replace('<span class="nt">D</span> → <span class="nt">Xa</span><span class="nt">E2</span>', '<br><span class="nt">D</span> → <span class="nt">Xa</span><span class="nt">E2</span>')
html = html.replace('<span class="nt">D</span> → <span class="nt">Xb</span><span class="nt">E3</span>', '<br><span class="nt">D</span> → <span class="nt">Xb</span><span class="nt">E3</span>')
html = html.replace('<span class="nt">D</span> → <span class="nt">Xa</span><span class="nt">Xa</span>', '<br><span class="nt">D</span> → <span class="nt">Xa</span><span class="nt">Xa</span>')
html = html.replace('<span class="nt">Xa</span> → <span class="t">a</span>', '<br><span class="nt">Xa</span> → <span class="t">a</span>')

# Block 4:
html = html.replace(' S → <span class="nt">A</span><span class="nt">F2</span> (from', '<br>S → <span class="nt">A</span><span class="nt">F2</span> (from')
html = html.replace(' S → <span class="nt">A</span><span class="nt">F3</span> where', '<br>S → <span class="nt">A</span><span class="nt">F3</span> where')
html = html.replace(' S → <span class="nt">C</span><span class="nt">D</span> |', '<br>S → <span class="nt">C</span><span class="nt">D</span> |')

with open('pyq_2024.html', 'w') as f:
    f.write(html)
print("Reformatted grammar")
