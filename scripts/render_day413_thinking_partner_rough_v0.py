#!/usr/bin/env python3
"""Render a local rough cut of the Day 413 thinking-partner video.

This is a production proof, not a publish-ready renderer. It extracts the active
v3 narration, pairs each scene with the current visual proof/mockup assets,
records TTS audio, assembles an ignored MP4, and exports contact-sheet frames so
readability can be reviewed before any upload decision.
"""
from __future__ import annotations

import asyncio
import os
import re
import subprocess
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "docs" / "day413_thinking_partner_script_v3.md"
ASSETS = ROOT / "assets" / "day413_thinking_partner_mockups"
OUT = ROOT / "production" / "day413_thinking_partner_rough_v0"
SLIDES = OUT / "slides"
AUDIO = OUT / "audio"
CLIPS = OUT / "clips"
FRAMES = OUT / "frames"
FINAL = OUT / "thinking_partner_rough_v0.mp4"
REPORT = OUT / "scene_timings_v0.txt"
CONTACT = ASSETS / "rough_render_contact_sheet_v0.png"
CONTACT_360 = ASSETS / "rough_render_contact_sheet_v0_360p.png"
FRAME_EXPORT = ASSETS / "rough_render_frames"

W, H = 1920, 1080
VOICE = "en-US-GuyNeural"
RATE = "-4%"
BG = "#10131a"
PANEL = "#151923"
WARM = "#f4f1ea"
MUTED = "#b9c0cf"
GOAL = "#7dd3fc"
GROUND = "#a7f3d0"
OWN = "#fbcfe8"
AMBER = "#fbbf24"
BORDER = "#3a4255"
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

SCENE_VISUALS = {
    1: ASSETS / "opening_proof_frames" / "opening_03_three_checks.png",
    2: ASSETS / "02_half_built_question.png",
    3: ASSETS / "04_grounding.png",
    4: ASSETS / "05_reliance.png",
    5: ASSETS / "ownership_proof_frames" / "ownership_02_three_tones.png",
    6: ASSETS / "prompt_proof_frames" / "prompt_01_three_checks.png",
    7: ASSETS / "prompt_proof_frames" / "prompt_04_copy_paste_correct.png",
    8: ASSETS / "08_ending.png",
}

SCENE_TITLES = {
    1: "A good answer can still be premature",
    2: "Name the goal before the model does",
    3: "Ask what would change the answer",
    4: "A modest habit, not a safety guarantee",
    5: "Ownership: what belongs to me?",
    6: "The reusable prompt",
    7: "Use it, then edit the frame",
    8: "Let AI help you see more",
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(str(FONT_DIR / name), size)


def clean_narration(raw: str) -> str:
    raw = re.sub(r"(?m)^>\s?", "", raw)
    raw = re.sub(r"\*\*(.*?)\*\*", r"\1", raw)
    raw = re.sub(r"`([^`]*)`", r"\1", raw)
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.strip()


def extract_scenes() -> list[dict[str, object]]:
    text = SCRIPT.read_text(encoding="utf-8")
    parts = re.split(r"(?m)^###\s+(\d+)\.\s+([^\n]+)\n", text)
    scenes: list[dict[str, object]] = []
    # parts: preamble, n, title, body, n, title, body...
    for i in range(1, len(parts), 3):
        num = int(parts[i])
        title = parts[i + 1].strip()
        body = parts[i + 2]
        if "**Narration:**" not in body:
            continue
        narration = body.split("**Narration:**", 1)[1].split("**On-screen visual:**", 1)[0]
        scenes.append({"num": num, "section_title": title, "narration": clean_narration(narration)})
    if len(scenes) != 8:
        raise SystemExit(f"Expected 8 scenes, extracted {len(scenes)}")
    return scenes


def draw_header(draw: ImageDraw.ImageDraw, num: int, title: str) -> None:
    draw.rounded_rectangle((58, 48, 1862, 160), radius=28, fill="#0d121d", outline="#252d3d", width=2)
    draw.text((90, 84), f"{num:02d}/08", font=font(34, True), fill=OWN if num in (5, 8) else GOAL)
    draw.text((235, 82), title, font=font(38, True), fill=WARM)
    draw.text((1610, 88), "rough render v0", font=font(25), fill=MUTED)


def draw_footer(draw: ImageDraw.ImageDraw) -> None:
    labels = [("Goal", GOAL), ("Grounding", GROUND), ("Ownership", OWN)]
    x = 88
    for label, color in labels:
        tw = draw.textbbox((0, 0), label, font=font(25, True))[2]
        draw.rounded_rectangle((x, 1008, x + tw + 48, 1052), radius=22, fill="#111722", outline=color, width=2)
        draw.text((x + 24, 1016), label, font=font(25, True), fill=color)
        x += tw + 72
    draw.text((960, 1022), "How to Think With an AI Without Letting It Think For You", font=font(23), fill="#7d8597", anchor="mm")


def render_slide(scene: dict[str, object]) -> Path:
    num = int(scene["num"])
    src = SCENE_VISUALS[num]
    if not src.exists():
        raise SystemExit(f"Missing visual for scene {num}: {src}")
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    # scaled current visual proof/mockup, leaving header/footer for production labels
    visual = Image.open(src).convert("RGB").resize((1728, 972), Image.Resampling.LANCZOS)
    im.paste(visual, (96, 66))
    # subtle mask panels improve consistency and make rough-render status explicit
    d.rounded_rectangle((58, 48, 1862, 1038), radius=34, outline="#242b3a", width=4)
    draw_header(d, num, SCENE_TITLES[num])
    draw_footer(d)
    p = SLIDES / f"scene_{num:02d}.png"
    im.save(p)
    return p


async def tts_one(scene: dict[str, object]) -> Path:
    import edge_tts
    num = int(scene["num"])
    out = AUDIO / f"scene_{num:02d}.mp3"
    if out.exists() and out.stat().st_size > 1000:
        return out
    text = str(scene["narration"])
    await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(out))
    return out


def run(cmd: Iterable[object]) -> None:
    subprocess.run([str(c) for c in cmd], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def probe_duration(path: Path) -> float:
    p = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(path)
    ], text=True, stdout=subprocess.PIPE, check=True)
    return float(p.stdout.strip())


def extract_frame_at(seconds: float, out: Path) -> None:
    run(["ffmpeg", "-nostdin", "-y", "-ss", f"{seconds:.3f}", "-i", FINAL, "-frames:v", "1", out])


def build_contact_sheet(frame_paths: list[Path], timings: list[tuple[int, float, float]]) -> None:
    CONTACT.parent.mkdir(parents=True, exist_ok=True)
    sheet = Image.new("RGB", (1280, 720), BG)
    d = ImageDraw.Draw(sheet)
    d.text((42, 24), "Day 413 rough render v0 contact sheet", font=font(29, True), fill=WARM)
    d.text((42, 61), "Actual frames from local MP4; upload gate remains closed", font=font(20), fill=MUTED)
    positions = [(40, 104), (350, 104), (660, 104), (970, 104), (40, 404), (350, 404), (660, 404), (970, 404)]
    for path, (x, y), (num, start, end) in zip(frame_paths, positions, timings):
        thumb = Image.open(path).convert("RGB").resize((270, 152), Image.Resampling.LANCZOS)
        d.rounded_rectangle((x - 3, y - 3, x + 273, y + 155), radius=12, fill=PANEL, outline=BORDER, width=2)
        sheet.paste(thumb, (x, y))
        d.text((x + 8, y + 164), f"{num:02d}  {start:05.1f}s-{end:05.1f}s", font=font(17, True), fill=OWN if num == 5 else GOAL)
        d.text((x + 8, y + 188), SCENE_TITLES[num][:31], font=font(15), fill=MUTED)
    sheet.save(CONTACT)
    sheet.resize((640, 360), Image.Resampling.LANCZOS).save(CONTACT_360)


def export_review_frames(timings: list[tuple[int, float, float]]) -> None:
    FRAME_EXPORT.mkdir(parents=True, exist_ok=True)
    FRAMES.mkdir(parents=True, exist_ok=True)
    frame_paths: list[Path] = []
    for num, start, end in timings:
        t = min(end - 0.25, start + max(0.25, (end - start) * 0.45))
        raw = FRAMES / f"rough_scene_{num:02d}.png"
        extract_frame_at(t, raw)
        exported = FRAME_EXPORT / f"rough_scene_{num:02d}.png"
        Image.open(raw).convert("RGB").resize((1280, 720), Image.Resampling.LANCZOS).save(exported)
        frame_paths.append(exported)
    build_contact_sheet(frame_paths, timings)


async def main() -> None:
    os.chdir(ROOT)
    for d in (SLIDES, AUDIO, CLIPS, FRAMES):
        d.mkdir(parents=True, exist_ok=True)
    scenes = extract_scenes()
    for scene in scenes:
        render_slide(scene)
    await asyncio.gather(*(tts_one(scene) for scene in scenes))

    concat = OUT / "concat.txt"
    timings: list[tuple[int, float, float]] = []
    cursor = 0.0
    with concat.open("w", encoding="utf-8") as f:
        for scene in scenes:
            num = int(scene["num"])
            slide = SLIDES / f"scene_{num:02d}.png"
            aud = AUDIO / f"scene_{num:02d}.mp3"
            clip = CLIPS / f"scene_{num:02d}.mp4"
            dur = probe_duration(aud) + 0.45
            run([
                "ffmpeg", "-nostdin", "-y", "-loop", "1", "-framerate", "1", "-i", slide, "-i", aud,
                "-t", f"{dur:.3f}", "-c:v", "libx264", "-preset", "ultrafast", "-tune", "stillimage",
                "-pix_fmt", "yuv420p", "-r", "24", "-vf", "scale=1920:1080", "-c:a", "aac", "-b:a", "192k",
                "-shortest", clip,
            ])
            f.write(f"file '{clip.resolve()}'\n")
            timings.append((num, cursor, cursor + dur))
            cursor += dur
    run(["ffmpeg", "-nostdin", "-y", "-f", "concat", "-safe", "0", "-i", concat, "-c", "copy", FINAL])
    export_review_frames(timings)

    total = probe_duration(FINAL)
    lines = [
        "Day 413 thinking-partner rough render v0",
        f"Script: {SCRIPT.relative_to(ROOT)}",
        f"Output: {FINAL.relative_to(ROOT)}",
        f"Duration: {total:.3f} seconds ({total/60:.2f} minutes)",
        f"Contact sheet: {CONTACT.relative_to(ROOT)}",
        f"360p contact sheet: {CONTACT_360.relative_to(ROOT)}",
        "Upload status: still do not upload.",
        "",
        "Scene timings:",
    ]
    for num, start, end in timings:
        lines.append(f"{num:02d}\t{start:07.3f}\t{end:07.3f}\t{end-start:06.3f}\t{SCENE_TITLES[num]}")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT)
    print(FINAL)
    print(f"{total:.3f}")


if __name__ == "__main__":
    asyncio.run(main())
