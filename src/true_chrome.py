import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

chrome_css = r'''
        .chrome-text, h1, h2, p, .subtitle, .disclaimer, .phone, .quote {
            background: linear-gradient(to bottom right, #ffffff 0%, #cbd5e1 20%, #94a3b8 45%, #ffffff 50%, #e2e8f0 75%, #ffffff 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent !important;
            text-shadow: 0px 1px 2px rgba(0,0,0,0.6);
        }

        /* Override links */
        .menu-item, .btn-enter, .btn-back {
            background: linear-gradient(to bottom right, #ffffff 0%, #94a3b8 45%, #ffffff 50%, #cbd5e1 75%, #ffffff 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent !important;
            text-shadow: 0px 1px 2px rgba(0,0,0,0.6);
            border-color: #cbd5e1;
        }
        
        .menu-item:hover, .btn-enter:hover, .btn-back:hover {
            background: linear-gradient(to bottom right, #ffffff 0%, #e2e8f0 45%, #ffffff 50%, #ffffff 60%, #f8fafc 100%);
            -webkit-background-clip: text;
            background-clip: text;
            text-shadow: 0px 0px 15px rgba(255,255,255,0.8);
            color: transparent !important;
            border-color: #ffffff;
        }
'''

for f_name in html_files:
    with open(f_name, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where .chrome-text starts and </style> ends
    start_idx = content.find('.chrome-text,')
    end_idx = content.find('</style>')
    
    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + chrome_css.strip() + '\n    ' + content[end_idx:]

    # Phone Canvas Updates for index.html
    if f_name == 'index.html':
        content = re.sub(r'gradient\.addColorStop\(0, "[^"]+"\);', r'gradient.addColorStop(0, "#ffffff");', content)
        content = re.sub(r'gradient\.addColorStop\(0\.25, "[^"]+"\);', r'gradient.addColorStop(0.25, "#9ca3af");', content)
        content = re.sub(r'gradient\.addColorStop\(0\.5, "[^"]+"\);', r'gradient.addColorStop(0.5, "#ffffff");', content)
        content = re.sub(r'gradient\.addColorStop\(0\.75, "[^"]+"\);', r'gradient.addColorStop(0.75, "#e2e8f0");', content)
        content = re.sub(r'gradient\.addColorStop\(1, "[^"]+"\);', r'gradient.addColorStop(1, "#ffffff");', content)

    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(content)
