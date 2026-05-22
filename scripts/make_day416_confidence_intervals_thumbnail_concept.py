#!/usr/bin/env python3
"""Generate local thumbnail concept images for the confidence-interval future video.

This creates non-live mockups only. It does not upload or publish anything.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("assets/day416_confidence_intervals_mockups")
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
BG = "#10131a"
GRID = "#1c2433"
PANEL = "#151923"
TEXT = "#f4f1ea"
MUTED = "#b9c0cf"
GREEN = "#86efac"
BLUE = "#7dd3fc"
AMBER = "#fbbf24"
BORDER = "#2b3445"

FONT_DIRS = [Path("/usr/share/fonts/truetype/dejavu"), Path("/usr/share/fonts/truetype/liberation2")]

def font(name, size, bold=False):
    candidates = []
    if bold:
        candidates += ["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf"]
    candidates += ["DejaVuSans.ttf", "LiberationSans-Regular.ttf"]
    for d in FONT_DIRS:
        for c in candidates:
            p = d / c
            if p.exists():
                return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()

F_NUM = font("sans", 150, True)
F_HEAD = font("sans", 82, True)
F_TAG = font("sans", 42, True)
F_LABEL = font("sans", 30, True)
F_SMALL = font("sans", 25, False)
F_CHIP = font("sans", 28, True)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# subtle diagonal grid
for x in range(-W, W * 2, 64):
    d.line([(x, 0), (x - 420, H)], fill=GRID, width=1)
for x in range(0, W * 2, 96):
    d.line([(x, 0), (x + 360, H)], fill="#151c29", width=1)

# left text block
left_x = 70
d.text((left_x, 92), "+0.29", font=F_NUM, fill=GREEN)
d.text((left_x, 252), "ISN'T", font=F_HEAD, fill=TEXT)
d.text((left_x, 342), "ENOUGH", font=F_HEAD, fill=TEXT)
d.line((left_x, 448, 510, 448), fill=GREEN, width=6)

# supporting chip
chip = (70, 590, 545, 650)
d.rounded_rectangle(chip, radius=18, fill="#111827", outline=BORDER, width=3)
d.text((95, 606), "AI evaluation • one study • one slice", font=F_SMALL, fill=MUTED)

# right panel
panel = (610, 105, 1210, 590)
d.rounded_rectangle(panel, radius=28, fill=PANEL, outline=BORDER, width=3)
d.text((650, 145), "READ THE RANGE", font=F_TAG, fill=TEXT)

# axis mapping for interval rail
axis_left, axis_right = 690, 1135
axis_y = 355
vmin, vmax = -0.05, 0.55

def sx(v):
    return axis_left + (v - vmin) / (vmax - vmin) * (axis_right - axis_left)

# zero line
x0 = sx(0.0)
d.line((x0, 250, x0, 470), fill=TEXT, width=3)
d.text((x0 - 35, 480), "zero", font=F_SMALL, fill=MUTED)

# interval rail and endpoints
lo, mid, hi = 0.14, 0.29, 0.45
xlo, xmid, xhi = sx(lo), sx(mid), sx(hi)
d.line((xlo, axis_y, xhi, axis_y), fill=BLUE, width=18)
d.ellipse((xlo - 10, axis_y - 10, xlo + 10, axis_y + 10), fill=BLUE)
d.ellipse((xhi - 10, axis_y - 10, xhi + 10, axis_y + 10), fill=BLUE)
d.ellipse((xmid - 24, axis_y - 24, xmid + 24, axis_y + 24), fill=GREEN, outline=TEXT, width=4)

# labels
for v, x in [(lo, xlo), (mid, xmid), (hi, xhi)]:
    label = f"+{v:.2f}"
    bbox = d.textbbox((0, 0), label, font=F_LABEL)
    d.text((x - (bbox[2]-bbox[0]) / 2, axis_y - 74), label, font=F_LABEL, fill=TEXT if v == mid else MUTED)

# Keep this panel sparse at thumbnail size. The endpoint labels and rail carry the
# statistical idea; extra explanatory text made the 360p version cluttered.

out = OUT / "confidence_interval_thumbnail_concept_v0.png"
img.save(out)
small = img.resize((640, 360), Image.Resampling.LANCZOS)
small.save(OUT / "confidence_interval_thumbnail_concept_v0_360p.png")
print(out)
print(OUT / "confidence_interval_thumbnail_concept_v0_360p.png")
