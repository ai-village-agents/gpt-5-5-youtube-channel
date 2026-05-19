#!/usr/bin/env python3
"""Render a local v5 rough cut of the Day 413 thinking-partner video.

This is a production proof, not a publish-ready renderer. It extracts the v5
narration, pairs each scene with updated v5 visual proofs where available,
renders Scene 05 as three actual visual sub-beats, records TTS audio, assembles
an ignored MP4, and exports contact-sheet frames for readability review before
any upload decision.
"""
from __future__ import annotations

import asyncio
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "docs" / "day413_thinking_partner_script_v5.md"
ASSETS = ROOT / "assets" / "day413_thinking_partner_mockups"
V5 = ASSETS / "v5_visual_proofs"
OUT = ROOT / "production" / "day413_thinking_partner_rough_v3"
SLIDES = OUT / "slides"
AUDIO = OUT / "audio"
CLIPS = OUT / "clips"
FRAMES = OUT / "frames"
FINAL = OUT / "thinking_partner_rough_v3.mp4"
REPORT = OUT / "scene_timings_v3.txt"
CONTACT = ASSETS / "rough_render_contact_sheet_v3.png"
CONTACT_360 = ASSETS / "rough_render_contact_sheet_v3_360p.png"
FRAME_EXPORT = ASSETS / "rough_render_frames_v3"

W, H = 1920, 1080
VOICE = "en-US-GuyNeural"
RATE = "-4%"
BG = "#10131a"
PANEL = "#151923"
WARM = "#f4f1ea"
MUTED = "#b9c0cf"
GOAL = "#7dd3fc"
EVIDENCE = "#a7f3d0"
OWN = "#fbcfe8"
BORDER = "#3a4255"
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

SCENE_VISUALS = {
    1: V5 / "v5_01_goal_evidence_ownership.png",
    2: ASSETS / "02_half_built_question.png",
    3: V5 / "v5_03_evidence_checklist.png",
    4: V5 / "v5_04_modest_gauge_evidence.png",
    6: ASSETS / "prompt_proof_frames" / "prompt_01_three_checks_v5.png",
    7: ASSETS / "prompt_proof_frames" / "prompt_04_copy_paste_correct_v5.png",
    8: V5 / "v5_08_delegate_keep.png",
}

SCENE05_VISUALS = {
    "05a": V5 / "v5_05a_email_purpose.png",
    "05b": V5 / "v5_05b_three_wordings.png",
    "05c": V5 / "v5_05c_stand_behind.png",
}

SCENE_TITLES = {
    1: "A good answer can still be premature",
    2: "Name the goal before the model does",
    3: "Ask what would change the answer",
    4: "A modest habit, not a safety guarantee",
    5: "Ownership: what belongs to me?",
    6: "The reusable prompt",
    7: "Use it, then edit the frame",
    8: "Keep the decision visible",
}

SUBBEAT_TITLES = {
    "05a": "Ownership: what is this email for?",
    "05b": "Ownership: gentle, direct, or firm?",
    "05c": "Ownership: what will I stand behind?",
}


@dataclass(frozen=True)
class Segment:
    scene_num: int
    key: str
    title: str
    narration: str
    visual: Path


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


def split_scene05(narration: str) -> list[tuple[str, str]]:
    marker_b = "Same facts. Different posture. Different risk."
    marker_c = "A better request is:"
    if marker_b not in narration or marker_c not in narration:
        raise SystemExit("Could not find v5 Scene 05 split markers")
    i_b = narration.index(marker_b)
    i_c = narration.index(marker_c)
    a = narration[:i_b].strip()
    b = narration[i_b:i_c].strip()
    c = narration[i_c:].strip()
    b_flat = re.sub(r"\s+", " ", b)
    if not (a.endswith("Those goals can lead to different wording.") and b.startswith("Same facts. Different posture. Different risk.") and "the line you are willing to stand behind." in b_flat):
        raise SystemExit("Scene 05 split did not match expected natural boundaries")
    return [("05a", a), ("05b", b), ("05c", c)]


def make_segments(scenes: list[dict[str, object]]) -> list[Segment]:
    segments: list[Segment] = []
    for scene in scenes:
        num = int(scene["num"])
        narration = str(scene["narration"])
        if num == 5:
            for key, text in split_scene05(narration):
                segments.append(Segment(num, key, SUBBEAT_TITLES[key], text, SCENE05_VISUALS[key]))
        else:
            visual = SCENE_VISUALS[num]
            segments.append(Segment(num, f"{num:02d}", SCENE_TITLES[num], narration, visual))
    return segments


def draw_header(draw: ImageDraw.ImageDraw, scene_num: int, title: str) -> None:
    draw.rounded_rectangle((58, 48, 1862, 160), radius=28, fill="#0d121d", outline="#252d3d", width=2)
    draw.text((90, 84), f"{scene_num:02d}/08", font=font(34, True), fill=OWN if scene_num in (5, 8) else GOAL)
    draw.text((235, 82), title, font=font(38, True), fill=WARM)
    draw.text((1610, 88), "rough render v3", font=font(25), fill=MUTED)


def draw_footer(draw: ImageDraw.ImageDraw) -> None:
    labels = [("Goal", GOAL), ("Evidence", EVIDENCE), ("Ownership", OWN)]
    x = 88
    for label, color in labels:
        bbox = draw.textbbox((0, 0), label, font=font(25, True))
        tw = bbox[2] - bbox[0]
        draw.rounded_rectangle((x, 1008, x + tw + 48, 1052), radius=22, fill="#111722", outline=color, width=2)
        draw.text((x + 24, 1016), label, font=font(25, True), fill=color)
        x += tw + 72
    draw.text((960, 1022), "How to Think With an AI Without Letting It Think For You", font=font(23), fill="#7d8597", anchor="mm")


def render_slide(segment: Segment) -> Path:
    if not segment.visual.exists():
        raise SystemExit(f"Missing visual for {segment.key}: {segment.visual}")
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    visual = Image.open(segment.visual).convert("RGB").resize((1728, 972), Image.Resampling.LANCZOS)
    im.paste(visual, (96, 66))
    d.rounded_rectangle((58, 48, 1862, 1038), radius=34, outline="#242b3a", width=4)
    draw_header(d, segment.scene_num, segment.title)
    draw_footer(d)
    p = SLIDES / f"segment_{segment.key}.png"
    im.save(p)
    return p


async def tts_one(segment: Segment) -> Path:
    import edge_tts
    out = AUDIO / f"segment_{segment.key}.mp3"
    if out.exists() and out.stat().st_size > 1000:
        return out
    await edge_tts.Communicate(segment.narration, VOICE, rate=RATE).save(str(out))
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


def build_contact_sheet(items: list[tuple[Path, str, str]]) -> None:
    CONTACT.parent.mkdir(parents=True, exist_ok=True)
    sheet = Image.new("RGB", (1280, 960), BG)
    d = ImageDraw.Draw(sheet)
    d.text((42, 24), "Day 413 rough render v3 contact sheet", font=font(29, True), fill=WARM)
    d.text((42, 61), "V5 script with Goal/Evidence/Ownership and real Scene 05 sub-beats; upload gate closed", font=font(19), fill=MUTED)
    positions = [(40, 104), (350, 104), (660, 104), (970, 104), (40, 384), (350, 384), (660, 384), (970, 384), (40, 664), (350, 664), (660, 664)]
    for (path, label, detail), (x, y) in zip(items, positions):
        thumb = Image.open(path).convert("RGB").resize((270, 152), Image.Resampling.LANCZOS)
        d.rounded_rectangle((x - 3, y - 3, x + 273, y + 155), radius=12, fill=PANEL, outline=BORDER, width=2)
        sheet.paste(thumb, (x, y))
        color = OWN if label.startswith("05") or label.startswith("08") else EVIDENCE if label.startswith("03") else GOAL
        d.text((x + 8, y + 164), label, font=font(17, True), fill=color)
        d.text((x + 8, y + 188), detail[:34], font=font(14), fill=MUTED)
    sheet.save(CONTACT)
    sheet.resize((640, 480), Image.Resampling.LANCZOS).save(CONTACT_360)


def export_review_frames(
    scene_timings: list[tuple[int, float, float]],
    segment_timings: list[tuple[str, int, float, float, str]],
) -> None:
    FRAME_EXPORT.mkdir(parents=True, exist_ok=True)
    FRAMES.mkdir(parents=True, exist_ok=True)
    contact_items: list[tuple[Path, str, str]] = []
    for num, start, end in scene_timings:
        if num == 5:
            seg = next(s for s in segment_timings if s[0] == "05b")
            t = seg[2] + (seg[3] - seg[2]) * 0.5
        else:
            t = min(end - 0.25, start + max(0.25, (end - start) * 0.45))
        raw = FRAMES / f"rough_scene_v3_{num:02d}.png"
        extract_frame_at(t, raw)
        exported = FRAME_EXPORT / f"rough_scene_v3_{num:02d}.png"
        Image.open(raw).convert("RGB").resize((1280, 720), Image.Resampling.LANCZOS).save(exported)
        contact_items.append((exported, f"{num:02d}  {start:05.1f}s-{end:05.1f}s", SCENE_TITLES[num]))
    for key in ("05a", "05b", "05c"):
        seg = next(s for s in segment_timings if s[0] == key)
        _, _, start, end, title = seg
        t = min(end - 0.25, start + max(0.25, (end - start) * 0.50))
        raw = FRAMES / f"rough_scene_v3_{key}.png"
        extract_frame_at(t, raw)
        exported = FRAME_EXPORT / f"rough_scene_v3_{key}.png"
        Image.open(raw).convert("RGB").resize((1280, 720), Image.Resampling.LANCZOS).save(exported)
        contact_items.append((exported, f"{key}  {start:05.1f}s-{end:05.1f}s", title))
    build_contact_sheet(contact_items)


async def main() -> None:
    os.chdir(ROOT)
    for d in (SLIDES, AUDIO, CLIPS, FRAMES):
        d.mkdir(parents=True, exist_ok=True)
    scenes = extract_scenes()
    segments = make_segments(scenes)
    for segment in segments:
        render_slide(segment)
    await asyncio.gather(*(tts_one(segment) for segment in segments))

    concat = OUT / "concat.txt"
    scene_starts: dict[int, float] = {}
    scene_ends: dict[int, float] = {}
    segment_timings: list[tuple[str, int, float, float, str]] = []
    cursor = 0.0
    with concat.open("w", encoding="utf-8") as f:
        for segment in segments:
            slide = SLIDES / f"segment_{segment.key}.png"
            aud = AUDIO / f"segment_{segment.key}.mp3"
            clip = CLIPS / f"segment_{segment.key}.mp4"
            dur = probe_duration(aud) + 0.45
            run([
                "ffmpeg", "-nostdin", "-y", "-loop", "1", "-framerate", "1", "-i", slide, "-i", aud,
                "-t", f"{dur:.3f}", "-c:v", "libx264", "-preset", "ultrafast", "-tune", "stillimage",
                "-pix_fmt", "yuv420p", "-r", "24", "-vf", "scale=1920:1080", "-c:a", "aac", "-b:a", "192k",
                "-shortest", clip,
            ])
            f.write(f"file '{clip.resolve()}'\n")
            scene_starts.setdefault(segment.scene_num, cursor)
            scene_ends[segment.scene_num] = cursor + dur
            segment_timings.append((segment.key, segment.scene_num, cursor, cursor + dur, segment.title))
            cursor += dur
    run(["ffmpeg", "-nostdin", "-y", "-f", "concat", "-safe", "0", "-i", concat, "-c", "copy", "-movflags", "+faststart", FINAL])
    scene_timings = [(num, scene_starts[num], scene_ends[num]) for num in range(1, 9)]
    export_review_frames(scene_timings, segment_timings)

    total = probe_duration(FINAL)
    lines = [
        "Day 413 thinking-partner rough render v3",
        f"Script: {SCRIPT.relative_to(ROOT)}",
        f"Output: {FINAL.relative_to(ROOT)}",
        f"Duration: {total:.3f} seconds ({total/60:.2f} minutes)",
        f"Contact sheet: {CONTACT.relative_to(ROOT)}",
        f"360p contact sheet: {CONTACT_360.relative_to(ROOT)}",
        "Scene 05 is rendered as three real visual sub-beats: 05a purpose, 05b wordings, 05c stand-behind.",
        "Upload status: still do not upload.",
        "",
        "Scene timings:",
    ]
    for num, start, end in scene_timings:
        lines.append(f"{num:02d}\t{start:07.3f}\t{end:07.3f}\t{end-start:06.3f}\t{SCENE_TITLES[num]}")
    lines.extend(["", "Segment timings:"])
    for key, scene_num, start, end, title in segment_timings:
        lines.append(f"{key}\t{scene_num:02d}\t{start:07.3f}\t{end:07.3f}\t{end-start:06.3f}\t{title}")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT)
    print(FINAL)
    print(f"{total:.3f}")


if __name__ == "__main__":
    asyncio.run(main())
