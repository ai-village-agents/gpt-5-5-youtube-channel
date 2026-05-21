"""Generate v11 caption-band-clearance visual polish assets for green-checkmarks scenes 03-06.

Local visual experiment only: these PNGs support review of whether moving lower
callouts out of the caption band improves readability, with extra lower clearance in scenes 05-06. They are not upload
approval and do not make any video publish-ready.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "day414_green_checkmarks_mockups"
PROOFS = OUT / "visual_proofs"
PROOFS.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
BG = "#10131a"; PANEL = "#151923"; PANEL2 = "#111827"; TEXT = "#f4f1ea"
MUTED = "#b9c0cf"; GREEN = "#86efac"; BLUE = "#7dd3fc"; AMBER = "#fbbf24"
PINK = "#fbcfe8"; ORANGE = "#f59e0b"; BORDER = "#2b3445"


def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

F_TITLE = font(68, True); F_BIG = font(56, True); F_MED = font(42, True)
F_BODY = font(34); F_SMALL = font(28); F_TINY = font(24)


def rounded(draw, xy, radius=28, fill=PANEL, outline=BORDER, width=3):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def centered(draw, xy, text, fnt, fill=TEXT, spacing=8):
    x1, y1, x2, y2 = xy
    lines = text.split("\n")
    sizes = []
    for line in lines:
        box = draw.textbbox((0, 0), line, font=fnt)
        sizes.append((box[2] - box[0], box[3] - box[1]))
    total_h = sum(h for _, h in sizes) + spacing * (len(lines) - 1)
    y = y1 + (y2 - y1 - total_h) / 2
    for line, (w, h) in zip(lines, sizes):
        draw.text((x1 + (x2 - x1 - w) / 2, y), line, font=fnt, fill=fill)
        y += h + spacing


def draw_check(draw, cx, cy, scale=1.0, fill=GREEN, width=26):
    pts = [(cx-95*scale, cy+5*scale), (cx-35*scale, cy+65*scale), (cx+105*scale, cy-80*scale)]
    draw.line(pts, fill=fill, width=int(width*scale), joint="curve")


def footer(draw, active=None):
    items = [("Fresh base", BLUE), ("Right diff", AMBER), ("Uncovered risk", PINK)]
    x = 64
    for label, color in items:
        w = 260 if label != "Uncovered risk" else 330
        rounded(draw, (x, 990, x+w, 1045), radius=24, fill="#0f1722", outline=color, width=2)
        draw.text((x+24, 1003), label, font=F_TINY, fill=color if active == label else TEXT)
        x += w + 24


def base(title, scene):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    rounded(d, (60, 52, 1860, 160), radius=28, fill="#0b111c", outline="#233044", width=2)
    d.text((92, 86), scene, font=F_SMALL, fill=PINK)
    d.text((210, 78), title, font=F_MED, fill=TEXT)
    d.text((1600, 92), "visual proof v11", font=F_TINY, fill=MUTED)
    return img, d


def save(img, name):
    path = PROOFS / name
    img.save(path)
    img.resize((640, 360), Image.Resampling.LANCZOS).save(PROOFS / name.replace(".png", "_360p.png"))
    return path


def frame03():
    img, d = base("Fresh base: green on an old base is old evidence", "03/07")
    footer(d, "Fresh base")
    y = 455
    d.line((260, y, 1550, y), fill=MUTED, width=6)
    d.ellipse((245, y-15, 275, y+15), fill=BLUE); d.ellipse((1535, y-15, 1565, y+15), fill=BLUE)
    d.text((210, y-80), "main at check time", font=F_BODY, fill=TEXT)
    d.text((1460, y-80), "main now", font=F_BODY, fill=TEXT)
    d.line((460, y, 710, 665), fill=GREEN, width=5)
    d.ellipse((695, 650, 725, 680), fill=GREEN)
    d.text((650, 705), "PR checked", font=F_BODY, fill=GREEN)
    rounded(d, (1180, 585, 1660, 795), radius=28, fill=PANEL2, outline=BLUE)
    centered(d, (1210, 600, 1630, 685), "144 / 610 PR heads", F_MED, fill=BLUE)
    centered(d, (1210, 690, 1630, 780), "not descendants\nof recorded base", F_SMALL, fill=MUTED)
    rounded(d, (820, 585, 1135, 655), radius=22, fill="#172033", outline=ORANGE)
    centered(d, (838, 590, 1117, 650), "triage signal\nnot failure label", F_TINY, fill=ORANGE, spacing=4)
    return save(img, "green_03_fresh_base_caption_band_v11.png")


def frame04():
    img, d = base("Right diff: inspect the change that will land", "04/07")
    footer(d, "Right diff")
    rounded(d, (700, 180, 1220, 245), radius=22, fill="#172033", outline=AMBER)
    centered(d, (720, 184, 1200, 240), "case appendix example", F_SMALL, fill=AMBER)
    rounded(d, (170, 285, 850, 790), radius=32, fill=PANEL, outline=BORDER)
    rounded(d, (1070, 285, 1750, 790), radius=32, fill=PANEL, outline=AMBER, width=4)
    d.text((230, 345), "preview I remember", font=F_MED, fill=MUTED)
    d.text((1130, 345), "current diff", font=F_MED, fill=AMBER)
    for i in range(5):
        yy = 455 + i * 58
        d.rectangle((250, yy, 780, yy+34), fill="#202838")
        d.rectangle((1150, yy, 1680, yy+34), fill="#202838")
    d.text((310, 585), "+ add at end", font=F_BODY, fill=GREEN)
    d.text((1210, 525), "+ inserted before tail", font=F_BODY, fill=GREEN)
    d.text((1210, 705), "already-merged tail", font=F_SMALL, fill=PINK)
    d.line((850, 550, 1070, 550), fill=AMBER, width=8)
    d.polygon([(1070, 550), (1025, 525), (1025, 575)], fill=AMBER)
    return save(img, "green_04_right_diff_caption_band_v11.png")


def frame05():
    img, d = base("Uncovered risk: what remains if the robot is right?", "05/07")
    footer(d, "Uncovered risk")
    rounded(d, (475, 178, 1445, 238), radius=22, fill="#172033", outline=PINK)
    centered(d, (495, 182, 1425, 233), "What would still worry me if the robot is right?", F_SMALL, fill=TEXT)
    rounded(d, (220, 260, 1700, 720), radius=32, fill=PANEL)
    d.text((310, 315), "Checked", font=F_MED, fill=GREEN)
    d.text((980, 315), "Still ask", font=F_MED, fill=PINK)
    rows = [("build passed", "recent work removed?"), ("tests passed", "source shape preserved?"), ("mergeable", "user impact changed?")]
    for i, (left, right) in enumerate(rows):
        yy = 405 + i * 92
        draw_check(d, 335, yy+12, scale=.35, width=22)
        d.text((390, yy-10), left, font=F_BODY, fill=TEXT)
        d.text((990, yy-10), "?", font=F_MED, fill=PINK)
        d.text((1050, yy-10), right, font=F_BODY, fill=TEXT)
        d.line((300, yy+60, 1620, yy+60), fill="#263044", width=2)
    return save(img, "green_05_uncovered_risk_caption_band_v11.png")


def frame06():
    img, d = base("Signals point. Review decides.", "06/07")
    footer(d)
    rounded(d, (420, 180, 1500, 245), radius=22, fill="#172033", outline=MUTED)
    centered(d, (445, 184, 1475, 240), "Signals are not verdicts in either direction.", F_SMALL, fill=MUTED)
    chips = [("stale base", "≠ unsafe by itself", BLUE), ("large deletion", "≠ bad by itself", AMBER), ("green check", "≠ enough by itself", GREEN)]
    yy = 300
    for left, right, color in chips:
        rounded(d, (360, yy, 1560, yy+105), radius=28, fill=PANEL, outline=color, width=3)
        d.text((430, yy+28), left, font=F_MED, fill=color)
        d.text((850, yy+28), right, font=F_MED, fill=TEXT)
        yy += 135
    return save(img, "green_06_signals_not_verdicts_caption_band_v11.png")


def contact_sheet(paths):
    thumbs = [Image.open(p).resize((480, 270), Image.Resampling.LANCZOS) for p in paths]
    sheet = Image.new("RGB", (1000, 660), BG)
    d = ImageDraw.Draw(sheet)
    d.text((40, 28), "Green checkmarks caption-band visual polish v11 clearance", font=font(30, True), fill=TEXT)
    for idx, im in enumerate(thumbs):
        x = 40 + (idx % 2) * 480
        y = 100 + (idx // 2) * 280
        sheet.paste(im, (x, y))
        d.rectangle((x, y, x+480, y+270), outline=BORDER, width=2)
        d.text((x+8, y+248), paths[idx].name, font=font(16), fill=MUTED)
    path = OUT / "green_checkmarks_caption_band_v11_clearance_contact_sheet.png"
    sheet.save(path)
    return path


if __name__ == "__main__":
    paths = [frame03(), frame04(), frame05(), frame06()]
    paths.append(contact_sheet(paths))
    for p in paths:
        print(p)
