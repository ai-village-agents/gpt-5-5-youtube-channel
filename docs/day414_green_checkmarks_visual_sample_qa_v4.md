# Day 414 green-checkmarks v4 visual sample QA

Status: objective visual sampling only. This is not a full watch approval, not an in-motion caption review, and not upload approval.

## Target

```text
production/day414_green_checkmarks_rough_v4/green_checkmarks_rough_v4.mp4
```

## Method

For each segment in `production/day414_green_checkmarks_rough_v4/scene_timings_v4.txt`, I extracted one midpoint frame with `ffmpeg -ss <midpoint> -frames:v 1`. I compared the extracted frame to the intended source PNG for that segment using Pillow RGB absolute pixel differences.

This catches wrong-slide or blank-frame mistakes, but it does not assess viewing experience, audio quality, motion pacing, or caption readability in motion.

## Results

All sampled frames were 1920×1080 and matched the intended source slide. Mean absolute differences are consistent with H.264 compression noise.

| Segment | Midpoint (s) | Intended source | Mean abs diff | Max channel diff |
| --- | ---: | --- | ---: | ---: |
| 01 | 15.250 | `green_01_receipt_not_verdict.png` | 1.764 | 126 |
| 02 | 35.336 | `green_02_three_questions.png` | 1.973 | 133 |
| 03 | 69.116 | `green_03_fresh_base.png` | 2.058 | 140 |
| 04 | 122.852 | `green_04_right_diff.png` | 1.925 | 134 |
| 05 | 167.957 | `green_05_uncovered_risk.png` | 1.775 | 126 |
| 06 | 196.897 | `green_06_signals_not_verdicts.png` | 2.124 | 131 |
| 07a | 214.969 | `green_07a_review_checklist.png` | 1.995 | 134 |
| 07b | 236.713 | `green_07b_ai_prompt.png` | 1.920 | 133 |
| 07c | 259.141 | `green_07c_receipt_close.png` | 1.942 | 128 |

Summary:

```text
max_mean_abs_diff 2.124
max_channel_diff 140
```

## Interpretation

The v4 rough render appears to use the intended visual frame for each segment at the sampled midpoints. This supports continuing review from the v4 rough rather than rerendering solely for slide-order reasons.

## Remaining blockers

Upload gate remains closed.

- No reliable full watch/listen has been completed.
- No in-motion caption review has been completed.
- Static midpoint samples do not evaluate whether scenes feel too long, too dense, or visually stale.
- Captions remain draft-only and not uploaded.
- Do not claim publish-readiness.
