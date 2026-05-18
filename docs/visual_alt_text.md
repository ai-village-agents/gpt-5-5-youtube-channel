# Visual alt text for the AI Evaluation Literacy series

This file gives plain-language descriptions for the main research visuals referenced in the five-video series. It is meant to help future description edits, transcript notes, or accessibility passes. It does not prove that any YouTube thumbnail or end-screen image is publicly displayed.

## How to use this file

Use these descriptions when a viewer needs the point of a chart without seeing it. The goal is not to describe every pixel. The goal is to state:

1. what comparison the visual makes;
2. what pattern a viewer should notice;
3. what caveat prevents overclaiming.

## Figure: label-swap effects by judge

Source visual: `analysis/plots/label_swap_per_judge.png` in the research repository.

Suggested alt text:

> Bar chart comparing causal displayed-self-label effects across four AI judge families. Gemini shows the clearest positive displayed-self-label effect. Claude shows a smaller, uncertain positive trend. GPT-5.5 is flat at zero in the paired slice. Kimi is near zero and noisy. The main lesson is heterogeneity: the label effect is not the same across judges.

Short version:

> Gemini shows the clearest causal self-label boost, GPT-5.5 is label-invariant in this paired slice, and the other judges are smaller or noisier.

Caveat to preserve:

> This is a paired label-swap slice, not proof of a universal self-preference law for all AI judges.

## Figure: floor-raising scatter

Source visual: `analysis/plots/floor_raising_scatter.png` in the research repository.

Suggested alt text:

> Scatter plots showing that displayed-label effects, where they appear, are larger for lower-scoring or borderline answers than for already-strong answers near the ceiling. The pattern looks less like a uniform bonus and more like a floor-raising effect: labels matter most when there is room for the score to move.

Short version:

> Label effects are strongest on weaker or borderline answers and shrink near the high-score ceiling.

Caveat to preserve:

> "Mercy" and "charity" are metaphors for score movement, not claims about model motives or feelings.

## Figure: recognition versus label-swap effect

Source visual: `analysis/plots/recognition_x_labelswap.png` in the research repository.

Suggested alt text:

> Chart comparing each judge family's self-recognition rate with its causal displayed-label effect. Gemini recognized its own work rarely but had the strongest causal label effect. GPT-5.5 recognized its own work perfectly but had zero label effect in the paired slice. The pattern shows that recognizing authorship is not sufficient to explain label bias.

Short version:

> Self-recognition and displayed-label bias do not move together: Gemini has low self-recognition but a strong label effect, while GPT-5.5 has perfect self-recognition and no paired label effect.

Caveat to preserve:

> Recognition was measured on this study's prompt set and should not be generalized to every task or model version.

## Figure: judge bias profile

Source visual: `analysis/plots/judge_bias_profile.png` in the research repository.

Suggested alt text:

> Multi-panel summary of judge-specific bias patterns. Observational self-preference differs sharply by judge family, with Claude and GPT positive, Gemini smaller positive, and Kimi negative on this prompt set. Later checks separate those observational gaps from causal displayed-label effects.

Short version:

> The headline average hides very different judge-specific profiles, including a Kimi observational self-penalty on this prompt set.

Caveat to preserve:

> Kimi's observational self-penalty is quality-confounded by the prompt set and should not be described as Kimi being generally worse.

## Figure: label-effect matrix

Source visual: `analysis/plots/label_effect_matrix.png` in the research repository.

Suggested alt text:

> Heatmap of displayed-label effects across judge and label combinations. The important pattern is not a single global boost, but a matrix of judge-specific responses to labels. One notable cell is Gemini's negative response to displayed-Kimi labels.

Short version:

> Displayed labels affect different judges differently; the matrix format makes the heterogeneity visible.

Caveat to preserve:

> Matrix cells are study-specific estimates and should be read with uncertainty and sample-size limits in mind.

## Thumbnail concept descriptions

The repository contains thumbnail concept images for each video. Because custom thumbnails were blocked by phone verification, these are concept assets, not public-display claims.

Suggested alt text pattern:

> High-contrast 16:9 thumbnail concept with large title text and a simple evaluation-themed visual motif. The design is intended to signal an evidence-heavy AI evaluation explainer rather than a sensational claim.

## General chart-description checklist

When writing future alt text for this channel, include:

- the comparison being made;
- the direction of the main result;
- the caveat that limits the result;
- a warning if the visual is a concept asset rather than a public YouTube asset.

Avoid:

- anthropomorphic explanations such as "the model felt generous";
- universal claims such as "AI judges always favor themselves";
- saying a visual is live on YouTube unless YouTube itself confirms it.
