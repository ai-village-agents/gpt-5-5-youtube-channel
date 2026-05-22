# Day 416 confidence-interval explainer script v0

Working title: **The Line Around the Number: Reading Confidence Intervals in AI Claims**  
Status: **script draft only; not rendered, not captioned, not reviewed, and not upload approval.**  
Brief: [`day416_confidence_intervals_creative_brief_v0.md`](day416_confidence_intervals_creative_brief_v0.md)  
Outline: [`day416_confidence_intervals_outline_v0.md`](day416_confidence_intervals_outline_v0.md)  
Source map: [`day416_confidence_intervals_source_claim_map_v0.md`](day416_confidence_intervals_source_claim_map_v0.md)

## Script draft

### 01 — The lonely number

A number can look more certain than it is.

Imagine reading an AI evaluation claim that says: plus zero point two nine.

That is clean. It is compact. It fits in a headline.

But a point estimate is not the whole result. It is the center of a claim.

The question is: how much room is there around that center?

A single number is a headline. The interval around it is the part that tells you
how carefully to read the headline.

### 02 — Add the line around the number

So put the line back.

In one paired slice of an AI-judge study, Gemini's displayed-self-label gap was
reported as plus zero point two nine, with an interval from plus zero point one
four to plus zero point four five.

Now the number has a shape.

The dot is the estimate. The line is the range that remained plausible under
that analysis.

Here, the line stays above zero. That does not make it universal. It does not say
all judges behave this way. It says that, in this paired slice, the positive
direction is supported more clearly than the dot alone could show.

### 03 — When the line crosses zero

Now compare a different example.

For Claude in the same kind of paired slice, the displayed-self-label gap was
reported as plus zero point one two, with an interval from minus zero point zero
seven to plus zero point three zero.

The dot still leans positive.

But the line crosses zero.

That changes the reading. It is not the same kind of evidence as a line that
stays entirely above zero.

The dot says: the center leans positive. The line says: do not treat that lean as
settled.

Crossing zero does not prove the effect is exactly zero. It means this estimate,
with this uncertainty, is not enough by itself to make a clean positive claim.

### 04 — Near zero with a wide line

A near-zero dot can also mislead if you quote it alone.

For Kimi in that paired slice, the gap was about plus zero point zero one, with
an interval from minus zero point three zero to plus zero point three four.

If you only quote the dot, it sounds like nothing happened.

But the line says something more careful: this estimate is near zero, and the
range still spans negative and positive values.

A near-zero dot is useful. A wide line says what it has not ruled out.

So do not turn this into: Kimi has no label bias. The honest reading is narrower:
this paired estimate was near zero, with uncertainty on both sides.

### 05 — Your threshold may not be zero

Zero is not always the decision you care about.

Suppose you would only act on an evaluation gap if it were at least plus zero
point five. That threshold is not from the study. It is just an example of a
practical decision line.

Now look again at the Gemini interval: plus zero point one four to plus zero
point four five.

It stays above zero, so the direction is clearer. But if your action threshold is
plus zero point five, the whole interval is still below the line you care about.

That is the difference between a statistical reading and a practical decision.

An interval can support a direction and still be too small for your use case.

### 06 — Statistical uncertainty is not the only uncertainty

One more caution.

A confidence interval is not a force field around a claim.

It describes uncertainty under the analysis that produced it. It does not remove
questions about the prompt set, the paired slice, the judge family, the scoring
rubric, or the decision you are trying to make.

That is why the label matters: one study, one slice, one decision.

The interval helps you read the estimate. It does not erase the design caveats
around the estimate.

### 07 — The five-question habit

Here is the habit I want you to keep.

First: what is the point estimate?

Second: what range is still plausible under this analysis?

Third: does that range cross zero, or the decision threshold I actually care
about?

Fourth: is the range narrow enough for this decision?

Fifth: what design caveat remains even if the interval was computed correctly?

If you ask those five questions, you do not have to reject the number. You can
use it more honestly.

### 08 — Closing

The goal is not to make every result feel vague.

The goal is to stop a clean number from pretending to be the whole result.

Keep the number.

Just do not quote it without the line around it.

## Script guardrails

This draft intentionally uses the paired SELF-OTHER label-gap examples for the
main sequence and does not use the pooled C1 interval as a headline claim. It
also keeps the `+0.50` threshold explicitly illustrative. Before any rendering,
run a fresh source-claim review, caption-readability pass, and full publish-gate
process from scratch.
