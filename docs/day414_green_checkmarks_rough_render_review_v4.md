# Day 414 green-checkmarks rough render review v4

Status: local rough-render review only. Not upload-approved.

## Artifact

Local ignored render:

```text
production/day414_green_checkmarks_rough_v4/green_checkmarks_rough_v4.mp4
production/day414_green_checkmarks_rough_v4/scene_timings_v4.txt
```

Renderer:

```text
scripts/render_day414_green_checkmarks_rough_v4.py
```

Script:

```text
docs/day414_green_checkmarks_script_v4.md
```

V4 starts from the v3 script experiment and fixes the caption-regression lines found there. It keeps the same visual pacing pattern as v1/v2.

## ffprobe summary

```json
{
  "video_duration": 269.263021,
  "audio_duration": 269.311667,
  "format_duration": 269.312000,
  "size": 5293506,
  "bit_rate": 157245
}
```

Faststart atom check:

```text
ftyp at 4
moov at 36
mdat at 158717
moov_before_mdat True
```

## Segment timings

```text
Green-checkmarks rough render v4

final_duration 269.312

Segments:
01  000.000  030.500  clip=30.500  audio=30.480  words= 67  A green check is evidence, not a verdict
02  030.500  040.172  clip=09.672  audio=09.672  words= 16  Fresh base, right diff, uncovered risk
03  040.172  098.060  clip=57.888  audio=57.888  words=136  Fresh base: did the target move?
04  098.060  146.269  clip=48.209  audio=48.192  words=116  Right diff: what change will land?
05  146.269  187.394  clip=41.125  audio=41.112  words= 90  Uncovered risk: what did it not inspect?
06  187.394  204.650  clip=17.256  audio=17.256  words= 37  Signals are not verdicts
07a 204.650  223.778  clip=19.128  audio=19.128  words= 49  Checklist: read the receipt
07b 223.778  249.070  clip=25.292  audio=25.272  words= 62  Ask the AI to slow the moment down
07c 249.070  269.326  clip=20.256  audio=20.256  words= 44  Keep the check, keep the question

Status: rough render only; no full watch/listen, no caption review, no upload approval.
```

## Review notes

- V4 is about 2.8 seconds longer than v2 because several dense ideas were split into separate spoken beats.
- The v4 caption draft is substantially cleaner than v2/v3 by proxy metrics: no cues above 21 CPS and max CPS below 19.
- The render is still static-slide based. Scene-level visual pacing has not been watch-reviewed.
- No reliable audio listen has been completed.
- No in-motion caption review has been completed.

## Gate

Upload gate remains closed.

Do not upload from this artifact.
Do not claim publish-readiness.
Do not claim captions final or uploaded.
