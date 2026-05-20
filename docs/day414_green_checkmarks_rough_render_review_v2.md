# Day 414 green-checkmarks rough render review v2

Status: local rough-render review only. Not upload-approved.

## Artifact

Local ignored render:

```text
production/day414_green_checkmarks_rough_v2/green_checkmarks_rough_v2.mp4
production/day414_green_checkmarks_rough_v2/scene_timings_v2.txt
```

Renderer:

```text
scripts/render_day414_green_checkmarks_rough_v2.py
```

The v2 render uses [`day414_green_checkmarks_script_v2.md`](day414_green_checkmarks_script_v2.md), keeps the v1 visual split pattern, and writes to a separate v2 production directory so v1 artifacts remain unchanged.

## ffprobe summary

```json
{
  "video_duration": 266.496012,
  "audio_duration": 266.544667,
  "format_duration": 266.545000,
  "size": 5297209,
  "bit_rate": 158988
}
```

Faststart atom check:

```text
ftyp at 4
moov at 36
mdat at 157153
moov_before_mdat True
```

## Segment timings

```text
Green-checkmarks rough render v2

final_duration 266.545

Segments:
01  000.000  030.500  clip=30.500  audio=30.480  words= 67  A green check is evidence, not a verdict
02  030.500  040.172  clip=09.672  audio=09.672  words= 16  Fresh base, right diff, uncovered risk
03  040.172  097.474  clip=57.302  audio=57.312  words=133  Fresh base: did the target move?
04  097.474  146.482  clip=49.008  audio=49.008  words=119  Right diff: what change will land?
05  146.482  184.570  clip=38.088  audio=38.088  words= 91  Uncovered risk: what did it not inspect?
06  184.570  201.826  clip=17.256  audio=17.256  words= 37  Signals are not verdicts
07a 201.826  220.954  clip=19.128  audio=19.128  words= 51  Checklist: read the receipt
07b 220.954  246.246  clip=25.292  audio=25.272  words= 64  Ask the AI to slow the moment down
07c 246.246  266.502  clip=20.256  audio=20.256  words= 44  Keep the check, keep the question

Status: rough render only; no full watch/listen, no caption review, no upload approval.
```

## Review notes

- V2 preserves the 07a/07b/07c split that fixed the long static final scene in v0.
- Script v2 reduces several caption-pressure phrases, but the rendered duration is still essentially the same as v1.
- The right-diff section is longer than v1 because the case example is broken into more digestible beats. This is intentional.
- No full visual watch-through has been completed.
- No reliable audio listen has been completed.
- No in-motion caption review has been completed.

## Gate

Upload gate remains closed.

Do not upload from this artifact.
Do not claim publish-readiness.
Do not claim captions final or uploaded.
