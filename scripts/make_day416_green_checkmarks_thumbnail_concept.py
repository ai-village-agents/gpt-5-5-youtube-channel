from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

root = Path('/home/computeruse/youtube-channel-2026')
out_dir = root / 'assets/day414_green_checkmarks_mockups'
out_dir.mkdir(parents=True, exist_ok=True)
W, H = 1280, 720
BG_TOP = (13, 16, 25)
BG_BOTTOM = (18, 23, 34)
PANEL = (19, 25, 37)
PANEL2 = (15, 23, 35)
TEXT = (248, 247, 241)
MUTED = (185, 193, 207)
GREEN = (134, 239, 172)
BLUE = (125, 211, 252)
AMBER = (251, 191, 36)
BORDER = (43, 52, 69)
RED = (248, 113, 113)

def font(size, bold=False):
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    ]
    for c in candidates:
        try:
            return ImageFont.truetype(c, size)
        except OSError:
            pass
    return ImageFont.load_default()

def shadow_text(draw, xy, text, fnt, fill, shadow=(0, 0, 0), offset=5):
    x, y = xy
    draw.text((x + offset, y + offset), text, font=fnt, fill=shadow)
    draw.text((x, y), text, font=fnt, fill=fill)

def centered_text(draw, box, text, fnt, fill, dy=0):
    x1, y1, x2, y2 = box
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((x1 + (x2 - x1 - tw) / 2, y1 + (y2 - y1 - th) / 2 + dy), text, font=fnt, fill=fill)

def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

img = Image.new('RGB', (W, H), BG_TOP)
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / (H - 1)
    fill = tuple(int(BG_TOP[i] * (1 - t) + BG_BOTTOM[i] * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=fill)

# soft diagonal grid / signal traces
for x in range(-240, W, 96):
    d.line([(x, 0), (x + 360, H)], fill=(24, 31, 48), width=1)
for y in range(72, H, 96):
    d.line([(0, y), (W, y)], fill=(23, 30, 47), width=1)

# left receipt card
rounded(d, (70, 82, 565, 610), 36, PANEL, GREEN, 4)
rounded(d, (108, 124, 527, 202), 24, (10, 20, 17), GREEN, 3)
centered_text(d, (108, 124, 527, 202), 'CHECK PASSED', font(38, True), GREEN)
# check icon
rounded(d, (134, 240, 296, 402), 30, (12, 31, 24), GREEN, 5)
d.line([(172, 323), (216, 362), (264, 281)], fill=GREEN, width=18, joint='curve')
# receipt lines
for i, (label, color) in enumerate([('version?', BLUE), ('diff?', AMBER), ('risk?', RED)]):
    y = 458 + i * 45
    rounded(d, (138, y, 238, y + 24), 10, color)
    d.text((258, y - 5), label, font=font(28, True), fill=MUTED)

# big title
shadow_text(d, (620, 84), 'GREEN CHECK', font(76, True), GREEN)
shadow_text(d, (620, 168), '≠ VERDICT', font(86, True), TEXT)
d.line((624, 286, 1180, 286), fill=GREEN, width=9)
d.line((624, 298, 1100, 298), fill=(63, 83, 73), width=3)

# subtitle chips
chip_y = 344
chips = [('fresh base', BLUE), ('right diff', AMBER), ('risk left', RED)]
x = 626
for text, color in chips:
    tw = d.textbbox((0, 0), text, font=font(29, True))[2]
    w = tw + 38
    rounded(d, (x, chip_y, x + w, chip_y + 62), 20, PANEL2, color, 3)
    d.text((x + 19, chip_y + 14), text, font=font(29, True), fill=TEXT)
    x += w + 18

# bottom question strip
rounded(d, (620, 482, 1180, 590), 30, (245, 247, 242), GREEN, 4)
d.text((650, 506), 'Read the receipt', font=font(44, True), fill=(15, 23, 35))
d.text((650, 556), 'before approval', font=font(30, True), fill=(46, 58, 76))

# series line
rounded(d, (70, 642, 1210, 686), 16, (10, 15, 26), BORDER, 2)
d.text((96, 653), 'GPT-5.5 Model • practical software review habits', font=font(24, True), fill=(206, 216, 235))

# subtle vignette
mask = Image.new('L', (W, H), 0)
md = ImageDraw.Draw(mask)
md.rectangle((0, 0, W, H), fill=30)
md.ellipse((-180, -140, W + 180, H + 160), fill=0)
mask = mask.filter(ImageFilter.GaussianBlur(35))
overlay = Image.new('RGB', (W, H), (0, 0, 0))
img = Image.composite(overlay, img, mask)

out = out_dir / 'thumbnail_concept_v0.png'
img.save(out, optimize=True)
small = img.resize((640, 360), Image.Resampling.LANCZOS)
small.save(out_dir / 'thumbnail_concept_v0_360p.png', optimize=True)
print(out.relative_to(root))
print((out_dir / 'thumbnail_concept_v0_360p.png').relative_to(root))
