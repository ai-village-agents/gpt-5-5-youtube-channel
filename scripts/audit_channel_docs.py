#!/usr/bin/env python3
"""Lightweight audit for the GPT-5.5 YouTube channel repository.

Checks are intentionally local and deterministic: they do not call YouTube or
GitHub. The goal is to catch broken repo links, malformed manifest data, missing
per-video documentation, broken Markdown links, thumbnails, and obviously broken draft caption files before commits.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_VIDEO_FILES = [
    "publish_log.md",
    "production_notes.md",
    "creative_brief.md",
]

REQUIRED_MANIFEST_KEYS = {
    "number",
    "title",
    "url",
    "video_id",
    "runtime",
    "slug",
    "core_lesson",
    "transcript",
    "captions",
    "captions_srt",
    "thumbnail_concept",
    "production_notes",
    "publish_log",
}


def fail(message: str) -> None:
    print(f"AUDIT FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: str | Path) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check_manifest() -> dict:
    try:
        manifest = json.loads(read("series_manifest.json"))
    except json.JSONDecodeError as exc:
        fail(f"series_manifest.json is invalid JSON: {exc}")

    videos = manifest.get("videos")
    if not isinstance(videos, list) or not videos:
        fail("series_manifest.json must contain a non-empty videos list")

    series = manifest.get("series", {})
    if series.get("count") != len(videos):
        fail("series.count does not match videos list length")

    seen_numbers: set[int] = set()
    seen_slugs: set[str] = set()
    for entry in videos:
        missing = REQUIRED_MANIFEST_KEYS - set(entry)
        if missing:
            fail(f"manifest entry missing keys {sorted(missing)}: {entry}")
        number = entry["number"]
        slug = entry["slug"]
        if number in seen_numbers:
            fail(f"duplicate manifest video number: {number}")
        if slug in seen_slugs:
            fail(f"duplicate manifest slug: {slug}")
        seen_numbers.add(number)
        seen_slugs.add(slug)
        if not str(entry["url"]).startswith("https://youtu.be/"):
            fail(f"manifest URL is not a youtu.be URL: {entry['url']}")
        if entry["video_id"] not in entry["url"]:
            fail(f"manifest video_id not present in URL: {entry}")
    return manifest


def check_manifest_paths(manifest: dict) -> None:
    for entry in manifest["videos"]:
        slug = entry["slug"]
        folder = ROOT / "videos" / slug
        if not folder.is_dir():
            fail(f"missing video folder for slug {slug}")
        for rel in REQUIRED_VIDEO_FILES:
            if not (folder / rel).exists():
                fail(f"missing required file: videos/{slug}/{rel}")
        for key in ["transcript", "captions", "captions_srt", "thumbnail_concept", "production_notes", "publish_log"]:
            path = ROOT / entry[key]
            if not path.exists():
                fail(f"manifest path for {key} does not exist: {entry[key]}")


def check_markdown_links() -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    docs = sorted(ROOT.rglob("*.md"))
    for path in docs:
        rel = str(path.relative_to(ROOT))
        if not path.exists():
            fail(f"document listed for link checking is missing: {rel}")
        text = path.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local, _, _anchor = target.partition("#")
            if local and not (path.parent / local).resolve().exists():
                fail(f"broken local Markdown link in {rel}: {target}")


def check_captions() -> None:
    vtt_files = sorted((ROOT / "videos").glob("*/captions/*.vtt"))
    srt_files = sorted((ROOT / "videos").glob("*/captions/*.srt"))
    if not vtt_files:
        fail("no VTT caption files found")
    if len(srt_files) != len(vtt_files):
        fail(f"expected one SRT caption file per VTT file; found {len(vtt_files)} VTT and {len(srt_files)} SRT")
    for path in vtt_files:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("WEBVTT"):
            fail(f"caption file does not start with WEBVTT: {path.relative_to(ROOT)}")
        if "-->" not in text:
            fail(f"caption file has no cues: {path.relative_to(ROOT)}")
        srt_path = path.with_suffix(".srt")
        if not srt_path.exists():
            fail(f"missing SRT companion for {path.relative_to(ROOT)}")
        srt_text = srt_path.read_text(encoding="utf-8")
        if not re.search(r"(?m)^1\n\d\d:\d\d:\d\d,\d{3} --> \d\d:\d\d:\d\d,\d{3}", srt_text):
            fail(f"SRT caption file does not start with a numbered cue: {srt_path.relative_to(ROOT)}")
        if "-->" not in srt_text:
            fail(f"SRT caption file has no cues: {srt_path.relative_to(ROOT)}")


def check_thumbnails(manifest: dict) -> None:
    try:
        from PIL import Image
    except ImportError as exc:
        fail(f"Pillow is required for thumbnail audit: {exc}")
    for entry in manifest["videos"]:
        path = ROOT / entry["thumbnail_concept"]
        if not path.exists():
            fail(f"thumbnail concept path missing: {entry['thumbnail_concept']}")
        with Image.open(path) as image:
            if image.size != (1280, 720):
                fail(f"thumbnail concept is not 1280x720: {entry['thumbnail_concept']} has {image.size}")
            if image.format != "PNG":
                fail(f"thumbnail concept is not a PNG: {entry['thumbnail_concept']}")


def check_readme_mentions(manifest: dict) -> None:
    readme = read("README.md")
    for entry in manifest["videos"]:
        if entry["title"] not in readme:
            fail(f"README does not mention title: {entry['title']}")
        if entry["url"] not in readme:
            fail(f"README does not mention URL: {entry['url']}")
        for key in ["transcript", "captions", "captions_srt", "thumbnail_concept", "production_notes", "publish_log"]:
            if entry[key] not in readme:
                fail(f"README does not link {key} for {entry['slug']}: {entry[key]}")


def main() -> None:
    manifest = check_manifest()
    check_manifest_paths(manifest)
    check_markdown_links()
    check_captions()
    check_thumbnails(manifest)
    check_readme_mentions(manifest)
    print(
        "Channel documentation audit passed: "
        f"{manifest['series']['count']} videos, "
        "manifest paths, README links, all Markdown links, thumbnails, and VTT/SRT files are consistent."
    )


if __name__ == "__main__":
    main()
