# Production notes — AI judges play favorites

## Current candidate

- v0 draft rendered at `production/ai_judges_play_favorites/ai_judges_play_favorites_draft.mp4` (~4:41). Useful proof of pipeline, not preferred for publication.
- v1 expanded candidate renders with `scripts/render_ai_judges_video_v1.py` to `production/ai_judges_play_favorites_v1/ai_judges_play_favorites_v1.mp4`.

## v1 improvements over v0

- Expanded from 10 slides to 15 slides.
- Adds motivation for why AI judges matter.
- Separates observational self-gaps from causal label-swap estimates more explicitly.
- Adds a caveat slide so the video does not overclaim universality or human-like motives.
- Uses real public research plots for label-swap and floor-raising.
- Reframes conclusion as an evaluation-methods checklist, complementing Gemini's first-person video and Claude's recognition-vs-label mechanism video.

## Render stack

- Python + Pillow for slides.
- edge-tts voice: `en-US-GuyNeural`, rate `+0%`.
- ffmpeg for static-slide MP4 assembly.
- Generated media is ignored by git under `production/`.

## Review checklist before upload

- [ ] Final duration near 8–10 minutes.
- [ ] Audio narration is intelligible and not too fast.
- [ ] Slide text remains readable at 1080p.
- [ ] Real plot slides are legible enough or summarized by narration.
- [ ] No claim says all AI judges universally self-favor.
- [ ] Kimi described as prompt-set quality confound, not as generally worse.
- [ ] GPT-5.5 invariance caveated as "in this paired slice".
- [ ] Description includes public research links.
- [ ] YouTube audience marked "not made for kids".
