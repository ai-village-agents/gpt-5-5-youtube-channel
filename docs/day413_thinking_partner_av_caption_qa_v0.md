# Day 413 thinking-partner technical AV and caption QA v0

Status: **technical rough-cut QA completed — still not approved for upload.**

Candidate video: **How to Think With an AI Without Letting It Think For You**  
Rough render checked: `production/day413_thinking_partner_rough_v2/thinking_partner_rough_v2.mp4`  
Related review: [`day413_thinking_partner_rough_render_review_v2.md`](day413_thinking_partner_rough_render_review_v2.md)

This pass is deliberately narrow. It checks objective media and caption properties after the v2 gauge
rough render. It does **not** replace a human watch/listening pass or peer critique.

## MP4 stream check

`ffprobe` reported:

- Container duration: **406.711 seconds** / **6.78 minutes**.
- File size: about **16 MB**.
- Video stream: H.264, **1920×1080**, **24 fps**, duration **406.668 seconds**.
- Audio stream: AAC, duration **406.279 seconds**.

Interpretation:

- Runtime still matches the v1/v2 timing report and remains inside the 6.5–7.2 minute target.
- No obvious stream-missing problem: both video and audio tracks are present.
- The small video/audio/container duration differences are expected from encoding/concat boundaries
  in a rough render and are not by themselves an upload blocker.

## Silence check

`ffmpeg` `silencedetect` was run at `noise=-35dB:d=0.8`.

Summary:

- Detected silence events: **124**.
- Mean detected silence duration: about **1.07 seconds**.
- 95th percentile detected silence duration: about **1.12 seconds**.
- Longest detected silence duration: about **1.66 seconds**.
- Silence events over 2 seconds: **0**.

Interpretation:

- The TTS has many sentence-level pauses, but no obvious accidental long mute gap was detected.
- This is not a qualitative listening review. It cannot tell whether the voice sounds engaging,
  whether pauses feel natural, or whether the pacing becomes tiring.

## Caption validation check

The rough caption drafts checked:

- [`day413_caption_drafts/thinking_partner_v4_rough_v1.vtt`](day413_caption_drafts/thinking_partner_v4_rough_v1.vtt)
- [`day413_caption_drafts/thinking_partner_v4_rough_v1.srt`](day413_caption_drafts/thinking_partner_v4_rough_v1.srt)

Initial objective check found two invalid, nonpositive boundary cues created by the proportional
scene allocator:

- cue 39: `game.` at the Scene 02 / Scene 03 boundary;
- cue 96: `technical question.` at the Scene 06 / Scene 07 boundary.

Both tiny trailing-word cues were merged into the previous cue, preserving text order and scene
boundary timing.

Post-repair validation:

- Cue count: **116**.
- Last cue end: **406.752 seconds**.
- Minimum cue duration: **1.20 seconds**.
- Maximum cue duration: **5.852 seconds**.
- Maximum gap between cues: about **0.08 seconds**.
- Nonpositive cue count: **0**.
- Overlap count: **0**.

Interpretation:

- The rough caption files are now structurally safer than the first v4/v1 draft.
- They remain rough scene-timed captions, not manually synchronized captions.
- The reusable prompt section and opening triad still need manual timing review against the actual
  MP4 before any upload.

## Upload-gate impact

This pass reduces two technical blockers:

1. It confirms the v2 rough MP4 has expected audio/video streams and no long accidental mute gap.
2. It fixes objectively invalid rough-caption cue boundaries.

It does not close the upload gate. Remaining blockers include:

- full watch/listening pass;
- peer/no-feedback disposition;
- manual caption synchronization;
- final title/description choice;
- publish-now rationale.

Decision: **still do not upload.**
