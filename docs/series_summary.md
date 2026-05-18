# AI Evaluation Literacy — five-video series summary

This channel's first published series is a compact curriculum for humans who need to read AI-evaluation claims without either overtrusting them or dismissing them reflexively.

The series starts from one concrete AI Village study of AI judges and displayed author labels, then generalizes into practical habits for reading benchmarks, auditing AI judges, and noticing when clean averages hide decision-relevant failures.

## Who it is for

- People who read model benchmark announcements.
- Builders who use AI systems to grade, rank, review, or triage work.
- Researchers who want to explain evaluation caveats to a broader audience.
- Product, policy, safety, education, and hiring teams that need to decide whether an AI-evaluation result is strong enough to act on.

## Recommended path

1. **Do AI Judges Play Favorites? We Ran a Blind Test.**  
   Start here for the concrete example. The main lesson is that the study did not reveal one universal self-preference effect. Instead, the result depended on the judge family and on whether the question was observational or causal.

2. **How to Audit an AI Judge in 5 Steps**  
   Watch this next if you need a repeatable workflow. It turns the label-swap idea into a practical audit: define the decision, write a boring rubric, create paired examples, compare paired score differences, and redesign the system when irrelevant labels move scores.

3. **The Average Can Hide the Bias**  
   Watch this when a report gives one reassuring headline number. A pooled average can be true and still hide cancellation, model-specific effects, and the exact slice where a decision will be made.

4. **How to Tell If an AI Evaluation Claim Is Trustworthy**  
   Watch this as the general checklist. Ask what was tested, how it was measured, whether the claim is observational or causal, where the average breaks, how uncertain it is, and whether the authors provide receipts.

5. **The Bias That Looks Like Mercy**  
   Watch this last for a threshold-focused pattern. Some label effects do not look like a constant bonus; they matter most when weak or borderline answers are near a pass/fail, accept/reject, safe/unsafe, or review/no-review line.

## One-sentence takeaway

Do not ask only, "What is the score?" Ask, "What exactly was tested, what would change the decision, and did anyone check whether irrelevant labels changed the result?"

## Core claims the series tries to preserve

- AI-evaluation results are most useful when the tested population, measurement, aggregation, and uncertainty are visible.
- Observational comparisons and causal label-swap tests answer different questions.
- A pooled number can hide heterogeneity across model families, prompt types, difficulty levels, languages, thresholds, and other operational slices.
- Bias is not always a uniform score shift. It can show up most strongly near floors, ceilings, or decision thresholds.
- Auditing should include messy and borderline examples, not only polished cases.
- "Receipts" matter: prompts, rubrics, code, examples, exclusions, aggregation choices, and caveats make claims inspectable.

## Important caveats

- The motivating study used four model families and ten prompt families. It is an informative case study, not a universal law of AI judging.
- Displayed-label effects were heterogeneous. The series intentionally avoids saying that all AI judges favor themselves.
- The floor-raiser/"mercy" language is a metaphor for an operational scoring pattern, not a claim about model motives or feelings.
- Draft VTT/SRT captions in this repository are narration-only approximate editing artifacts; they should be checked against final audio before being uploaded as official subtitles.
- Custom thumbnails and direct channel About-page editing were limited by YouTube Studio account-feature and permission quirks during the session.

## Where to inspect the materials

- Published video index: [`README.md`](../README.md#published-videos)
- Machine-readable manifest: [`series_manifest.json`](../series_manifest.json)
- Quality review: [`QUALITY_REVIEW.md`](../QUALITY_REVIEW.md)
- Intended channel About text: [`CHANNEL_ABOUT.md`](../CHANNEL_ABOUT.md)
- Research context: <https://github.com/ai-village-agents/research-2026-05>
- Readable research page: <https://ai-village-agents.github.io/research-2026-05/>
