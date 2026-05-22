# Day 416 Confidence Intervals Narration Pronunciation Guide v0

Status: preproduction narration-support note only. This is not a render, audio file,
caption file, Studio asset, peer review, publish-gate decision, or upload approval.
Current gate remains: **No render exists. Audio review impossible. Do not upload.**

## Purpose

The confidence-interval script uses short decimal estimates and bracketed ranges.
Those lines are easy for text-to-speech or captions to make awkward if the number
format is copied too literally. This guide records how the numbers should sound in
future narration, while keeping the visual text precise on screen.

## General rule

- On screen, keep compact mathematical notation: `+0.29 [ +0.14, +0.45 ]`.
- In narration, prefer human-readable phrasing: `plus zero point two nine, with a
  line from plus zero point one four to plus zero point four five`.
- Do not say `ninety-five percent chance the true value is inside this interval`.
- Do not turn a number into a verdict. Every example remains one study / one paired
  slice / one analysis.

## Number-by-number narration targets

### Gemini paired SELF-OTHER example

Visual text:

```text
+0.29 [ +0.14, +0.45 ]
```

Preferred narration:

```text
plus zero point two nine, with an interval from plus zero point one four to plus zero point four five
```

Avoid:

```text
zero point twenty-nine proves self-preference
Gemini is biased by zero point twenty-nine
ninety-five percent true range
```

### Claude paired SELF-OTHER example

Visual text:

```text
+0.12 [ -0.07, +0.30 ]
```

Preferred narration:

```text
plus zero point one two, with an interval from minus zero point zero seven to plus zero point three zero
```

Acceptable shorter narration if the visual carries the full bracket:

```text
the center is plus zero point one two, but the interval crosses zero
```

Avoid:

```text
Claude has no effect
Claude proves a positive effect
crossing zero means nothing happened
```

### Kimi paired SELF-OTHER example

Visual text:

```text
+0.01 [ -0.30, +0.34 ]
```

Preferred narration:

```text
plus zero point zero one, with an interval from minus zero point three zero to plus zero point three four
```

Acceptable shorter narration:

```text
a near-zero center, with uncertainty on both sides
```

Avoid:

```text
Kimi has no label bias
Kimi is worse
Kimi is unbiased
```

### Hypothetical action line

Visual text:

```text
hypothetical action line: +0.50
not from the study
```

Preferred narration:

```text
imagine my action line is plus zero point five zero
```

Required nearby caveat:

```text
That threshold is illustrative, not from the study.
```

Avoid:

```text
the study threshold
scientific cutoff
safe line
```

## Model-name and term pronunciation notes

- `SELF-OTHER`: say `self minus other` or `self other label gap`; do not say the
  punctuation mark.
- `AI-evaluation`: say `AI evaluation`, not `A-eye dash evaluation`.
- `confidence interval`: keep the phrase, but immediately frame it as a reading
  aid rather than a proof.
- `point estimate`: if used twice close together, vary with `the dot` when the
  visual already establishes the mapping.
- `zero`: in the script, zero means the no-gap reference for the displayed-label
  comparison. Do not imply zero is the only possible decision threshold.

## Caption readability risks for future render

Decimal-heavy caption lines can become too long. If captions are generated later,
prefer splitting these as standalone cues:

```text
plus zero point two nine,
with an interval from plus zero point one four

to plus zero point four five.
```

```text
The dot leans positive.
The line crosses zero.
```

```text
That threshold is illustrative,
not from the study.
```

```text
A confidence interval is not
a force field around a claim.
```

Do not shorten captions into unsafe claims such as `no effect`, `proves bias`, or
`true range`.

## Future QA reminder

When a render exists, this guide is only a checklist for listening. It cannot
substitute for a reliable full watch/listen, in-motion caption review, metadata
review, peer-feedback disposition, publish-now rationale, or upload log.
