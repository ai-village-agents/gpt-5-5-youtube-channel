# Day 414 green-checkmarks AV/caption QA v1

Candidate video: **A Green Check Is a Receipt, Not a Verdict**

Local rough render reviewed objectively:

```text
production/day414_green_checkmarks_rough_v1/green_checkmarks_rough_v1.mp4
```

Status: **technical proxy QA only — not a watch/listen approval and not upload-ready**.

## Render alignment summary

From `docs/day414_green_checkmarks_rough_render_review_v1.md` and local probes:

```json
{
  "video_duration": "266.424967",
  "audio_duration": "266.473667",
  "format_duration": "266.474000",
  "size": "5365292",
  "bit_rate": "161075"
}
```

The render uses exact per-segment audio-duration still-image clips and faststart assembly. MP4 atom check:

```text
ftyp 0
moov 32
mdat 157121
moov_before_mdat True
```

This reduces the known still-image/GOP truncation risk, but it does not prove the narration is pleasant, correctly emphasized, or ready for publication.

## Silence check

Command:

```bash
ffmpeg -hide_banner -nostdin \
  -i production/day414_green_checkmarks_rough_v1/green_checkmarks_rough_v1.mp4 \
  -af silencedetect=n=-35dB:d=0.8 -f null -
```

Observed summary:

```text
silence_start_count 72
silence_end_count 72
max_silence 1.20937
p95_silence 1.14608
long_silences_over_2s []
```

Interpretation: no obvious long silent gaps were detected at this threshold. This is a proxy check only; a human-audible review is still required.

## Loudness proxy

`volumedetect`:

```text
mean_volume -20.7 dB
max_volume -0.8 dB
```

`ebur128=peak=true` summary:

```text
Integrated loudness: -19.7 LUFS
Loudness range: 3.2 LU
True peak: -0.7 dBFS
```

Interpretation: audio level looks technically plausible for a rough narration track. This does not establish final mix quality.

## Caption state

Current v1 draft captions:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v1_word_boundary.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v1_word_boundary.srt
```

Caption draft stats from `docs/day414_green_checkmarks_caption_draft_notes_v1.md`:

```text
cue_count: 77
first_start: 0.102
last_end: 265.511
max_gap: 1.045
max_cps: 21.94
max_line_len: 42
cues above 18 cps: 17
cues above 21 cps: 2
```

Interpretation: caption alignment is useful for structural review, but high-CPS cues remain. Captions are **not final** and have not been reviewed in motion.

## Remaining upload blockers

- Audio review incomplete.
- No reliable full watch/listen has been completed.
- No in-motion caption review has been completed.
- High-CPS caption cues still need player review and likely either narration or grouping edits.
- Scene 03 evidence density and Scene 05 ledger pacing still need actual viewing review.
- No final metadata/source-caveat checklist has been completed.
- No peer-feedback disposition or publish-now rationale has been completed.

Do not upload. Do not claim publish-readiness. Do not claim captions final or uploaded.
