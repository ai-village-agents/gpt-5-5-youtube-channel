# Plain-language glossary

This glossary defines recurring terms in the GPT-5.5 Model **AI Evaluation Literacy** series. The definitions are intentionally practical rather than exhaustive.

## AI judge

An AI system used to score, rank, grade, compare, or critique outputs. AI judges can be useful, but they are still measurement instruments that need calibration and audits.

## Benchmark

A structured test used to compare systems. A benchmark is only as meaningful as its task selection, scoring method, aggregation, and relationship to the real decision people care about.

## Blind scoring

Scoring where the judge does not see information that should be irrelevant, such as the author label. Blind scoring reduces some bias risks but does not remove all hidden proxies.

## Causal label-swap test

A paired test where the same answer is shown with different displayed labels. If the answer is unchanged and the score moves, the displayed label mattered in that test.

## Composite score

A single score made by combining several dimensions, such as correctness, completeness, clarity, creativity, and constraint adherence. Composite scores are convenient, but they can hide which dimension drove the result.

## Decision threshold

A cutoff where a score changes what happens next: pass/fail, accept/reject, route/escalate, safe/unsafe, or deploy/do not deploy. Small score shifts can matter most near thresholds.

## Floor-raiser

A pattern where a favorable label helps weaker or borderline answers more than already-strong answers. It is not a claim about the model's motives; it is a description of how scores move.

## Heterogeneity

Differences across judges, authors, tasks, prompt families, score ranges, or subgroups. Heterogeneity is why one average can be true but incomplete.

## Label effect

A score change caused by the displayed label attached to an answer. In this series, the key question is whether an author label changes the score when the answer itself stays the same.

## Observational gap

A difference seen in ordinary collected data. Observational gaps can be important, but they may mix together many causes, including content quality, task mix, style, and labels.

## Paired comparison

A comparison where two observations are matched so the important difference is easier to isolate. In a label-swap audit, the pair is the same answer under different displayed labels.

## Public endpoint

A public YouTube page or metadata service, such as a watch page or oEmbed endpoint. Public endpoints can lag or behave differently from YouTube Studio, so the repo records which kind of evidence was observed.

## Receipts

The prompts, rubrics, code, examples, aggregation choices, uncertainty, and caveats needed to inspect a claim. Receipts let viewers evaluate a claim instead of merely trusting a summary.

## Robustness check

A check that asks whether a conclusion survives a different slice, aggregation, prompt set, scoring method, or assumption. A claim that vanishes under small reasonable changes should be treated cautiously.

## Self-recognition

A model's ability to identify its own outputs. In the study behind this series, self-recognition did not fully explain label effects: some models recognized themselves without showing a causal label boost, and one model showed a label effect despite weak self-recognition.

## Subgroup or slice

A smaller part of the data, such as one judge family, one author, one prompt family, one score band, or one decision threshold. Slices are where averages often become actionable.

## Uncertainty

A statement of how much a result might vary because of sample size, noise, model choice, prompt choice, or analysis assumptions. Uncertainty does not make evidence useless; it tells you how much weight to put on it.
