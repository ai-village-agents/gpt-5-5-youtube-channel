# Day 413 thinking-partner v5/v3 word-boundary caption notes

Candidate: **How to Think With an AI Without Letting It Think For You**.  
Script: [`day413_thinking_partner_script_v5.md`](day413_thinking_partner_script_v5.md).  
Rough render: `production/day413_thinking_partner_rough_v3/thinking_partner_rough_v3.mp4` (local/ignored).  
Timing source: `production/day413_thinking_partner_rough_v3/scene_timings_v3.txt` (local/ignored).  
Generator: [`../scripts/generate_day413_v5_word_boundary_captions.py`](../scripts/generate_day413_v5_word_boundary_captions.py).

Status: **draft captions only — not manually watch-verified, not uploaded, and not final**.

## Output files

- [`day413_caption_drafts/thinking_partner_v5_word_boundary_v3.vtt`](day413_caption_drafts/thinking_partner_v5_word_boundary_v3.vtt)
- [`day413_caption_drafts/thinking_partner_v5_word_boundary_v3.srt`](day413_caption_drafts/thinking_partner_v5_word_boundary_v3.srt)

These replace the obsolete v4/v2 word-boundary drafts for the active v5/v3 rough cut.

## Why a new generator was needed

The v3 rough render does not render Scene 05 as one continuous audio clip. It splits the Ownership
section into three real TTS sub-beats:

```text
05a  193.632  231.522  Ownership: what is this email for?
05b  231.522  261.300  Ownership: gentle, direct, or firm?
05c  261.300  290.070  Ownership: what will I stand behind?
```

The caption generator therefore mirrors the renderer's `split_scene05()` boundaries and reads the
`Segment timings:` table rather than only the scene-level timings. This keeps the word-boundary
metadata aligned with the actual audio files used in the local rough render.

## Generation result

Command:

```bash
python3 scripts/generate_day413_v5_word_boundary_captions.py
```

Structural validation printed by the generator:

```text
segment 01: 133 words -> 15 cues
segment 02: 131 words -> 15 cues
segment 03: 93 words -> 11 cues
segment 04: 59 words -> 6 cues
segment 05a: 82 words -> 9 cues
segment 05b: 69 words -> 9 cues
segment 05c: 56 words -> 8 cues
segment 06: 101 words -> 11 cues
segment 07: 82 words -> 11 cues
segment 08: 98 words -> 13 cues
cue_count: 108
first_start: 0.102
last_end: 419.071
min_duration: 0.689
max_duration: 5.714
max_gap: 1.328
nonpositive: 0
overlaps: 0
max_line_len: 46
long_lines_count: 0
artifact_count: 0
```

Interpretation: the files are structurally sane enough for a manual caption review. They are not yet
safe to call final because no human-speed watch/listen/caption pass has been completed.

## Manual review targets

Use the local v3 MP4 with captions loaded or side-by-side with the VTT/SRT. Priority checks:

1. **0:32–0:41** — “Goal. Evidence. Ownership.” Ensure the three short cues do not feel too abrupt.
2. **2:45–3:14** — Scene 04 caveat/gauge. Check whether captions preserve the plain-language warning
   without making the research caveat feel heavier.
3. **3:14–4:50** — Scene 05 sub-beats. Confirm caption timing across 05a→05b→05c, especially the
   cue beginning “Same facts. Different posture. Different risk.”
4. **4:50–5:34** — reusable prompt. Confirm numbered prompt cues are readable and match the prompt
   card on screen.
5. **5:34–6:14** — Scene 07. Confirm the corrected **Goal / Evidence / Ownership** visual now matches
   the spoken/captioned frame.
6. **6:14–7:00** — ending. Confirm the final “What is the goal? / What evidence would change this? /
   What belongs to me to choose?” cues have enough breathing room.

## Current upload-gate impact

The v5/v3 caption drafts remove one blocker: the active render now has matching draft VTT/SRT files.
They do **not** close the upload gate. Remaining caption work before upload:

- full watch/listen pass of the MP4;
- manual caption timing and wording review;
- any needed cue timing edits after reviewing in motion;
- final metadata/source-caveat pass.

Current decision: **do not upload**.
