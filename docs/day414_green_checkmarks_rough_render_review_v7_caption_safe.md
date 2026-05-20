# Day 414 green-checkmarks rough render review v7 — caption-safe prompt visual

Status: rough render only. This is **not** upload approval, not final caption approval, and not a completed in-motion caption review.

## What changed from v6

V7 keeps the v4 narration, v5 caption-safe 07a review-checklist slide, and v6 timing grid. It changes only the 07b AI-prompt visual.

Reason for the change: static cue-midpoint review of v6 showed that the prompt scaffold was much better than v5, but burned-in captions still overlapped the lower stacked prompt card and the green callout strip. V7 moves the three prompt concepts into compact top-row cards and leaves a larger sparse lower area for captions.

New committed assets:

```text
assets/day414_green_checkmarks_mockups/visual_proofs/green_07b_ai_prompt_caption_safe_v7.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_07b_ai_prompt_caption_safe_v7_360p.png
scripts/render_day414_green_checkmarks_rough_v7_caption_safe.py
```

Local ignored review artifacts:

```text
production/day414_green_checkmarks_rough_v7_caption_safe/green_checkmarks_rough_v7_caption_safe.mp4
production/day414_green_checkmarks_rough_v7_caption_safe/scene_timings_v7_caption_safe.txt
production/day414_green_checkmarks_v7_caption_safe_review/green_checkmarks_v7_caption_safe_manual_line_tuned_font20_burnin.mp4
production/day414_green_checkmarks_v7_caption_safe_review/clips/ai_prompt_caption_safe_v7_manual_line_tuned_font20_review.mp4
production/day414_green_checkmarks_v7_caption_safe_review/line_tuned_prompt_frames_montage_v7.png
```

## Objective render facts

`ffprobe` summary:

```json
{
  "streams": [
    {
      "codec_name": "h264",
      "codec_type": "video",
      "width": 1920,
      "height": 1080,
      "r_frame_rate": "24/1",
      "duration": "269.263021"
    },
    {
      "codec_name": "aac",
      "codec_type": "audio",
      "duration": "269.311667"
    }
  ],
  "format": {
    "duration": "269.312000",
    "size": "5217897",
    "bit_rate": "154999"
  }
}
```

Faststart check:

```text
{'ftyp': 4, 'moov': 36, 'mdat': 158717, 'moov_before_mdat': True}
```

New visual asset sizes:

```text
green_07b_ai_prompt_caption_safe_v7.png       1920x1080  54,275 bytes
green_07b_ai_prompt_caption_safe_v7_360p.png   640x360   45,337 bytes
```

Timing report summary:

```text
final_duration 269.312
01 000.000-030.500  A green check is evidence, not a verdict
02 030.500-040.172  Fresh base, right diff, uncovered risk
03 040.172-098.060  Fresh base: did the target move?
04 098.060-147.644  Right diff: what change will land?
05 147.644-188.269  Uncovered risk: what did it not inspect?
06 188.269-205.525  Signals are not verdicts
07a 205.525-224.413  Checklist: read the receipt
07b 224.413-249.013  Ask the AI to slow the moment down
07c 249.013-269.269  Keep the check, keep the question
```

## Midpoint visual mapping

Scene midpoint frame comparisons confirm the expected source images, including the v7 07b prompt visual:

```text
01 t=015.250 mean_abs_diff=1.764 max_channel_diff=126 source=green_01_receipt_not_verdict.png
02 t=035.336 mean_abs_diff=1.973 max_channel_diff=133 source=green_02_three_questions.png
03 t=069.116 mean_abs_diff=2.058 max_channel_diff=140 source=green_03_fresh_base.png
04 t=122.852 mean_abs_diff=1.925 max_channel_diff=134 source=green_04_right_diff.png
05 t=167.957 mean_abs_diff=1.775 max_channel_diff=126 source=green_05_uncovered_risk.png
06 t=196.897 mean_abs_diff=2.124 max_channel_diff=131 source=green_06_signals_not_verdicts.png
07a t=214.969 mean_abs_diff=2.046 max_channel_diff=134 source=green_07a_review_checklist_caption_safe_v5.png
07b t=236.713 mean_abs_diff=1.933 max_channel_diff=131 source=green_07b_ai_prompt_caption_safe_v7.png
07c t=259.141 mean_abs_diff=1.942 max_channel_diff=128 source=green_07c_receipt_close.png
```

## Focused static caption observation

A focused prompt-scene montage sampled these times:

```text
224.8, 227.0, 231.0, 235.0, 240.0, 242.0, 246.0, 259.0
```

Static observation:

- The v7 prompt cards sit high enough that prompt-scene captions mostly land in open space below the cards.
- This is an improvement over v6, where several prompt-scene captions overlapped the lower `Human decision left` card and the green callout strip.
- V7 removes the v6 green callout strip, so the prompt captions no longer compete with that extra text.
- The closing receipt slide is unchanged; captions still overlap the low footer strip there, but not the main `Keep the green check`, `It is useful`, or `Just read it like a receipt` lines in the sampled frame.

## Gate status

This v7 prompt visual is the best current static direction for the 07b scene, but the upload gate remains closed:

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
```

Next action: if possible, perform a real in-motion caption review of the v7 rough with the line-tuned caption draft, followed by a reliable full watch/listen before any publish decision.
