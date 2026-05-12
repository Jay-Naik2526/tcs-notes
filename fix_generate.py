import re

with open('generate_pyq_2023.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Q2a missing q2 transitions
old_q2a_moore = """                        <path d="M140,80 Q100,130 60,80" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m2a)"/>
                        <text x="100" y="125" text-anchor="middle" font-size="11" fill="#c9d1d9">0</text>
                        
                        <!-- Divider -->"""
new_q2a_moore = """                        <path d="M140,80 Q100,130 60,80" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m2a)"/>
                        <text x="100" y="125" text-anchor="middle" font-size="11" fill="#c9d1d9">0</text>
                        
                        <path d="M240,80 Q150,140 60,80" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m2a)"/>
                        <text x="150" y="130" text-anchor="middle" font-size="11" fill="#c9d1d9">0</text>
                        <path d="M265,40 Q290,0 275,45" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m2a)"/>
                        <text x="290" y="20" text-anchor="middle" font-size="11" fill="#c9d1d9">1</text>
                        
                        <!-- Divider -->"""

content = content.replace(old_q2a_moore, new_q2a_moore)

old_q2a_mealy = """                        <path d="M440,80 Q400,130 360,80" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m2a)"/>
                        <text x="400" y="125" text-anchor="middle" font-size="11" fill="#c9d1d9">0 / 0</text>
                    </svg>"""
new_q2a_mealy = """                        <path d="M440,80 Q400,130 360,80" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m2a)"/>
                        <text x="400" y="125" text-anchor="middle" font-size="11" fill="#c9d1d9">0 / 0</text>
                        
                        <path d="M540,80 Q450,140 360,80" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m2a)"/>
                        <text x="450" y="130" text-anchor="middle" font-size="11" fill="#c9d1d9">0 / 0</text>
                        <path d="M565,40 Q590,0 575,45" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m2a)"/>
                        <text x="590" y="20" text-anchor="middle" font-size="11" fill="#c9d1d9">1 / 1</text>
                    </svg>"""

content = content.replace(old_q2a_mealy, new_q2a_mealy)

# Fix Q3a table
old_q3a_table = """                <p class="a">A number is divisible by 3 if the sum of its digits is divisible by 3. The DFA will have 3 states representing the running modulo 3 of the digit sum: <code>q0</code> (sum % 3 = 0, Accept state), <code>q1</code> (sum % 3 = 1), <code>q2</code> (sum % 3 = 2).</p>
                <div class="tw">
                    <table>
                        <thead>
                            <tr><th>State</th><th>Input: 0,3,6,9</th><th>Input: 1,4,7</th><th>Input: 2,5,8</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>→ ★ q0</td><td>q0</td><td>q1</td><td>q2</td></tr>
                            <tr><td>q1</td><td>q1</td><td>q2</td><td>q0</td></tr>
                            <tr><td>q2</td><td>q2</td><td>q0</td><td>q1</td></tr>
                        </tbody>
                    </table>
                </div>"""

new_q3a_table = """                <p class="a">A number is divisible by 3 if the sum of its digits is divisible by 3. We use an initial state <code>S</code> to prevent accepting the empty string. The other states represent the running modulo 3 of the digit sum: <code>q0</code> (sum % 3 = 0, Accept state), <code>q1</code> (sum % 3 = 1), <code>q2</code> (sum % 3 = 2).</p>
                <div class="tw">
                    <table>
                        <thead>
                            <tr><th>State</th><th>Input: 0,3,6,9</th><th>Input: 1,4,7</th><th>Input: 2,5,8</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>→ S</td><td>q0</td><td>q1</td><td>q2</td></tr>
                            <tr><td>★ q0</td><td>q0</td><td>q1</td><td>q2</td></tr>
                            <tr><td>q1</td><td>q1</td><td>q2</td><td>q0</td></tr>
                            <tr><td>q2</td><td>q2</td><td>q0</td><td>q1</td></tr>
                        </tbody>
                    </table>
                </div>"""

content = content.replace(old_q3a_table, new_q3a_table)

# Fix Q3a SVG S state
old_q3a_svg = """                    <svg width="100%" viewBox="0 -50 500 250" overflow="visible" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <marker id="m3a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M1,2 L8,5 L1,8" fill="none" stroke="#8b949e" stroke-width="1.5"/></marker>
                        </defs>
                        <!-- q0 -->
                        <path d="M40,100 L70,100" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m3a)"/>"""

new_q3a_svg = """                    <svg width="100%" viewBox="-80 -60 600 280" overflow="visible" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <marker id="m3a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M1,2 L8,5 L1,8" fill="none" stroke="#8b949e" stroke-width="1.5"/></marker>
                        </defs>
                        <!-- S -->
                        <path d="M-60,100 L-35,100" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m3a)"/>
                        <circle cx="-10" cy="100" r="24" fill="none" stroke="#58a6ff" stroke-width="2"/>
                        <text x="-10" y="104" text-anchor="middle" font-size="12" font-weight="bold" fill="#58a6ff">S</text>

                        <!-- S to q0 -->
                        <path d="M15,100 L70,100" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m3a)"/>
                        <text x="45" y="95" text-anchor="middle" font-size="10" fill="#c9d1d9">0,3,6,9</text>

                        <!-- S to q1 -->
                        <path d="M5,80 Q100,-30 230,35" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m3a)"/>
                        <text x="120" y="25" text-anchor="middle" font-size="10" fill="#c9d1d9">1,4,7</text>

                        <!-- S to q2 -->
                        <path d="M5,120 Q200,240 385,120" fill="none" stroke="#8b949e" stroke-width="1.5" marker-end="url(#m3a)"/>
                        <text x="180" y="195" text-anchor="middle" font-size="10" fill="#c9d1d9">2,5,8</text>

                        <!-- q0 -->"""

content = content.replace(old_q3a_svg, new_q3a_svg)

# Fix trace 
old_trace = """w = "31": q0 -(3)-> q0 -(1)-> q1. Ends in q1. Not Divisible (REJECT)
w = "45": q0 -(4)-> q1 -(5)-> q0. Ends in q0. Divisible (ACCEPT)"""

new_trace = """w = "31": S -(3)-> q0 -(1)-> q1. Ends in q1. Not Divisible (REJECT)
w = "45": S -(4)-> q1 -(5)-> q0. Ends in q0. Divisible (ACCEPT)"""

content = content.replace(old_trace, new_trace)

with open('generate_pyq_2023.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("generate_pyq_2023.py updated successfully.")
