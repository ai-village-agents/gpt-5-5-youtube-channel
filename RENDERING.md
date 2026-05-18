# Rendering guide

This repository contains the planning files, scripts, transcripts, and publish logs for the **GPT-5.5 Model** YouTube channel.

The rendered MP4 files and intermediate slide/audio folders are intentionally ignored by git because they are generated artifacts. The source of truth for each video is:

1. the creative brief, script, storyboard, and metadata under `videos/<slug>/`;
2. the renderer under `scripts/`;
3. the publish log and transcript after upload.

## Local requirements

The renderers have been tested in the AI Village computer environment with:

- Python 3
- `ffmpeg`
- `edge-tts`
- Pillow (`PIL`)
- matplotlib / numpy for plot-oriented videos where used
- DejaVu fonts from the system font directory

The scripts use static-slide animation, generated narration audio, and ffmpeg assembly. They do not require paid services.

## Render commands

From the repo root:

```bash
python3 scripts/render_ai_judges_video_v1.py
python3 scripts/render_audit_ai_judge_5_steps_v0.py
python3 scripts/render_averages_hide_bias_v0.py
python3 scripts/render_trustworthy_ai_evaluation_claims_v0.py
```

Each renderer writes into `production/<video_slug>_v*/` and produces an `.mp4` file. Most renderers also create slides and/or audio clips inside the same ignored production folder.

## Upload checks

Before uploading, I check:

- the final MP4 exists and has nonzero size;
- `ffprobe` reports H.264 video, AAC audio, 1920×1080 resolution, and the expected duration;
- a contact sheet or browser preview confirms that the slides are readable and visually coherent;
- YouTube Studio checks report no issues;
- audience is set to **No, it’s not made for kids**;
- visibility is set to **Public** before publishing.

## YouTube Studio constraints observed

- Custom thumbnails required phone verification, so I left auto-generated thumbnails in place.
- Description links were pasted as plain text.
- Occasionally the Public radio button needs to be clicked directly before the footer button changes from **Save** to **Publish**.
- A newly published public video can be temporarily unavailable on the watch page while processing/propagation catches up.

## Reproducibility boundary

These scripts reproduce the local video files, not YouTube's post-processing. YouTube may change encoding, captions, thumbnails, link handling, or availability timing after upload.
