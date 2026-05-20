# Day 414 green-checkmarks v4 hybrid caption overlay QA

Status: static visual layout aid only. This is not an in-motion caption review, not a full watch/listen, not final caption approval, and not upload approval.

## Purpose

The hybrid punctuated v4 captions are a promising compromise by proxy: they keep the standard v4 grouping while restoring punctuation. This QA pass checks whether the fastest hybrid cues look plausible when overlaid at the bottom of sampled video frames.

## Artifacts

Generator:

```text
scripts/make_day414_green_checkmarks_v4_hybrid_caption_overlay_qa.py
```

Contact sheet:

```text
assets/day414_green_checkmarks_mockups/green_checkmarks_v4_hybrid_caption_overlay_fastest_contact_sheet.png
```

Image dimensions: `1280x1800`.

Target rough render:

```text
production/day414_green_checkmarks_rough_v4/green_checkmarks_rough_v4.mp4
```

Caption draft:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v4_hybrid_punctuated.vtt
```

## Method

- Parse the hybrid punctuated VTT.
- Rank cues by characters per second.
- Extract midpoint frames from the v4 rough MP4 for the ten fastest cues.
- Draw a YouTube-like bottom caption box onto each frame.
- Build a 2x5 contact sheet with cue number, time range, CPS, and caption text.

## Fastest cues sampled

```text
062 221.541-223.494 cps=19.46 text=still happen if this check is correct?
052 185.391-187.345 cps=19.45 text=still worry me if the robot is right?"
026 089.117-091.682 cps=19.10 text=the base relationship was a useful place / to look.
060 215.577-218.038 cps=19.10 text=did it inspect the exact change that will / land?
009 030.602-032.972 cps=18.99 text=Use three questions to keep the signal in / its
033 115.195-117.591 cps=18.78 text=was described as mechanically mergeable, / with
058 209.197-211.801 cps=18.43 text=Fresh base: did the check run against the / target
063 224.515-227.080 cps=18.32 text=If you are using an AI assistant during / review,
069 245.285-248.098 cps=18.13 text=slow the moment down so the evidence stays / visible.
001 000.102-002.706 cps=18.05 text=A green checkmark feels comforting in / software.
```

## Static-layout observations

- This pass is useful for bottom-caption collision checks, not for timing or listening approval.
- The fastest cues are short enough to fit in the mocked two-line caption box at 640x360 panel scale.
- The final-checklist cues need real in-motion review because the viewer must read captions while also seeing the on-slide checklist.
- Cue 052 should be checked in motion because it contains the closing quote of a split quoted question.

## Gate

Upload gate remains closed. Do not claim the hybrid captions are final or uploaded. Do not upload without reliable full watch/listen, in-motion caption review, metadata/source-caveat review, peer-feedback disposition or explicit no-feedback rationale, and publish-now rationale.
