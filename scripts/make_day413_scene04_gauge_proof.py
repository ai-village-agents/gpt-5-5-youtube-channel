from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets/day413_thinking_partner_mockups'
OUT = ASSETS / 'scene04_gauge_proof_v2.png'
OUT360 = ASSETS / 'scene04_gauge_proof_v2_360p.png'
W, H = 1280, 720
BG = '#10131a'
PANEL = '#151923'
INK = '#f4f1ea'
MUTED = '#b9c0cf'
BLUE = '#7dd3fc'
GREEN = '#a7f3d0'
AMBER = '#fbbf24'
RED = '#fb7185'
LINE = '#283246'

def font(size, bold=False):
    names = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    ]
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            pass
    return ImageFont.load_default()

def text(draw, xy, s, fill=INK, size=32, bold=False, anchor=None, align='left'):
    draw.text(xy, s, font=font(size, bold), fill=fill, anchor=anchor, align=align)

img = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(img)

# Header
d.rounded_rectangle((72, 56, 1208, 650), radius=28, fill=PANEL, outline='#263044', width=2)
text(d, (104, 88), 'A modest habit, not a safety guarantee', size=34, bold=True)
text(d, (104, 132), 'Use the frame to keep the choice visible — not to prove the answer is safe.', fill=MUTED, size=23)

# Gauge base
cx, cy = 640, 455
r_outer = 225
r_inner = 176
start, end = 180, 360
segments = [
    (180, 238, BLUE, 'No help'),
    (238, 302, GREEN, 'Appropriate reliance'),
    (302, 360, RED, 'Blind acceptance'),
]
for a0, a1, col, _ in segments:
    d.pieslice((cx-r_outer, cy-r_outer, cx+r_outer, cy+r_outer), start=a0, end=a1, fill=col)
# Cut out inner and lower half for a clean arc
d.pieslice((cx-r_inner, cy-r_inner, cx+r_inner, cy+r_inner), start=180, end=360, fill=PANEL)
d.rectangle((cx-r_outer-5, cy, cx+r_outer+5, cy+r_outer+10), fill=PANEL)
# Arc outline
for rr in (r_outer, r_inner):
    d.arc((cx-rr, cy-rr, cx+rr, cy+rr), start=180, end=360, fill=LINE, width=3)

# Tick labels
label_y = cy + 42
text(d, (cx-r_outer+5, label_y), 'No help', fill=BLUE, size=22, bold=True, anchor='mm')
text(d, (cx, label_y), 'Appropriate\nreliance', fill=GREEN, size=21, bold=True, anchor='mm', align='center')
text(d, (cx+r_outer-5, label_y), 'Blind\nacceptance', fill=RED, size=22, bold=True, anchor='mm', align='center')

# Needle slightly left of center: the habit aims toward appropriate reliance, not certainty.
value = 0.47
angle = math.radians(180 + value * 180)
needle_len = 190
nx = cx + math.cos(angle) * needle_len
ny = cy + math.sin(angle) * needle_len
# shadow and needle
d.line((cx, cy, nx+4, ny+4), fill='#05070b', width=12)
d.line((cx, cy, nx, ny), fill=INK, width=9)
d.ellipse((cx-18, cy-18, cx+18, cy+18), fill=INK, outline='#05070b', width=3)

# Three small cards below: keep tied to existing frame.
card_w, card_h, gap = 300, 78, 28
x0 = 170
cards = [('GOAL', 'What are we trying to do?', BLUE), ('GROUNDING', 'What evidence would change it?', GREEN), ('OWNERSHIP', 'What is mine to choose?', '#fbcfe8')]
for i, (title, body, col) in enumerate(cards):
    x = x0 + i*(card_w+gap)
    d.rounded_rectangle((x, 542, x+card_w, 542+card_h), radius=14, fill='#101622', outline=col, width=2)
    text(d, (x+20, 559), title, fill=col, size=19, bold=True)
    text(d, (x+20, 588), body, fill=INK, size=18)

# Footnote
text(d, (104, 636), 'Motivated by decision-support research; not a validated intervention.', fill=AMBER, size=19)

img.save(OUT)
img.resize((640, 360), Image.Resampling.LANCZOS).save(OUT360)
print(OUT)
print(OUT360)
