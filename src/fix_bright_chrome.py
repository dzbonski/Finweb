import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

old_gradient1 = 'linear-gradient(to bottom right, #f8fafc 0%, #9ca3af 30%, #ffffff 50%, #64748b 70%, #cbd5e1 100%)'
new_gradient1 = 'linear-gradient(to bottom right, #ffffff 0%, #e2e8f0 30%, #ffffff 50%, #cbd5e1 75%, #f8fafc 100%)'

old_gradient2_links = 'linear-gradient(to bottom right, #e2e8f0 0%, #9ca3af 45%, #ffffff 50%, #475569 55%, #cbd5e1 100%)'
new_gradient2_links = 'linear-gradient(to bottom right, #ffffff 0%, #cbd5e1 45%, #ffffff 50%, #e2e8f0 65%, #f8fafc 100%)'

old_gradient3_hover = 'linear-gradient(to bottom right, #ffffff 0%, #cbd5e1 45%, #64748b 50%, #ffffff 55%, #e2e8f0 100%)'
new_gradient3_hover = 'linear-gradient(to bottom right, #ffffff 0%, #f8fafc 45%, #e2e8f0 50%, #ffffff 55%, #cbd5e1 100%)'

for f_name in html_files:
    with open(f_name, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(old_gradient1, new_gradient1)
    content = content.replace(old_gradient2_links, new_gradient2_links)
    content = content.replace(old_gradient3_hover, new_gradient3_hover)

    if f_name == 'index.html':
        content = content.replace('gradient.addColorStop(0, "#9ca3af");', 'gradient.addColorStop(0, "#ffffff");')
        content = content.replace('gradient.addColorStop(0.25, "#f8fafc");', 'gradient.addColorStop(0.25, "#e2e8f0");')
        content = content.replace('gradient.addColorStop(0.5, "#64748b");', 'gradient.addColorStop(0.5, "#ffffff");')
        content = content.replace('gradient.addColorStop(0.75, "#ffffff");', 'gradient.addColorStop(0.75, "#cbd5e1");')
        content = content.replace('gradient.addColorStop(1, "#9ca3af");', 'gradient.addColorStop(1, "#f8fafc");')

    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(content)
