# Series claims matrix

This matrix summarizes the five-video AI Evaluation Literacy arc. It is designed for skeptical viewers and future maintainers who want the core claim, evidence type, caveat, and viewer action for each video in one place.

| Video | Core claim | Evidence type | Main caveat | Viewer action |
| --- | --- | --- | --- | --- |
| V1 — [Do AI Judges Play Favorites? We Ran a Blind Test.](https://youtu.be/AHLi0xU0WXs) | AI-judge behavior is heterogeneous; one headline self-preference claim is too simple. | Mixed study overview: blind scoring, recognition checks, observational gaps, and paired label swaps. | Do not turn this into "all AI judges always favor themselves." Kimi's observational result is prompt-set quality-confounded. | Ask whether an evaluation separates observational patterns from causal label tests. |
| V2 — [How to Audit an AI Judge in 5 Steps](https://youtu.be/aS1QOuY33Qs) | A practical audit can test whether irrelevant labels move AI-judge scores. | Method explainer built around paired label-swap comparisons and rubric discipline. | Label hiding is useful but not complete; proxies, rubrics, thresholds, and aggregation choices still matter. | Define the decision, freeze the rubric, swap labels, compare paired differences, and redesign if labels move scores. |
| V3 — [The Average Can Hide the Bias](https://youtu.be/IBBc7qiupIk) | A pooled average can hide judge-specific direction changes and risky slices. | Decomposition of pooled observational and judge-specific results. | The average is not fake; it is incomplete when heterogeneous effects cancel or concentrate. | Report the average, then inspect the parts before trusting the headline. |
| V4 — [How to Tell If an AI Evaluation Claim Is Trustworthy](https://youtu.be/3tFwuXbqO00) | Trustworthy evaluation claims answer concrete questions about test scope, measurement, causality, heterogeneity, uncertainty, and receipts. | General reader checklist distilled from the study and repo artifacts. | A checklist cannot make weak evidence strong; it makes missing evidence visible. | Fill in a trust statement: tested population, measured outcome, main confound, important slices, uncertainty, and receipts. |
| V5 — [The Bias That Looks Like Mercy](https://youtu.be/GcTM2DFHmXc) | Some label effects matter most near the floor or decision threshold, not as a uniform bonus. | Floor-raiser pattern from paired label-swap effects and threshold examples. | "Mercy" is an operational metaphor for score movement, not a claim about model motives. GPT-5.5 was label-invariant only in the paired slice. | Inspect borderline cases; a small score movement can flip a decision even when the mean effect looks modest. |

## Cross-series claims

The series repeatedly uses these claims, each with an explicit limit:

| Claim | Safer wording | Limit |
| --- | --- | --- |
| Label effects exist in the study. | Some displayed-label effects appear in some judge families and slices. | Not universal across judges; GPT-5.5 is invariant in the paired slice. |
| Recognition is relevant. | Recognition and displayed-label effects should both be measured. | Recognition does not by itself explain label bias. |
| Averages are useful. | Averages are a starting point. | Heterogeneity can make a pooled average misleading for a specific decision. |
| Kimi's observational result is striking. | Kimi shows an observational self-penalty on this prompt set. | It is quality-confounded and not a general Kimi-quality claim. |
| Thresholds matter. | Small score movements near decision cutoffs can be practically important. | Practical importance depends on the decision rule and error costs. |

## One-sentence viewer takeaway

Before trusting an AI-evaluation headline, ask: **what exactly was tested, what changed, what stayed fixed, where does the average break, how uncertain is it, and where are the receipts?**

## Related docs

- [`evidence_map.md`](evidence_map.md) maps claims to source artifacts.
- [`viewer_faq.md`](viewer_faq.md) answers common skeptical questions.
- [`ai_evaluation_reader_checklist.md`](ai_evaluation_reader_checklist.md) gives the standalone checklist.
- [`evaluation_claim_audit_template.md`](evaluation_claim_audit_template.md) gives a fillable worksheet.
- [`errata_policy.md`](errata_policy.md) describes how to correct mistakes without silently rewriting claims.
