#!/usr/bin/env python3
"""Generate 1280x720 concept thumbnails for the GPT-5.5 video series.

Custom thumbnail upload was gated by YouTube phone verification, but keeping
thumbnail concepts in git makes the channel package more complete and gives a
future uploader ready-to-review visual assets.
"""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
W, H = 1280, 720

VIDEOS = [
    {
        "slug": "ai_judges_play_favorites",
        "out": "videos/ai_judges_play_favorites/thumbnail/thumbnail_v1.png",
        "eyebrow": "BLIND LABEL-SWAP TEST",
        "title": ["DO AI JUDGES", "PLAY FAVORITES?"],
        "subtitle": "Same answer. Different name tag.",
        "accent": (116, 214, 255),
        "icon": "?",
        "chips": ["Claude", "Gemini", "GPT-5.5", "Kimi"],
    },
    {
        "slug": "audit_ai_judge_5_steps",
        "out": "videos/audit_ai_judge_5_steps/thumbnail/thumbnail_v0.png",
        "eyebrow": "PRACTICAL CHECKLIST",
        "title": ["AUDIT AN", "AI JUDGE"],
        "subtitle": "5 steps before you trust the score",
        "accent": (68, 216, 141),
        "icon": "5",
        "chips": ["Rubric", "Pairs", "Blind", "Compare"],
    },
    {
        "slug": "averages_hide_bias",
        "out": "videos/averages_hide_bias/thumbnail/thumbnail_v0.png",
        "eyebrow": "EVALUATION LITERACY",
        "title": ["THE AVERAGE", "CAN HIDE BIAS"],
        "subtitle": "One number. Four different stories.",
        "accent": (255, 186, 73),
        "icon": "μ",
        "chips": ["Slice", "Split", "Inspect", "Report"],
    },
    {
        "slug": "trustworthy_ai_evaluation_claims",
        "out": "videos/trustworthy_ai_evaluation_claims/thumbnail/thumbnail_v0.png",
        "eyebrow": "READ THE RECEIPTS",
        "title": ["CAN YOU TRUST", "THIS AI CLAIM?"],
        "subtitle": "Five questions for every benchmark headline",
        "accent": (159, 115, 255),
        "icon": "✓",
        "chips": ["Tested?", "Measured?", "Causal?", "Uncertain?"],
    },
    {
        "slug": "floor_raiser_effect",
        "out": "videos/floor_raiser_effect/thumbnail/thumbnail_v0.png",
        "eyebrow": "THRESHOLD BIAS",
        "title": ["BIAS THAT", "LOOKS LIKE MERCY"],
        "subtitle": "Who gets rescued at the line?",
        "accent": (255, 120, 120),
        "icon": "↗",
        "chips": ["Weak", "Borderline", "Label", "Flip"],
    },
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            pass
    return ImageFont.load_default()


def text_shadow(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill, shadow=(0, 0, 0)) -> None:
    x, y = xy
    draw.text((x + 4, y + 4), text, font=fnt, fill=shadow)
    draw.text((x, y), text, font=fnt, fill=fill)


def make_thumb(spec: dict) -> None:
    accent = spec["accent"]
    img = Image.new("RGB", (W, H), (8, 10, 22))
    d = ImageDraw.Draw(img)

    # Vertical gradient.
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=(int(8 + 10 * t), int(10 + 8 * t), int(22 + 35 * t)))

    # Subtle grid and diagonal motion lines.
    for x in range(-140, W, 90):
        d.line([(x, 0), (x + 260, H)], fill=(20, 28, 52), width=1)
    for y in range(70, H, 90):
        d.line([(0, y), (W, y)], fill=(18, 25, 47), width=1)

    # Eyebrow chip.
    d.rounded_rectangle((70, 54, 540, 104), radius=18, fill=(17, 24, 48), outline=accent, width=2)
    d.text((95, 67), spec["eyebrow"], font=font(24, True), fill=accent)

    # Big title.
    y = 138
    for line in spec["title"]:
        text_shadow(d, (70, y), line, font(76, True), (248, 250, 255))
        y += 88
    for width, alpha_color in [(18, tuple(min(255, c + 15) for c in accent)), (6, accent)]:
        d.line((72, 330, 710, 330), fill=alpha_color, width=width)

    # Subtitle card.
    d.rounded_rectangle((70, 382, 770, 492), radius=28, fill=(244, 247, 255), outline=accent, width=4)
    d.text((104, 413), spec["subtitle"], font=font(34, True), fill=(16, 20, 38))

    # Right icon badge.
    d.ellipse((830, 105, 1180, 455), fill=(22, 28, 58), outline=accent, width=7)
    bbox = d.textbbox((0, 0), spec["icon"], font=font(190, True))
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((1005 - tw / 2, 275 - th / 2 - 20), spec["icon"], font=font(190, True), fill=(248, 250, 255))

    # Mini chart bars.
    base_x, base_y = 830, 590
    for i, h in enumerate([66, 112, 44, 92]):
        x = base_x + i * 82
        color = tuple(max(0, min(255, c - i * 13)) for c in accent)
        d.rounded_rectangle((x, base_y - h, x + 46, base_y), radius=10, fill=color)
    d.line((805, base_y, 1175, base_y), fill=(160, 170, 190), width=3)

    # Bottom chips.
    x = 70
    for chip in spec["chips"]:
        w = max(118, d.textbbox((0, 0), chip, font=font(23, True))[2] + 42)
        d.rounded_rectangle((x, 585, x + w, 636), radius=18, fill=(14, 20, 40), outline=(75, 89, 130), width=2)
        d.text((x + 20, 599), chip, font=font(23, True), fill=(220, 230, 245))
        x += w + 18

    d.text((72, 660), "GPT-5.5 Model • AI Evaluation Literacy", font=font(24, True), fill=(206, 216, 235))

    out = ROOT / spec["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, optimize=True)
    print(out.relative_to(ROOT))


def main() -> None:
    for spec in VIDEOS:
        make_thumb(spec)


if __name__ == "__main__":
    main()
