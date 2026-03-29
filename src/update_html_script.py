import os
import re

def update_html_files():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update CSS root variables to chrome colors
        content = re.sub(r'--gold-primary: #d4af37;', r'--gold-primary: #cbd5e1;', content)
        content = re.sub(r'--gold-light: #f3e5ab;', r'--gold-light: #f8fafc;', content)
        
        # Remove the rectangle block mapping
        content = re.sub(r'background-color: rgba\(25, 30, 40, 0\.4\);\s*border-radius: 12px;\s*box-shadow: [^;]+;\s*backdrop-filter: blur\([^\)]+\);\s*border: 1px solid rgba\(212, 175, 55, 0\.15\);', 'background: transparent;', content)
        
        # Make the page background look like the graphic background (match the deep dark colors exactly, and blend the logo image)
        # We will use exactly #040811 as the outer radial color which blends with the image edges.
        # body background radial gradient change:
        body_bg_pattern = r'background: radial-gradient\(circle at center, #1e293b 0%, #0f172a 100%\);'
        # We can set the background to the image directly as requested: "Make the whole page look like the graphic back ground"
        # Or match the colors. Let's use the image itself as background to be absolutely sure we do what they meant.
        # If the image is the body background, we shouldn't show it as an IMG tag.
        # But wait, if they say "remove the gemini logo from the graphic", that implies the graphic is still shown as a graphic!
        # If the graphic is still shown as an img, making the body look like the graphic background means matching the gradient!
        new_body_bg = r'background: radial-gradient(circle at top right, #3a4149 0%, #040811 60%, #000204 100%);'
        content = re.sub(body_bg_pattern, new_body_bg, content)

        # But wait, let's actually set the background to be #040811 so it blends with the logo edges better 
        # Actually, let's just make the body background #040811 flat so perfectly matches logo bottom.

        # Change linear gradients
        content = re.sub(r'linear-gradient\(to right, #bf953f, #fcf6ba, #b38728, #fbf5b7, #aa771c\)', r'linear-gradient(to right, #9ca3af, #f8fafc, #64748b, #ffffff, #9ca3af)', content)
        content = re.sub(r'linear-gradient\(135deg, #bf953f 0%, #aa771c 100%\)', r'linear-gradient(135deg, #cbd5e1 0%, #64748b 100%)', content)
        content = re.sub(r'linear-gradient\(135deg, #fcf6ba 0%, #bf953f 100%\)', r'linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%)', content)
        content = re.sub(r'box-shadow: 0 4px 15px rgba\(191, 149, 63, 0\.3\)', r'box-shadow: 0 4px 15px rgba(203, 213, 225, 0.3)', content)
        content = re.sub(r'box-shadow: 0 6px 20px rgba\(191, 149, 63, 0\.5\)', r'box-shadow: 0 6px 20px rgba(203, 213, 225, 0.5)', content)

        # Update link/button borders hovering colors
        content = re.sub(r'rgba\(212, 175, 55,', r'rgba(203, 213, 225,', content)
        content = re.sub(r'border: 1px solid var\(--gold-primary\);', r'border: 1px solid var(--gold-primary);', content)

        # Index page rectangle blocks removal
        if filename == 'indexpage1.html':
            content = re.sub(r'background-color: rgba\(15, 23, 42, 0\.8\);\s*backdrop-filter: blur\([^\)]+\);\s*box-shadow: [^;]+;', 'background: transparent; border-bottom: none;', content)
            content = re.sub(r'background-color: #080c13;\s*', 'background: transparent;\n            ', content)
            # Remove menu-item background blocks
            content = re.sub(r'background-color: rgba\(255, 255, 255, 0\.02\);\s*', 'background: transparent;\n            ', content)

        # Update image source from shiny1-logo.png to shiny1-logo-clean.png
        content = re.sub(r'shiny1-logo\.png', r'shiny1-logo-clean.png', content)

        # Remove "david Zbonski, investment advisor representative"
        # The HTML is `<div class="subtitle">David Zbonski, Investment Advisor Representative</div>`
        content = re.sub(r'<div class="subtitle">David Zbonski, Investment Advisor Representative</div>\n*', '', content)

        # Phone graphic conversion
        if filename == 'index.html':
            phone_div = r'<div class="phone">865 - 855 - 4555</div>'
            phone_canvas = '''<canvas id="phoneCanvas" width="300" height="60" style="margin: 1rem 0 2.5rem 0; display: block; margin-left: auto; margin-right: auto;"></canvas>
        <script>
            const canvas = document.getElementById('phoneCanvas');
            const ctx = canvas.getContext('2d');
            ctx.font = '700 28px Cinzel, serif';
            let gradient = ctx.createLinearGradient(0, 0, canvas.width, 0);
            gradient.addColorStop(0, "#9ca3af");
            gradient.addColorStop(0.25, "#f8fafc");
            gradient.addColorStop(0.5, "#64748b");
            gradient.addColorStop(0.75, "#ffffff");
            gradient.addColorStop(1, "#9ca3af");
            ctx.fillStyle = gradient;
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.shadowColor = 'rgba(255, 255, 255, 0.2)';
            ctx.shadowBlur = 8;
            ctx.fillText('865 - 855 - 4555', canvas.width/2, canvas.height/2);
        </script>'''
            content = content.replace(phone_div, phone_canvas)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    update_html_files()
