import os
from PIL import Image, ImageDraw

def process_image():
    img_path = 'shiny1-logo.png'
    out_path = 'shiny1-logo-clean.png'
    if not os.path.exists(img_path):
        print("Image not found")
        return
        
    with Image.open(img_path) as img:
        img = img.convert("RGBA")
        width, height = img.size
        
        # Remove Gemini Logo (bottom right)
        draw = ImageDraw.Draw(img)
        # Sample background color just above the bottom right area
        sample_x, sample_y = width - 150, height - 150
        bg_color = img.getpixel((sample_x, sample_y))
        
        # Draw a rectangle over the logo
        draw.rectangle([width - 150, height - 150, width, height], fill=bg_color)
        
        img.save(out_path)
        
        # Get corner colors to help set the webpage background
        tl = img.getpixel((0, 0))
        tr = img.getpixel((width-1, 0))
        bl = img.getpixel((0, height-1))
        
        print(f"Top-Left: {tl}")
        print(f"Top-Right: {tr}")
        print(f"Bottom-Left: {bl}")
        print(f"Sampled BG for Gemini Logo removal: {bg_color}")
        
if __name__ == '__main__':
    process_image()
