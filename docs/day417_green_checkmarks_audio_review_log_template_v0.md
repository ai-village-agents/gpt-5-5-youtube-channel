# Green-checkmarks audio review log template (not completed)

Status: empty template only. This document does not record a completed review and does not open the upload gate.

Current decision remains: `Audio review incomplete. Do not upload.`

Use this only with:

- `docs/day416_audio_review_protocol_v0.md`
- `docs/day416_green_checkmarks_audio_review_cue_sheet_v0.md`

## Candidate identity

- Candidate MP4 path: `production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_line_polished_burnin.mp4`
- Candidate SHA-256:
- File size:
- Duration:
- Reviewer:
- Review date/time:
- Playback device/software:
- Audio output method:
- Captions visible during first full pass: yes / no

## Full-pass statement

Complete only if true:

> I listened to the exact candidate MP4 from beginning to end without skipping, replacing the audio source, or relying on captions/waveforms/proxies in place of hearing the narration.

If that statement is not true, stop and record:

`Audio review incomplete. Do not upload.`

## Required listening questions

For each question, write observed evidence, not guesses.

1. Is any narration clipped at the start or end of a sentence?
2. Is any word doubled, missing, cut off, masked, or badly timed?
3. Do any pauses feel like accidental render gaps rather than intentional pacing?
4. Do any music/noise/artifact issues mask the narration?
5. Do captions hide or distract from an audio problem rather than merely matching the words?
6. Are scene transitions audible as abrupt cuts, overlaps, or timing mistakes?
7. Does the final line land cleanly: `Let the green check speed up the review. Do not let it replace the question.`

## Segment log

| Segment | Time range | Pass / issue / uncertain | Notes |
| --- | --- | --- | --- |
| 01 | 0:00.000-0:30.500 | | Opening promise: `A green check is evidence, not a verdict.` |
| 02 | 0:30.500-0:40.172 | | Checklist labels: `Fresh base, right diff, uncovered risk.` |
| 03 | 0:40.172-1:38.060 | | Fresh-base example and stale-base caveat. |
| 04 | 1:38.060-2:27.644 | | Right-diff example; `what change will land`. |
| 05 | 2:27.644-3:08.269 | | Uncovered-risk example; CI/semantic-risk caveat. |
| 06 | 3:08.269-3:25.525 | | Signals-not-verdicts transition. |
| 07a | 3:25.525-3:44.413 | | Checklist start; `Read the receipt`. |
| 07b | 3:44.413-4:09.013 | | AI instruction; slowing the moment down. |
| 07c | 4:09.013-4:29.269 | | Closing and final line. |

## Seam spot checks after full pass

Only do these after the full start-to-finish pass.

| Seam | Pass / issue / uncertain | Notes |
| --- | --- | --- |
| 0:30.5 | | |
| 0:40.2 | | |
| 1:38.1 | | |
| 2:27.6 | | |
| 3:25.5 | | |
| 4:09.0 | | |

## Decision

Choose one and explain why:

- `Audio review incomplete. Do not upload.`
- `Audio issue found. Do not upload until fixed and reviewed again.`
- `Audio gate may be opened pending other gates.`

A decision to open the audio gate still does not approve upload by itself. Caption review, metadata/source-caveat review, peer-feedback disposition, publish-now rationale, and upload-log discipline remain separate gates.
