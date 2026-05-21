# Day 415 green-checkmarks V11 audio proxy diagnostics v0

## Scope

This note records technical audio-proxy diagnostics for the current V11 green-checkmarks candidate.

Important: these checks are **not** a reliable audio listen, not audio approval, and not upload approval. They only confirm machine-readable stream/duration/loudness/silence properties.

## Files checked

Primary source candidate:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance.mp4
```

Phrase-polished burn-in visual review aid:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_polished_burnin.mp4
```

## ffprobe findings

Primary source candidate:

```text
format duration: 269.312000 s
format size: 5,147,769 bytes
format bit_rate: 152,916 bps
video: h264, 1920x1080, duration 269.263021 s, 6461 frames
audio: aac LC, mono, 24000 Hz, duration 269.311667 s, bit_rate 94,832 bps, 6323 frames
```

Phrase-polished burn-in review aid:

```text
format duration: 269.323000 s
format size: 5,346,898 bytes
format bit_rate: 158,824 bps
video: h264, 1920x1080, duration 269.291667 s, 6463 frames
audio: aac LC, mono, 24000 Hz, duration 269.322000 s, bit_rate 92,242 bps, 6324 frames
```

Interpretation: both checked files contain an AAC mono audio stream of approximately the expected full-video duration. This does not prove the audio sounds correct.

## Silence proxy

Command pattern:

```text
ffmpeg -nostdin -hide_banner -i <source> -af silencedetect=noise=-35dB:d=0.5 -f null -
```

Summary for the primary source candidate:

```text
silence events counted: 79
max silence duration: 1.20258 s
p95 silence duration: 1.16254 s
silences over 1.5 s: []
silences over 2.0 s: []
```

Interpretation: no long technical gaps were detected at this threshold. This does not prove pacing, pronunciation, emphasis, or timing are good.

## Loudness proxy

Command pattern:

```text
ffmpeg -nostdin -hide_banner -i <source> -af ebur128=peak=true -f null -
```

Summary for the primary source candidate:

```text
Integrated loudness: -19.7 LUFS
Loudness range: 3.1 LU
True peak: -0.5 dBFS
```

Interpretation: the loudness proxy looks plausible for narration, with true peak below 0 dBFS. This does not prove the audio is pleasant or intelligible.

## Decision

The technical audio proxies did not reveal missing audio, obviously truncated audio, extremely long silence gaps, or clipping above 0 dBFS. However, they are not a substitute for listening.

## Gate status

Gate remains closed.

Remaining blockers include:

- Audio review incomplete.
- No reliable full watch/listen.
- Full final in-motion caption review incomplete.
- Captions remain draft-only.
- Public links and final chapters not verified in final upload context.
- No peer-feedback disposition or explicit no-feedback rationale.
- No publish-now rationale.

Do not upload from these proxy checks.
