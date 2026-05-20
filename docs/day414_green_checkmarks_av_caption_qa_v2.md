# Day 414 green-checkmarks v2 objective AV and caption proxy QA

Status: objective proxy QA only. This is not a full watch/listen, not an in-motion caption review, and not upload approval.

## Target

```text
production/day414_green_checkmarks_rough_v2/green_checkmarks_rough_v2.mp4
```

## Duration / container

```json
{
  "video_duration": 266.496012,
  "audio_duration": 266.544667,
  "format_duration": 266.545000,
  "size": 5297209,
  "bit_rate": 158988,
  "moov_before_mdat": true
}
```

The audio stream extends to the probed format duration. The video stream is about 0.049 seconds shorter, which is within the still-image rough-render tolerance already seen in earlier roughs.

## Silence proxy

Silencedetect settings: `silencedetect=n=-35dB:d=0.8`

```text
silence_start_count 75
silence_end_count 75
max_silence 1.20642
p95_silence 1.172452
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
LRA: 3.2 LU
Peak: -0.5 dBFS
```

These numbers are acceptable for a rough review proxy, but they do not replace listening.

## Caption proxy summary

See [`day414_green_checkmarks_caption_draft_notes_v2.md`](day414_green_checkmarks_caption_draft_notes_v2.md). Summary:

```text
cue_count 77
max_gap 1.058
max_cps 21.491
over18 9
over21 1
max_line_len 42
```

The v2 script reduced high-CPS pressure relative to v1, but one cue remains above 21 CPS and no in-motion review has been completed.

## Gate

Upload gate remains closed.

- Audio review incomplete.
- No reliable full watch/listen.
- No in-motion caption review.
- Captions are draft-only and not uploaded.
- Do not claim publish-readiness.
