#!/usr/bin/env python3
"""Generate additional v1 visual pacing frames for the green-checkmarks rough.

These frames split the long final checklist beat into three phone-readable
static visuals. They are production aids only, not upload approval.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

ROOT = Path(__file__).resolve().parents[1]
PROOFS = ROOT / "assets" / "day414_green_checkmarks_mockups" / "visual_proofs"
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
BORDER = "#2b3445"


def font(size: int, bold: bool = False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

F_TITLE = font(62, True)
F_MED = font(42, True)
F_BODY = font(36)
F_SMALL = font(28)
F_TINY = font(24)


def rounded(draw, xy, radius=28, fill=PANEL, outline=BORDER, width=3):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_wrapped(draw, xy, text, fnt, fill=TEXT, width_chars=42, spacing=10):
    x, y = xy
    for line in textwrap.wrap(text, width=width_chars):
        draw.text((x, y), line, font=fnt, fill=fill)
        box = draw.textbbox((x, y), line, font=fnt)
        y += (box[3] - box[1]) + spacing
    return y


def centered(draw, xy, text, fnt, fill=TEXT, spacing=8):
    x1, y1, x2, y2 = xy
    lines = text.split("\n")
    sizes = [draw.textbbox((0, 0), line, font=fnt) for line in lines]
    widths = [b[2] - b[0] for b in sizes]
    heights = [b[3] - b[1] for b in sizes]
    total_h = sum(heights) + spacing * (len(lines) - 1)
    y = y1 + (y2 - y1 - total_h) / 2
    for line, w, h in zip(lines, widths, heights):
        draw.text((x1 + (x2 - x1 - w) / 2, y), line, font=fnt, fill=fill)
        y += h + spacing


def footer(draw, active=None):
    items = [("Fresh base", BLUE), ("Right diff", AMBER), ("Uncovered risk", PINK)]
    x = 64
    for label, color in items:
        w = 260 if label != "Uncovered risk" else 330
        rounded(draw, (x, 990, x+w, 1045), radius=24, fill="#0f1722", outline=color, width=2)
        draw.text((x+24, 1003), label, font=F_TINY, fill=color if active == label else TEXT)
        x += w + 24


def base(title: str, scene: str):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    rounded(d, (60, 52, 1860, 160), radius=28, fill="#0b111c", outline="#233044", width=2)
    d.text((92, 86), scene, font=F_SMALL, fill=PINK)
    d.text((250, 78), title, font=F_MED, fill=TEXT)
    d.text((1580, 92), "rough v1 visual", font=F_TINY, fill=MUTED)
    return img, d


def save(img, name: str) -> Path:
    path = PROOFS / name
    img.save(path)
    img.resize((640, 360), Image.Resampling.LANCZOS).save(PROOFS / name.replace(".png", "_360p.png"))
    return path


def frame07a():
    img, d = base("Review checklist", "07a/09")
    cards = [
        (170, 260, 610, 790, "Fresh base", "Did it run against the target I am about to merge or deploy into?", BLUE),
        (740, 260, 1180, 790, "Right diff", "Did it inspect the exact change that will land?", AMBER),
        (1310, 260, 1750, 790, "Uncovered risk", "What important failure could still happen even if this check result is correct?", PINK),
    ]
    for x1, y1, x2, y2, title, body, color in cards:
        rounded(d, (x1, y1, x2, y2), radius=34, fill=PANEL, outline=color, width=4)
        centered(d, (x1+25, y1+55, x2-25, y1+150), title, F_MED, fill=color)
        draw_wrapped(d, (x1+45, y1+230), body, F_BODY, fill=TEXT, width_chars=19, spacing=12)
    centered(d, (310, 850, 1610, 925), "A green check is evidence. These questions say what kind.", F_BODY, fill=MUTED)
    footer(d)
    return save(img, "green_07a_review_checklist.png")


def frame07b():
    img, d = base("Ask the AI before trusting the check", "07b/09")
    questions = [
        ("1", "What version, base branch, and diff did this check run on?", BLUE),
        ("2", "What files, behaviors, or risks did it not inspect?", AMBER),
        ("3", "What human decision remains even if the check result is correct?", PINK),
    ]
    y = 235
    for num, q, color in questions:
        rounded(d, (250, y, 1670, y+185), radius=30, fill=PANEL2, outline=color, width=3)
        rounded(d, (295, y+42, 375, y+122), radius=40, fill="#0f1722", outline=color, width=3)
        centered(d, (295, y+42, 375, y+122), num, F_MED, fill=color)
        draw_wrapped(d, (435, y+48), q, F_BODY, fill=TEXT, width_chars=54, spacing=12)
        y += 220
    rounded(d, (420, 885, 1500, 955), radius=28, fill="#10201a", outline=GREEN, width=3)
    centered(d, (450, 888, 1470, 952), "Slow the moment down before the result becomes approval.", F_SMALL, fill=GREEN)
    footer(d)
    return save(img, "green_07b_ai_prompt.png")


def frame07c():
    img, d = base("Receipt, not verdict", "07c/09")
    rounded(d, (240, 235, 1680, 825), radius=38, fill=PANEL, outline=GREEN, width=4)
    d.text((330, 320), "Keep the green check.", font=F_TITLE, fill=GREEN)
    d.text((330, 440), "It is useful.", font=F_MED, fill=TEXT)
    d.text((330, 560), "Just read it like a receipt.", font=F_TITLE, fill=TEXT)
    rounded(d, (330, 705, 1590, 790), radius=28, fill="#10201a", outline=GREEN, width=3)
    centered(d, (355, 710, 1565, 785), "Let it speed up the review. Do not let it replace the question.", F_SMALL, fill=GREEN)
    footer(d)
    return save(img, "green_07c_receipt_close.png")


def main() -> None:
    paths = [frame07a(), frame07b(), frame07c()]
    for path in paths:
        print(path)
        print(path.with_name(path.stem + "_360p" + path.suffix))


if __name__ == "__main__":
    main()
