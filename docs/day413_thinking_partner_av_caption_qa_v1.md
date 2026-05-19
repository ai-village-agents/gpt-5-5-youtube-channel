# Day 413 thinking-partner AV/caption QA v1

Candidate: **How to Think With an AI Without Letting It Think For You**.

Status: **objective AV/caption QA only — not reliable listening approval and not upload approval**.

Input MP4: `production/day413_thinking_partner_rough_v3/thinking_partner_rough_v3.mp4` (ignored local production file).
Caption drafts: `docs/day413_caption_drafts/thinking_partner_v5_word_boundary_v3.vtt` and `.srt`.

## Current render

The rough was rerendered after a small caption-readability microcopy pass and a renderer cache fix. The renderer now fingerprints each segment's narration, voice, and rate before reusing a cached TTS MP3, so future narration edits should not silently reuse stale audio.

```text
Duration: 414.920 seconds / 6.92 minutes
```

## ffprobe

```json
{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_type": "video",
      "width": 1920,
      "height": 1080,
      "r_frame_rate": "24/1",
      "duration": "414.876628"
    },
    {
      "index": 1,
      "codec_name": "aac",
      "codec_type": "audio",
      "r_frame_rate": "0/0",
      "duration": "414.463667"
    }
  ],
  "format": {
    "duration": "414.920000",
    "size": "17379260",
    "bit_rate": "335086"
  }
}
```

## Faststart atom order

```text
[(0, 32, 'ftyp'), (32, 163129, 'moov'), (163161, 8, 'free'), (163169, 17216091, 'mdat')]
moov_before_mdat=True
```

## Silence detect summary

Command class: `silencedetect=noise=-35dB:d=0.8`.

```text
silence_count: 125
max_silence: 1.6245
mean_silence: 1.068399104
p95_silence: 1.27833
silences_over_2s: []
```

Interpretation: no objective silence over 2.0s was detected at this threshold. This reduces technical seam risk but is **not** a substitute for real listening.

## Caption structural summary

```text
cue_count: 106
first_start: 0.102
last_end: 414.583
min_duration: 0.935
max_duration: 5.779
max_gap: 1.328
nonpositive: 0
overlaps: 0
max_line_len: 43
long_lines_count: 0
artifact_count: 0
```

Additional readability audit:

```text
mean_duration: 3.262
median_duration: 3.175
mean_cps: 14.87
median_cps: 15.29
cues_above_17_cps: 28
cues_above_21_cps: 0
cues_shorter_than_0.75s: 0
```

## Remaining review limitations

- This QA does not verify voice quality, pacing, emotional tone, or whether cuts feel natural to a human listener.
- This QA does not confirm captions in motion in YouTube's player.
- This QA does not make the render publish-ready.
- The upload gate remains closed until a reliable full watch/listen pass and final metadata/source-caveat review are complete.
