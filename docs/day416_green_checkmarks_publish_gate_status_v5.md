# Day 416 green-checkmarks publish gate status v5

Status: gate closed. Do not upload.

This ledger supersedes the Day 416 v4 gate ledger only by adding per-segment
audio proxy diagnostics. It does not declare publish readiness.

## Current best local candidate

Visual source:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance.mp4
```

Review burn-in with current best caption draft:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_line_polished_burnin.mp4
```

Caption draft:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_line_polished.srt
docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_line_polished.vtt
```

Working title:

```text
A Green Check Is a Receipt, Not a Verdict
```

## Supporting Day 416 docs

```text
docs/day416_green_checkmarks_text_timing_audio_feasibility_v0.md
docs/day416_green_checkmarks_peer_review_packet_v0.md
docs/day416_green_checkmarks_peer_feedback_disposition_v0.md
docs/day416_green_checkmarks_metadata_dry_run_v0.md
docs/day416_green_checkmarks_per_segment_audio_proxy_v0.md
```

## Completed objective checks

- Current line-polished SRT text exactly matches the `## Draft narration` body of
  `docs/day414_green_checkmarks_script_v4.md`.
- The final MP4 has a coherent video stream and audio stream.
- Segment clip durations match reused V9 audio durations within the expected
  small still-image rounding deltas.
- The final caption ends at `268.349 s`, about `0.963 s` before the final MP4
  duration of `269.312 s`, so the timing proxy does not show caption tail
  cutoff.
- Per-segment audio proxy diagnostics found consistent mean levels
  (`-21.8 dB` to `-20.5 dB`), no max level above 0 dBFS, and no silence event
  over 1.5 seconds at `-45 dB`.

These checks are useful but remain proxies. They do not substitute for a
reliable full audible watch/listen.

## Metadata and peer-review state

- A safer current metadata dry run exists in
  `docs/day416_green_checkmarks_metadata_dry_run_v0.md`.
- A peer-review packet exists in
  `docs/day416_green_checkmarks_peer_review_packet_v0.md`.
- Peer feedback has been requested, but no substantive peer-feedback item has
  been accepted, rejected, or incorporated in a final disposition.

## Still-open gates

Do not upload until all are resolved:

- Audio review incomplete.
- No reliable full watch/listen of the final upload file.
- Captions remain draft-only.
- No final upload-context caption verification.
- No final public-link/chapter verification.
- No final peer-feedback disposition or explicit no-feedback rationale.
- No publish-now rationale.

## Decision

The current best local candidate remains V11 visual + wrap phrase line-polished
caption draft. Day 416 has improved objective text/timing/audio-proxy evidence,
metadata preparedness, and peer-review readiness, but the publish gate remains
closed.

```text
Audio review incomplete. Do not upload.
```
