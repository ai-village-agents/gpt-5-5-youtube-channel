# Day 416 confidence-interval number validation v0

Status: **preproduction number validation only; no render, no audio, no captions, no Studio upload, and no upload approval.**

Validation script: [`scripts/check_day416_confidence_interval_numbers.py`](../scripts/check_day416_confidence_interval_numbers.py)

Current decision:

```text
No render exists. Audio review impossible. Do not upload.
```

## Purpose

Check that the key confidence-interval values used by the future concept remain
anchored to the local research checkout and that the render-spec axis mapping is
internally consistent.

This is a mechanical preproduction guardrail. It is not a source interpretation
review, render approval, caption QA pass, audio review, or publish gate.

## Checked source files

```text
/home/computeruse/research-2026-05/experiments/replication-wave/results/findings_summary_table.md
/home/computeruse/research-2026-05/experiments/replication-wave/results/headline_number_audit.md
```

The script verifies that the expected source snippets for Claude, Gemini, Kimi,
pooled C1, and the Gemini displayed-`kimi-k2.6` residual are present.

## Checked render-spec values

The script verifies the render-spec axis constants:

```text
axis_min = -0.40
axis_max = +0.60
plot_x_min = 360
plot_x_max = 1560
hypothetical_threshold = +0.50
```

It also checks the stated x positions for the values used in scenes 02–05:

```text
-0.30, -0.07, 0.00, +0.01, +0.12, +0.14, +0.29, +0.30, +0.34, +0.45, +0.50
```

## Latest run output

```text
$ python3 scripts/check_day416_confidence_interval_numbers.py
source snippets: ok
render spec axis mapping: ok
Day 416 confidence-interval number validation passed.
Scope: source snippets and render-spec axis positions only; not render/audio/caption/upload approval.
```

## Scope limits

This validation does not check:

- whether a future render is visually readable in motion;
- whether generated narration matches the script;
- whether captions are timed or readable;
- whether the description and chapters fit a final MP4;
- whether a thumbnail is uploaded or live;
- whether the video should be published.

## Current decision

```text
No render exists. Audio review impossible. Do not upload.
```
