#!/usr/bin/env python3
"""Generate v5 reusable-prompt visuals for the Day 413 thinking-partner video.

These replace older prompt-proof frames that used the public-facing label
"Grounding." The v5 video uses Goal / Evidence / Ownership throughout.
"""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "day413_thinking_partner_mockups" / "prompt_proof_frames"
OUT.mkdir(parents=True, exist_ok=True)

BG = "#10131a"
PANEL = "#151923"
CARD = "#1b2130"
WARM = "#f4f1ea"
MUTED = "#b9c0cf"
DIM = "#7d8597"
GOAL = "#7dd3fc"
EVIDENCE = "#a7f3d0"
OWN = "#fbcfe8"
BORDER = "#3a4255"
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(str(FONT_DIR / name), size)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    left, top, right, bottom = draw.textbbox((0, 0), text, font=fnt)
    return right - left, bottom - top


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if text_size(draw, candidate, fnt)[0] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    max_width: int,
    fill: str = WARM,
    gap: int = 8,
) -> int:
    x, y = xy
    line_height = text_size(draw, "Ag", fnt)[1] + gap
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += line_height
    return y


def chip(draw: ImageDraw.ImageDraw, xy: tuple[int, int], label: str, color: str, size: int = 36) -> int:
    x, y = xy
    fnt = font(size, True)
    tw, th = text_size(draw, label, fnt)
    pad_x = 30
    pad_y = 17
    draw.rounded_rectangle(
        (x, y, x + tw + 2 * pad_x, y + th + 2 * pad_y),
        radius=22,
        fill="#111722",
        outline=color,
        width=3,
    )
    draw.text((x + pad_x, y + pad_y - 2), label, font=fnt, fill=color)
    return x + tw + 2 * pad_x


def base() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((70, 58, 1210, 646), radius=32, fill=PANEL, outline="#263044", width=2)
    draw.ellipse((930, 70, 1120, 260), fill="#172637", outline="#234a61", width=3)
    draw.arc((110, 500, 245, 635), 200, 50, fill="#463141", width=5)
    return image, draw


def save(image: Image.Image, name: str) -> Path:
    path = OUT / name
    image.save(path)
    image.resize((640, 360), Image.Resampling.LANCZOS).save(OUT / f"{path.stem}_360p.png")
    return path


def draw_number(draw: ImageDraw.ImageDraw, center: tuple[int, int], number: str, color: str) -> None:
    cx, cy = center
    draw.ellipse((cx - 25, cy - 25, cx + 25, cy + 25), fill=color)
    draw.text((cx, cy - 2), number, font=font(30, True), fill=BG, anchor="mm")


def prompt_three_checks() -> Path:
    image, draw = base()
    draw.text((130, 120), "Before answering...", font=font(50, True), fill=WARM)
    draw.text((130, 178), "help me keep ownership of this decision", font=font(31), fill=MUTED)

    items = [
        ("1", "Restate the goal you think I am pursuing.", GOAL),
        ("2", "List facts or evidence that would change your answer.", EVIDENCE),
        ("3", "Identify what depends on my values or risk tolerance.", OWN),
    ]
    y = 300
    for num, text, color in items:
        draw_number(draw, (165, y + 14), num, color)
        draw_wrapped(draw, (215, y - 7), text, font(35), 915, fill=WARM, gap=7)
        y += 82
    return save(image, "prompt_01_three_checks_v5.png")


def copy_paste_correct() -> Path:
    image, draw = base()
    draw.text((130, 125), "Copy. Paste. Correct. Then decide.", font=font(47, True), fill=WARM)

    x = 165
    y = 315
    for label, color in (("GOAL", GOAL), ("EVIDENCE", EVIDENCE), ("OWNERSHIP", OWN)):
        x = chip(draw, (x, y), label, color, size=34) + 44

    draw.text(
        (640, 548),
        "Use AI for options and tradeoffs. Keep the judgment with you.",
        font=font(29),
        fill=WARM,
        anchor="mm",
    )
    draw.text((640, 604), "Goal / Evidence / Ownership", font=font(22, True), fill=DIM, anchor="mm")
    return save(image, "prompt_04_copy_paste_correct_v5.png")


def main() -> None:
    paths = [prompt_three_checks(), copy_paste_correct()]
    for path in paths:
        print(path.relative_to(ROOT))
        print((path.with_name(f"{path.stem}_360p.png")).relative_to(ROOT))


if __name__ == "__main__":
    main()
