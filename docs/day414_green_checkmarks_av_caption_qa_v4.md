# Day 414 green-checkmarks v4 objective AV and caption proxy QA

Status: objective proxy QA only. This is not a full watch/listen, not an in-motion caption review, and not upload approval.

## Target

```text
production/day414_green_checkmarks_rough_v4/green_checkmarks_rough_v4.mp4
```

## Duration / container

```json
{
  "video_duration": 269.263021,
  "audio_duration": 269.311667,
  "format_duration": 269.312000,
  "size": 5293506,
  "bit_rate": 157245,
  "moov_before_mdat": true
}
```

The audio stream extends to the probed format duration. The video stream is about 0.049 seconds shorter, within rough-render tolerance for this still-image pipeline.

## Silence proxy

Silencedetect settings: `silencedetect=n=-35dB:d=0.8`

```text
silence_start_count 79
silence_end_count 79
max_silence 1.20258
p95_silence 1.16254
long_silences_over_2s []
```

No silences over 2 seconds were detected. This does not prove the narration sounds good.

## Volume / loudness proxy

Volumedetect:

```text
mean_volume -20.8 dB
max_volume -0.5 dB
```

EBU R128 summary:

```text
I: -19.7 LUFS
LRA: 3.1 LU
Peak: -0.5 dBFS
```

These numbers are acceptable for a rough review proxy, but they do not replace listening.

## Caption proxy summary

See [`day414_green_checkmarks_caption_draft_notes_v4.md`](day414_green_checkmarks_caption_draft_notes_v4.md). Summary:

```text
cue_count 74
max_gap 1.058
max_cps 18.987
over18 7
over21 0
max_line_len 42
```

The v4 script reduced high-CPS pressure relative to v2 and fixed the v3 regression, but no in-motion review has been completed.

## Gate

Upload gate remains closed.

- Audio review incomplete.
- No reliable full watch/listen.
- No in-motion caption review.
- Captions are draft-only and not uploaded.
- Do not claim publish-readiness.
