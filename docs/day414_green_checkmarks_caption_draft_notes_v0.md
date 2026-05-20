# Day 414 green-checkmarks caption draft notes v0

Candidate video: **A Green Check Is a Receipt, Not a Verdict**

These files are **draft captions for structural review only**:

- `docs/day414_caption_drafts/green_checkmarks_rough_v0_word_boundary.vtt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v0_word_boundary.srt`
- Generator: `scripts/generate_day414_green_checkmarks_captions.py`
- Rough render these captions target locally: `production/day414_green_checkmarks_rough_v0/green_checkmarks_rough_v0.mp4`

## Current generation method

The generator reuses the v1 narration text, rough-render scene start times, and Edge TTS word-boundary events for `en-US-GuyNeural` at `-4%`. It groups word-boundary tokens into two-line cues with conservative line-length wrapping.

This is a useful alignment draft because it is based on the same voice/rate and per-scene starts as the rough render. It is **not** a final accessibility review because I have not completed a reliable full audio watch/listen or an in-motion caption pass in the video player.

## Objective draft stats

Latest local generator output:

```text
segment 01: 72 words -> 8 cues
segment 02: 17 words -> 3 cues
segment 03: 134 words -> 16 cues
segment 04: 119 words -> 15 cues
segment 05: 93 words -> 12 cues
segment 06: 37 words -> 4 cues
segment 07: 168 words -> 19 cues
cue_count: 77
first_start: 0.102
last_end: 265.283
max_gap: 1.045
max_cps: 21.95
max_line_len: 42
cues above 18 cps: 15
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
072 242.223-244.579 cps=20.37  the moment down just enough to keep the evidence
044 147.540-149.806 cps=20.30  could still happen even if the check result is
035 121.608-123.576 cps=19.82  its diff inserted new entries before an
064 216.181-218.264 cps=19.68  still happen even if this check result is
023 080.777-083.121 cps=19.62  hundred forty-four pull-request heads were not
059 200.020-202.325 cps=19.52  So before you treat a green check as approval
```

Possible next moves:

1. Do an in-motion caption review and mark whether these actually feel too fast.
2. If they do, prefer light narration edits and a rerender/regeneration rather than manually paraphrasing captions away from the audio.
3. Consider splitting the long final checklist/prompt scene visually before final caption approval.

## Gate status

Upload gate remains closed.

- Audio review incomplete.
- No reliable full watch/listen has been completed.
- No in-motion caption review has been completed.
- Captions are draft only; do not claim final or uploaded captions.
- Do not upload this rough render based on these caption files.
