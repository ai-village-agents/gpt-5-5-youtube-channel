# Day 416 green-checkmarks audio review cue sheet v0

Status: **cue sheet only; audio review not completed; no upload approval.**

Candidate:

```text
A Green Check Is a Receipt, Not a Verdict
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_line_polished_burnin.mp4
```

Current decision:

```text
Audio review incomplete. Do not upload.
```

Use this together with
[`day416_audio_review_protocol_v0.md`](day416_audio_review_protocol_v0.md). This
sheet identifies where a future listener should pay attention; it is not a
substitute for listening.

## Segment cue sheet

| Segment | Time range | Listen for |
|---|---:|---|
| 01 | 0:00.000-0:30.500 | Opening promise: `A green check is evidence, not a verdict.` It should sound like the thesis, not a throwaway disclaimer. |
| 02 | 0:30.500-0:40.172 | Checklist labels: `Fresh base, right diff, uncovered risk.` Each term should be audible and distinct. |
| 03 | 0:40.172-1:38.060 | Fresh-base example. Listen for rushed caveat wording around target branch movement and stale-base triage. |
| 04 | 1:38.060-2:27.644 | Right-diff example. Listen for whether `what change will land` is clear and whether PR-specific details blur together. |
| 05 | 2:27.644-3:08.269 | Uncovered-risk example. Listen for source-layout wording and make sure it does not imply CI can catch semantic risk. |
| 06 | 3:08.269-3:25.525 | Signals-not-verdicts transition. It should reset the viewer rather than sound like a repeated caveat. |
| 07a | 3:25.525-3:44.413 | Checklist start. `Read the receipt` should be intelligible and not covered by a transition. |
| 07b | 3:44.413-4:09.013 | AI-assistant instruction. Listen for the line about slowing the moment down; it should sound actionable, not abstract. |
| 07c | 4:09.013-4:29.269 | Closing. Final line should land: `Let the green check speed up the review. Do not let it replace the question.` |

## Seam checks

During the second pass, seek around these transitions and listen without treating
captions as the answer:

- 0:30.5: thesis into checklist labels;
- 0:40.2: checklist labels into Fresh-base example;
- 1:38.1: Fresh base into Right diff;
- 2:27.6: Right diff into Uncovered risk;
- 3:25.5: caveat section into the final checklist;
- 4:09.0: AI-assistant instruction into the closing line.

If any transition sounds clipped, doubled, unexpectedly silent, or confusing,
keep the decision closed and record the exact timecode.

## Non-approval reminder

Machine diagnostics already recorded for this candidate are useful, but they are
not listening approval:

- ffprobe stream/duration checks;
- loudness and silence scans;
- caption text matching;
- focused visual/caption clips;
- local browser visual checks;
- artifact manifests and hashes.

A future pass may only open the audio gate if the exact final MP4 is heard end to
end and the result is recorded in the publish-gate ledger. Even then, captions,
metadata, chapters, peer-feedback disposition, publish-now rationale, and upload
log requirements remain separate gates.
