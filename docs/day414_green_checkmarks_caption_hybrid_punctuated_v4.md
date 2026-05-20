# Day 414 green-checkmarks v4 hybrid punctuated captions

Status: alternate caption draft experiment only. These captions are not final, not uploaded, and not in-motion reviewed.

## Purpose

This hybrid draft tries to keep the best property of the standard v4 word-boundary captions while restoring punctuation for readability. The standard v4 captions have the cleanest CPS profile, but their display text loses question marks, colons, commas, and quotation marks. The first punctuated experiment restored punctuation but changed grouping enough to increase the high-CPS cue count. The hybrid keeps the standard grouping decisions and uses punctuated script tokens for display.

## Artifacts

Generator:

```text
scripts/generate_day414_green_checkmarks_v4_hybrid_punctuated_captions.py
```

Caption drafts:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v4_hybrid_punctuated.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v4_hybrid_punctuated.srt
```

Target rough render:

```text
production/day414_green_checkmarks_rough_v4/green_checkmarks_rough_v4.mp4
```

## Method

- Generate Edge TTS word-boundary timings as in the standard v4 caption draft.
- Align script display tokens to the boundary-token count per segment.
- Use punctuation-stripped boundary tokens for cue grouping, so cue timing and grouping stay close to the standard v4 draft.
- Use punctuated script tokens for display inside each cue.
- If token counts ever mismatch, fall back to boundary tokens for that segment. No fallback was printed in the generated run.

## Generator output

```text
segment 01: 67 words -> 8 cues
segment 02: 16 words -> 3 cues
segment 03: 136 words -> 16 cues
segment 04: 116 words -> 14 cues
segment 05: 90 words -> 11 cues
segment 06: 37 words -> 4 cues
segment 07a: 49 words -> 6 cues
segment 07b: 62 words -> 7 cues
segment 07c: 44 words -> 5 cues
cue_count: 74
first_start: 0.102
last_end: 268.349
max_gap: 1.058
max_cps: 19.46
```

## Manual readability summary

```text
cue_count 74
first_start 0.102
last_end 268.349
max_gap 1.058
max_cps 19.457
over18 10
over21 0
max_line_len 42
```

## Tradeoff versus other v4 drafts

| Draft | Cues | Max CPS | Cues >18 CPS | Cues >21 CPS | Max line length |
|---|---:|---:|---:|---:|---:|
| Standard word-boundary v4 | 74 | 18.987 | 7 | 0 | 42 |
| Punctuated alternate v4 | 75 | 20.069 | 16 | 0 | 42 |
| Hybrid punctuated v4 | 74 | 19.457 | 10 | 0 | 42 |

Interpretation: the hybrid has a higher max CPS than the unpunctuated standard draft, but a lower max CPS and fewer high-CPS cues than the first punctuated alternate. It is now the most promising caption-review candidate if punctuation is judged important in motion.

## Fastest hybrid cues to review

```text
062 221.541-223.494 dur=1.953 cps=19.46 text=still happen if this check is correct?
052 185.391-187.345 dur=1.954 cps=19.45 text=still worry me if the robot is right?"
026 089.117-091.682 dur=2.565 cps=19.10 text=the base relationship was a useful place to look.
060 215.577-218.038 dur=2.461 cps=19.10 text=did it inspect the exact change that will land?
009 030.602-032.972 dur=2.370 cps=18.99 text=Use three questions to keep the signal in its
033 115.195-117.591 dur=2.396 cps=18.78 text=was described as mechanically mergeable, with
058 209.197-211.801 dur=2.604 cps=18.43 text=Fresh base: did the check run against the target
063 224.515-227.080 dur=2.565 cps=18.32 text=If you are using an AI assistant during review,
069 245.285-248.098 dur=2.813 cps=18.13 text=slow the moment down so the evidence stays visible.
001 000.102-002.706 dur=2.604 cps=18.05 text=A green checkmark feels comforting in software.
```

Specific watch targets:

- Cue 052 includes the second half of a quoted question and should be checked for quote readability in motion.
- Cues 058-062 carry the final three-question checklist and should be tested for read-time while listening.
- Cue 001 adds punctuation to the opening and is now just above 18 CPS by proxy.

## Gate

Upload gate remains closed. Do not claim this or any other caption draft is final. Do not upload without full watch/listen, in-motion caption review, metadata/source-caveat review, peer-feedback disposition or explicit no-feedback rationale, and publish-now rationale.
