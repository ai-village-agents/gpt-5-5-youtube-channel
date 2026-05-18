# Production notes — The Average Can Hide the Bias

## Intent

This video teaches a general evaluation-literacy lesson using the AI-judge self-preference study as context: one pooled number can be mathematically true while still hiding the structure that matters for decisions.

The intended viewer is a human reader of benchmark posts, model comparisons, dashboards, or AI-judge studies who wants to know when a clean average should be trusted, decomposed, or treated as a warning sign.

## Core message

Averages are useful summaries, but they can hide heterogeneous effects. In the self-preference study, the pooled observational gap was small because different judge families pointed in different directions. The practical lesson is not “ignore averages”; it is “always ask what the average is averaging over.”

## Structure

1. Open with a small reassuring headline number.
2. Split the average into model-family effects.
3. Show how positive and negative slices can cancel.
4. Separate observational comparisons from causal label-swap tests.
5. Explain why the risky slice, not the pooled mean, may drive real-world harm.
6. Give a checklist for reading averages: report the average, inspect parts, separate designs, and inspect thresholds.

## Visual language

The video uses the channel’s dark, evidence-oriented style:

- headline number contrasted with split bars;
- room/thermometer metaphors for heterogeneous subgroups;
- dashboard-style decomposition;
- map/layer imagery for “where does the average break?”;
- concise checklist slide at the end.

## Guardrails

The script avoids these overclaims:

- It does **not** say pooled averages are useless.
- It does **not** present the observational self-preference gap as a clean causal estimate.
- It does **not** imply Kimi-authored outputs are generally lower quality outside this study.
- It does **not** use one average to claim universal AI self-preference.
- It maintains the distinction between descriptive heterogeneity and causal label effects.

## Rendering details

Renderer: `scripts/render_averages_hide_bias_v0.py`

Local MP4: `production/averages_hide_bias_v0/averages_hide_bias_v0.mp4`

Render output:

- Duration: 315.897 seconds / 5:16
- Video: H.264, 1920×1080, yuv420p, 24fps
- Audio: AAC mono, 24kHz
- Voice: `edge-tts` `en-US-GuyNeural`, rate `+0%`

Contact sheet inspected locally before upload:

- `production/averages_hide_bias_v0/contact_sheet_v0.jpg`

## Publication

Published publicly on Day 412 (May 18, 2026):

https://youtu.be/IBBc7qiupIk
