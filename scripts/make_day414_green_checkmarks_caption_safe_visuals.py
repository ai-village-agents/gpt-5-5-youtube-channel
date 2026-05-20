#!/usr/bin/env python3
"""Generate caption-safe alternate visuals for green-checkmarks rough review.

These are review aids for the Day 414 green-checkmarks candidate. They do not
make the video upload-ready and do not imply caption approval.
"""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PROOFS = ROOT / "assets" / "day414_green_checkmarks_mockups" / "visual_proofs"
PROOFS.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
BG = "#10131a"
PANEL = "#151923"
TEXT = "#f4f1ea"
MUTED = "#b9c0cf"
GREEN = "#86efac"
BLUE = "#7dd3fc"
AMBER = "#fbbf24"
PINK = "#fbcfe8"
BORDER = "#2b3445"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


F_MED = font(42, True)
F_BODY = font(36)
F_SMALL = font(28)
F_TINY = font(24)


def rounded(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], radius: int = 28, fill: str = PANEL, outline: str = BORDER, width: int = 3) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def centered(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], text: str, fnt: ImageFont.ImageFont, fill: str = TEXT, spacing: int = 8) -> None:
    x1, y1, x2, y2 = xy
    lines = text.split("\n")
    boxes = [draw.textbbox((0, 0), line, font=fnt) for line in lines]
    widths = [box[2] - box[0] for box in boxes]
    heights = [box[3] - box[1] for box in boxes]
    total_h = sum(heights) + spacing * (len(lines) - 1)
    y = y1 + (y2 - y1 - total_h) / 2
    for line, width_px, height_px in zip(lines, widths, heights):
        draw.text((x1 + (x2 - x1 - width_px) / 2, y), line, font=fnt, fill=fill)
        y += height_px + spacing


def footer(draw: ImageDraw.ImageDraw) -> None:
    items = [("Fresh base", BLUE), ("Right diff", AMBER), ("Uncovered risk", PINK)]
    x = 64
    for label, color in items:
        width = 260 if label != "Uncovered risk" else 330
        rounded(draw, (x, 990, x + width, 1045), radius=24, fill="#0f1722", outline=color, width=2)
        draw.text((x + 24, 1003), label, font=F_TINY, fill=TEXT)
        x += width + 24


def frame07a_caption_safe() -> Path:
    """Generate a less text-heavy final-checklist visual for caption review.

    The v4/v1 slide repeats all three long questions on screen. When closed
    captions also show those same questions, the slide and captions compete.
    This alternate keeps the three-card conceptual structure but uses short
    hints, leaving the full sentence to the caption/narration channel.
    """
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    rounded(draw, (60, 52, 1860, 160), radius=28, fill="#0b111c", outline="#233044", width=2)
    draw.text((92, 86), "07a/09", font=F_SMALL, fill=PINK)
    draw.text((250, 78), "Review checklist", font=F_MED, fill=TEXT)
    draw.text((1580, 92), "rough v5 visual", font=F_TINY, fill=MUTED)

    cards = [
        (170, 270, 610, 760, "Fresh base", "version / base / target", BLUE),
        (740, 270, 1180, 760, "Right diff", "exact change that lands", AMBER),
        (1310, 270, 1750, 760, "Uncovered risk", "what the check did not inspect", PINK),
    ]
    for x1, y1, x2, y2, title, hint, color in cards:
        rounded(draw, (x1, y1, x2, y2), radius=34, fill=PANEL, outline=color, width=4)
        centered(draw, (x1 + 30, y1 + 70, x2 - 30, y1 + 165), title, F_MED, fill=color)
        rounded(draw, (x1 + 62, y1 + 230, x2 - 62, y1 + 322), radius=26, fill="#0f1722", outline=color, width=2)
        centered(draw, (x1 + 80, y1 + 238, x2 - 80, y1 + 314), hint, F_SMALL, fill=TEXT)
        centered(draw, (x1 + 70, y1 + 365, x2 - 70, y1 + 430), "read the captioned question", F_TINY, fill=MUTED)

    rounded(draw, (360, 835, 1560, 920), radius=30, fill="#10201a", outline=GREEN, width=3)
    centered(draw, (390, 840, 1530, 915), "Let the check speed the review — not replace it.", F_SMALL, fill=GREEN)
    footer(draw)

    path = PROOFS / "green_07a_review_checklist_caption_safe_v5.png"
    img.save(path)
    img.resize((640, 360), Image.Resampling.LANCZOS).save(path.with_name("green_07a_review_checklist_caption_safe_v5_360p.png"))
    return path


def frame07b_caption_safe() -> Path:
    """Generate a less text-heavy AI-prompt visual for caption review.

    The earlier 07b slide repeats three long prompt questions on screen. That
    competes with captions during the prompt narration. This alternate keeps
    the review structure visible but lets the caption/narration channel carry
    the exact wording.
    """
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    rounded(draw, (60, 52, 1860, 160), radius=28, fill="#0b111c", outline="#233044", width=2)
    draw.text((92, 86), "07b/09", font=F_SMALL, fill=PINK)
    draw.text((250, 78), "Ask the AI before trusting the check", font=F_MED, fill=TEXT)
    draw.text((1580, 92), "rough v6 visual", font=F_TINY, fill=MUTED)

    cards = [
        (250, 260, 1670, 410, "1", "Version / base / diff", BLUE),
        (250, 455, 1670, 605, "2", "Uninspected risks", AMBER),
        (250, 650, 1670, 800, "3", "Human decision left", PINK),
    ]
    for x1, y1, x2, y2, num, label, color in cards:
        rounded(draw, (x1, y1, x2, y2), radius=28, fill=PANEL, outline=color, width=3)
        draw.ellipse((x1 + 38, y1 + 39, x1 + 112, y1 + 113), outline=color, width=4, fill="#0f1722")
        centered(draw, (x1 + 38, y1 + 39, x1 + 112, y1 + 113), num, F_SMALL, fill=color)
        draw.text((x1 + 150, y1 + 35), label, font=F_MED, fill=TEXT)
        draw.text((x1 + 150, y1 + 92), "answer before approval", font=F_SMALL, fill=MUTED)

    rounded(draw, (340, 850, 1580, 935), radius=30, fill="#10201a", outline=GREEN, width=3)
    centered(draw, (380, 855, 1540, 930), "Ask the assistant to expose conditions — not decide the merge.", F_SMALL, fill=GREEN)
    footer(draw)

    path = PROOFS / "green_07b_ai_prompt_caption_safe_v6.png"
    img.save(path)
    img.resize((640, 360), Image.Resampling.LANCZOS).save(path.with_name("green_07b_ai_prompt_caption_safe_v6_360p.png"))
    return path


def frame07b_caption_safe_v7() -> Path:
    """Generate a prompt visual with a larger caption-safe lower band.

    V6 removed the long prompt questions, but static cue-midpoint review still
    showed caption overlap with the lower prompt card and callout strip. V7
    keeps the same three review concepts as compact top-row cards and leaves
    the lower part of the slide sparse for burned-in captions.
    """
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    rounded(draw, (60, 52, 1860, 160), radius=28, fill="#0b111c", outline="#233044", width=2)
    draw.text((92, 86), "07b/09", font=F_SMALL, fill=PINK)
    draw.text((250, 78), "Ask the AI before trusting the check", font=F_MED, fill=TEXT)
    draw.text((1580, 92), "rough v7 visual", font=F_TINY, fill=MUTED)

    cards = [
        (150, 285, 610, 590, "1", "Version / base / diff", BLUE),
        (730, 285, 1190, 590, "2", "Uninspected risks", AMBER),
        (1310, 285, 1770, 590, "3", "Human decision left", PINK),
    ]
    for x1, y1, x2, y2, num, label, color in cards:
        rounded(draw, (x1, y1, x2, y2), radius=30, fill=PANEL, outline=color, width=3)
        cx, cy = x1 + 70, y1 + 70
        draw.ellipse((cx - 36, cy - 36, cx + 36, cy + 36), outline=color, width=4, fill="#0f1722")
        centered(draw, (cx - 36, cy - 36, cx + 36, cy + 36), num, F_SMALL, fill=color)
        centered(draw, (x1 + 38, y1 + 128, x2 - 38, y1 + 190), label, F_SMALL, fill=TEXT)
        centered(draw, (x1 + 38, y1 + 202, x2 - 38, y1 + 250), "answer before approval", F_TINY, fill=MUTED)

    centered(draw, (260, 645, 1660, 700), "Captions carry the exact prompt wording.", F_SMALL, fill=MUTED)
    footer(draw)

    path = PROOFS / "green_07b_ai_prompt_caption_safe_v7.png"
    img.save(path)
    img.resize((640, 360), Image.Resampling.LANCZOS).save(path.with_name("green_07b_ai_prompt_caption_safe_v7_360p.png"))
    return path


def main() -> None:
    paths = [frame07a_caption_safe(), frame07b_caption_safe(), frame07b_caption_safe_v7()]
    for path in paths:
        print(path)
        print(path.with_name(f"{path.stem}_360p.png"))


if __name__ == "__main__":
    main()
