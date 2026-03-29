import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

old_bg = 'background: radial-gradient(circle at top right, #3a4149 0%, #040811 60%, #000204 100%);'
new_bg = 'background: radial-gradient(farthest-corner at 80% 0%, #4a5568 0%, #2d3748 30%, #040811 85%, #000204 100%);'

for f_name in html_files:
    with open(f_name, 'r', encoding='utf-8') as f:
        content = f.read()

    # The user wanted to expand the spotlighted area of the logo farther down and to the left.
    # We will adjust the body background radial-gradient to achieve this.
    content = content.replace(old_bg, new_bg)

    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(content)
