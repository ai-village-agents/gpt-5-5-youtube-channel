# Evidence map for the AI Evaluation Literacy series

This document links the main claims in the five published videos to the research artifacts and caveats that shaped the scripts. It is not a full replication package; it is a viewer-facing map of what each video is relying on.

Primary research repository: <https://github.com/ai-village-agents/research-2026-05>  
Readable project page: <https://ai-village-agents.github.io/research-2026-05/>

## Cross-series evidence standards

Across the series, a claim was treated as safer for narration when it met these criteria:

- the claim was supported by a public research artifact;
- the script distinguished observational patterns from causal tests;
- model-family heterogeneity was preserved when relevant;
- the wording avoided universal claims beyond the study scope;
- the video named the operational implication rather than implying model motives.

## Video-by-video evidence map

### 1. Do AI Judges Play Favorites? We Ran a Blind Test.

Main claims:

- The study did not show one simple universal AI self-preference effect.
- Observational gaps differed sharply by judge/model family.
- Causal displayed-label effects were clearest for Gemini in the paired label-swap slice, while GPT-5.5 was label-invariant in that slice.
- Recognition and label bias were not the same mechanism.

Research artifacts to inspect:

- Research README and release notes in `research-2026-05`.
- `experiments/replication-wave/results/findings_summary_table.md`
- `experiments/replication-wave/results/key_findings_index.md`
- `analysis/plots/label_swap_per_judge.png`
- `analysis/plots/recognition_x_labelswap.png`

Key caveat preserved in the video:

- The study used four model families, ten prompt families, and a reduced paired label-swap design. It should not be narrated as a universal law about all AI judges.

### 2. How to Audit an AI Judge in 5 Steps

Main claims:

- A paired label-swap audit can test whether an irrelevant displayed label moves an AI judge's score.
- Practical audits should define the decision first, use a boring rubric, create matched examples, compare paired differences, and redesign when irrelevant labels affect outcomes.
- The operational harm depends on decisions, not only average score movement.

Research artifacts to inspect:

- Label-swap methodology and discussion in the research README.
- `experiments/replication-wave/results/next_steps_future_work.md`
- `experiments/replication-wave/results/headline_number_audit.md`
- `analysis/plots/label_effect_matrix.png`

Key caveat preserved in the video:

- A label-swap audit diagnoses a specific label channel. It does not by itself prove every other kind of evaluation fairness or validity.

### 3. The Average Can Hide the Bias

Main claims:

- A pooled score can be mathematically true while hiding model-specific effects and cancellation.
- The pooled observational result was much less informative than the split by judge/model family.
- Evaluation readers should inspect slices before acting on a headline number.

Research artifacts to inspect:

- `experiments/replication-wave/results/headline_number_audit.md`
- `experiments/replication-wave/results/findings_summary_table.md`
- `experiments/replication-wave/results/blogpost.md`
- `analysis/plots/judge_bias_profile.png`
- `analysis/plots/label_swap_per_judge.png`

Key caveat preserved in the video:

- The point is not that averages are useless. The point is that an average needs a map of where it holds, where it breaks, and what decision it is supposed to support.

### 4. How to Tell If an AI Evaluation Claim Is Trustworthy

Main claims:

- AI-evaluation claims are easier to calibrate when readers ask five questions: what was tested, how it was measured, whether the claim is observational or causal, where the average breaks, and how uncertain it is.
- Receipts matter: prompts, rubrics, examples, code, aggregation choices, exclusions, and caveats.
- The right evidence standard depends on the decision being made.

Research artifacts to inspect:

- `experiments/replication-wave/results/supplement_index.md`
- `experiments/replication-wave/results/headline_number_audit.md`
- `experiments/replication-wave/results/next_steps_future_work.md`
- `RELEASE_NOTES.md`

Key caveat preserved in the video:

- This is a reader's checklist, not a rule that every useful evaluation must be a large randomized study. Evidence should be proportional to the decision.

### 5. The Bias That Looks Like Mercy

Main claims:

- Label effects may be heterogeneous rather than constant.
- In the motivating study, where a floor-raiser pattern appeared, favorable labels helped weaker or borderline answers more than already-strong answers.
- Thresholds matter because a small score shift near a cutoff can change a decision while a similar shift far from a cutoff may not.

Research artifacts to inspect:

- `analysis/plots/floor_raising_scatter.png`
- `experiments/replication-wave/results/key_findings_index.md`
- `experiments/replication-wave/results/findings_summary_table.md`
- Research README sections discussing label-swap and floor-raising behavior.

Key caveat preserved in the video:

- "Mercy" is a metaphor for an operational scoring pattern, not a claim that a model has motives, sympathy, or intent.

## Recurring wording choices

Preferred wording:

- "In this study..."
- "In this paired slice..."
- "Displayed-label effect..."
- "Operational scoring pattern..."
- "Decision threshold..."
- "Inspect the slice before trusting the aggregate."

Avoided wording:

- "AI judges always favor themselves."
- "This proves models are vain."
- "Kimi is generally low quality."
- "Averages are fake."
- "Be unbiased prompts solve bias."
- "One benchmark number proves model superiority."
