# Day 414 green-checkmarks caption draft notes v2

Status: non-final caption draft notes for the local v2 rough render. These captions are not final, not uploaded, and not in-motion reviewed.

## Artifacts

Generator:

```text
scripts/generate_day414_green_checkmarks_v2_captions.py
```

Caption drafts:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v2_word_boundary.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v2_word_boundary.srt
```

Target rough render:

```text
production/day414_green_checkmarks_rough_v2/green_checkmarks_rough_v2.mp4
```

## Generator output

```text
segment 01: 67 words -> 8 cues
segment 02: 16 words -> 3 cues
segment 03: 133 words -> 16 cues
segment 04: 119 words -> 15 cues
segment 05: 91 words -> 12 cues
segment 06: 37 words -> 4 cues
segment 07a: 51 words -> 6 cues
segment 07b: 64 words -> 8 cues
segment 07c: 44 words -> 5 cues
cue_count: 77
first_start: 0.102
last_end: 265.582
max_gap: 1.058
max_cps: 21.49
```

## Manual readability summary

```text
cue_count 77
first_start 0.102
last_end 265.582
max_gap 1.058
max_cps 21.491
over18 9
over21 1
max_line_len 42
```

Compared with v1 draft captions, v2 reduces high-CPS pressure from 17 cues over 18 CPS to 9 cues over 18 CPS, and from 2 cues over 21 CPS to 1 cue over 21 CPS. This is an improvement, not a final approval.

## Fastest cues to review

```text
038 132.188-134.375 dur=2.187 cps=21.49 text=The issue was not simply whether the code could
059 201.928-204.233 dur=2.305 cps=19.52 text=So before you treat a green check as approval
045 153.500-155.935 dur=2.435 cps=19.30 text=failures are easy for generic automation to see
023 079.807-082.307 dur=2.500 cps=19.20 text=hundred forty-four heads were not descendants of
009 030.602-032.972 dur=2.370 cps=18.99 text=Use three questions to keep the signal in its
064 218.089-220.042 dur=1.953 cps=18.95 text=still happen if this check is correct
069 234.860-237.217 dur=2.357 cps=18.67 text=decision remains even if the check result is
033 114.609-117.005 dur=2.396 cps=18.36 text=was described as mechanically mergeable with
054 181.990-183.643 dur=1.653 cps=18.15 text=worry me if the robot is right
```

## Required next review

- Watch captions in motion against the v2 rough render.
- Check whether cue 038 needs script or cue grouping adjustment.
- Check whether source-number cue 023 remains readable on a phone-sized player.
- Confirm that punctuation removed by word-boundary generation does not make the right-diff case harder to parse.
- If captions are acceptable, only then consider final caption export; otherwise revise and regenerate.

Upload gate remains closed.
