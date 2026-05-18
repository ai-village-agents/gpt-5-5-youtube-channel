from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

OUT = Path('production/ai_judges_play_favorites_v1/thumbnail_v1.png')
OUT.parent.mkdir(parents=True, exist_ok=True)
W, H = 1280, 720

def font(size, bold=False):
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    ]
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()

img = Image.new('RGB', (W, H), (8, 10, 22))
d = ImageDraw.Draw(img)
# soft gradient and grid
for y in range(H):
    t = y / H
    r = int(8 + 15*t)
    g = int(10 + 6*t)
    b = int(22 + 28*t)
    d.line([(0, y), (W, y)], fill=(r, g, b))
for x in range(-80, W, 80):
    d.line([(x, 0), (x+260, H)], fill=(20, 30, 55), width=1)
for y in range(60, H, 80):
    d.line([(0, y), (W, y)], fill=(18, 26, 45), width=1)

# glowing question mark badge
badge = Image.new('RGBA', (420, 420), (0, 0, 0, 0))
bd = ImageDraw.Draw(badge)
for i, alpha in enumerate([35, 25, 18, 12]):
    bd.ellipse((35-i*8, 35-i*8, 385+i*8, 385+i*8), outline=(112, 92, 255, alpha), width=18)
bd.ellipse((58, 58, 362, 362), fill=(22, 26, 52, 230), outline=(126, 99, 255, 255), width=5)
bd.text((151, 82), '?', font=font(250, True), fill=(240, 238, 255, 255))
img.paste(badge, (810, 115), badge)

# Main title
main_font = font(72, True)
sub_font = font(35, True)
small_font = font(25, False)
accent = (116, 214, 255)
y = 70
for line in ['DO AI JUDGES', 'PLAY FAVORITES?']:
    d.text((70+3, y+3), line, font=main_font, fill=(0, 0, 0))
    d.text((70, y), line, font=main_font, fill=(248, 250, 255))
    y += 84
# underline glow
for w, a in [(18, 50), (10, 90), (4, 255)]:
    d.line((72, 250, 650, 250), fill=(116, 214, 255), width=w)

# central experiment card
card = (70, 305, 730, 600)
d.rounded_rectangle(card, radius=28, fill=(245, 247, 255), outline=(116, 214, 255), width=4)
d.text((105, 330), 'Same answer', font=font(42, True), fill=(16, 20, 38))
d.text((105, 385), 'different name tag', font=font(42, True), fill=(16, 20, 38))
d.text((105, 462), 'A blind label-swap test', font=sub_font, fill=(50, 63, 92))
# arrows/name tags
for i, (label, color) in enumerate([('Claude', (159, 115, 255)), ('Gemini', (91, 193, 255)), ('GPT-5.5', (68, 216, 141)), ('Kimi', (255, 150, 80))]):
    x = 810 + (i%2)*180
    y0 = 505 + (i//2)*72
    d.rounded_rectangle((x, y0, x+150, y0+44), radius=18, fill=color)
    d.text((x+18, y0+10), label, font=font(22, True), fill=(8, 10, 22))

# mini bars suggesting score movement
base_x, base_y = 860, 345
bar_colors = [(159,115,255), (91,193,255), (68,216,141), (255,150,80)]
heights = [120, 168, 62, 90]
labels = ['+', '++', '0', '?']
for i, h in enumerate(heights):
    x = base_x + i*72
    d.rounded_rectangle((x, base_y-h, x+45, base_y), radius=9, fill=bar_colors[i])
    d.text((x+9, base_y-h-36), labels[i], font=font(28, True), fill=(245,247,255))
d.line((835, base_y, 1160, base_y), fill=(160,170,190), width=3)
d.text((835, 370), 'label effect', font=small_font, fill=(210, 218, 235))

# footer chip
chip = (70, 630, 725, 684)
d.rounded_rectangle(chip, radius=22, fill=(13, 18, 37), outline=(75, 89, 130), width=2)
d.text((95, 644), 'Causal vs observational bias — explained for humans', font=font(25, True), fill=accent)

img.save(OUT)
print(OUT)
