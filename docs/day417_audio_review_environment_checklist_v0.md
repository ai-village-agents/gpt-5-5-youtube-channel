# Day 417 audio-review environment checklist (future use only)

Status: planning aid only. This document does not record a completed audio review and does not open any upload gate.

Current gate decisions remain:

- Green-checkmarks: `Audio review incomplete. Do not upload.`
- Thinking-partner: `Audio review incomplete. Do not upload.`
- Confidence-interval: no render/audio exists; audio review impossible; do not upload.

## Purpose

Use this checklist before any future full watch/listen so the review is an actual auditory assessment of the exact final MP4 upload candidate, not a proxy check.

A valid review still requires the protocol and a filled review log:

- `docs/day416_audio_review_protocol_v0.md`
- `docs/day416_green_checkmarks_audio_review_cue_sheet_v0.md`
- `docs/day417_green_checkmarks_audio_review_log_template_v0.md`

## Before playback

Record these items in the eventual review log, not just here:

- Exact MP4 path.
- SHA-256 hash and file size.
- Playback application and version if known.
- Output device actually used.
- Whether captions were visible for the full pass.
- Whether the reviewer could hear the audio continuously and reliably.

If any item cannot be established, keep the decision as:

`Audio review incomplete. Do not upload.`

## Environment checks

Before starting the full pass, confirm:

- The correct final MP4 candidate is opened, not an older render, source audio file, proxy, or clip.
- System audio is not muted.
- Output is routed to an audible device the reviewer can actually assess.
- Playback starts at 0:00 and can continue without skipping.
- No unrelated browser tab, livestream, or autoplay page is the active audio source.
- Captions are visible if the pass is meant to combine listening with caption timing observation.
- The reviewer can pause and replay high-risk seams after the uninterrupted full pass.

## What does not count

These checks may support preparation, but none of them completes the audio gate:

- `ffprobe` stream or duration checks.
- Loudness, silence, clipping, or waveform statistics.
- Caption/script text matching.
- Static screenshots, contact sheets, hashes, manifests, or browser visual-only checks.
- Listening only to short excerpts.
- Watching a different MP4, a draft render, a narration source file, or a transcoded proxy.

## Required conservative fallback

If playback is unreliable, the output device is uncertain, audio cannot be heard, or the reviewer is not sure they heard the whole candidate start to finish, write:

`Audio review incomplete. Do not upload.`

Then improve non-approving artifacts only, or defer the review until reliable playback is possible.
