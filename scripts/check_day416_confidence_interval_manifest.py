#!/usr/bin/env python3
"""Validate Day 416 confidence-interval artifact manifest identity rows.

This is an identity/drift-control check only. Passing it is not render, audio,
caption, Studio, peer-review, publish-gate, or upload approval.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/day416_confidence_intervals_artifact_manifest_v0.md"
ROW_RE = re.compile(r"^\| `([^`]+)` \| (\d+) \| `([0-9a-f]{64})` \|$")


def main() -> int:
    text = MANIFEST.read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        match = ROW_RE.match(line)
        if match:
            rows.append((match.group(1), int(match.group(2)), match.group(3)))

    if not rows:
        print("manifest validation failed: no artifact rows found")
        return 1

    failures: list[str] = []
    for rel_path, expected_size, expected_sha in rows:
        path = ROOT / rel_path
        if not path.exists():
            failures.append(f"missing: {rel_path}")
            continue
        data = path.read_bytes()
        actual_size = len(data)
        actual_sha = hashlib.sha256(data).hexdigest()
        if actual_size != expected_size:
            failures.append(
                f"size mismatch: {rel_path}: expected {expected_size}, got {actual_size}"
            )
        if actual_sha != expected_sha:
            failures.append(
                f"sha mismatch: {rel_path}: expected {expected_sha}, got {actual_sha}"
            )

    if failures:
        print("Day 416 confidence-interval artifact manifest validation failed:")
        for failure in failures:
            print("-", failure)
        print("Scope: identity/drift control only; not upload approval.")
        return 1

    print(f"Day 416 confidence-interval artifact manifest validation passed ({len(rows)} rows).")
    print("Scope: identity/drift control only; not render/audio/caption/upload approval.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
