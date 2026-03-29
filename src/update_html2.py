import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

chrome_css = r'''
        .chrome-text {
            background: linear-gradient(to bottom right, #f8fafc 0%, #94a3b8 40%, #ffffff 50%, #64748b 60%, #cbd5e1 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0px 2px 4px rgba(0,0,0,0.8);
        }

        body, p, h1, h2, a, div, span, .disclaimer, .bio-content, .quote {
            color: transparent;
        }

        /* Override links */
        .menu-item, .btn-enter, .btn-back {
            background: linear-gradient(to bottom right, #e2e8f0 0%, #9ca3af 45%, #ffffff 50%, #475569 55%, #cbd5e1 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
        }
        
        .menu-item:hover, .btn-enter:hover, .btn-back:hover {
            background: linear-gradient(to bottom right, #ffffff 0%, #cbd5e1 45%, #64748b 50%, #ffffff 55%, #e2e8f0 100%);
            -webkit-background-clip: text;
            background-clip: text;
            text-shadow: 0px 0px 10px rgba(255,255,255,0.4);
        }
'''

for f_name in html_files:
    with open(f_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Image logo replacement
    content = content.replace('shiny1-logo-clean.png', 'shiny1-logo-chrome.png')

    # Double image sizes & blend mode
    # Index.html logo is 250px inside css previously? Wait, I didn't verify index.html css correctly. 
    # Ah, in index.html, it's defined in `.logo-img`
    content = re.sub(r'\.logo-img {\s*max-width: [0-9]+px;', r'.logo-img { max-width: 500px; width: 90%; mix-blend-mode: screen;', content)

    # placeholder pages logo is inline: style="max-width: 150px; margin-bottom: 2rem; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5));"
    content = re.sub(r'style="max-width: 150px([^"]*)"', r'style="max-width: 300px; width: 90%; mix-blend-mode: screen;\1"', content)

    # Let's apply chrome text to everything.
    # We will add chrome_css to <style>
    if '.chrome-text' not in content:
        content = content.replace('</style>', chrome_css + '\n    </style>')

    # Apply chrome text to all elements by adding the class where appropriate
    content = re.sub(r'<h1(.*?)>', r'<h1 class="chrome-text"\1>', content)
    content = re.sub(r'<h2(.*?)>', r'<h2 class="chrome-text"\1>', content)
    content = re.sub(r'<p(.*?)>', r'<p class="chrome-text"\1>', content)
    content = re.sub(r'<div class="subtitle"(.*?)>', r'<div class="subtitle chrome-text"\1>', content)
    content = re.sub(r'<div class="phone"(.*?)>', r'<div class="phone chrome-text"\1>', content)
    content = re.sub(r'<div class="disclaimer"(.*?)>', r'<div class="disclaimer chrome-text"\1>', content)
    content = re.sub(r'<strong(.*?)>', r'<strong class="chrome-text"\1>', content)

    # Remove conflicting text gradient in existing H1 css
    content = re.sub(r'background: linear-gradient\([^\)]+\);\s*-webkit-background-clip: text;\s*background-clip: text;\s*color: transparent;', '', content)
    
    # Also clean up the phone canvas gradient, make it chrome instead of silver
    content = re.sub(r'let gradient2 = ctx.createLinearGradient\(0, 0, canvas.width, 0\);', r'let gradient = ctx.createLinearGradient(0, 0, canvas.width, 0);\n            gradient.addColorStop(0, "#cbd5e1");\n            gradient.addColorStop(0.5, "#ffffff");\n            gradient.addColorStop(1, "#cbd5e1");', content)
    
    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(content)
