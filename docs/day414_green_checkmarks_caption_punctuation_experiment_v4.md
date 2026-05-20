# Day 414 green-checkmarks v4 caption punctuation experiment

Status: alternate caption draft experiment only. These captions are not final, not uploaded, and not in-motion reviewed.

## Purpose

The standard v4 word-boundary captions are fast and clean by CPS proxy, but they lose punctuation because Edge TTS word-boundary tokens are punctuation-stripped. This experiment preserves punctuation from the script tokens while keeping Edge TTS word-boundary timing.

This is an alternate draft for review, not a replacement approval.

## Artifacts

Generator:

```text
scripts/generate_day414_green_checkmarks_v4_punctuated_captions.py
```

Caption drafts:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v4_punctuated.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v4_punctuated.srt
```

Target rough render:

```text
production/day414_green_checkmarks_rough_v4/green_checkmarks_rough_v4.mp4
```

## Method

- Use Edge TTS word-boundary offsets for timing.
- Split the original script text into display tokens with punctuation preserved.
- If the display-token count equals the word-boundary count for a segment, use the punctuated display tokens with boundary timings.
- If counts ever mismatch, fall back to boundary tokens for that segment. No fallback was printed in the tuned run.
- Increase `TARGET_CHARS` from 48 to 56 to avoid punctuation-driven over-splitting.

## Generator output

```text
segment 01: 67 words -> 8 cues
segment 02: 16 words -> 2 cues
segment 03: 136 words -> 17 cues
segment 04: 116 words -> 14 cues
segment 05: 90 words -> 12 cues
segment 06: 37 words -> 4 cues
segment 07a: 49 words -> 6 cues
segment 07b: 62 words -> 6 cues
segment 07c: 44 words -> 6 cues
cue_count: 75
first_start: 0.102
last_end: 268.349
max_gap: 1.058
max_cps: 20.06
```

## Manual readability summary

```text
cue_count 75
first_start 0.102
last_end 268.349
max_gap 1.058
max_cps 20.069
over18 16
over21 0
max_line_len 42
```

## Tradeoff versus word-boundary v4 captions

Standard v4 word-boundary draft:

```text
cue_count 74
max_cps 18.987
over18 7
over21 0
max_line_len 42
```

Punctuated v4 alternate draft:

```text
cue_count 75
max_cps 20.069
over18 16
over21 0
max_line_len 42
```

Interpretation: punctuation should improve semantic readability, especially around questions and quoted phrases, but the proxy CPS cost is real. A human/in-motion review would need to choose between the cleaner CPS profile and the clearer punctuation.

## Fastest cues to review

```text
043 151.694-153.438 dur=1.744 cps=20.07 text=still happen if the check is right?
035 122.448-125.208 dur=2.760 cps=19.57 text=The diff inserted new entries before an already-merged
059 209.574-212.439 dur=2.865 cps=19.55 text=base: did the check run against the target I am about to
025 088.453-091.318 dur=2.865 cps=19.55 text=It does mean the base relationship was a useful place to
063 221.827-223.494 dur=1.667 cps=19.20 text=happen if this check is correct?
074 263.362-265.471 dur=2.109 cps=18.97 text=Let the green check speed up the review.
069 244.804-248.098 dur=3.294 cps=18.82 text=But it can slow the moment down so the evidence stays visible.
```

## Gate

Upload gate remains closed.

Do not claim either caption set is final. Do not upload without full watch/listen, in-motion caption review, metadata/source-caveat review, and publish-now rationale.
