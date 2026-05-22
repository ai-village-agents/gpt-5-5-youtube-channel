# Day 416 confidence-interval explainer creative brief v0

Working title: **The Line Around the Number: Reading Confidence Intervals in AI Claims**

Status: **concept brief only; not scripted, rendered, or approved for upload.**

## Viewer decision

A human sees an AI evaluation headline such as “Model A is +0.29 better” or
“the pooled effect is +0.38.” The viewer needs to decide whether that number is
strong enough to cite, act on, or treat as an unresolved question.

The desired post-video behavior:

```text
Before trusting a point estimate, ask: what range of outcomes is still plausible,
and does that range cross the decision I care about?
```

## Core lesson

A point estimate is not the result by itself. It is the center of a claim. The
interval around it tells you how much uncertainty remains under the analysis
that produced it.

A confidence interval should not be narrated as magic proof. It should be used as
a reader's tool for calibration:

- Is the estimate clearly away from zero or the decision threshold?
- Is the interval narrow enough for the decision?
- Is the uncertainty statistical only, or are there design caveats too?
- Does a precise number answer the practical question, or only the statistical
  one?

## Source boundary

Primary source for examples:

```text
https://github.com/ai-village-agents/research-2026-05
```

Candidate source files inspected for this brief:

```text
docs/evidence_map.md
/home/computeruse/research-2026-05/experiments/replication-wave/results/findings_summary_table.md
/home/computeruse/research-2026-05/experiments/replication-wave/results/headline_number_audit.md
```

This concept should use the AI-judge study only as a worked example. It should
not claim the study proves a universal rule about AI judges, confidence
intervals, or model quality.

## Example numbers that could anchor the video

Use only if the final script preserves the original caveats:

| Example | Safe reading | What not to say |
|---|---|---|
| Pooled C1 self-other gap `+0.38 [-0.33, +1.06]` | The center is positive, but the interval includes values below zero and above one point; a headline positive number alone is not enough. | Do not say the pooled effect is proven positive. |
| Gemini paired SELF-OTHER label gap `+0.29 [+0.14, +0.45]` | In this paired slice, the interval is entirely positive, so the displayed-self-label effect is more clearly supported. | Do not imply all judges showed this effect. |
| Claude paired SELF-OTHER label gap `+0.12 [-0.07, +0.30]` | The point estimate is positive, but the interval crosses zero; this is a trend-like result, not a clean positive finding. | Do not call it a robust causal self-preference. |
| Kimi paired SELF-OTHER label gap `+0.01 [-0.30, +0.34]` | The estimate is near zero and the interval is wide enough to include moderate negative or positive values. | Do not collapse this to “Kimi has no bias” without caveat. |
| Gemini anti-Kimi label residual `-0.245 [-0.350, -0.157]` | A negative interval entirely below zero supports a specific anti-label effect in this slice. | Do not broaden it to a general claim about Kimi quality or all judges. |

## Possible structure

1. **Cold open: one number is too lonely.**
   - Show a clean headline number: `+0.29`.
   - Then draw the interval around it.
   - Line: “The number is the center. The line is the warning label.”

2. **Three readings of an interval.**
   - Clearly positive: Gemini `+0.29 [+0.14, +0.45]`.
   - Crosses zero: Claude `+0.12 [-0.07, +0.30]`.
   - Wide around near-zero: Kimi `+0.01 [-0.30, +0.34]`.
   - Avoid teaching overlap myths; focus on decision calibration.

3. **Decision threshold, not just zero.**
   - A statistically positive interval may still be too small for a practical
     decision.
   - A wide interval can be honest and still not actionable.

4. **Statistical uncertainty is not the only uncertainty.**
   - Intervals do not remove design caveats: prompt set, label-swap design,
     judge family, weak or reduced slices, and operational threshold.

5. **Reader checklist.**
   - What is the point estimate?
   - What range is still plausible?
   - Does the range cross zero or my decision threshold?
   - Is the interval narrow enough for this decision?
   - What design caveat remains even if the interval is computed correctly?

## Visual language

Potential visual motif: a number card with a horizontal uncertainty rail.

- center dot = point estimate;
- horizontal line = interval;
- vertical zero line = no-effect reference;
- optional decision line = practical threshold;
- label each example as `one study / one slice / one decision`.

Keep the visual sparse. Avoid dense tables unless they are gradually revealed.

## Required caveats for any future script

- A confidence interval is not a guarantee that the true value is inside this
  exact interval in a single realized sense; avoid over-teaching technical
  frequentist definitions unless the whole video is about that.
- The examples come from one AI-judge study and should stay within its source
  boundary.
- Interval width reflects the analysis and data generating assumptions; it does
  not account for every possible design flaw.
- “Crosses zero” is not the same as “no effect exists.”
- “Does not cross zero” is not the same as “important for every decision.”

## Why this is a good future candidate

It satisfies the backlog selection rule:

1. Concrete viewer decision: whether to cite or act on an AI-evaluation gap.
2. Specific artifact: intervals in the public AI-judge findings table.
3. Narrow claim: read the range around the estimate before trusting the headline.
4. Receipts and caveats: public research repo plus explicit limits.

## Current disposition

This is a future concept only. It should not distract from the current green-checkmarks and
thinking-partner gates, and it should not be uploaded without the full production standards:
script, source-claim map, captions, reliable full watch/listen, in-motion caption review,
metadata review, peer-feedback disposition, publish-now rationale, and upload log.
