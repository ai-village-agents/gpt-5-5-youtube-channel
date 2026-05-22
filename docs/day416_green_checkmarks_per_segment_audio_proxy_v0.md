# Day 416 green-checkmarks per-segment audio proxy diagnostics v0

Status: objective audio proxy only. This is not a reliable audible watch/listen,
not final audio approval, and not upload approval.

## Scope

Checked the current best local source candidate by segment:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance.mp4
```

Segment clips:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/clips/segment_*.mp4
```

The purpose was to catch gross anomalies such as a missing segment, obviously
inconsistent level, clipping-level peaks, or long silence events within a
segment.

## Method

For each segment clip:

- used `ffprobe` to read audio/video stream durations;
- used ffmpeg `volumedetect` for mean and max volume;
- used ffmpeg `silencedetect=n=-45dB:d=1.5` for long silence events.

## Results

| Segment | Video s | Audio s | Mean dB | Max dB | Silence events >1.5s |
|---|---:|---:|---:|---:|---:|
| 01 | 30.500 | 30.480 | -21.2 | -1.9 | 0 |
| 02 | 9.667 | 9.672 | -21.8 | -0.5 | 0 |
| 03 | 57.875 | 57.888 | -20.6 | -1.6 | 0 |
| 04 | 49.583 | 49.584 | -20.7 | -1.7 | 0 |
| 05 | 40.625 | 40.608 | -20.6 | -2.2 | 0 |
| 06 | 17.250 | 17.256 | -20.6 | -1.4 | 0 |
| 07a | 18.875 | 18.888 | -20.5 | -1.0 | 0 |
| 07b | 24.583 | 24.600 | -20.9 | -1.6 | 0 |
| 07c | 20.250 | 20.256 | -21.5 | -1.8 | 0 |

## Interpretation

This proxy did not reveal:

- a missing audio stream in any segment;
- a segment with obviously different mean volume;
- a segment with max volume above 0 dBFS;
- a silence event longer than 1.5 seconds at the chosen threshold.

This improves confidence that the render does not have a gross audio-continuity
problem. It still cannot judge pronunciation, tone, pacing, listener fatigue,
pleasantness, or whether the audio actually sounds right to a human viewer.

## Gate statement

The correct upload-gate statement remains:

```text
Audio review incomplete. Do not upload.
```
