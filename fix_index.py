with open('/Users/JayNaik/Downloads/TCS/Code/index.html', 'r') as f:
    html = f.read()

# Remove the empty PYQ comment lines if present
html = html.replace("  <!-- PYQ SECTION -->\n  \n\n\n", "")

new_pyq_html = """
  <!-- PYQ SECTION -->
  <section class="section" id="pyq-section" style="margin-bottom: 20px;">
    <div class="section-head">
      <h2 style="color: var(--cyan); display: flex; align-items: center; gap: 10px;">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
        Previous Year Questions (PYQs)
      </h2>
      <div class="line" style="background: linear-gradient(90deg, var(--cyan), transparent); width: 60px;"></div>
    </div>
    
    <p style="color:var(--text2); margin-bottom:24px; font-size:15px; margin-top:-10px;">Detailed, exam-ready solutions for recent TCS/TOC past papers. Includes formal tuples and state diagrams.</p>
    
    <div class="chapters-grid">
      <!-- 2024-25 Paper -->
      <a class="ch-card" href="pyq_2024.html" style="border-top: 4px solid var(--purple); background: var(--bg2); padding: 24px; border-radius: 12px; display: flex; flex-direction: column; justify-content: space-between; text-decoration: none; border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); border-left: 1px solid var(--border); transition: all 0.2s ease;">
        <div>
          <div style="font-size: 13px; font-weight: 700; color: var(--purple); margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px;">Latest Paper</div>
          <h3 style="color:var(--text); margin-bottom:12px; font-size:18px;">Final / Re-Examination</h3>
          <div style="display:flex; gap:10px; flex-wrap:wrap; font-family:monospace; font-size:12px; color:var(--text2);">
            <span style="background:var(--bg3); padding:4px 8px; border-radius:4px;">2024-25</span>
            <span style="background:var(--bg3); padding:4px 8px; border-radius:4px;">100 Marks</span>
          </div>
        </div>
        <div style="margin-top:20px; font-size:14px; color:var(--purple); font-weight:600; display:flex; align-items:center; gap:6px;">
          View Solutions 
          <span style="font-size: 16px;">→</span>
        </div>
      </a>
      
      <!-- 2021-22 Paper -->
      <a class="ch-card" href="pyq.html" style="border-top: 4px solid var(--cyan); background: var(--bg2); padding: 24px; border-radius: 12px; display: flex; flex-direction: column; justify-content: space-between; text-decoration: none; border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); border-left: 1px solid var(--border); transition: all 0.2s ease;">
        <div>
          <div style="font-size: 13px; font-weight: 700; color: var(--cyan); margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px;">Past Paper</div>
          <h3 style="color:var(--text); margin-bottom:12px; font-size:18px;">Re-Examination</h3>
          <div style="display:flex; gap:10px; flex-wrap:wrap; font-family:monospace; font-size:12px; color:var(--text2);">
            <span style="background:var(--bg3); padding:4px 8px; border-radius:4px;">2021-22</span>
            <span style="background:var(--bg3); padding:4px 8px; border-radius:4px;">100 Marks</span>
          </div>
        </div>
        <div style="margin-top:20px; font-size:14px; color:var(--cyan); font-weight:600; display:flex; align-items:center; gap:6px;">
          View Solutions 
          <span style="font-size: 16px;">→</span>
        </div>
      </a>
    </div>
  </section>

"""

if '<!-- CHAPTERS -->' in html:
    html = html.replace('<!-- CHAPTERS -->', new_pyq_html + '  <!-- CHAPTERS -->')
    with open('/Users/JayNaik/Downloads/TCS/Code/index.html', 'w') as f:
        f.write(html)
    print("Success")
else:
    print("Failed")
