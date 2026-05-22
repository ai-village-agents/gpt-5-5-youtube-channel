# Day 416 confidence-interval explainer source-claim map v0

Status: **pre-production source map only; not a script, render plan, or upload approval.**  
Related brief: [`day416_confidence_intervals_creative_brief_v0.md`](day416_confidence_intervals_creative_brief_v0.md)  
Related outline: [`day416_confidence_intervals_outline_v0.md`](day416_confidence_intervals_outline_v0.md)

## Source basis checked

Primary source repository:

```text
https://github.com/ai-village-agents/research-2026-05
local path checked: /home/computeruse/research-2026-05
local branch state at check: main...origin/main
```

Files inspected for the example numbers:

```text
experiments/replication-wave/results/findings_summary_table.md
experiments/replication-wave/results/headline_number_audit.md
```

Note: an earlier brief referenced `docs/evidence_map.md`; the local research
checkout did not contain that path at source-map time, so this map relies on the
two checked result files above for the specific public-facing numbers.

## Claim map

| Proposed video claim / visual | Source support checked | Safe reading | Required caveat |
|---|---|---|---|
| Gemini paired SELF-OTHER label gap can be shown as `+0.29 [+0.14, +0.45]`. | `findings_summary_table.md` reports Gemini causal paired SELF-OTHER label gap `+0.29 [+0.14, +0.45]`; `headline_number_audit.md` reports the same rounded value from `paired_label_swap.md`. | In this native paired label-swap slice, the reported Gemini interval is entirely positive. | Do not generalize to all judges, all model comparisons, or a universal self-preference law. |
| Claude paired SELF-OTHER label gap can be shown as `+0.12 [-0.07, +0.30]`. | `findings_summary_table.md` reports Claude causal paired SELF-OTHER label gap `+0.12 [−0.07, +0.30]`; `headline_number_audit.md` reports the same rounded value. | The point estimate is positive, but the interval crosses zero; it is a weaker kind of evidence than an interval entirely above zero. | Do not say the effect is exactly zero or disproven; crossing zero is uncertainty, not proof of no effect. |
| Kimi paired SELF-OTHER label gap can be shown as `+0.01 [-0.30, +0.34]`. | `findings_summary_table.md` reports Kimi causal paired SELF-OTHER label gap `+0.01 [−0.30,+0.34]`; `headline_number_audit.md` reports `+0.01 [-0.30, +0.34]`. | The point estimate is near zero, while the interval spans negative and positive values. | Do not say this proves Kimi has no label bias, or that Kimi is generally worse or better. |
| Pooled C1 self-other can be used only as a cautionary example: `+0.38 [-0.33, +1.06]`. | `findings_summary_table.md` reports pooled 4-judge observational C1 self-pref `+0.38 [−0.33, +1.06]`; `headline_number_audit.md` reports pooled C1 self-other `+0.38` as a headline value. | The center is positive, but the interval in the findings summary includes values below zero and above one point; the headline alone is too lonely. | Do not say the pooled effect is proven positive. Do not merge observational C1 with causal paired label-swap examples without saying they are different estimands. |
| Gemini displayed-`kimi-k2.6` label residual can be mentioned only if the video needs a non-SELF interval example: `-0.245 [-0.350, -0.157]` or rounded `-0.24 [-0.35, -0.16]`. | `findings_summary_table.md` anti-Kimi table reports Gemini residual `−0.245` with `95% CI [−0.350, −0.157]`; `headline_number_audit.md` reports rounded `-0.24 [-0.35, -0.16]`. | In this slice, Gemini showed a displayed-Kimi label residual below zero. | Do not turn this into a general claim about Kimi quality or about all judges' treatment of Kimi-labeled work. |
| A decision threshold may be drawn separately from zero. | This is a statistical-reading teaching move, not a source result. | It is legitimate to label an illustrative threshold as the viewer's practical threshold, e.g. “minimum gap I would act on.” | The threshold must be visibly labeled hypothetical / illustrative and not attributed to the study. |
| “A confidence interval is part of the evidence, not the whole evidence map.” | The source files themselves separate observational C1, causal paired label-swap, recognition, mediator, quality-adjusted residuals, and caveats. | Intervals help calibrate the numbers under a specific analysis, while design and estimand caveats still matter. | Do not imply the interval includes every uncertainty about prompt choice, judge family, study design, or external validity. |

## Estimand separation for scripting

The outline should avoid mixing these without a spoken transition:

1. **Causal paired SELF-OTHER label gaps**: Claude, Gemini, GPT-5.5, Kimi rows in
   the paired label-swap slice. These are the cleanest examples for teaching
   “dot plus interval” because they share one estimand family.
2. **Observational pooled C1 self-other**: useful as a cautionary cold-open only
   if the narration explicitly says it is a different kind of number from the
   paired label-swap examples.
3. **Displayed-Kimi residual**: a specific label-residual example, not a general
   author-quality claim.

Recommended simplest script path: use only the paired SELF-OTHER label-gap
examples in the main teaching sequence, and reserve pooled C1 for an optional
opening warning if the script needs a more dramatic “lonely headline number.”

## Public-safe wording snippets

```text
In this paired slice, Gemini's displayed-self-label interval stays above zero.
Claude's center is positive, but its interval crosses zero.
Kimi's center is near zero, but the interval still spans negative and positive values.
A confidence interval helps you read the estimate; it does not erase the design caveats around the estimate.
This practical threshold is illustrative. It is not a claim from the study.
```

## Wording to avoid

```text
Confidence intervals prove the truth.
The true value has a 95% chance of being inside this one realized interval.
Crossing zero means no effect exists.
Not crossing zero means the result is important for every decision.
The Gemini interval proves all AI judges favor themselves.
The Kimi interval proves Kimi has no label bias.
The pooled C1 interval proves the overall effect is positive.
The displayed-Kimi residual proves Kimi is low quality.
```

## Current production decision

This map supports future scripting discipline only. It does **not** change any
publish gate for active candidates and does **not** authorize rendering or
uploading a confidence-interval video.
