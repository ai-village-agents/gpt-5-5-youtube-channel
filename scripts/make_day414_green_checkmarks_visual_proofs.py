from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "day414_green_checkmarks_mockups"
PROOFS = OUT / "visual_proofs"
PROOFS.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
BG = "#10131a"
PANEL = "#151923"
PANEL2 = "#111827"
TEXT = "#f4f1ea"
MUTED = "#b9c0cf"
GREEN = "#86efac"
BLUE = "#7dd3fc"
AMBER = "#fbbf24"
PINK = "#fbcfe8"
ORANGE = "#f59e0b"
BORDER = "#2b3445"


def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

F_TITLE = font(68, True)
F_BIG = font(56, True)
F_MED = font(42, True)
F_BODY = font(34)
F_SMALL = font(28)
F_TINY = font(24)


def rounded(draw, xy, radius=28, fill=PANEL, outline=BORDER, width=3):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def centered(draw, xy, text, fnt, fill=TEXT, spacing=8):
    x1, y1, x2, y2 = xy
    lines = text.split("\n")
    heights = []
    widths = []
    for line in lines:
        box = draw.textbbox((0,0), line, font=fnt)
        widths.append(box[2]-box[0])
        heights.append(box[3]-box[1])
    total = sum(heights) + spacing*(len(lines)-1)
    y = y1 + (y2-y1-total)/2
    for line, h, w in zip(lines, heights, widths):
        draw.text((x1+(x2-x1-w)/2, y), line, font=fnt, fill=fill)
        y += h + spacing


def draw_check(draw, cx, cy, scale=1.0, fill=GREEN, width=26):
    pts = [
        (cx-95*scale, cy+5*scale),
        (cx-35*scale, cy+65*scale),
        (cx+105*scale, cy-80*scale),
    ]
    draw.line(pts, fill=fill, width=int(width*scale), joint="curve")


def footer(draw, active=None):
    items = [("Fresh base", BLUE), ("Right diff", AMBER), ("Uncovered risk", PINK)]
    x = 64
    for label, color in items:
        w = 260 if label != "Uncovered risk" else 330
        rounded(draw, (x, 990, x+w, 1045), radius=24, fill="#0f1722", outline=color, width=2)
        draw.text((x+24, 1003), label, font=F_TINY, fill=color if active == label else TEXT)
        x += w + 24


def base(title=None, scene=None):
    img = Image.new("RGB", (W,H), BG)
    d = ImageDraw.Draw(img)
    rounded(d, (60, 52, 1860, 160), radius=28, fill="#0b111c", outline="#233044", width=2)
    if scene:
        d.text((92, 86), scene, font=F_SMALL, fill=PINK)
    if title:
        d.text((210 if scene else 92, 78), title, font=F_MED, fill=TEXT)
    d.text((1600, 92), "visual proof v0", font=F_TINY, fill=MUTED)
    return img, d


def save(img, name):
    path = PROOFS / name
    img.save(path)
    small = img.resize((640,360), Image.Resampling.LANCZOS)
    small.save(PROOFS / name.replace(".png", "_360p.png"))
    return path


def frame01():
    img, d = base("A green check is a receipt, not a verdict", "01/07")
    rounded(d, (180, 230, 850, 820), radius=36, fill=PANEL)
    draw_check(d, 515, 435, scale=1.7, width=28)
    centered(d, (210, 590, 820, 700), "All checks passed", F_BIG)
    rounded(d, (1040, 260, 1660, 790), radius=28, fill=PANEL2, outline=GREEN)
    d.text((1100, 320), "Receipt", font=F_BIG, fill=GREEN)
    d.text((1100, 405), "not verdict", font=F_BIG, fill=TEXT)
    for i, line in enumerate(["check: passed", "version: abc123", "conditions: specific"]):
        d.text((1100, 535+i*62), line, font=F_BODY, fill=MUTED)
    footer(d)
    return save(img, "green_01_receipt_not_verdict.png")


def frame02():
    img, d = base("Three questions keep the signal in its lane", "02/07")
    cards = [
        (180, 300, 620, 760, "Fresh base", "current target?", BLUE),
        (740, 300, 1180, 760, "Right diff", "actual change?", AMBER),
        (1300, 300, 1740, 760, "Uncovered risk", "what remains?", PINK),
    ]
    for x1,y1,x2,y2,title,sub,color in cards:
        rounded(d, (x1,y1,x2,y2), radius=34, fill=PANEL, outline=color, width=4)
        centered(d, (x1+20,y1+80,x2-20,y1+190), title, F_BIG, fill=color)
        centered(d, (x1+30,y1+245,x2-30,y2-60), sub, F_BODY, fill=TEXT)
    footer(d)
    return save(img, "green_02_three_questions.png")


def frame03():
    img, d = base("Fresh base: green on an old base is old evidence", "03/07")
    footer(d, "Fresh base")
    y = 470
    d.line((260,y,1550,y), fill=MUTED, width=6)
    d.ellipse((245,y-15,275,y+15), fill=BLUE)
    d.ellipse((1535,y-15,1565,y+15), fill=BLUE)
    d.text((210, y-80), "main at check time", font=F_BODY, fill=TEXT)
    d.text((1460, y-80), "main now", font=F_BODY, fill=TEXT)
    d.line((460,y,710,700), fill=GREEN, width=5)
    d.ellipse((695,685,725,715), fill=GREEN)
    d.text((650, 730), "PR checked", font=F_BODY, fill=GREEN)
    rounded(d, (1180, 610, 1660, 820), radius=28, fill=PANEL2, outline=BLUE)
    centered(d, (1210, 625, 1630, 710), "144 / 610 PR heads", F_MED, fill=BLUE)
    centered(d, (1210, 715, 1630, 805), "not descendants\nof recorded base", F_SMALL, fill=MUTED)
    rounded(d, (260, 790, 840, 865), radius=22, fill="#172033", outline=ORANGE)
    centered(d, (280, 792, 820, 862), "triage signal, not failure label", F_SMALL, fill=ORANGE)
    return save(img, "green_03_fresh_base.png")


def frame04():
    img, d = base("Right diff: inspect the change that will land", "04/07")
    footer(d, "Right diff")
    rounded(d, (170, 260, 850, 790), radius=32, fill=PANEL, outline=BORDER)
    rounded(d, (1070, 260, 1750, 790), radius=32, fill=PANEL, outline=AMBER, width=4)
    d.text((230, 320), "preview I remember", font=F_MED, fill=MUTED)
    d.text((1130, 320), "current diff", font=F_MED, fill=AMBER)
    for i in range(5):
        y=430+i*58
        d.rectangle((250,y,780,y+34), fill="#202838")
        d.rectangle((1150,y,1680,y+34), fill="#202838")
    d.text((310, 560), "+ add at end", font=F_BODY, fill=GREEN)
    d.text((1210, 500), "+ inserted before tail", font=F_BODY, fill=GREEN)
    d.text((1210, 680), "already-merged tail", font=F_SMALL, fill=PINK)
    d.line((850, 525, 1070, 525), fill=AMBER, width=8)
    d.polygon([(1070,525),(1025,500),(1025,550)], fill=AMBER)
    rounded(d, (700, 830, 1220, 900), radius=22, fill="#172033", outline=AMBER)
    centered(d, (720, 835, 1200, 895), "case appendix example", F_SMALL, fill=AMBER)
    return save(img, "green_04_right_diff.png")


def frame05():
    img, d = base("Uncovered risk: what remains if the robot is right?", "05/07")
    footer(d, "Uncovered risk")
    rounded(d, (220, 250, 1700, 830), radius=32, fill=PANEL)
    d.text((310, 320), "Checked", font=F_MED, fill=GREEN)
    d.text((980, 320), "Still ask", font=F_MED, fill=PINK)
    rows = [
        ("build passed", "recent work removed?"),
        ("tests passed", "source shape preserved?"),
        ("mergeable", "user impact changed?"),
    ]
    for i,(left,right) in enumerate(rows):
        y=430+i*115
        draw_check(d, 335, y+12, scale=.35, width=22)
        d.text((390, y-10), left, font=F_BODY, fill=TEXT)
        d.text((990, y-10), "?", font=F_MED, fill=PINK)
        d.text((1050, y-10), right, font=F_BODY, fill=TEXT)
        d.line((300, y+70, 1620, y+70), fill="#263044", width=2)
    centered(d, (360, 760, 1560, 820), "What would still worry me if the robot is right?", F_BODY, fill=TEXT)
    return save(img, "green_05_uncovered_risk.png")


def frame06():
    img, d = base("Signals point. Review decides.", "06/07")
    footer(d)
    chips = [
        ("stale base", "≠ unsafe by itself", BLUE),
        ("large deletion", "≠ bad by itself", AMBER),
        ("green check", "≠ enough by itself", GREEN),
    ]
    y=260
    for left,right,color in chips:
        rounded(d, (360,y,1560,y+130), radius=30, fill=PANEL, outline=color, width=3)
        d.text((430,y+38), left, font=F_MED, fill=color)
        d.text((850,y+38), right, font=F_MED, fill=TEXT)
        y+=180
    centered(d, (420, 845, 1500, 925), "Signals are not verdicts in either direction.", F_BODY, fill=MUTED)
    return save(img, "green_06_signals_not_verdicts.png")


def frame07():
    img, d = base("Final checklist", "07/07")
    items = [
        ("Fresh base", "Did it run against today's target?", BLUE),
        ("Right diff", "Did it inspect the change that will land?", AMBER),
        ("Uncovered risk", "What important failure remains possible?", PINK),
    ]
    y=235
    for title, sub, color in items:
        rounded(d, (260,y,1660,y+165), radius=30, fill=PANEL, outline=color, width=3)
        d.text((325,y+36), title, font=F_MED, fill=color)
        d.text((740,y+42), sub, font=F_BODY, fill=TEXT)
        y+=210
    rounded(d, (430, 890, 1490, 970), radius=28, fill="#10201a", outline=GREEN, width=3)
    centered(d, (450, 895, 1470, 965), "Let it speed up the review. Do not let it replace the question.", F_SMALL, fill=GREEN)
    footer(d)
    return save(img, "green_07_final_checklist.png")


paths = [frame01(), frame02(), frame03(), frame04(), frame05(), frame06(), frame07()]

# Contact sheet
thumbs = [Image.open(p).resize((480,270), Image.Resampling.LANCZOS) for p in paths]
sheet = Image.new("RGB", (1440, 840), BG)
d = ImageDraw.Draw(sheet)
d.text((40, 28), "Green checkmarks visual proof contact sheet v0", font=font(36, True), fill=TEXT)
for idx, im in enumerate(thumbs):
    x = 40 + (idx % 3) * 470
    y = 100 + (idx // 3) * 330
    sheet.paste(im, (x,y))
    d.rectangle((x,y,x+480,y+270), outline=BORDER, width=2)
    d.text((x+8,y+278), paths[idx].name, font=font(18), fill=MUTED)
sheet.save(OUT / "green_checkmarks_contact_sheet_v0.png")
print(f"wrote {len(paths)} frames to {PROOFS}")
print(OUT / "green_checkmarks_contact_sheet_v0.png")
