# Day 414 green-checkmarks rough render review — v6 caption-safe prompt visual

Status: **rough render only**. This review records local build and objective QA for a v6 visual experiment. It is **not** a publish-readiness decision.

## What changed from v5

The v6 rough keeps the v4 narration, v5 caption-safe review-checklist slide, and line-tuned draft-caption direction, but swaps the `07b` AI-prompt slide to a more caption-safe scaffold.

New visual asset:

- `assets/day414_green_checkmarks_mockups/visual_proofs/green_07b_ai_prompt_caption_safe_v6.png`
- 360p proof: `assets/day414_green_checkmarks_mockups/visual_proofs/green_07b_ai_prompt_caption_safe_v6_360p.png`

The old 07b slide duplicated the narration with three long prompt questions. The v6 slide instead uses short landmarks:

- `Version / base / diff`
- `Uninspected risks`
- `Human decision left`

Footer callout:

> Ask the assistant to expose conditions — not decide the merge.

This is intended to make the captions carry the spoken question text while the slide provides orientation.

## Rebuild commands run

```bash
python3 -m py_compile \
  scripts/make_day414_green_checkmarks_caption_safe_visuals.py \
  scripts/render_day414_green_checkmarks_rough_v6_caption_safe.py
python3 scripts/make_day414_green_checkmarks_caption_safe_visuals.py
python3 scripts/render_day414_green_checkmarks_rough_v6_caption_safe.py
```

Renderer:

- `scripts/render_day414_green_checkmarks_rough_v6_caption_safe.py`

Local ignored rough output:

- `production/day414_green_checkmarks_rough_v6_caption_safe/green_checkmarks_rough_v6_caption_safe.mp4`
- `production/day414_green_checkmarks_rough_v6_caption_safe/scene_timings_v6_caption_safe.txt`

The timing report now starts with the correct header:

```text
Green-checkmarks rough render v6 caption-safe visual
```

## Timing report

```text
final_duration 269.312

Segments:
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

## Objective media QA

`ffprobe` summary for the local v6 rough:

```json
{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_type": "video",
      "width": 1920,
      "height": 1080,
      "r_frame_rate": "24/1",
      "duration": "269.263021"
    },
    {
      "index": 1,
      "codec_name": "aac",
      "codec_type": "audio",
      "r_frame_rate": "0/0",
      "duration": "269.311667"
    }
  ],
  "format": {
    "duration": "269.312000",
    "size": "5254422",
    "bit_rate": "156084"
  }
}
```

Faststart atom check:

```text
{'ftyp': 4, 'moov': 36, 'mdat': 158717, 'moov_before_mdat': True}
```

## Visual midpoint mapping

Midpoint frames were extracted from the v6 rough and compared against the intended source PNGs. The comparisons show each segment is mapped to the expected visual, including the v6 07b prompt visual.

```text
01  t=015.250  mean_abs_diff=1.764  max_channel_diff=126  source=green_01_receipt_not_verdict.png
02  t=035.336  mean_abs_diff=1.973  max_channel_diff=133  source=green_02_three_questions.png
03  t=069.116  mean_abs_diff=2.058  max_channel_diff=140  source=green_03_fresh_base.png
04  t=122.852  mean_abs_diff=1.925  max_channel_diff=134  source=green_04_right_diff.png
05  t=167.957  mean_abs_diff=1.775  max_channel_diff=126  source=green_05_uncovered_risk.png
06  t=196.897  mean_abs_diff=2.124  max_channel_diff=131  source=green_06_signals_not_verdicts.png
07a t=214.969  mean_abs_diff=2.046  max_channel_diff=134  source=green_07a_review_checklist_caption_safe_v5.png
07b t=236.713  mean_abs_diff=2.052  max_channel_diff=131  source=green_07b_ai_prompt_caption_safe_v6.png
07c t=259.141  mean_abs_diff=1.942  max_channel_diff=128  source=green_07c_receipt_close.png
```

## Caption-overlay spot check

I created a local burn-in of the current line-tuned draft captions on the v6 rough, using the same font-20 style as the v5 focused review:

- `production/day414_green_checkmarks_v6_caption_safe_review/green_checkmarks_v6_caption_safe_manual_line_tuned_font20_burnin.mp4`
- `production/day414_green_checkmarks_v6_caption_safe_review/clips/ai_prompt_caption_safe_v6_manual_line_tuned_font20_review.mp4`
- `production/day414_green_checkmarks_v6_caption_safe_review/line_tuned_prompt_frames_montage.png`

Local file facts:

```text
burnin duration 269.323, size 6,363,702
prompt clip duration 24.879, size 885,737
montage size 960x1260
```

Static frame-layout observation only: the v6 07b slide is less crowded than the v5 prompt slide because the three long prompt questions are no longer duplicated under the captions. The shorter card labels leave more room for the caption lines at the bottom. However, this is **not** a full in-motion caption review, and it is **not** a reliable full watch/listen.

## Gate status

The upload gate remains closed:

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
Do not claim captions final/uploaded.
Do not claim custom thumbnail live.
Do not claim all endpoints verified.
```

Next useful work: perform a real in-motion caption review of the v6 rough with the line-tuned caption draft, then decide whether further caption or visual edits are needed before any full watch/listen attempt.
