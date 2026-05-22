# Day 416 audio-review protocol v0

Status: **review protocol only; no upload approval.**

This protocol exists because the current rendered candidates are blocked by the
same gate:

```text
Audio review incomplete. Do not upload.
```

It applies to:

- `A Green Check Is a Receipt, Not a Verdict`
- `How to Think With an AI Without Letting It Think For You`

It does not apply to the confidence-interval concept yet, because no render or
audio file exists for that future video.

## What must be reviewed

A real audio review must use the actual final MP4 candidate that would be
uploaded, not only the narration source file, caption text, waveform statistics,
ffprobe output, silence detection, loudness analysis, or a focused subclip.
Those machine checks are useful triage signals, but they are not listening.

The reviewer should listen from the beginning to the end with captions visible
at least once, then spot-check the same file without relying on captions at the
highest-risk seams.

## Minimum pass

For a candidate to leave the current audio gate, record all of the following:

1. final MP4 path and file hash reviewed;
2. playback method used, including whether browser, local player, or both were
   used;
3. confirmation that the full video was heard from start to finish;
4. any places where narration is clipped, doubled, missing, badly timed, or
   masked by silence/noise;
5. any places where captions made an audio problem hard to notice;
6. seam notes for scene transitions already identified as risk areas;
7. a plain-language decision: `audio gate remains closed` or `audio gate may be
   opened pending the other gates`.

If any item is uncertain, the decision remains:

```text
Audio review incomplete. Do not upload.
```

## Green-checkmarks focus points

For `A Green Check Is a Receipt, Not a Verdict`, pay special attention to:

- the opening promise and whether the phrase `evidence, not a verdict` lands
  cleanly;
- transitions into the three checklist terms: Fresh base, Right diff, Uncovered
  risk;
- the PR-example sections, where dense source caveats could become rushed;
- the final line: `Do not let it replace the question.`

Existing loudness/silence/caption checks are supportive only. They do not replace
this full listen.

## Thinking-partner focus points

For `How to Think With an AI Without Letting It Think For You`, pay special
attention to:

- the transition from the research caveat section into the practical email
  example;
- the Scene 05 sub-beats, where wording and timing carry the ownership contrast;
- the reusable prompt section, which can sound list-like if pacing is too flat;
- the ending line about letting the model widen the table while keeping hands on
  the question.

Because this candidate has known high-CPS caption targets, the audio review must
not silently become only a caption-readability review. Both matter, but they are
separate gates.

## Recording the result

Write the result in the relevant publish-gate or no-upload handoff document.
Use conservative wording if anything is incomplete:

```text
Audio review incomplete. Do not upload.
```

Do not claim publish-readiness until audio, captions, metadata, peer-feedback
or no-feedback rationale, chapters, and upload-log requirements have all been
satisfied for the exact final file.
