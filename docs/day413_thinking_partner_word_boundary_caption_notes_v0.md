# Day 413 thinking-partner word-boundary caption notes v0

Source script: [`day413_thinking_partner_script_v4.md`](day413_thinking_partner_script_v4.md).  
Rough render: `production/day413_thinking_partner_rough_v2/thinking_partner_rough_v2.mp4`.  
Timing source: `production/day413_thinking_partner_rough_v2/scene_timings_v2.txt`.

Caption files:

- [`day413_caption_drafts/thinking_partner_v4_word_boundary_v2.vtt`](day413_caption_drafts/thinking_partner_v4_word_boundary_v2.vtt)
- [`day413_caption_drafts/thinking_partner_v4_word_boundary_v2.srt`](day413_caption_drafts/thinking_partner_v4_word_boundary_v2.srt)

Generator:

- [`../scripts/generate_day413_word_boundary_captions.py`](../scripts/generate_day413_word_boundary_captions.py)

Status: **draft only — not final, not uploaded, and not manually verified against playback**.

## What changed from the previous rough captions

The earlier v4 rough captions used actual scene start/end times, but allocated cue timing
inside each scene by text length. That made the files structurally useful but only loosely
synchronized.

This pass uses Edge TTS `WordBoundary` metadata for the same voice and rate used by the v2
rough render:

- voice: `en-US-GuyNeural`
- rate: `-4%`
- boundary: `WordBoundary`

The generator collects word offsets for each scene, adds the measured scene start time, restores
script punctuation for readability, and groups timestamped words into caption cues. The result is
better grounded in the generated narration than the proportional-caption draft, but it still needs
a real watch/listen check before any upload.

## Validation summary

Generator output:

```text
scene 01: 133 words -> 14 cues
scene 02: 131 words -> 15 cues
scene 03: 93 words -> 12 cues
scene 04: 74 words -> 8 cues
scene 05: 167 words -> 18 cues
scene 06: 101 words -> 11 cues
scene 07: 82 words -> 11 cues
scene 08: 84 words -> 10 cues
cue_count: 99
first_start: 0.102
last_end: 405.544
min_duration: 0.966
max_duration: 5.740
max_gap: 1.330
nonpositive: 0
overlaps: 0
```

Additional structural check:

```text
cue_count 99
nonpositive 0
overlaps 0
max_gap 1.330
max_line_len 46
long_lines_count 0
artifact_count 0
last_end 405.544
```

The `max_gap` is expected because the TTS render has sentence-level pauses and the captions do
not force text to stay on screen through every pause. This is acceptable for a draft but should be
checked during playback.

## Manual-review targets

Before any upload, check at least these regions in the MP4:

1. **0:32–0:41** — “Goal. Grounding. Ownership.” The cue timing is now based on word-boundary
   metadata, but the triplet should be checked for comfortable reading.
2. **2:50–3:26** — the Scene 04 caveat/gauge. Claude's feedback says the gauge helps credibility
   but the section may slow momentum.
3. **3:26–4:43** — the Ownership/email example. Scene 05 is the longest static stretch and should
   probably be split into sub-beats before upload.
4. **4:43–5:08** — the reusable prompt. The numbered lines are separated into readable cues, but
   this is the highest-risk section for caption/visual timing mismatch.
5. **6:08–6:46** — the ending. The captions are structurally clean; the script may need a stronger
   “what you keep vs. what you delegate” close to satisfy the title promise.

## Upload-gate impact

This improves the caption artifact from “rough scene-proportional timing” to “draft word-boundary
timing,” but it does **not** close the caption gate. Captions are not final until they have been
watched/listened against the actual MP4 and adjusted if needed.

Do not describe these files as final captions or YouTube-published captions.
