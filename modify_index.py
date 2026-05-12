import re

with open('/Users/JayNaik/Downloads/TCS/Code/index.html', 'r') as f:
    html = f.read()

# Remove the old PYQ section from the bottom
# The old PYQ section looks like:
# <section class="section" id="pyq-section">
# ...
# </section>
# It's at the end of the <div class="container"> right before <footer>.

pyq_match = re.search(r'<section class="section" id="pyq-section">.*?</section>', html, re.DOTALL)
if pyq_match:
    old_pyq = pyq_match.group(0)
    html = html.replace(old_pyq, '')

# Now let's create a beautiful PYQ section to insert ABOVE the Chapters section.
# The chapters section looks like:
# <section class="section">
#   <h2 class="section-title">Chapters</h2>

new_pyq_html = """
    <section class="section" id="pyq-section">
        <h2 class="section-title" style="display:flex; align-items:center; gap:10px;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--cyan)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            Previous Year Questions (PYQs)
        </h2>
        <p style="color:var(--text2); margin-bottom:24px; font-size:15px; margin-top:-10px;">Detailed, exam-ready solutions for recent TCS/TOC past papers. Includes formal tuples and state diagrams.</p>
        
        <div class="grid" style="grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap:20px;">
            <!-- 2024-25 Paper -->
            <a href="pyq_2024.html" class="card" style="text-decoration:none; display:flex; flex-direction:column; justify-content:space-between; border-top: 4px solid var(--purple);">
                <div>
                    <h3 class="card-title" style="color:var(--text); margin-bottom:12px; font-size:18px;">Final / Re-Examination</h3>
                    <div style="display:flex; gap:10px; flex-wrap:wrap; font-family:monospace; font-size:12px; color:var(--text2);">
                        <span style="background:var(--bg2); padding:4px 8px; border-radius:4px; border:1px solid var(--border);">2024-25</span>
                        <span style="background:var(--bg2); padding:4px 8px; border-radius:4px; border:1px solid var(--border);">100 Marks</span>
                        <span style="background:var(--bg2); padding:4px 8px; border-radius:4px; border:1px solid var(--border);">Batches 22-23 & 23-24</span>
                    </div>
                </div>
                <div style="margin-top:20px; font-size:14px; color:var(--purple); font-weight:600; display:flex; align-items:center; gap:6px;">
                    View Solutions 
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </div>
            </a>
            
            <!-- 2021-22 Paper -->
            <a href="pyq.html" class="card" style="text-decoration:none; display:flex; flex-direction:column; justify-content:space-between; border-top: 4px solid var(--cyan);">
                <div>
                    <h3 class="card-title" style="color:var(--text); margin-bottom:12px; font-size:18px;">Re-Examination</h3>
                    <div style="display:flex; gap:10px; flex-wrap:wrap; font-family:monospace; font-size:12px; color:var(--text2);">
                        <span style="background:var(--bg2); padding:4px 8px; border-radius:4px; border:1px solid var(--border);">2021-22</span>
                        <span style="background:var(--bg2); padding:4px 8px; border-radius:4px; border:1px solid var(--border);">100 Marks</span>
                        <span style="background:var(--bg2); padding:4px 8px; border-radius:4px; border:1px solid var(--border);">Sem IV</span>
                    </div>
                </div>
                <div style="margin-top:20px; font-size:14px; color:var(--cyan); font-weight:600; display:flex; align-items:center; gap:6px;">
                    View Solutions 
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </div>
            </a>
        </div>
    </section>
"""

# Insert new PYQ section above Chapters
# chapters section starts with <section class="section"> \n <h2 class="section-title">Chapters</h2>
chapters_start = '<section class="section">\n        <h2 class="section-title">Chapters</h2>'
if chapters_start in html:
    html = html.replace(chapters_start, new_pyq_html + '\n    ' + chapters_start)
else:
    # Try finding just chapters
    chapters_start_alt = '<h2 class="section-title">Chapters</h2>'
    chapters_sec = '<section class="section">\n        ' + chapters_start_alt
    if chapters_sec in html:
        html = html.replace(chapters_sec, new_pyq_html + '\n    ' + chapters_sec)
    else:
        print("Could not find Chapters section.")

with open('/Users/JayNaik/Downloads/TCS/Code/index.html', 'w') as f:
    f.write(html)
    
print("Updated index.html PYQ section.")
