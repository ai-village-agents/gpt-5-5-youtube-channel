#!/usr/bin/env python3
"""Render a local v6 caption-safe visual rough of the green-checkmarks candidate.

This v6 rough uses the caption/readability-focused v4 narration while swapping
the final checklist and AI-prompt slides for caption-safe visuals. It remains a local rough
only and is not upload-ready without full watch/listen and in-motion caption
review.
"""
from __future__ import annotations

import asyncio
import hashlib
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "docs" / "day414_green_checkmarks_script_v4.md"
ASSETS = ROOT / "assets" / "day414_green_checkmarks_mockups" / "visual_proofs"
OUT = ROOT / "production" / "day414_green_checkmarks_rough_v6_caption_safe"
AUDIO = OUT / "audio"
CLIPS = OUT / "clips"
FINAL = OUT / "green_checkmarks_rough_v6_caption_safe.mp4"
REPORT = OUT / "scene_timings_v6_caption_safe.txt"
VOICE = "en-US-GuyNeural"
RATE = "-4%"
FPS = 24

@dataclass(frozen=True)
class Segment:
    key: str
    title: str
    visual: Path
    narration: str

VISUALS = {
    "01": ASSETS / "green_01_receipt_not_verdict.png",
    "02": ASSETS / "green_02_three_questions.png",
    "03": ASSETS / "green_03_fresh_base.png",
    "04": ASSETS / "green_04_right_diff.png",
    "05": ASSETS / "green_05_uncovered_risk.png",
    "06": ASSETS / "green_06_signals_not_verdicts.png",
    "07a": ASSETS / "green_07a_review_checklist_caption_safe_v5.png",
    "07b": ASSETS / "green_07b_ai_prompt_caption_safe_v6.png",
    "07c": ASSETS / "green_07c_receipt_close.png",
}

TITLES = {
    "01": "A green check is evidence, not a verdict",
    "02": "Fresh base, right diff, uncovered risk",
    "03": "Fresh base: did the target move?",
    "04": "Right diff: what change will land?",
    "05": "Uncovered risk: what did it not inspect?",
    "06": "Signals are not verdicts",
    "07a": "Checklist: read the receipt",
    "07b": "Ask the AI to slow the moment down",
    "07c": "Keep the check, keep the question",
}

MARKERS = [
    ("01", "A green checkmark feels comforting in software.", "Use three questions to keep the signal in its lane:"),
    ("02", "Use three questions to keep the signal in its lane:", "First: Fresh base."),
    ("03", "First: Fresh base.", "Second: Right diff."),
    ("04", "Second: Right diff.", "Third: Uncovered risk."),
    ("05", "Third: Uncovered risk.", "This is also the caveat."),
    ("06", "This is also the caveat.", "Before treating a green check as approval, ask:"),
    ("07a", "Before treating a green check as approval, ask:", "If you are using an AI assistant during review, ask it the same thing:"),
    ("07b", "If you are using an AI assistant during review, ask it the same thing:", "Keep the green check."),
    ("07c", "Keep the green check.", None),
]


def run(cmd: Iterable[object]) -> None:
    subprocess.run([str(c) for c in cmd], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def probe_duration(path: Path) -> float:
    p = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(path)
    ], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return float(p.stdout.strip())


def extract_narration() -> str:
    text = SCRIPT.read_text(encoding="utf-8")
    body = text.split("## Draft narration", 1)[1].split("## Required description caveat", 1)[0]
    return re.sub(r"\n{3,}", "\n\n", body).strip()


def segment_text(body: str, start: str, end: str | None) -> str:
    if start not in body:
        raise SystemExit(f"Missing start marker: {start}")
    i = body.index(start)
    if end is None:
        j = len(body)
    else:
        if end not in body[i:]:
            raise SystemExit(f"Missing end marker after {start}: {end}")
        j = body.index(end, i)
    return body[i:j].strip()


def make_segments() -> list[Segment]:
    body = extract_narration()
    segments = []
    for key, start, end in MARKERS:
        visual = VISUALS[key]
        if not visual.exists():
            if key in {"07a", "07b"}:
                raise SystemExit(
                    f"Missing visual: {visual}. Run scripts/make_day414_green_checkmarks_caption_safe_visuals.py first."
                )
            raise SystemExit(f"Missing visual: {visual}. Run scripts/make_day414_green_checkmarks_v1_visuals.py first.")
        segments.append(Segment(key, TITLES[key], visual, segment_text(body, start, end)))
    return segments


async def tts_one(segment: Segment) -> Path:
    import edge_tts
    AUDIO.mkdir(parents=True, exist_ok=True)
    out = AUDIO / f"segment_{segment.key}.mp3"
    meta = AUDIO / f"segment_{segment.key}.sha256"
    fingerprint = hashlib.sha256(f"{VOICE}\n{RATE}\n{segment.narration}".encode("utf-8")).hexdigest()
    if out.exists() and out.stat().st_size > 1000 and meta.exists() and meta.read_text().strip() == fingerprint:
        return out
    if out.exists():
        out.unlink()
    await edge_tts.Communicate(segment.narration, VOICE, rate=RATE).save(str(out))
    meta.write_text(fingerprint + "\n", encoding="utf-8")
    return out


def make_clip(segment: Segment, audio: Path) -> tuple[Path, float]:
    CLIPS.mkdir(parents=True, exist_ok=True)
    dur = probe_duration(audio)
    clip = CLIPS / f"segment_{segment.key}.mp4"
    run([
        "ffmpeg", "-nostdin", "-y",
        "-loop", "1", "-framerate", str(FPS), "-i", segment.visual,
        "-i", audio,
        "-t", f"{dur:.3f}",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "160k",
        "-shortest", clip,
    ])
    return clip, dur


async def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    segments = make_segments()
    audios = [await tts_one(s) for s in segments]
    clips: list[Path] = []
    timings = []
    t = 0.0
    for seg, audio in zip(segments, audios):
        clip, audio_dur = make_clip(seg, audio)
        clip_dur = probe_duration(clip)
        start = t
        end = t + clip_dur
        timings.append((seg.key, seg.title, start, end, clip_dur, audio_dur, len(seg.narration.split())))
        t = end
        clips.append(clip)
    concat = OUT / "concat.txt"
    concat.write_text("".join(f"file '{c}'\n" for c in clips), encoding="utf-8")
    run(["ffmpeg", "-nostdin", "-y", "-f", "concat", "-safe", "0", "-i", concat, "-c", "copy", "-movflags", "+faststart", FINAL])
    final_dur = probe_duration(FINAL)
    lines = ["Green-checkmarks rough render v6 caption-safe visual", "", f"final_duration {final_dur:.3f}", "", "Segments:"]
    for key, title, start, end, clip_dur, audio_dur, words in timings:
        lines.append(f"{key:<3} {start:07.3f}  {end:07.3f}  clip={clip_dur:06.3f}  audio={audio_dur:06.3f}  words={words:3d}  {title}")
    lines.append("")
    lines.append("Status: rough render only; no full watch/listen, no final caption approval, no upload approval.")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(FINAL)
    print(REPORT)
    print(f"{final_dur:.3f}")

if __name__ == "__main__":
    asyncio.run(main())
