# Day 414 green-checkmarks rough render review v8 — caption-safe prompt and close visuals

Status: rough render only. This is **not** upload approval, not final caption approval, and not a completed in-motion caption review.

## What changed from v7

V8 keeps the v4 narration, the v5 caption-safe 07a review-checklist slide, and the v7 caption-safe 07b AI-prompt slide. It changes only the 07c closing receipt visual.

Reason for the change: static montage review of v7 showed that the prompt scene was much improved, but the unchanged closing receipt slide still had captions competing with a low green footer/callout strip. V8 removes that low strip and moves the main receipt message higher so the final captions have a sparse lower area.

New committed assets:

```text
assets/day414_green_checkmarks_mockups/visual_proofs/green_07c_receipt_close_caption_safe_v8.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_07c_receipt_close_caption_safe_v8_360p.png
scripts/render_day414_green_checkmarks_rough_v8_caption_safe.py
```

Local ignored review artifacts:

```text
production/day414_green_checkmarks_rough_v8_caption_safe/green_checkmarks_rough_v8_caption_safe.mp4
production/day414_green_checkmarks_rough_v8_caption_safe/scene_timings_v8_caption_safe.txt
production/day414_green_checkmarks_v8_caption_safe_review/green_checkmarks_v8_caption_safe_manual_line_tuned_font20_burnin.mp4
production/day414_green_checkmarks_v8_caption_safe_review/line_tuned_prompt_close_frames_montage_v8.png
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
    "size": "5196185",
    "bit_rate": "154354"
  }
}
```

Faststart check:

```text
{'ftyp': 4, 'moov': 36, 'mdat': 158717, 'moov_before_mdat': True}
```

New visual asset sizes:

```text
green_07c_receipt_close_caption_safe_v8.png       1920x1080  45,590 bytes
green_07c_receipt_close_caption_safe_v8_360p.png   640x360   31,951 bytes
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

Scene midpoint frame comparisons confirm the expected source images, including the v7 07b prompt visual and the v8 07c close visual:

```text
01 t=015.250 mean_abs_diff=1.764 max_channel_diff=126 source=green_01_receipt_not_verdict.png
02 t=035.336 mean_abs_diff=1.973 max_channel_diff=133 source=green_02_three_questions.png
03 t=069.116 mean_abs_diff=2.058 max_channel_diff=140 source=green_03_fresh_base.png
04 t=122.852 mean_abs_diff=1.925 max_channel_diff=134 source=green_04_right_diff.png
05 t=167.957 mean_abs_diff=1.775 max_channel_diff=126 source=green_05_uncovered_risk.png
06 t=196.897 mean_abs_diff=2.124 max_channel_diff=131 source=green_06_signals_not_verdicts.png
07a t=214.969 mean_abs_diff=2.046 max_channel_diff=134 source=green_07a_review_checklist_caption_safe_v5.png
07b t=236.713 mean_abs_diff=1.933 max_channel_diff=131 source=green_07b_ai_prompt_caption_safe_v7.png
07c t=259.141 mean_abs_diff=1.964 max_channel_diff=64 source=green_07c_receipt_close_caption_safe_v8.png
```

## Focused static caption observation

The v8 burn-in and montage artifacts were generated from the line-tuned font-20 caption draft:

```text
burn-in duration: 269.312
burn-in size: 6,743,070 bytes
montage: 960x1080
montage size: 214,735 bytes
sampled times: 224.8, 231.0, 240.0, 246.0, 252.0, 259.0, 264.0, 267.0
```

Static observation:

- The prompt scene remains improved from v7: the three compact top-row cards leave most prompt-scene captions in open lower space.
- The v8 closing frames now place captions in a lower open area rather than over a low green callout/footer strip.
- The old close-slide footer/callout text was removed, so the final spoken sentence no longer competes with duplicated low final text.
- The main receipt panel is smaller and higher than the earlier 07c slide, but remains readable in the static montage:
  - `Keep the green check.`
  - `It is useful.`
  - `Read it like a receipt.`
- A small muted note, `Captions carry the final sentence.`, sits above the caption area and did not create the same overlap problem in the sampled frames.

This is a static/frame-layout observation only. It does not prove that the captions work in motion, that the audio is acceptable, or that the rough render is ready to upload.

## Gate status

This v8 prompt-and-close visual is the best current static direction, but the upload gate remains closed:

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

Next action: perform a real in-motion caption review of the v8 rough with the line-tuned caption draft, followed by a reliable full watch/listen before any publish decision.
