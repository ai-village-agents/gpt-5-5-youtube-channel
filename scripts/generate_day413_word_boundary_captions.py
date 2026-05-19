#!/usr/bin/env python3
"""Generate word-boundary draft captions for the Day 413 v2 rough render.

These captions are still drafts: they use Microsoft Edge TTS word-boundary
metadata for the exact v4 scene text/voice/rate, then group words into readable
caption cues. They are intended to improve on the earlier scene-proportional
rough captions, not to replace a manual watch/listen pass.
"""
from __future__ import annotations

import asyncio
import html
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "docs" / "day413_thinking_partner_script_v4.md"
TIMINGS = ROOT / "production" / "day413_thinking_partner_rough_v2" / "scene_timings_v2.txt"
OUT_DIR = ROOT / "docs" / "day413_caption_drafts"
OUT_VTT = OUT_DIR / "thinking_partner_v4_word_boundary_v2.vtt"
OUT_SRT = OUT_DIR / "thinking_partner_v4_word_boundary_v2.srt"
VOICE = "en-US-GuyNeural"
RATE = "-4%"


@dataclass
class Scene:
    num: int
    title: str
    text: str
    start: float
    end: float


@dataclass
class Word:
    text: str
    start: float
    end: float


@dataclass
class Cue:
    start: float
    end: float
    text: str


def clean_narration(raw: str) -> str:
    raw = re.sub(r"(?m)^>\s?", "", raw)
    raw = re.sub(r"\*\*(.*?)\*\*", r"\1", raw)
    raw = re.sub(r"`([^`]*)`", r"\1", raw)
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.strip()


def extract_scene_texts() -> list[tuple[int, str, str]]:
    text = SCRIPT.read_text(encoding="utf-8")
    parts = re.split(r"(?m)^###\s+(\d+)\.\s+([^\n]+)\n", text)
    scenes: list[tuple[int, str, str]] = []
    for i in range(1, len(parts), 3):
        num = int(parts[i])
        title = parts[i + 1].strip()
        body = parts[i + 2]
        if "**Narration:**" not in body:
            continue
        narration = body.split("**Narration:**", 1)[1].split("**On-screen visual:**", 1)[0]
        scenes.append((num, title, clean_narration(narration)))
    if len(scenes) != 8:
        raise SystemExit(f"Expected 8 scenes, extracted {len(scenes)}")
    return scenes


def read_timings() -> dict[int, tuple[float, float]]:
    timings: dict[int, tuple[float, float]] = {}
    for line in TIMINGS.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\d\d\t", line):
            continue
        num_s, start_s, end_s, *_ = line.split("\t")
        timings[int(num_s)] = (float(start_s), float(end_s))
    if len(timings) != 8:
        raise SystemExit(f"Expected 8 scene timings, found {len(timings)}")
    return timings


def load_scenes() -> list[Scene]:
    timings = read_timings()
    scenes: list[Scene] = []
    for num, title, text in extract_scene_texts():
        start, end = timings[num]
        scenes.append(Scene(num, title, text, start, end))
    return scenes


def script_tokens(text: str) -> list[str]:
    """Return display tokens roughly corresponding to spoken word boundaries."""
    # Keep punctuation attached for readability. Split contractions as one token.
    pattern = re.compile(r"(?:\d+\.)|(?:[A-Za-z0-9]+(?:[’'\-][A-Za-z0-9]+)*[.,;:!?]?)")
    return pattern.findall(text.replace("—", " "))


def norm_token(token: str) -> str:
    token = html.unescape(token).lower()
    token = token.strip()
    token = re.sub(r"^[^a-z0-9]+|[^a-z0-9]+$", "", token)
    token = token.replace("’", "'")
    return token


async def boundary_words(scene: Scene) -> list[Word]:
    comm = edge_tts.Communicate(scene.text, VOICE, rate=RATE, boundary="WordBoundary")
    raw: list[tuple[str, float, float]] = []
    async for chunk in comm.stream():
        if chunk["type"] != "WordBoundary":
            continue
        start = scene.start + chunk["offset"] / 10_000_000
        end = scene.start + (chunk["offset"] + chunk["duration"]) / 10_000_000
        raw.append((str(chunk["text"]), start, end))

    display = script_tokens(scene.text)
    words: list[Word] = []
    warnings: list[str] = []
    j = 0
    for edge_text, start, end in raw:
        chosen = edge_text
        edge_norm = norm_token(edge_text)
        # Usually the token counts match exactly. If they do not, scan forward a
        # little so punctuation/numbering differences do not derail the rest.
        if j < len(display) and norm_token(display[j]) == edge_norm:
            chosen = display[j]
            j += 1
        else:
            found = None
            for k in range(j, min(len(display), j + 5)):
                if norm_token(display[k]) == edge_norm:
                    found = k
                    break
            if found is not None:
                warnings.append(f"scene {scene.num}: skipped display tokens {display[j:found]} before {edge_text!r}")
                chosen = display[found]
                j = found + 1
            else:
                warnings.append(f"scene {scene.num}: used edge text {edge_text!r} near display token {display[j:j+1]}")
        words.append(Word(chosen, start, min(end, scene.end)))
    if j != len(display):
        warnings.append(f"scene {scene.num}: unused display tokens tail {display[j:j+8]}")
    if len(raw) != len(display):
        warnings.append(f"scene {scene.num}: edge words {len(raw)} vs script tokens {len(display)}")
    for warning in warnings[:12]:
        print("WARNING:", warning)
    if len(warnings) > 12:
        print(f"WARNING: scene {scene.num}: {len(warnings) - 12} additional token warnings suppressed")
    return words


def is_sentence_end(token: str) -> bool:
    return token.endswith(('.', '?', '!'))


def is_prompt_number(token: str) -> bool:
    return bool(re.fullmatch(r"[1-3]\.", token))


def cue_text(tokens: list[str]) -> str:
    joined = " ".join(tokens)
    joined = re.sub(r"\s+([.,;:!?])", r"\1", joined)
    words = joined.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else current + " " + word
        if len(trial) <= 42 or not current:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) <= 2:
        return "\n".join(lines)
    # Rebalance to two lines by character length rather than word count. This
    # keeps occasional dense cues readable without creating very long lines.
    best_split = 1
    best_score = 10**9
    for split in range(1, len(words)):
        left = " ".join(words[:split])
        right = " ".join(words[split:])
        score = max(len(left), len(right)) * 10 + abs(len(left) - len(right))
        if score < best_score:
            best_score = score
            best_split = split
    return " ".join(words[:best_split]) + "\n" + " ".join(words[best_split:])


def group_scene(words: list[Word], scene: Scene) -> list[Cue]:
    cues: list[Cue] = []
    group: list[Word] = []

    def flush() -> None:
        nonlocal group
        if not group:
            return
        start = group[0].start
        end = min(scene.end, max(group[-1].end + 0.18, group[-1].start + 0.55))
        if end <= start:
            end = min(scene.end, start + 0.8)
        cues.append(Cue(start, end, cue_text([w.text for w in group])))
        group = []

    for idx, word in enumerate(words):
        if group and is_prompt_number(word.text):
            flush()
        group.append(word)
        duration = group[-1].end - group[0].start
        chars = len(" ".join(w.text for w in group))
        sentence = is_sentence_end(word.text)
        short_standalone = sentence and len(group) <= 3 and duration >= 0.7
        next_is_number = idx + 1 < len(words) and is_prompt_number(words[idx + 1].text)
        should_break = False
        if duration >= 5.55:
            should_break = True
        elif chars >= 74 and duration >= 2.0:
            should_break = True
        elif sentence and duration >= 1.6:
            should_break = True
        elif short_standalone:
            should_break = True
        elif next_is_number and duration >= 1.0:
            should_break = True
        if should_break:
            flush()
    flush()

    # Remove accidental overlaps within the scene.
    for i in range(1, len(cues)):
        if cues[i].start < cues[i - 1].end:
            midpoint = (cues[i].start + cues[i - 1].end) / 2
            cues[i - 1].end = max(cues[i - 1].start + 0.25, midpoint - 0.02)
            cues[i].start = min(cues[i].end - 0.25, midpoint + 0.02)
    return cues


def fmt_time(seconds: float, comma: bool = False) -> str:
    seconds = max(0.0, seconds)
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    if ms == 1000:
        s += 1
        ms = 0
    sep = ',' if comma else '.'
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def validate(cues: list[Cue]) -> dict[str, float | int]:
    durations = [c.end - c.start for c in cues]
    gaps = [cues[i].start - cues[i - 1].end for i in range(1, len(cues))]
    return {
        "cue_count": len(cues),
        "first_start": cues[0].start if cues else 0.0,
        "last_end": cues[-1].end if cues else 0.0,
        "min_duration": min(durations) if durations else 0.0,
        "max_duration": max(durations) if durations else 0.0,
        "max_gap": max(gaps) if gaps else 0.0,
        "nonpositive": sum(1 for d in durations if d <= 0),
        "overlaps": sum(1 for g in gaps if g < -0.001),
    }


def write_outputs(cues: list[Cue]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    vtt_lines = ["WEBVTT", "", "NOTE Draft word-boundary captions for Day 413 rough render v2; not final or uploaded.", ""]
    srt_lines: list[str] = []
    for idx, cue in enumerate(cues, start=1):
        vtt_lines.append(f"{fmt_time(cue.start)} --> {fmt_time(cue.end)}")
        vtt_lines.append(cue.text)
        vtt_lines.append("")
        srt_lines.append(str(idx))
        srt_lines.append(f"{fmt_time(cue.start, comma=True)} --> {fmt_time(cue.end, comma=True)}")
        srt_lines.append(cue.text)
        srt_lines.append("")
    OUT_VTT.write_text("\n".join(vtt_lines), encoding="utf-8")
    OUT_SRT.write_text("\n".join(srt_lines), encoding="utf-8")


async def main() -> None:
    scenes = load_scenes()
    all_cues: list[Cue] = []
    for scene in scenes:
        words = await boundary_words(scene)
        scene_cues = group_scene(words, scene)
        print(f"scene {scene.num:02d}: {len(words)} words -> {len(scene_cues)} cues")
        all_cues.extend(scene_cues)
    # Global overlap guard between scenes/cues.
    all_cues.sort(key=lambda c: (c.start, c.end))
    for i in range(1, len(all_cues)):
        if all_cues[i].start < all_cues[i - 1].end:
            all_cues[i - 1].end = max(all_cues[i - 1].start + 0.25, all_cues[i].start - 0.02)
    write_outputs(all_cues)
    print(f"wrote {OUT_VTT.relative_to(ROOT)}")
    print(f"wrote {OUT_SRT.relative_to(ROOT)}")
    for key, value in validate(all_cues).items():
        if isinstance(value, float):
            print(f"{key}: {value:.3f}")
        else:
            print(f"{key}: {value}")


if __name__ == "__main__":
    asyncio.run(main())
