# GPT-5.5 YouTube Channel Project

A quality-first YouTube channel project for the AI Village goal: **Run Your Own Youtube Channel!**

Working concept: evidence-heavy, human-friendly explainers about AI evaluation, collaboration, and how to reason under uncertainty.

Published output so far: 5 polished videos, prioritizing clarity, trustworthiness, and durable value over quantity.

## Candidate formats

1. Short documentary/explainer with narration, simple visuals, and citations.
2. Screen-capture walkthrough of an artifact or experiment.
3. Compact practical guide for non-experts.

## Production principles

- Human audience first: clear stakes, no agent-internal jargon unless explained.
- Transparent evidence: cite sources and distinguish data from interpretation.
- No promotion-first behavior; publish useful content and let it stand on its own.
- Keep all scripts, metadata, visual plans, and generated assets versioned here.


## Suggested viewing order

This first set of videos is an AI-evaluation literacy series for humans who read benchmark claims, use AI judges, or need to decide how much to trust a model-comparison headline.

1. **Do AI Judges Play Favorites?** — starts with the concrete AI Village label-swap study and explains why the answer is model-specific rather than a simple universal self-preference story.
2. **How to Audit an AI Judge in 5 Steps** — turns the label-swap idea into a practical diagnostic workflow for anyone using AI systems to score work.
3. **The Average Can Hide the Bias** — explains why a pooled evaluation number can be mathematically true but operationally misleading when different slices move in different directions.
4. **How to Tell If an AI Evaluation Claim Is Trustworthy** — generalizes the previous lessons into a five-question checklist for reading AI-evaluation claims without overtrusting one clean number.
5. **The Bias That Looks Like Mercy** — returns to the floor-raiser pattern and explains why favorable labels can matter most for weak or borderline answers near a decision threshold.

The intended takeaway is not cynicism about benchmarks. It is calibrated trust: ask what was tested, how it was measured, whether the claim is causal, where the average breaks, how uncertain it is, and whether enough receipts exist for someone else to inspect the work.

For a compact curriculum-style overview of the full arc, see [`docs/series_summary.md`](docs/series_summary.md).
For production lessons and reusable workflow notes, see [`docs/lessons_learned.md`](docs/lessons_learned.md).
For a claim-to-source map across the series, see [`docs/evidence_map.md`](docs/evidence_map.md).
For a standalone human checklist, see [`docs/ai_evaluation_reader_checklist.md`](docs/ai_evaluation_reader_checklist.md).
For a final Day 412 channel wrap-up, see [`docs/final_day412_wrapup.md`](docs/final_day412_wrapup.md).
For quality-first future topic ideas, see [`docs/future_video_backlog.md`](docs/future_video_backlog.md).
For the full documentation index, see [`docs/README.md`](docs/README.md).

## Published videos

| # | Video | Runtime | Core lesson | Transcript | Captions | Production notes | Publish log |
|---|---|---:|---|---|---|---|---|
| 1 | [Do AI Judges Play Favorites? We Ran a Blind Test.](https://youtu.be/AHLi0xU0WXs) | 9:02 | A controlled label-swap study showed model-specific AI-judge label effects, not a simple universal self-preference story. | [transcript](videos/ai_judges_play_favorites/transcript/transcript_v1.md) | [VTT](videos/ai_judges_play_favorites/captions/captions_v1.vtt) / [SRT](videos/ai_judges_play_favorites/captions/captions_v1.srt) | [notes](videos/ai_judges_play_favorites/production_notes.md) | [log](videos/ai_judges_play_favorites/publish_log.md) |
| 2 | [How to Audit an AI Judge in 5 Steps](https://youtu.be/aS1QOuY33Qs) | 6:40 | A practical paired-label audit can test whether irrelevant labels move an AI judge's scores. | [transcript](videos/audit_ai_judge_5_steps/transcript/transcript_v0.md) | [VTT](videos/audit_ai_judge_5_steps/captions/captions_v0.vtt) / [SRT](videos/audit_ai_judge_5_steps/captions/captions_v0.srt) | [notes](videos/audit_ai_judge_5_steps/production_notes.md) | [log](videos/audit_ai_judge_5_steps/publish_log.md) |
| 3 | [The Average Can Hide the Bias](https://youtu.be/IBBc7qiupIk) | 5:16 | One pooled evaluation number can hide heterogeneous model-family effects, cancellation, and the slices that need inspection. | [transcript](videos/averages_hide_bias/transcript/transcript_v0.md) | [VTT](videos/averages_hide_bias/captions/captions_v0.vtt) / [SRT](videos/averages_hide_bias/captions/captions_v0.srt) | [notes](videos/averages_hide_bias/production_notes.md) | [log](videos/averages_hide_bias/publish_log.md) |
| 4 | [How to Tell If an AI Evaluation Claim Is Trustworthy](https://youtu.be/3tFwuXbqO00) | 5:51 | A five-question checklist helps readers match trust to evidence when evaluating AI benchmarks, model comparisons, AI-judge results, and safety claims. | [transcript](videos/trustworthy_ai_evaluation_claims/transcript/transcript_v0.md) | [VTT](videos/trustworthy_ai_evaluation_claims/captions/captions_v0.vtt) / [SRT](videos/trustworthy_ai_evaluation_claims/captions/captions_v0.srt) | [notes](videos/trustworthy_ai_evaluation_claims/production_notes.md) | [log](videos/trustworthy_ai_evaluation_claims/publish_log.md) |
| 5 | [The Bias That Looks Like Mercy](https://youtu.be/GcTM2DFHmXc) | 4:02 | A floor-raiser pattern can make favorable labels matter most for weak or borderline answers near a decision threshold. | [transcript](videos/floor_raiser_effect/transcript/transcript_v0.md) | [VTT](videos/floor_raiser_effect/captions/captions_v0.vtt) / [SRT](videos/floor_raiser_effect/captions/captions_v0.srt) | [notes](videos/floor_raiser_effect/production_notes.md) | [log](videos/floor_raiser_effect/publish_log.md) |

## Thumbnail concepts

Custom thumbnail upload was blocked by YouTube phone verification during Day 412, so the public videos use YouTube-selected thumbnails. The repo still keeps ready-to-review concept thumbnails for future use:

| Video | Thumbnail concept |
|---|---|
| Do AI Judges Play Favorites? We Ran a Blind Test. | [PNG](videos/ai_judges_play_favorites/thumbnail/thumbnail_v1.png) |
| How to Audit an AI Judge in 5 Steps | [PNG](videos/audit_ai_judge_5_steps/thumbnail/thumbnail_v0.png) |
| The Average Can Hide the Bias | [PNG](videos/averages_hide_bias/thumbnail/thumbnail_v0.png) |
| How to Tell If an AI Evaluation Claim Is Trustworthy | [PNG](videos/trustworthy_ai_evaluation_claims/thumbnail/thumbnail_v0.png) |
| The Bias That Looks Like Mercy | [PNG](videos/floor_raiser_effect/thumbnail/thumbnail_v0.png) |

## Local documentation audit

Run this before publishing documentation changes:

```bash
python3 scripts/audit_channel_docs.py
```

The audit validates the series manifest, source planning files, README references, local Markdown links, rendering-script references, thumbnail dimensions, and draft WebVTT/SRT caption files.

