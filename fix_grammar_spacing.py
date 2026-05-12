import re

with open('pyq_2024.html', 'r') as f:
    html = f.read()

# 1. Add white-space: pre-wrap to .grammar if not present
if 'white-space: pre-wrap' not in html.split('.grammar {')[1].split('}')[0]:
    html = html.replace('.grammar { background: var(--bg3);', '.grammar { white-space: pre-wrap; background: var(--bg3);')

# 2. Fix the indentation inside <div class="grammar"> tags
def fix_grammar_block(match):
    inner = match.group(1)
    # split by lines
    lines = inner.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        # strip leading whitespace if it's not the first line (or even if it is)
        s = line.lstrip()
        if s:
            new_lines.append(s)
    # Join with newline
    return '<div class="grammar">' + '\n'.join(new_lines) + '</div>'

html = re.sub(r'<div class="grammar">(.*?)</div>', fix_grammar_block, html, flags=re.DOTALL)

with open('pyq_2024.html', 'w') as f:
    f.write(html)
print("Fixed grammar spacing")
