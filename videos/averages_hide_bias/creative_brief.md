# Creative brief — The Average Can Hide the Bias

## Working title
The Average Can Hide the Bias

## Purpose
Create a human-facing explainer about a common evaluation mistake: collapsing heterogeneous AI-judge behavior into one headline average. The video uses the AI Village label-swap/self-preference study as a concrete case, but the durable lesson is broader: when systems behave differently, the average can cancel the thing you needed to notice.

## Audience
Humans who read AI benchmark reports, use LLM judges, manage evaluation pipelines, or make decisions from dashboards. No prior statistics background assumed.

## Core promise
By the end, viewers should know how to look past a single pooled score and ask for subgroup/model-specific results, paired contrasts, and uncertainty before acting on an AI evaluation claim.

## Main idea
A pooled number can be mathematically true and practically misleading. In the study, the pooled observational self-preference gap was small: about +0.38 points. But that average combined large positive gaps for Claude and GPT, a smaller positive Gemini gap, and a large negative Kimi gap. The average did not reveal one simple reality; it mixed several different realities.

## Key facts to use
- Observational C1 self-preference gaps:
  - Claude +2.433
  - Gemini +0.627
  - GPT +1.327
  - Kimi −2.873
  - Pooled +0.378 [−0.330,+1.055]
- Native paired label-swap self-vs-other residuals:
  - Claude +0.120 [−0.067,+0.304]
  - Gemini +0.293 [+0.142,+0.452]
  - GPT +0.000 [+0.000,+0.000]
  - Kimi +0.007 [−0.305,+0.344]
  - Pooled 4J +0.105
- Interpretation: not one universal self-preference; heterogeneous model-family behavior.
- Practical lesson: report the average, but also report the parts.

## Tone
Calm, useful, slightly visual. Avoid statistics jargon where possible. Explain with simple physical metaphors: heat map, four thermometers, cancellation, averaging hot and cold rooms.

## Distinctness from earlier videos
- Video 1: study overview and checklist.
- Video 2: practical five-step audit.
- This video: interpretation discipline — why pooled averages can hide actionable behavior.

## Guardrails
- Do not claim averages are bad. Say they are useful summaries with failure modes.
- Do not imply Kimi's negative observational gap means Kimi is generally worse; emphasize this prompt set and design.
- Separate observational gaps from causal label-swap effects.
- Avoid saying “Simpson’s paradox” as the main frame unless clearly explained; the target lesson is simpler: cancellation and heterogeneity.
