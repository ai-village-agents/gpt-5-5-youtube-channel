#!/usr/bin/env python3
"""Make static overlay QA images for the fastest hybrid green-checkmarks captions.

This is a visual layout aid only. It is not an in-motion caption review.
"""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
MP4 = ROOT / "production/day414_green_checkmarks_rough_v4/green_checkmarks_rough_v4.mp4"
VTT = ROOT / "docs/day414_caption_drafts/green_checkmarks_rough_v4_hybrid_punctuated.vtt"
OUTDIR = ROOT / "assets/day414_green_checkmarks_mockups"
OUT = OUTDIR / "green_checkmarks_v4_hybrid_caption_overlay_fastest_contact_sheet.png"
THUMB_W = 640
THUMB_H = 360
COLS = 2
ROWS = 5
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def parse_time(s: str) -> float:
    h, m, rest = s.split(":")
    sec, ms = rest.split(".")
    return int(h)*3600 + int(m)*60 + int(sec) + int(ms)/1000


def parse_vtt() -> list[tuple[int, float, float, str]]:
    blocks = VTT.read_text(encoding="utf-8").strip().split("\n\n")[1:]
    cues = []
    for idx, block in enumerate(blocks, 1):
        lines = block.splitlines()
        if not lines or "-->" not in lines[0]:
            continue
        a, b = [x.strip() for x in lines[0].split("-->")]
        text = "\n".join(lines[1:])
        cues.append((idx, parse_time(a), parse_time(b), text))
    return cues


def cue_cps(cue: tuple[int, float, float, str]) -> float:
    _, a, b, text = cue
    return len(text.replace("\n", " ")) / (b-a)


def extract_frame(t: float, path: Path) -> Image.Image:
    subprocess.run([
        "ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", "-ss", f"{t:.3f}",
        "-i", str(MP4), "-frames:v", "1", "-q:v", "2", str(path)
    ], check=True)
    return Image.open(path).convert("RGB").resize((THUMB_W, THUMB_H), Image.LANCZOS)


def draw_caption(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int, int, int]:
    lines = text.split("\n")
    pad_x, pad_y = 14, 10
    line_heights = []
    max_w = 0
    for line in lines:
        box = draw.textbbox((0,0), line, font=font)
        max_w = max(max_w, box[2]-box[0])
        line_heights.append(box[3]-box[1])
    leading = 8
    text_h = sum(line_heights) + leading*(len(lines)-1)
    box_w = max_w + pad_x*2
    box_h = text_h + pad_y*2
    x = (THUMB_W - box_w)//2
    y = THUMB_H - box_h - 22
    return x, y, x+box_w, y+box_h


def overlay_caption(img: Image.Image, cue: tuple[int,float,float,str]) -> Image.Image:
    idx, a, b, text = cue
    img = img.copy().convert("RGBA")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, 22)
    meta_font = ImageFont.truetype(FONT_BOLD, 16)
    x1, y1, x2, y2 = draw_caption(draw, text, font)
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    od = ImageDraw.Draw(overlay)
    od.rounded_rectangle((x1,y1,x2,y2), radius=10, fill=(0,0,0,205), outline=(255,255,255,120), width=1)
    y = y1 + 10
    for line in text.split("\n"):
        box = draw.textbbox((0,0), line, font=font)
        tx = (THUMB_W - (box[2]-box[0]))//2
        od.text((tx,y), line, font=font, fill=(255,255,255,255))
        y += (box[3]-box[1]) + 8
    label = f"cue {idx:03d}  {a:.3f}-{b:.3f}s  cps={cue_cps(cue):.2f}"
    od.rectangle((0,0,THUMB_W,30), fill=(12,15,22,235))
    od.text((10,6), label, font=meta_font, fill=(244,241,234,255))
    return Image.alpha_composite(img, overlay).convert("RGB")


def main() -> None:
    if not MP4.exists():
        raise SystemExit(f"Missing rough render: {MP4}")
    OUTDIR.mkdir(parents=True, exist_ok=True)
    cues = sorted(parse_vtt(), key=cue_cps, reverse=True)[:ROWS*COLS]
    sheet = Image.new("RGB", (COLS*THUMB_W, ROWS*THUMB_H), (16,19,26))
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        for n, cue in enumerate(cues):
            idx, a, b, _ = cue
            frame = extract_frame((a+b)/2, tmp / f"frame_{idx:03d}.jpg")
            panel = overlay_caption(frame, cue)
            x = (n % COLS) * THUMB_W
            y = (n // COLS) * THUMB_H
            sheet.paste(panel, (x,y))
    sheet.save(OUT)
    print(OUT)
    for cue in cues:
        idx,a,b,text=cue
        print(f"{idx:03d} {a:.3f}-{b:.3f} cps={cue_cps(cue):.2f} text={text.replace(chr(10),' / ')}")

if __name__ == "__main__":
    main()
