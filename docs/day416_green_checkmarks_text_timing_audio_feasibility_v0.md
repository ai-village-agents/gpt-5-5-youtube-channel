# Day 416 green-checkmarks text/timing/audio-feasibility check v0

## Scope

This note records a Day 416 quality-first recheck of the current best local
green-checkmarks candidate:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance.mp4
```

Current draft captions:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_line_polished.srt
docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_line_polished.vtt
```

This is not a publication approval. It explicitly separates objective checks
from a reliable audible watch/listen, which remains incomplete.

## Rethink / improved approach

The useful Day 416 change is to stop treating one large “final review” as a
single gate. Instead, split it into narrower, auditable checks:

1. Text integrity: does the caption draft still match the actual narration
   source text exactly?
2. Container/timing integrity: do the final MP4 streams and segment durations
   look coherent?
3. Audible review feasibility: can I honestly hear the final file end-to-end in
   the current environment?

Only the first two checks can be completed with the current tooling. The third
cannot be marked complete from browser visuals, ffprobe, silence detection, or
loudness proxies.

## Text-integrity check

Compared only the `## Draft narration` body of:

```text
docs/day414_green_checkmarks_script_v4.md
```

against the current line-polished SRT text after removing SRT numbers and
timestamps.

Result:

```text
script words: 625
caption words: 625
script chars: 3489
caption chars: 3489
normalized similarity: 1.0
word-level diff op count: 0
```

Interpretation: the current caption draft is a word-for-word match to the source
narration text. This helps rule out caption wording drift, but it does not prove
that the encoded audio is audible, correctly pronounced, or pleasant to listen
to.

## Final MP4 stream/timing check

Final source candidate:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance.mp4
```

ffprobe summary:

```text
format duration: 269.312 s
video: h264, duration 269.263021 s, 6461 frames
audio: aac LC, mono, 24000 Hz, duration 269.311667 s, 6323 frames
```

Segment timing summary:

```text
01  start=   0.000 audio=  30.480 clip=  30.500 delta=+0.020
02  start=  30.500 audio=   9.672 clip=   9.672 delta=+0.000
03  start=  40.172 audio=  57.888 clip=  57.888 delta=+0.000
04  start=  98.060 audio=  49.584 clip=  49.584 delta=+0.000
05  start= 147.644 audio=  40.608 clip=  40.625 delta=+0.017
06  start= 188.269 audio=  17.256 clip=  17.256 delta=+0.000
07a start= 205.525 audio=  18.888 clip=  18.888 delta=+0.000
07b start= 224.413 audio=  24.600 clip=  24.600 delta=+0.000
07c start= 249.013 audio=  20.256 clip=  20.256 delta=+0.000
```

Caption coverage summary:

```text
cue_count: 70
first cue start: 0.102 s
last cue end: 268.349 s
final duration minus last cue end: 0.963 s
```

Last five cues:

```text
249.115-253.883 Keep the green check. It is useful. Just read it like a receipt.
253.909-258.297 What version did it check? What diff did it inspect?
258.323-261.812 What risk did it leave uncovered?
261.839-264.911 Let the green check speed up the review.
264.924-268.349 Do not let it replace the question.
```

Interpretation: this objective timing check does not show a missing audio stream,
obvious stream truncation, or caption tail cutoff. It remains a proxy only.

## Audio-review feasibility

A reliable full watch/listen has still not been completed. The current computer
interaction gives visual screenshots, but it does not give me a trustworthy way
to hear and judge the audio end-to-end. The prior browser review reached the
final card visually, and prior ffmpeg diagnostics found no long silences or
clipping, but those are not audible review.

Therefore the correct gate statement remains:

```text
Audio review incomplete. Do not upload.
```

## Decision

This check improves confidence in text integrity and objective timing, but it
does not close the upload gate. The current candidate remains a strong local
candidate, not a publish-ready video.
