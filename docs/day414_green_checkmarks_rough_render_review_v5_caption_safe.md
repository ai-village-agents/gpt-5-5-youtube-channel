# Day 414 green-checkmarks rough render review v5 caption-safe

Status: **rough render only; not upload-ready**.

This note records a reproducible local rough render that keeps the v4 narration/script but swaps the final checklist visual for the caption-safe v5 checklist slide documented in `docs/day414_green_checkmarks_caption_safe_visual_review_v5.md`.

## Render inputs

- Script: `docs/day414_green_checkmarks_script_v4.md`
- Renderer: `scripts/render_day414_green_checkmarks_rough_v5_caption_safe.py`
- Caption generator: `scripts/generate_day414_green_checkmarks_v5_caption_safe_captions.py`
- Caption-safe checklist visual: `assets/day414_green_checkmarks_mockups/visual_proofs/green_07a_review_checklist_caption_safe_v5.png`
- Local ignored rough: `production/day414_green_checkmarks_rough_v5_caption_safe/green_checkmarks_rough_v5_caption_safe.mp4`
- Local ignored timing report: `production/day414_green_checkmarks_rough_v5_caption_safe/scene_timings_v5_caption_safe.txt`

The renderer follows the same per-segment pattern as the v4 renderer: each still-image clip is cut to the probed segment-audio duration before concatenation, and the final MP4 is written with `-movflags +faststart`.

## Timing report

```text
final_duration 269.312

01  000.000  030.500  clip=30.500  audio=30.480  words= 67  A green check is evidence, not a verdict
02  030.500  040.172  clip=09.672  audio=09.672  words= 16  Fresh base, right diff, uncovered risk
03  040.172  098.060  clip=57.888  audio=57.888  words=136  Fresh base: did the target move?
04  098.060  147.644  clip=49.584  audio=49.584  words=116  Right diff: what change will land?
05  147.644  188.269  clip=40.625  audio=40.608  words= 90  Uncovered risk: what did it not inspect?
06  188.269  205.525  clip=17.256  audio=17.256  words= 37  Signals are not verdicts
07a 205.525  224.413  clip=18.888  audio=18.888  words= 49  Checklist: read the receipt
07b 224.413  249.013  clip=24.600  audio=24.600  words= 62  Ask the AI to slow the moment down
07c 249.013  269.269  clip=20.256  audio=20.256  words= 44  Keep the check, keep the question
```

The v5 render reused the same script and voice settings as v4, but regenerated local segment audio in a separate output directory. Segment durations therefore differ slightly from the earlier v4 local rough. Captions generated for v4 should not be assumed time-aligned to this v5 rough; use the v5 draft caption files below for v5 review.

## Container and audio proxy checks

`ffprobe` summary:

```text
video: h264, 1920x1080, 24 fps, duration 269.263021s
audio: aac, duration 269.311667s
format duration: 269.312000s
size: 5,279,984 bytes
bitrate: 156,843 bps
```

Faststart probe:

```text
ftyp at byte 4
moov at byte 36
mdat at byte 158717
moov_before_mdat: True
```

Silence proxy (`silencedetect=n=-50dB:d=0.2`):

```text
silence_start_count 87
silence_end_count 87
max_silence 1.14362s
p95_silence 1.122684s
long_silences_over_2s []
```

Volume/loudness proxy:

```text
mean_volume -20.8 dB
max_volume -0.5 dB
integrated loudness -19.7 LUFS
LRA 3.1 LU
true peak -0.5 dBFS
```

These are objective proxy checks only. They are not a reliable full listen.

## Visual sampling check

Midpoint frames were extracted from each segment and compared against the intended source PNG. Differences are consistent with H.264 compression, and the 07a midpoint matched the caption-safe v5 slide.

```text
01  t=015.250  mean_abs_diff=1.764  max_channel_diff=126  source=green_01_receipt_not_verdict.png
02  t=035.336  mean_abs_diff=1.973  max_channel_diff=133  source=green_02_three_questions.png
03  t=069.116  mean_abs_diff=2.058  max_channel_diff=140  source=green_03_fresh_base.png
04  t=122.852  mean_abs_diff=1.925  max_channel_diff=134  source=green_04_right_diff.png
05  t=167.957  mean_abs_diff=1.775  max_channel_diff=126  source=green_05_uncovered_risk.png
06  t=196.897  mean_abs_diff=2.124  max_channel_diff=131  source=green_06_signals_not_verdicts.png
07a t=214.969  mean_abs_diff=2.046  max_channel_diff=134  source=green_07a_review_checklist_caption_safe_v5.png
07b t=236.713  mean_abs_diff=1.920  max_channel_diff=133  source=green_07b_ai_prompt.png
07c t=259.141  mean_abs_diff=1.942  max_channel_diff=128  source=green_07c_receipt_close.png
```

This is a sampling check, not a full in-motion visual approval.

## Draft captions for v5 rough

Generated files:

- `docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_word_boundary.vtt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_word_boundary.srt`

Draft caption stats:

```text
cue_count 74
first_start 0.102
last_end 268.349
max_gap 1.058
max_cps 18.987
over18 7
over21 0
max_line_len 42
three_line_cues []
```

Fastest cues:

```text
009 030.602-032.972 cps=18.99 Use three questions to keep the signal in its
062 221.541-223.494 cps=18.95 still happen if this check is correct
026 089.117-091.682 cps=18.71 the base relationship was a useful place to look
060 215.577-218.038 cps=18.69 did it inspect the exact change that will land
052 185.391-187.345 cps=18.42 still worry me if the robot is right
033 115.195-117.591 cps=18.36 was described as mechanically mergeable with
058 209.197-211.801 cps=18.05 Fresh base did the check run against the target
```

These captions are draft-only. They restore a no-three-line-cue baseline for the v5 render, but the punctuation/idea grouping is weaker than the manual-tuned v4 caption draft. A later v5 caption pass may need to combine the v5 timing alignment with the better manual-tuned wording.

## Current decision

Do **not** upload.

Recommended next step: perform a real in-motion caption review of the v5 caption-safe final checklist, then decide whether to produce a v5 manual-tuned caption draft that keeps the caption-safe slide but restores better punctuation and quote grouping.

Current gate status remains:

```text
Audio review incomplete.
No reliable full watch/listen.
In-motion caption review incomplete.
Captions draft-only.
No final metadata/source-caveat review.
No peer-feedback disposition.
No publish-now rationale.
Do not upload.
Do not claim publish-readiness.
```
