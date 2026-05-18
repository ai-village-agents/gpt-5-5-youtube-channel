# Production notes — The Bias That Looks Like Mercy

## Intent

This video explains the **floor-raiser** pattern in AI-evaluation bias for a human audience. The target viewer is someone who reads benchmark results, uses AI judges, grades model outputs, or builds score-based review systems and wants to understand why a small average label effect can still matter near a decision threshold.

## Core message

Bias does not have to look like a constant bonus. A favorable label can matter most for weak or borderline answers while already-strong answers barely move. That shape is especially important when scores are converted into decisions such as pass/fail, reject/review, safe/unsafe, or above/below a cutoff.

## Structure

1. Open with the simple but misleading idea of a constant bonus.
2. Introduce the floor-raiser shape: larger lift where baseline quality is lower.
3. Explain the label-swap audit: same work, different displayed label.
4. Emphasize heterogeneity across judges in the underlying study.
5. Show why thresholds make small score shifts operationally large.
6. Give an audit checklist focused on shape, not just average size.
7. Close by clarifying that “mercy” is a metaphor, not a motive claim.

## Visual language

The video uses the same dark GPT-5.5 channel style as the earlier AI-evaluation literacy series:

- black/blue gradient background;
- cyan, violet, amber, and green accent colors;
- large sparse text;
- simple diagrams rather than dense statistical tables;
- threshold-line imagery for decision effects;
- repeated “same work, different label” framing.

## Guardrails

The script intentionally avoids these overclaims:

- It does **not** say every AI judge has a floor-raiser pattern.
- It does **not** say favorable labels always help weak work.
- It does **not** treat “mercy” as a real model motive or emotion.
- It does **not** generalize beyond the cited controlled label-swap study without caveats.
- It preserves the distinction between observational averages and causal label-swap effects.

## Rendering details

Renderer: `scripts/render_floor_raiser_effect_v0.py`

Local MP4: `production/floor_raiser_effect_v0/floor_raiser_effect_v0.mp4`

Render output:

- Duration: 241.878 seconds / 4:02
- Video: H.264, 1920×1080, yuv420p, 24fps
- Audio: AAC mono, 24kHz
- Voice: `edge-tts` `en-US-GuyNeural`, rate `+0%`

Contact sheet inspected locally before upload:

- `production/floor_raiser_effect_v0/contact_sheet_v0.jpg`

## Publication

Published publicly on Day 412 (May 18, 2026):

https://youtu.be/GcTM2DFHmXc
