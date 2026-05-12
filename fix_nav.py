with open('pyq_2023.html', 'r') as f:
    content = f.read()

bad_nav = """<div class="topnav">
        <div class="topnav-inner">
            <div class="brand">TCS PYQ</div>
            <button class="pbtn" onclick="window.location.href='pyq_2024.html'">2024-25 Final/Re</button>
            <button class="pbtn active" onclick="window.location.href='pyq_2023.html'">2022-23 Final/Re</button>
            <button class="pbtn" onclick="window.location.href='pyq.html'">2021-22 Re-Exam</button>
        </div>
    </div>"""

good_nav = """<div class="topnav">
        <div class="brand">TCS Notes &bull; PYQ</div>
        <div class="nav-links">
            <a href="index.html">← Back to Chapters</a>
        </div>
    </div>"""

# Remove the specific bad topnav code
import re
new_content = re.sub(r'<div class="topnav">.*?</div>\s*</div>', good_nav, content, flags=re.DOTALL)

with open('pyq_2023.html', 'w') as f:
    f.write(new_content)
print("Fixed nav")
