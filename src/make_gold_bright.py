import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

new_css_block = r'''
        .chrome-text, h1, h2, p, .subtitle, .disclaimer, .phone, .quote {
            background: linear-gradient(to bottom right, #fdf5c9 0%, #d4af37 30%, #fffde7 50%, #b38728 70%, #fcf6ba 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent !important;
            text-shadow: 0px 1px 2px rgba(0,0,0,0.5);
        }

        /* Override links */
        .menu-item, .btn-enter, .btn-back {
            background: linear-gradient(to bottom right, #fcf6ba 0%, #d4af37 40%, #fffde7 50%, #b38728 60%, #fdf5c9 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent !important;
            text-shadow: 0px 1px 2px rgba(0,0,0,0.5);
            border-color: #d4af37;
        }
        
        .menu-item:hover, .btn-enter:hover, .btn-back:hover {
            background: linear-gradient(to bottom right, #ffffff 0%, #fdf5c9 45%, #d4af37 50%, #ffffff 55%, #fcf6ba 100%);
            -webkit-background-clip: text;
            background-clip: text;
            text-shadow: 0px 0px 15px rgba(255,215,0,0.4);
            color: transparent !important;
            border-color: #fdf5c9;
        }
'''

for f_name in html_files:
    with open(f_name, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'\.chrome-text,.*?border-color: #[a-f0-9]+;\s*\}', new_css_block.strip() + '\n', content, flags=re.DOTALL)
    
    content = content.replace('shiny1-logo-chrome.png', 'shiny1-logo-blend.png')
    
    # Phone Canvas Updates for index.html
    if f_name == 'index.html':
        content = re.sub(r'gradient\.addColorStop\(0, "[^"]+"\);', r'gradient.addColorStop(0, "#fdf5c9");', content)
        content = re.sub(r'gradient\.addColorStop\(0\.25, "[^"]+"\);', r'gradient.addColorStop(0.25, "#d4af37");', content)
        content = re.sub(r'gradient\.addColorStop\(0\.5, "[^"]+"\);', r'gradient.addColorStop(0.5, "#fffde7");', content)
        content = re.sub(r'gradient\.addColorStop\(0\.75, "[^"]+"\);', r'gradient.addColorStop(0.75, "#b38728");', content)
        content = re.sub(r'gradient\.addColorStop\(1, "[^"]+"\);', r'gradient.addColorStop(1, "#fcf6ba");', content)

    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(content)
