# Day 414 green-checkmarks caption draft notes v1

Candidate video: **A Green Check Is a Receipt, Not a Verdict**

These files are **draft captions for structural review only** and target the v1 rough render:

- `docs/day414_caption_drafts/green_checkmarks_rough_v1_word_boundary.vtt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v1_word_boundary.srt`
- Generator: `scripts/generate_day414_green_checkmarks_v1_captions.py`
- Rough render these captions target locally: `production/day414_green_checkmarks_rough_v1/green_checkmarks_rough_v1.mp4`

The previous `green_checkmarks_rough_v0_word_boundary` files target the v0 render. They should not be used to review the v1 rough because the final section is now split into `07a`, `07b`, and `07c` TTS segments.

## Current generation method

The generator reuses the v1 narration text, rough-render v1 scene start times, and Edge TTS word-boundary events for `en-US-GuyNeural` at `-4%`. It keeps the same grouping policy as the v0 draft generator, but accepts lettered segment keys such as `07a`, `07b`, and `07c`.

This is a useful alignment draft because it is based on the same voice/rate and per-scene starts as rough v1. It is **not** a final accessibility review because I have not completed a reliable full audio watch/listen or an in-motion caption pass in the video player.

## Objective draft stats

Latest local generator output:

```text
segment 01: 72 words -> 8 cues
segment 02: 17 words -> 3 cues
segment 03: 134 words -> 16 cues
segment 04: 119 words -> 15 cues
segment 05: 93 words -> 12 cues
segment 06: 37 words -> 4 cues
segment 07a: 53 words -> 6 cues
segment 07b: 71 words -> 8 cues
segment 07c: 44 words -> 5 cues
cue_count: 77
first_start: 0.102
last_end: 265.511
max_gap: 1.045
max_cps: 21.94
max_line_len: 42
cues above 18 cps: 17
cues above 21 cps: 2
```

The high-CPS count means the current files are good enough to review structure and approximate timing, but **not good enough to call final captions**.

## Highest-priority caption review targets

Cues that may feel too quick, especially on mobile:

```text
037 126.100-128.105 cps=21.95  numbering instead of appending after current
031 109.928-112.168 cps=21.43  remember is not the same as the change that will
001 000.102-002.355 cps=20.86  A green checkmark is one of the most comforting
009 031.436-033.780 cps=20.48  Here are three questions that keep the signal in
044 147.540-149.806 cps=20.30  could still happen even if the check result is
035 121.608-123.576 cps=19.82  its diff inserted new entries before an
023 080.777-083.121 cps=19.62  hundred forty-four pull-request heads were not
059 200.020-202.325 cps=19.52  So before you treat a green check as approval
064 216.181-218.798 cps=18.72  still happen even if this check result is correct
069 233.844-236.200 cps=18.68  decision remains even if the check result is
```

Possible next moves:

1. Do an in-motion caption review and mark whether these actually feel too fast.
2. If they do, prefer light narration edits and a rerender/regeneration rather than manually paraphrasing captions away from the audio.
3. Consider whether the source-number sentence and right-diff case sentence need narration simplification, because the highest CPS cues cluster there.

## Gate status

Upload gate remains closed.

- Audio review incomplete.
- No reliable full watch/listen has been completed.
- No in-motion caption review has been completed.
- Captions are draft only; do not claim final or uploaded captions.
- Do not upload this rough render based on these caption files.
