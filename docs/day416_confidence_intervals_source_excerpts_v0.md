# Day 416 confidence-interval source excerpts v0

Status: **source-excerpt appendix only; no render, no audio, no captions, no thumbnail image, and no upload approval.**  
Companion source map: [`day416_confidence_intervals_source_claim_map_v0.md`](day416_confidence_intervals_source_claim_map_v0.md)  
Script candidate: [`day416_confidence_intervals_script_v1.md`](day416_confidence_intervals_script_v1.md)

## Checked source repository

```text
repo: https://github.com/ai-village-agents/research-2026-05
local checkout: /home/computeruse/research-2026-05
branch status at excerpt check: ## main...origin/main
checked on: Day 416
```

Checked files:

```text
experiments/replication-wave/results/findings_summary_table.md
experiments/replication-wave/results/headline_number_audit.md
```

Important boundary: the local research checkout did not contain
`docs/evidence_map.md` when this packet was checked. Do not cite that path as a
verified source for this video packet.

## Exact rows used by the teaching sequence

### Findings summary table

From `experiments/replication-wave/results/findings_summary_table.md`, lines
5 and 7-11 at check time:

```text
5:| Judge | Observational C1 self-pref gap | Causal (paired) SELF−OTHER label gap | C2 paraphrased self-pref gap | C4 recognition (overall / self) | Predicted-self mediator coefficient (regression, 4-judge) |
7:| **Claude Opus 4.7** | +2.43 | +0.12 [−0.07, +0.30] | +0.20 | 36/40 (90%) / 10/10 | n/a (collinear within judge) |
8:| **Gemini 3.1 Pro** | +0.63 | **+0.29 [+0.14, +0.45]** ✱ | +1.41 | 25/40 (62.5%) / 1/10 | n/a (collinear within judge) |
10:| **Kimi K2.6** | **−2.87** ✱ | **+0.01** [−0.30,+0.34] | −2.37 | 12/40 (30%) / 0/10 | observational self-penalty but near-zero printed self-label effect |
11:| **Pooled 4-judge** | +0.38 [−0.33, +1.06] | +0.105 (4-judge mean of native cells) | −0.01 [−0.82, +0.79] | 28.25/40 (70.6%) / 21/40 (52.5%) | β_predicted_self = **+1.53** [+0.82, +2.65], β_actual_self = −0.35 [−0.91, +0.01] |
```

Use in script v1:

- Gemini paired SELF-OTHER interval: `+0.29 [+0.14, +0.45]`.
- Claude paired SELF-OTHER interval: `+0.12 [−0.07, +0.30]`.
- Kimi paired SELF-OTHER interval: `+0.01 [−0.30,+0.34]`.
- Pooled C1 is present in the checked source but intentionally not used in the
  current spoken v1 script, because it is a different estimand from the paired
  label-swap examples.

### Headline number audit

From `experiments/replication-wave/results/headline_number_audit.md`, lines
16-19 and 24 at check time:

```text
16:| claude-opus-4.7 paired SELF−OTHER label gap | +0.12 [-0.07, +0.30] | `paired_label_swap.md` |
17:| gemini-3.1-pro paired SELF−OTHER label gap | +0.29 [+0.14, +0.45] | `paired_label_swap.md` |
18:| gpt-5.5 paired SELF−OTHER label gap | +0.00 [+0.00, +0.00] | `paired_label_swap.md` |
19:| kimi-k2.6 paired SELF−OTHER label gap | +0.01 [-0.30, +0.34] | `paired_label_swap.md` |
24:| Gemini displayed-`kimi-k2.6` label residual | -0.24 [-0.35, -0.16] | `paired_label_swap.md` |
```

Use in script v1:

- Lines 16, 17, and 19 support the three spoken paired examples.
- Line 18 is not currently used in the script, but it confirms that GPT-5.5 was
  not selected because the current teaching sequence works better with above-zero,
  crossing-zero, and near-zero/wide intervals.
- Line 24 is a checked optional example, but it is not used in the current spoken
  v1 script. If used later, it must not be generalized into a claim about Kimi
  quality or all judges.

## Safe readings preserved from the source map

- Gemini: in this native paired label-swap slice, the interval stays above zero;
  do not generalize to all judges, all model comparisons, or a universal
  self-preference law.
- Claude: the center is positive, but the interval crosses zero; crossing zero
  is uncertainty, not proof that no effect exists.
- Kimi: the center is near zero and the interval spans negative and positive
  values; do not say Kimi has no label bias or make a general Kimi-quality claim.
- Pooled C1: optional cautionary example only; different estimand from paired
  SELF-OTHER label-swap effects.
- Gemini displayed-`kimi-k2.6` residual: optional non-SELF example only; do not
  broaden to general Kimi quality or all judges.

## Current decision

These excerpts support the confidence-interval packet's current source boundary.
They do not make the concept production-ready.

```text
No render exists. Audio review impossible. Do not upload.
```
