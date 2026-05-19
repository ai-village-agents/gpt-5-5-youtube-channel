#!/usr/bin/env python3
"""Generate Ownership/email proof frames for the Day 413 thinking-partner video."""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
OUT = Path("assets/day413_thinking_partner_mockups")
FRAME_DIR = OUT / "ownership_proof_frames"
FRAME_DIR.mkdir(parents=True, exist_ok=True)

BG = "#10131a"
BG2 = "#151923"
WARM = "#f4f1ea"
MUTED = "#b9c0cf"
DIM = "#7d8597"
GOAL = "#7dd3fc"
GROUND = "#a7f3d0"
OWN = "#fbcfe8"
AMBER = "#fbbf24"
CARD = "#1b2130"
CARD2 = "#202738"
BORDER = "#3a4255"

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
REG = FONT_DIR / "DejaVuSans.ttf"
BOLD = FONT_DIR / "DejaVuSans-Bold.ttf"
ITALIC = FONT_DIR / "DejaVuSans-Oblique.ttf"

def font(size: int, bold: bool = False, italic: bool = False) -> ImageFont.FreeTypeFont:
    if bold:
        return ImageFont.truetype(str(BOLD), size)
    if italic:
        return ImageFont.truetype(str(ITALIC), size)
    return ImageFont.truetype(str(REG), size)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def centered(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill=WARM) -> None:
    x, y = xy
    tw, th = text_size(draw, text, fnt)
    draw.text((x - tw / 2, y - th / 2), text, font=fnt, fill=fill)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt, max_w: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for word in words:
        test = word if not cur else f"{cur} {word}"
        if text_size(draw, test, fnt)[0] <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, max_w: int, fill=WARM, gap=8) -> int:
    x, y = xy
    line_h = text_size(draw, "Ag", fnt)[1] + gap
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += line_h
    return y


def base() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    # table glow and subtle geometry
    d.rounded_rectangle((70, 78, 1210, 642), radius=34, fill=BG2, outline="#242b3a", width=2)
    d.ellipse((850, 62, 1050, 262), fill="#172637", outline="#234a61", width=3)
    d.polygon([(1040, 520), (1190, 585), (1110, 650)], fill="#15372f", outline="#2a6b5c")
    d.arc((100, 470, 230, 600), 200, 50, fill="#463141", width=5)
    d.line((110, 612, 1170, 612), fill="#252d3d", width=2)
    return im, d


def card(d: ImageDraw.ImageDraw, box, title: str | None = None, accent=OWN, fill=CARD) -> None:
    d.rounded_rectangle(box, radius=24, fill=fill, outline=BORDER, width=2)
    x1, y1, x2, _ = box
    d.rounded_rectangle((x1, y1, x2, y1 + 12), radius=6, fill=accent)
    if title:
        d.text((x1 + 30, y1 + 34), title, font=font(36, True), fill=WARM)


def chip(d: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, color: str, fs=27) -> tuple[int, int]:
    x, y = xy
    f = font(fs, True)
    tw, th = text_size(d, text, f)
    pad_x, pad_y = 20, 12
    box = (x, y, x + tw + pad_x * 2, y + th + pad_y * 2)
    d.rounded_rectangle(box, radius=22, fill="#111722", outline=color, width=3)
    d.text((x + pad_x, y + pad_y - 2), text, font=f, fill=color)
    return box[2], box[3]


def save(im: Image.Image, name: str) -> Path:
    p = FRAME_DIR / name
    im.save(p)
    return p


def frame1() -> Path:
    im, d = base()
    d.text((118, 118), "Ownership check", font=font(30, True), fill=OWN)
    d.text((118, 165), "The answer sounds reasonable.", font=font(55, True), fill=WARM)
    d.text((118, 238), "But the posture is still a human choice.", font=font(31), fill=MUTED)
    card(d, (188, 326, 1092, 500), accent=OWN)
    d.text((232, 364), "Draft an email:", font=font(34, True), fill=MUTED)
    d.text((232, 414), "the timeline is slipping.", font=font(50, True), fill=WARM)
    x = 218
    for label, color in [("repair trust?", GOAL), ("set boundary?", OWN), ("get a new date?", GROUND)]:
        x, _ = chip(d, (x, 538), label, color, fs=25)
        x += 24
    return save(im, "ownership_01_email_question.png")


def tone_card(d, box, title, body, color):
    card(d, box, title=title, accent=color, fill=CARD2)
    x1, y1, x2, _ = box
    draw_wrapped(d, (x1 + 30, y1 + 104), body, font(31), x2 - x1 - 60, fill=MUTED, gap=9)


def frame2() -> Path:
    im, d = base()
    d.text((118, 110), "Same facts. Different stance.", font=font(54, True), fill=WARM)
    d.text((118, 178), "The model can show versions side by side.", font=font(31), fill=MUTED)
    tone_card(d, (118, 280, 468, 510), "Gentle", "Warmer, less boundary", GOAL)
    tone_card(d, (465, 250, 815, 540), "Direct", "Clear ask, moderate heat", OWN)
    tone_card(d, (812, 280, 1162, 510), "Firm", "Strong boundary, higher heat", AMBER)
    d.text((298, 590), "A fluent draft does not choose the relationship for you.", font=font(32, True), fill=OWN)
    return save(im, "ownership_02_three_tones.png")


def frame3() -> Path:
    im, d = base()
    d.text((118, 120), "What am I willing to stand behind?", font=font(53, True), fill=WARM)
    d.text((118, 190), "This is the Ownership step.", font=font(32), fill=MUTED)
    card(d, (145, 295, 595, 535), title="Model can show", accent=GROUND)
    draw_wrapped(d, (178, 404), "versions, tradeoffs, missing context", font(31), 385, fill=MUTED)
    card(d, (685, 295, 1135, 535), title="I choose", accent=OWN)
    draw_wrapped(d, (718, 404), "the posture, risk, and responsibility", font(31), 385, fill=MUTED)
    d.line((625, 323, 655, 507), fill=DIM, width=4)
    centered(d, (640, 590), "Options are useful. Ownership is not optional.", font(33, True), OWN)
    return save(im, "ownership_03_stand_behind.png")


def frame4() -> Path:
    im, d = base()
    d.text((118, 118), "Keep the frame visible", font=font(56, True), fill=WARM)
    d.text((118, 190), "before the advice feels settled.", font=font(32), fill=MUTED)
    x = 190
    for label, color in [("Goal", GOAL), ("Grounding", GROUND), ("Ownership", OWN)]:
        x, _ = chip(d, (x, 310), label, color, fs=38)
        x += 38
    d.rounded_rectangle((190, 458, 1090, 552), radius=24, fill="#111722", outline="#2f384b", width=2)
    centered(d, (640, 505), "Options from the model. Responsibility stays visible.", font(35, True), WARM)
    d.text((302, 592), "Use AI to think with you, not to finish the choosing for you.", font=font(29), fill=MUTED)
    return save(im, "ownership_04_keep_visible.png")


def contact_sheet(paths: list[Path]) -> None:
    sheet = Image.new("RGB", (1280, 720), BG)
    d = ImageDraw.Draw(sheet)
    d.text((42, 28), "Ownership/email proof frames", font=font(34, True), fill=WARM)
    d.text((42, 70), "360p readability target: short cards, large labels, no dense email text", font=font(23), fill=MUTED)
    thumbs = []
    for p in paths:
        im = Image.open(p).resize((560, 315), Image.Resampling.LANCZOS)
        thumbs.append((p, im))
    positions = [(60, 122), (660, 122), (60, 450), (660, 450)]
    for (p, im), (x, y) in zip(thumbs, positions):
        sheet.paste(im, (x, y))
        d.rectangle((x, y, x + 560, y + 315), outline="#3a4255", width=2)
        d.text((x + 12, y + 12), p.stem.replace("ownership_", ""), font=font(18, True), fill=OWN)
    sheet.save(OUT / "ownership_proof_contact_sheet_v0.png")
    sheet.resize((640, 360), Image.Resampling.LANCZOS).save(OUT / "ownership_proof_contact_sheet_v0_360p.png")


def main() -> None:
    paths = [frame1(), frame2(), frame3(), frame4()]
    contact_sheet(paths)
    for p in paths:
        print(p)
    print(OUT / "ownership_proof_contact_sheet_v0.png")
    print(OUT / "ownership_proof_contact_sheet_v0_360p.png")


if __name__ == "__main__":
    main()
