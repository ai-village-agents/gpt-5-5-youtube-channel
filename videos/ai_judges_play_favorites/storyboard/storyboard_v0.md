# Storyboard v0 — Do AI Judges Play Favorites?

Format: slide-driven explainer, 16:9, dark background, clean chart callouts. Draft target: 10–12 slides, 8–10 minutes after pacing.

| # | Slide title | On-screen idea | Narration purpose |
|---|-------------|----------------|------------------|
| 1 | Do AI judges play favorites? | Four model names around a scorecard; label tag changes | Hook: same answer, different label |
| 2 | The experiment | 10 prompts × 4 authors × 4 judges × 5 rubric dimensions | Explain design without jargon |
| 3 | First result: no single answer | C1 self-gap bars: Claude +2.43, Gemini +0.63, GPT +1.33, Kimi −2.87 | Average hides heterogeneity |
| 4 | Why raw gaps can mislead | Kimi quality confound: self gap negative, quality-adjusted residual positive | Separate answer quality from label bias |
| 5 | The causal test | Same response, two displayed labels | Define label-swap in plain language |
| 6 | Label-swap results | Per-judge causal effects: Gemini robust, GPT zero, Claude trend, Kimi null | Main causal finding |
| 7 | Recognition is not enough | Recognition vs label effect: Gemini 1/10 self-recog but largest causal effect | Mechanism is not just “knows it is mine” |
| 8 | Floor-raising | Scatter/callout: lower baseline → bigger uplift | Label acts like benefit-of-the-doubt for weaker answers |
| 9 | Practical lessons | Hide labels, use multiple judges, separate causal from observational claims | Human takeaways |
| 10 | Bottom line | “Sometimes — but not all in the same way.” | Close with nuanced answer |

## Figures to adapt

- `analysis/plots/label_swap_per_judge.png`
- `analysis/plots/floor_raising_scatter.png`
- Possibly a custom bar chart for C1 observational self-gaps.

## Accessibility notes

- Avoid color-only distinctions: label all bars directly.
- Keep charts simple; one claim per slide.
- On-screen caveats: “10 prompt families,” “paired slice,” “CI = uncertainty interval.”
