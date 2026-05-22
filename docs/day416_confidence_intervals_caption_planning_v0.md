# Day 416 confidence-interval caption planning v0

Status: **caption planning only; no audio generated, no captions generated, no render, no Studio upload, and no upload approval.**

Script candidate: [`day416_confidence_intervals_script_v1.md`](day416_confidence_intervals_script_v1.md)  
Visual text inventory: [`day416_confidence_intervals_visual_text_inventory_v0.md`](day416_confidence_intervals_visual_text_inventory_v0.md)

## Purpose

Identify caption risks before any future render. This concept has several lines
that protect against statistical or source overclaiming; those lines should not
be buried in long captions or split in ways that weaken the caveat.

No SRT/VTT exists. Do not treat this as caption QA.

## Lines that should be standalone or near-standalone cues

If captions are generated later, these lines deserve clean cue boundaries:

```text
This is not a full statistics lecture.
It is a reading habit.
```

```text
Crossing zero does not prove there is no effect.
```

```text
That threshold is illustrative, not from the study.
```

```text
A result can be statistically clearer than zero and still too small for the choice in front of you.
```

```text
A confidence interval is not a force field around a claim.
```

```text
Keep the number.
Just do not quote it without the line around it.
```

## Caption risks by scene

### Scene 01 — Lonely number

Risk: the bracketed interval is absent by design. Captions should not introduce
the full interval before the visual reveal unless the narration does.

Preferred caption grouping:

```text
A number can look more certain than it is.
Imagine an AI evaluation claim that says: plus zero point two nine.
```

### Scene 02 — Dot and rail

Risk: too many technical terms at once: estimate, interval, uncertainty rail,
paired comparison, displayed-self-label.

Keep “dot” and “line” phrases short. Let the visual carry the bracketed values.

### Scene 03 — Crosses zero

Risk: viewers may remember only “crosses zero.” The caveat line must be clean:

```text
Crossing zero does not prove there is no effect.
```

Avoid splitting as:

```text
Crossing zero does not prove
there is no effect, but...
```

The sentence should land before the next idea.

### Scene 04 — Near zero

Risk: caption grouping could accidentally imply “Kimi has no label bias.” Keep
the narrower reading visible:

```text
near-zero estimate,
uncertainty on both sides
```

Do not add a caption shorthand such as `no bias`.

### Scene 05 — Practical threshold

Risk: the illustrative `+0.50` action line can be misread as source-derived.
The caption should pair the threshold with its caveat:

```text
That threshold is illustrative,
not from the study.
```

### Scene 06 — Design caveats

Risk: captions plus caveat chips could overload the lower frame. If the visual
shows `prompt set`, `paired slice`, `judge family`, and `scoring setup`, the
caption can stay simpler:

```text
The interval answers one uncertainty question.
It does not answer every design question.
```

### Scene 07 — Five-question habit

Risk: a five-question list can become three-line caption clutter. Prefer short,
progressive captions, not all five questions at once.

Potential caption rhythm:

```text
What is the estimate?
What range remains?
Does it cross zero, or my decision line?
Is it narrow enough for this decision?
What design caveat remains?
```

### Scene 08 — Closing

Risk: final line should be memorable and not split awkwardly.

Preferred final cues:

```text
Keep the number.
```

```text
Just do not quote it without the line around it.
```

## Future caption QA requirements

If this concept is rendered later, run a fresh caption QA pass that checks:

- cue count, first/last cue timing, overlaps, and nonpositive durations;
- characters per second, with special attention to decimal-heavy lines;
- no three-line cues unless deliberately accepted;
- no caption lower-band collision with interval rails, caveat chips, or checklist
  cards;
- no shorthand that changes the source claim, especially `no effect`, `no bias`,
  or `proves`;
- full in-motion caption review after burn-in or upload-context captions exist.

## Current decision

This planning note makes future caption work safer. It does not create captions
or change the upload gate.

```text
No render exists. Audio review impossible. Do not upload.
```
