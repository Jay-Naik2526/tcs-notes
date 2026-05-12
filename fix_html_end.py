with open('pyq_2023.html', 'r') as f:
    content = f.read()

# We need to remove the extra </div> that matched with psec
import re
new_content = re.sub(r'</div>\s*</div>\s*</body>\s*</html>', '</div>\n</body>\n</html>', content)

with open('pyq_2023.html', 'w') as f:
    f.write(new_content)
