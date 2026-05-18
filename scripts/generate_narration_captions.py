#!/usr/bin/env python3
"""Generate draft VTT and SRT captions from narration-only transcript text.

The existing transcript files are useful production artifacts, but some include
slide titles, on-screen bullets, and markdown labels. Captions should reflect the
spoken narration, so this script extracts prose intended for voiceover and writes
approximate-timed WebVTT and SRT files beside each transcript.

Timing is proportional to word count within the published runtime. These files
are therefore draft accessibility aids, not frame-accurate human captions.
"""
from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "series_manifest.json"


def runtime_to_seconds(runtime: str) -> float:
    parts = [int(p) for p in runtime.strip().split(":")]
    if len(parts) == 2:
        minutes, seconds = parts
        return float(minutes * 60 + seconds)
    if len(parts) == 3:
        hours, minutes, seconds = parts
        return float(hours * 3600 + minutes * 60 + seconds)
    raise ValueError(f"Unsupported runtime format: {runtime!r}")


def clean_markdown_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^[-*]\s+", "", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_narration_v1(raw: str) -> list[str]:
    """Extract only paragraphs after **Narration:** blocks in the slide script."""
    paragraphs: list[str] = []
    for block in re.split(r"(?m)^##\s+Slide\s+\d+:", raw):
        if "**Narration:**" not in block:
            continue
        after = block.split("**Narration:**", 1)[1]
        # Drop anything after the next explicit markdown label if present.
        after = re.split(r"(?m)^\*\*[^\n]+:\*\*", after)[0]
        for para in re.split(r"\n\s*\n", after):
            cleaned = clean_markdown_text(para)
            if cleaned:
                paragraphs.append(cleaned)
    return paragraphs


def extract_plain_narration(raw: str) -> list[str]:
    """Extract prose paragraphs from cleaner transcript files."""
    # Remove production-header material before the transcript body separator.
    if "\n---\n" in raw:
        raw = raw.split("\n---\n", 1)[1]

    paragraphs: list[str] = []
    for para in re.split(r"\n\s*\n", raw):
        lines = []
        skip_para = False
        for line in para.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                skip_para = True
                break
            if re.match(r"^\*\*[^*]+:\*\*$", stripped):
                skip_para = True
                break
            if stripped.lower().startswith(("video:", "runtime:", "transcript derived")):
                skip_para = True
                break
            if stripped.startswith(("---", "[", "(")):
                skip_para = True
                break
            lines.append(stripped)
        if skip_para or not lines:
            continue
        cleaned = clean_markdown_text(" ".join(lines))
        # Keep sentence-like prose and short spoken quoted lines; drop obvious labels.
        if cleaned and not cleaned.endswith(":"):
            paragraphs.append(cleaned)
    return paragraphs



def split_into_caption_cues(paragraphs: list[str], max_words: int = 30, max_chars: int = 180) -> list[str]:
    """Split narration paragraphs into compact caption cues.

    We prefer sentence boundaries, but split long sentences at clause-ish word
    boundaries so captions do not linger as whole slide paragraphs.
    """
    cues: list[str] = []
    sentence_re = re.compile(r"(?<=[.!?])\s+")
    for para in paragraphs:
        sentences = [s.strip() for s in sentence_re.split(para) if s.strip()]
        current: list[str] = []
        for sentence in sentences:
            words = sentence.split()
            # Break unusually long sentences into word chunks.
            sentence_chunks = [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)] or [sentence]
            for chunk in sentence_chunks:
                candidate = " ".join(current + [chunk]).strip()
                candidate_words = len(candidate.split())
                if current and (candidate_words > max_words or len(candidate) > max_chars):
                    cues.append(" ".join(current).strip())
                    current = [chunk]
                else:
                    current.append(chunk)
        if current:
            cues.append(" ".join(current).strip())
    return [c for c in cues if c]

def wrap_caption(text: str) -> str:
    return "\n".join(textwrap.wrap(text, width=58, break_long_words=False))


def timestamp(seconds: float, sep: str) -> str:
    seconds = max(0.0, seconds)
    whole = int(seconds)
    ms = int(round((seconds - whole) * 1000))
    if ms == 1000:
        whole += 1
        ms = 0
    h = whole // 3600
    m = (whole % 3600) // 60
    s = whole % 60
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def cue_timings(paragraphs: list[str], total_seconds: float) -> list[tuple[float, float]]:
    counts = [max(1, len(re.findall(r"\w+", p))) for p in paragraphs]
    total_words = sum(counts) or 1
    timings = []
    cursor = 0.0
    for i, count in enumerate(counts):
        if i == len(counts) - 1:
            end = total_seconds
        else:
            end = cursor + total_seconds * (count / total_words)
            # Avoid zero-duration captions for very short lines.
            end = max(end, cursor + 1.0)
            end = min(end, total_seconds)
        timings.append((cursor, end))
        cursor = end
    return timings


def write_vtt(path: Path, paragraphs: list[str], timings: list[tuple[float, float]]) -> None:
    lines = ["WEBVTT", ""]
    for text, (start, end) in zip(paragraphs, timings):
        lines.append(f"{timestamp(start, '.')} --> {timestamp(end, '.')}")
        lines.append(wrap_caption(text))
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_srt(path: Path, paragraphs: list[str], timings: list[tuple[float, float]]) -> None:
    lines = []
    for idx, (text, (start, end)) in enumerate(zip(paragraphs, timings), start=1):
        lines.append(str(idx))
        lines.append(f"{timestamp(start, ',')} --> {timestamp(end, ',')}")
        lines.append(wrap_caption(text))
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for video in manifest["videos"]:
        transcript_path = ROOT / video["transcript"]
        caption_path = ROOT / video["captions"]
        srt_path = caption_path.with_suffix(".srt")
        raw = transcript_path.read_text(encoding="utf-8")
        if video["slug"] == "ai_judges_play_favorites":
            paragraphs = extract_narration_v1(raw)
        else:
            paragraphs = extract_plain_narration(raw)
        if not paragraphs:
            raise SystemExit(f"No narration paragraphs extracted from {transcript_path}")
        cues = split_into_caption_cues(paragraphs)
        timings = cue_timings(cues, runtime_to_seconds(video["runtime"]))
        write_vtt(caption_path, cues, timings)
        write_srt(srt_path, cues, timings)
        print(f"{video['slug']}: {len(cues)} cues -> {caption_path.relative_to(ROOT)}, {srt_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
