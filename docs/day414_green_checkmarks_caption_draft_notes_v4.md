# Day 414 green-checkmarks caption draft notes v4

Status: non-final caption draft notes for the local v4 rough render. These captions are not final, not uploaded, and not in-motion reviewed.

## Artifacts

Generator:

```text
scripts/generate_day414_green_checkmarks_v4_captions.py
```

Caption drafts:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v4_word_boundary.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v4_word_boundary.srt
```

Target rough render:

```text
production/day414_green_checkmarks_rough_v4/green_checkmarks_rough_v4.mp4
```

## Generator output

```text
segment 01: 67 words -> 8 cues
segment 02: 16 words -> 3 cues
segment 03: 136 words -> 16 cues
segment 04: 116 words -> 14 cues
segment 05: 90 words -> 11 cues
segment 06: 37 words -> 4 cues
segment 07a: 49 words -> 6 cues
segment 07b: 62 words -> 7 cues
segment 07c: 44 words -> 5 cues
cue_count: 74
first_start: 0.102
last_end: 268.349
max_gap: 1.058
max_cps: 18.99
```

## Manual readability summary

```text
cue_count 74
first_start 0.102
last_end 268.349
max_gap 1.058
max_cps 18.987
over18 7
over21 0
max_line_len 42
```

Compared with v2 draft captions, v4 reduces high-CPS pressure from 9 cues over 18 CPS to 7 cues over 18 CPS, and from 1 cue over 21 CPS to 0 cues over 21 CPS. Compared with the v3 experiment, v4 fixes the worst caption regression. This is an improvement, not final approval.

## Fastest cues to review

```text
009 030.602-032.972 dur=2.370 cps=18.99 text=Use three questions to keep the signal in its
062 221.541-223.494 dur=1.953 cps=18.95 text=still happen if this check is correct
026 089.117-091.682 dur=2.565 cps=18.71 text=the base relationship was a useful place to look
060 215.577-218.038 dur=2.461 cps=18.69 text=did it inspect the exact change that will land
052 185.391-187.345 dur=1.954 cps=18.42 text=still worry me if the robot is right
033 115.195-117.591 dur=2.396 cps=18.36 text=was described as mechanically mergeable with
058 209.197-211.801 dur=2.604 cps=18.05 text=Fresh base did the check run against the target
```

## Required next review

- Watch captions in motion against the v4 rough render.
- Check whether the seven remaining >18 CPS cues feel readable in context.
- Check whether word-boundary punctuation loss makes the checklist harder to parse.
- Confirm the v4 script changes did not weaken the right-diff/source-boundary explanation.
- If captions are acceptable, only then consider final caption export; otherwise revise and regenerate.

Upload gate remains closed.
