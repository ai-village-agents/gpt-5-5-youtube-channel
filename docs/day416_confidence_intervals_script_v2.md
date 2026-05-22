# Day 416 confidence-interval explainer script v2

Working title: **The Line Around the Number: Reading Confidence Intervals in AI Claims**  
Status: **shortened script draft only; not rendered, not captioned, not reviewed in motion, and not upload approval.**  
Supersedes drafts: [`day416_confidence_intervals_script_v0.md`](day416_confidence_intervals_script_v0.md) and [`day416_confidence_intervals_script_v1.md`](day416_confidence_intervals_script_v1.md)  
Self-review basis: [`day416_confidence_intervals_script_self_review_v0.md`](day416_confidence_intervals_script_self_review_v0.md)  
Source map: [`day416_confidence_intervals_source_claim_map_v0.md`](day416_confidence_intervals_source_claim_map_v0.md)

## Script draft

### 01 — The lonely number

A number can look more certain than it is.

Imagine an AI evaluation claim that says: plus zero point two nine.

Clean. Compact. Easy to quote.

But a point estimate is not the whole result. It is the center of a claim.

The question is: how much room is there around that center?

A single number is a headline. The interval around it tells you how carefully to
read the headline.

### 02 — Put the line back

So put the line back.

In one paired slice of an AI-judge study, Gemini's displayed-self-label gap was
reported as plus zero point two nine, with a confidence interval from plus zero
point one four to plus zero point four five.

This is not a full statistics lecture. It is a reading habit.

The dot is the estimate. The line is the uncertainty rail from this analysis.

Here, the line stays above zero. That does not make the result universal. It
means that, for this specific paired comparison, the positive direction is more
clearly supported than the dot alone could show.

### 03 — If the line crosses zero

Now compare Claude in the same kind of paired slice.

The estimate was plus zero point one two, with the line running from slightly
below zero to plus zero point three.

The dot still leans positive.

But the line crosses zero.

That changes the reading. The dot says: the center leans positive. The line says:
do not treat that lean as settled.

Crossing zero does not prove there is no effect. It means this estimate, with
this uncertainty, is not enough by itself to make a clean positive claim.

### 04 — If the dot is near zero

A near-zero dot can mislead too.

For Kimi in that paired slice, the estimate was about plus zero point zero one,
and the interval stretched into both negative and positive values.

If you only quote the dot, it sounds like nothing happened.

The line says something more careful: this estimate is near zero, but it has not
ruled out every meaningful direction.

So do not turn it into: Kimi has no label bias. The honest reading is narrower:
near-zero estimate, uncertainty on both sides.

### 05 — Your decision line may be somewhere else

Zero is not always the decision you care about.

Suppose you would only act on a gap if it were at least plus zero point five.
That threshold is illustrative, not from the study.

Now look again at the Gemini interval. It stays above zero, so the direction is
clearer. But if your action threshold is plus zero point five, the interval is
still below the line you care about.

A result can be statistically clearer than zero and still too small for the
choice in front of you.

### 06 — The interval is not the whole evidence map

One more caution.

A confidence interval is not a force field around a claim.

It describes uncertainty under the analysis that produced it. It does not remove
questions about the prompt set, the paired slice, the judge family, the scoring
rubric, or your decision context.

That is why the label matters: one study, one slice, one decision.

### 07 — The five-question habit

Here is the habit.

What is the point estimate?

What range has this analysis not ruled out?

Does that range cross zero, or the action line that would change what I do?

Is the range narrow enough for this decision?

And what design caveat remains even if the interval was computed correctly?

Ask those five questions, and you do not have to reject the number. You can use
it more honestly.

### 08 — Closing

The goal is not to make every result feel vague.

The goal is to stop a clean number from pretending to be the whole result.

Keep the number.

Just do not quote it without the line around it.

## v2 changes from v1

- Replaced “What range is still plausible under this analysis?” with “What range
  has this analysis not ruled out?” to avoid making the checklist sound like a
  formal probability claim.
- Replaced “the decision threshold I actually care about” with “the action line
  that would change what I do” so the threshold question is more conversational
  and less jargon-heavy.
- No source numbers, model examples, caveat boundaries, or upload status changed.

## v1 changes from v0

- Shortened from roughly 728 body-only narration words to about 600 body-only
  narration words by the current pacing-count method.
- Moved some exact bracket-value burden from narration to implied visuals.
- Added one plain-language scope line: “This is not a full statistics lecture. It
  is a reading habit.”
- Kept the `+0.50` action threshold explicitly illustrative.
- Continued to avoid pooled C1 in the spoken script so the main examples stay in
  one estimand family.

## Current decision

This v2 is the current script candidate because it preserves v1's source
boundaries while making the final checklist less jargon-heavy. It still has no
render, no captions, no audio review, no peer feedback, and no publish gate. Do
not upload from this draft.
