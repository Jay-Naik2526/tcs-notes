import re

with open('/Users/JayNaik/Downloads/TCS/Code/pyq_2024.html', 'r') as f:
    html = f.read()

# 1. Add missing CSS classes
css_additions = """
        .grammar { background: var(--bg3); border: 1px solid var(--border); border-radius: 6px; padding: 11px 15px; font-family: 'Courier New', monospace; font-size: 13px; margin: 9px 0; line-height: 2.2; color: var(--text3); }
        .grammar .nt { color: var(--orange); }
        .grammar .t { color: var(--green); }
        .trace { background: var(--bg4); border: 1px solid var(--border); border-radius: 6px; padding: 11px 15px; font-family: 'Courier New', monospace; font-size: 12.5px; color: var(--text3); margin: 9px 0; line-height: 1.95; white-space: pre-wrap; }
        .tbox { background: rgba(240, 192, 64, .05); border: 1px solid rgba(240, 192, 64, .2); border-left: 3px solid var(--gold); border-radius: 5px; padding: 11px 15px; margin: 10px 0; }
        .tbox .tl { font-size: 9px; font-weight: 800; color: var(--gold); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 7px; }
        .tbox ul { padding-left: 15px; }
        .tbox li { font-size: 13px; color: var(--text3); margin-bottom: 3px; }
        .pbox { background: rgba(63, 185, 80, .05); border: 1px solid rgba(63, 185, 80, .15); border-left: 3px solid var(--green); border-radius: 5px; padding: 11px 15px; margin: 10px 0; }
        .pbox .pl { font-size: 9px; font-weight: 800; color: var(--green); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 7px; }
        .nbox { background: rgba(255, 166, 87, .05); border: 1px solid rgba(255, 166, 87, .18); border-left: 3px solid var(--orange); border-radius: 5px; padding: 10px 14px; margin: 9px 0; font-size: 13px; color: var(--text3); }
        .nbox .nl { font-size: 9px; font-weight: 800; color: var(--orange); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
        .oosbox { background: rgba(248, 81, 73, .05); border: 1px solid rgba(248, 81, 73, .2); border-radius: 5px; padding: 11px 15px; margin: 9px 0; font-size: 13px; color: var(--red); }
"""
if '.grammar {' not in html:
    html = html.replace('</style>', css_additions + '\n    </style>')

# 2. Fix SVGs for Q3b
# qback -> q0
html = html.replace('d="M464,120 Q380,165 104,120"', 'd="M464,120 Q284,240 104,120"')
html = html.replace('x="280" y="178"', 'x="284" y="195"')

# q0 -> q5 on #
html = html.replace('d="M104,96 Q355,50 582,72"', 'd="M104,96 Q343,-30 582,72"')
html = html.replace('x="340" y="60"', 'x="343" y="0"')
html = html.replace('done)</text>', 'done)</text>').replace('\n                                done)</text>', 'done)</text>') # Fix multiline split if any

# mismatch -> rej
html = html.replace('<line x1="386" y1="65" x2="656" y2="148" stroke="#f85149" stroke-width="1.3"\n                                stroke-dasharray="3,2" marker-end="url(#a6)" />', '<path d="M 386,65 Q 520,150 656,148" fill="none" stroke="#f85149" stroke-width="1.3" stroke-dasharray="3,2" marker-end="url(#a6)" />')
html = html.replace('x="555" y="118"', 'x="520" y="130"')

with open('/Users/JayNaik/Downloads/TCS/Code/pyq_2024.html', 'w') as f:
    f.write(html)

print("Patched pyq_2024.html successfully.")
