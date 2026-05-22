# Day 416 confidence-interval explainer outline v0

Working title: **The Line Around the Number: Reading Confidence Intervals in AI Claims**  
Status: **outline only; not a script, render plan, or upload approval.**  
Parent brief: [`day416_confidence_intervals_creative_brief_v0.md`](day416_confidence_intervals_creative_brief_v0.md)

## One-sentence promise

After watching, a viewer should know how to read the range around an AI-evaluation
number before treating the headline estimate as a decision.

## Target viewer

A technically curious human who reads AI benchmark posts, model comparisons, or
evaluation papers, but does not want a full statistics lecture. They need a
practical habit for deciding whether a reported gap is clear, uncertain, or
irrelevant to their decision.

## Tone

Calm, practical, and caveated. The video should not mock readers for liking clean
numbers. It should say: clean numbers are useful, but they need their uncertainty
rail attached.

## Draft scene outline

### Scene 01 — The lonely number

**Viewer feeling:** A headline number looks decisive.

**Visual:** A single large card: `+0.29` with a small label, “reported gap.” The
card feels clean and authoritative.

**Narration job:** Introduce the problem: a point estimate is easy to quote
because it is compact, but compact is not the same as complete.

**Key line candidate:**

```text
A single number is a headline. The interval around it is the part that tells you how carefully to read the headline.
```

### Scene 02 — Add the line around the number

**Viewer feeling:** The same number becomes more interpretable when uncertainty
is visible.

**Visual:** The `+0.29` dot appears on a horizontal rail from `+0.14` to `+0.45`.
A vertical zero line sits left of the rail. Label: `one paired slice, one study`.

**Source example:** Gemini paired SELF-OTHER label gap `+0.29 [+0.14, +0.45]`.

**Narration job:** Explain that this is an example where the reported interval is
entirely positive in this paired slice, so the direction is better supported
than the point estimate alone would show.

**Required caveat:** Do not generalize this to all judges or all AI evaluations.

### Scene 03 — When the line crosses zero

**Viewer feeling:** A positive center does not always justify a positive
headline.

**Visual:** Claude paired SELF-OTHER label gap `+0.12 [-0.07, +0.30]` with the
rail crossing the zero line.

**Narration job:** Show that a positive center with an interval crossing zero is
not the same kind of evidence as a positive center whose interval stays positive.

**Key line candidate:**

```text
The dot leans positive. The line says: do not treat that lean as settled.
```

**Required caveat:** Crossing zero does not prove the effect is exactly zero.

### Scene 04 — Near zero with a wide line

**Viewer feeling:** “No effect” may be too strong if the interval is wide.

**Visual:** Kimi paired SELF-OTHER label gap `+0.01 [-0.30, +0.34]`; the dot sits
near zero, but the rail extends into both negative and positive territory.

**Narration job:** Distinguish “the estimate is near zero” from “we have ruled
out every meaningful effect.”

**Key line candidate:**

```text
A near-zero dot is useful. A wide line says what it has not ruled out.
```

### Scene 05 — Your decision threshold may not be zero

**Viewer feeling:** Statistical direction and practical action are different.

**Visual:** Reuse the Gemini positive interval, then add a vertical decision line
at `+0.50` or another clearly labeled hypothetical threshold: “minimum gap I’d
act on.” The interval is positive but still below the practical threshold.

**Narration job:** Explain that an interval can support a direction and still be
too small for the viewer's decision.

**Required caveat:** The decision threshold is illustrative, not from the source
study.

### Scene 06 — Statistical uncertainty is not the only uncertainty

**Viewer feeling:** A precise rail is not a whole evidence map.

**Visual:** The interval card gets three small tags around it: `prompt set`,
`paired slice`, `judge family`. A caption says: “intervals do not erase design
questions.”

**Narration job:** Explain that intervals describe uncertainty under the analysis
that produced them; they do not remove source-boundary caveats.

**Required caveats:** One study, reduced paired slice, model-family heterogeneity,
operational decision context.

### Scene 07 — The five-question habit

**Viewer feeling:** The viewer gets a usable checklist.

**Visual:** Five cards:

1. What is the point estimate?
2. What range is still plausible?
3. Does the range cross zero or my decision threshold?
4. Is the range narrow enough for this decision?
5. What design caveat remains?

**Narration job:** Turn the statistical lesson into a repeatable reading habit.

### Scene 08 — Closing

**Viewer feeling:** Numbers become more useful, not less useful, when uncertainty
is visible.

**Visual:** Return to the lonely `+0.29` card, then attach the rail. The final
image is a number plus its line, not a rejected number.

**Key line candidate:**

```text
Keep the number. Just do not quote it without the line around it.
```

## Source-claim guardrails

Safe claims:

```text
A point estimate is easier to quote than an interval, but the interval is part of the evidence.
In this paired slice, Gemini's displayed-self-label interval is entirely positive.
Claude's paired SELF-OTHER point estimate is positive, but its interval crosses zero.
Kimi's paired SELF-OTHER estimate is near zero, but the interval spans negative and positive values.
A confidence interval can help calibrate a decision, but it does not erase design caveats.
```

Avoid:

```text
Confidence intervals prove the truth.
If an interval crosses zero, there is no effect.
If an interval does not cross zero, the result matters for every decision.
The Gemini result proves all AI judges favor themselves.
The Kimi interval proves Kimi has no label bias.
The pooled interval proves the overall effect is positive.
```

## Open questions before scripting

- Should the examples use only paired SELF-OTHER label gaps, or also include the
  pooled C1 interval as a cautionary cold open?
- Is the title too abstract for non-statisticians? Alternatives:
  - **The Number Is Not the Whole Result**
  - **Before You Trust an AI Benchmark Gap, Read the Range**
  - **What the Error Bar Is Trying to Tell You**
- Should the video explicitly define “95% confidence interval,” or stay with the
  practical phrase “range still plausible under this analysis”?
- What runtime is appropriate? A 3.5–4.5 minute target may be better than a long
  statistics primer.

## Current disposition

This outline is future-facing pre-production material. It does not change the
current upload gates for the green-checkmarks or thinking-partner candidates, and
it is not a commitment to produce or upload this video during the current goal.
