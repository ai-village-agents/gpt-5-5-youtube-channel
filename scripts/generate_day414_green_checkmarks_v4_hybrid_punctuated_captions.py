#!/usr/bin/env python3
"""Generate hybrid punctuated VTT/SRT captions for green-checkmarks rough v4.

These are alternate draft captions for structural review only, not final/uploaded captions.
Grouping uses punctuation-stripped word-boundary tokens; display text uses script punctuation.
"""
from __future__ import annotations

import asyncio
import re
from dataclasses import dataclass
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "docs" / "day414_green_checkmarks_script_v4.md"
TIMINGS = ROOT / "production" / "day414_green_checkmarks_rough_v4" / "scene_timings_v4.txt"
OUTDIR = ROOT / "docs" / "day414_caption_drafts"
VTT = OUTDIR / "green_checkmarks_rough_v4_hybrid_punctuated.vtt"
SRT = OUTDIR / "green_checkmarks_rough_v4_hybrid_punctuated.srt"
VOICE = "en-US-GuyNeural"
RATE = "-4%"
MAX_CHARS = 42
MAX_DUR = 5.6
TARGET_CHARS = 48

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

@dataclass
class Word:
    text: str
    display: str
    start: float
    end: float

@dataclass
class Cue:
    start: float
    end: float
    text: str


def narration_body() -> str:
    text = SCRIPT.read_text(encoding="utf-8")
    return re.sub(r"\n{3,}", "\n\n", text.split("## Draft narration",1)[1].split("## Required description caveat",1)[0]).strip()


def segment_text(body: str, start: str, end: str | None) -> str:
    i = body.index(start)
    j = len(body) if end is None else body.index(end, i)
    return body[i:j].strip()


def load_segment_starts() -> dict[str, float]:
    starts = {}
    for line in TIMINGS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\d\d[a-z]?)\s+(\d+\.\d+)\s+", line)
        if m:
            starts[m.group(1)] = float(m.group(2))
    if set(starts) != {k for k,_,__ in MARKERS}:
        raise SystemExit(f"Bad segment starts: {starts}")
    return starts


def clean_word(text: str) -> str:
    return text.strip()


def display_tokens(text: str) -> list[str]:
    tokens: list[str] = []
    for raw in text.split():
        token = raw.strip()
        if any(ch.isalnum() for ch in token):
            tokens.append(token)
    return tokens


async def word_boundaries(text: str, offset: float) -> list[Word]:
    comm = edge_tts.Communicate(text, VOICE, rate=RATE, boundary="WordBoundary")
    base_words: list[tuple[str, float, float]] = []
    async for msg in comm.stream():
        if msg["type"] == "WordBoundary":
            token = clean_word(msg.get("text", ""))
            if not token:
                continue
            start = offset + msg["offset"] / 10_000_000
            dur = msg["duration"] / 10_000_000
            base_words.append((token, start, start + max(dur, 0.08)))
    displays = display_tokens(text)
    if len(displays) != len(base_words):
        print(f"hybrid punctuation fallback: script_tokens={len(displays)} boundary_words={len(base_words)}")
        displays = [w[0] for w in base_words]
    return [Word(token, display, start, end) for (token, start, end), display in zip(base_words, displays)]


def wrap_text(words: list[str]) -> str:
    lines: list[str] = []
    cur = ""
    for w in words:
        trial = w if not cur else cur + " " + w
        if len(trial) <= MAX_CHARS:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if len(lines) <= 2:
        return "\n".join(lines)
    # rebalance into two lines when possible
    text = " ".join(words)
    mid = len(text)//2
    spaces = [i for i,c in enumerate(text) if c == ' ']
    if spaces:
        split = min(spaces, key=lambda i: abs(i-mid))
        a,b = text[:split], text[split+1:]
        if len(a) <= MAX_CHARS and len(b) <= MAX_CHARS:
            return a + "\n" + b
    return "\n".join(lines[:2])


def group_words(words: list[Word]) -> list[Cue]:
    cues: list[Cue] = []
    cur: list[Word] = []
    for w in words:
        if not cur:
            cur = [w]
            continue
        current_text = " ".join(x.text for x in cur)
        trial_text = " ".join(x.text for x in cur + [w])
        dur = w.end - cur[0].start
        should_break_before_word = False
        if len(trial_text) > TARGET_CHARS and len(current_text) >= 24:
            should_break_before_word = True
        if dur >= MAX_DUR:
            should_break_before_word = True
        if cur[-1].text.endswith(('.', '?', '!')) and len(current_text) >= 28:
            should_break_before_word = True
        if should_break_before_word:
            cues.append(Cue(cur[0].start, cur[-1].end, wrap_text([x.display for x in cur])))
            cur = [w]
        else:
            cur.append(w)
    if cur:
        cues.append(Cue(cur[0].start, cur[-1].end, wrap_text([x.display for x in cur])))
    # Merge tiny final cues into previous where safe.
    merged: list[Cue] = []
    for cue in cues:
        if merged and (cue.end - cue.start) < 0.9 and cue.start - merged[-1].end <= 0.35 and cue.end - merged[-1].start <= 6.2:
            prev = merged.pop()
            text = wrap_text((prev.text.replace('\n',' ') + ' ' + cue.text.replace('\n',' ')).split())
            merged.append(Cue(prev.start, cue.end, text))
        else:
            merged.append(cue)
    return merged


def fmt_vtt(t: float) -> str:
    ms = int(round(t*1000))
    h, rem = divmod(ms, 3600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def fmt_srt(t: float) -> str:
    return fmt_vtt(t).replace('.', ',')


async def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    body = narration_body()
    starts = load_segment_starts()
    all_cues: list[Cue] = []
    for key, start_marker, end_marker in MARKERS:
        text = segment_text(body, start_marker, end_marker)
        words = await word_boundaries(text, starts[key])
        cues = group_words(words)
        all_cues.extend(cues)
        print(f"segment {key}: {len(words)} words -> {len(cues)} cues")
    all_cues.sort(key=lambda c: c.start)
    VTT.write_text("WEBVTT\n\n" + "\n\n".join(f"{fmt_vtt(c.start)} --> {fmt_vtt(c.end)}\n{c.text}" for c in all_cues) + "\n", encoding="utf-8")
    SRT.write_text("\n\n".join(f"{i}\n{fmt_srt(c.start)} --> {fmt_srt(c.end)}\n{c.text}" for i,c in enumerate(all_cues,1)) + "\n", encoding="utf-8")
    gaps=[all_cues[i+1].start-all_cues[i].end for i in range(len(all_cues)-1)]
    cps=[len(c.text.replace('\n',' '))/(c.end-c.start) for c in all_cues if c.end>c.start]
    print('cue_count:', len(all_cues))
    print('first_start:', f'{all_cues[0].start:.3f}')
    print('last_end:', f'{all_cues[-1].end:.3f}')
    print('max_gap:', f'{max(gaps):.3f}' if gaps else '0')
    print('max_cps:', f'{max(cps):.2f}' if cps else '0')
    print(VTT)
    print(SRT)

if __name__ == "__main__":
    asyncio.run(main())
