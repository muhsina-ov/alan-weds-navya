import math
from PIL import Image, ImageDraw, ImageFont

def create_og_image():
    W, H = 1200, 630
    
    # 1. Base Canvas - rich warm ivory cream gradient
    img = Image.new("RGB", (W, H), "#FAF5EC")
    draw = ImageDraw.Draw(img)
    
    # Subtle soft radial / vertical warm gradient
    for y in range(H):
        ratio = y / H
        # From #FDFBF7 at top to #F6ECE0 at bottom
        r = int(253 - ratio * (253 - 246))
        g = int(251 - ratio * (251 - 236))
        b = int(247 - ratio * (247 - 224))
        draw.line([(0, y), (W, y)], fill=(r, g, b))
    
    # 2. Add Cathedral Church Illustration on the left
    church_path = "images/cdn/mm_cathedral_church.png"
    church = Image.open(church_path).convert("RGBA")
    ch_h = 515
    ch_w = int(church.width * (ch_h / church.height))
    church_resized = church.resize((ch_w, ch_h), Image.Resampling.LANCZOS)
    
    # Place church anchored at bottom left
    church_pos = (-15, H - ch_h + 12)
    img.paste(church_resized, church_pos, church_resized)
    
    # Soft translucent overlay on right side to ensure text readability
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    for x in range(460, W):
        progress = (x - 460) / (W - 460)
        alpha = int(progress * 230)
        overlay_draw.line([(x, 0), (x, H)], fill=(250, 245, 236, alpha))
    img.paste(Image.alpha_composite(Image.new("RGBA", (W, H), (250, 245, 236, 0)), overlay), (0, 0), overlay)

    # 3. Add Floral Bouquet Element at bottom right
    floral_path = "images/cdn/623915249_2629494717.png"
    floral = Image.open(floral_path).convert("RGBA")
    
    fl_w = 430
    fl_h = int(floral.height * (fl_w / floral.width))
    floral_br = floral.resize((fl_w, fl_h), Image.Resampling.LANCZOS)
    # Position tucked into bottom right corner
    img.paste(floral_br, (W - fl_w + 70, H - fl_h + 85), floral_br)
    
    # 4. Elegant Double Gold Border
    gold_color = (195, 155, 85)       # #C39B55
    gold_light = (225, 200, 145)     # #E1C891
    
    # Outer thin border
    draw.rectangle([22, 22, W - 22, H - 22], outline=gold_color, width=2)
    # Inner thin border
    draw.rectangle([28, 28, W - 28, H - 28], outline=gold_light, width=1)
    
    # Corner squares / diamond flourishes
    corners = [(22, 22), (W - 22, 22), (22, H - 22), (W - 22, H - 22)]
    for cx, cy in corners:
        draw.rectangle([cx - 4, cy - 4, cx + 4, cy + 4], fill=gold_color)
        draw.rectangle([cx - 2, cy - 2, cx + 2, cy + 2], fill=(255, 252, 245))

    # 5. Typography on the Right Half
    # Fonts
    font_cinzel_large = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 46)
    font_ampersand = ImageFont.truetype("C:/Windows/Fonts/georgiai.ttf", 38)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 16)
    font_details = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 19)
    font_venue = ImageFont.truetype("C:/Windows/Fonts/georgiai.ttf", 18)

    text_center_x = 835  # Center for right column
    
    # Top Kicker
    kicker = "W E D D I N G   I N V I T A T I O N"
    k_box = draw.textbbox((0, 0), kicker, font=font_sub)
    k_w = k_box[2] - k_box[0]
    draw.text((text_center_x - k_w // 2, 75), kicker, font=font_sub, fill=(166, 125, 43))
    
    # Decorative line under kicker
    line_w = 110
    draw.line([(text_center_x - line_w, 108), (text_center_x + line_w, 108)], fill=gold_color, width=1)
    draw.ellipse([text_center_x - 3, 105, text_center_x + 3, 111], fill=gold_color)

    # Sub-header: Holy Matrimony
    holy = "HOLY MATRIMONY & RECEPTION"
    h_box = draw.textbbox((0, 0), holy, font=ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 14))
    h_w = h_box[2] - h_box[0]
    draw.text((text_center_x - h_w // 2, 126), holy, font=ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 14), fill=(140, 100, 60))

    # Groom Name
    groom = "Dr Alan Anand"
    g_box = draw.textbbox((0, 0), groom, font=font_cinzel_large)
    g_w = g_box[2] - g_box[0]
    draw.text((text_center_x - g_w // 2, 170), groom, font=font_cinzel_large, fill=(58, 26, 32))

    # Ampersand with delicate styling
    amp = "&"
    a_box = draw.textbbox((0, 0), amp, font=font_ampersand)
    a_w = a_box[2] - a_box[0]
    draw.text((text_center_x - a_w // 2, 235), amp, font=font_ampersand, fill=(185, 135, 50))

    # Bride Name
    bride = "Dr Navya S. Daniel"
    b_box = draw.textbbox((0, 0), bride, font=font_cinzel_large)
    b_w = b_box[2] - b_box[0]
    draw.text((text_center_x - b_w // 2, 290), bride, font=font_cinzel_large, fill=(58, 26, 32))

    # Decorative line under names
    draw.line([(text_center_x - line_w, 365), (text_center_x + line_w, 365)], fill=gold_color, width=1)
    draw.ellipse([text_center_x - 3, 362, text_center_x + 3, 368], fill=gold_color)

    # Date
    date_text = "MONDAY, 19TH OCTOBER 2026"
    d_box = draw.textbbox((0, 0), date_text, font=font_details)
    d_w = d_box[2] - d_box[0]
    draw.text((text_center_x - d_w // 2, 388), date_text, font=font_details, fill=(90, 55, 35))

    # Church / Venue
    venue_text = "Mateer Memorial Church, Trivandrum"
    v_box = draw.textbbox((0, 0), venue_text, font=font_venue)
    v_w = v_box[2] - v_box[0]
    draw.text((text_center_x - v_w // 2, 424), venue_text, font=font_venue, fill=(120, 90, 70))

    # Website link / invitation pill at bottom
    pill_text = "alan-weds-navya.invitingyou.top"
    pill_font = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 14)
    p_box = draw.textbbox((0, 0), pill_text, font=pill_font)
    p_w = p_box[2] - p_box[0]
    
    pill_padding = 18
    pill_x1 = text_center_x - (p_w // 2) - pill_padding
    pill_x2 = text_center_x + (p_w // 2) + pill_padding
    pill_y1 = 490
    pill_y2 = 524
    draw.rounded_rectangle([pill_x1, pill_y1, pill_x2, pill_y2], radius=17, fill=(245, 237, 222), outline=gold_color, width=1)
    draw.text((text_center_x - p_w // 2, 498), pill_text, font=pill_font, fill=(130, 90, 50))

    # Save high-quality optimized JPEG (< 200KB)
    output_path = "images/og-image.jpg"
    img.save(output_path, "JPEG", quality=92, optimize=True)
    
    # Also save to root as fallback
    img.save("og-image.jpg", "JPEG", quality=92, optimize=True)
    print(f"Created {output_path} and og-image.jpg successfully!")

if __name__ == "__main__":
    create_og_image()
