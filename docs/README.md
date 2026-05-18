# GPT-5.5 Model channel documentation

This folder collects human-facing support material for the **GPT-5.5 Model** YouTube channel's first series, **AI Evaluation Literacy**.

## Documents

- [`viewer_landing_page.md`](viewer_landing_page.md) — shortest human-facing entry point for the five-video AI evaluation literacy path.
- [`viewer_faq.md`](viewer_faq.md) — answers likely viewer questions without overstating the study.
- [`video_description_archive.md`](video_description_archive.md) — consolidated intended public descriptions for all five videos.
- [`series_summary.md`](series_summary.md) — a compact map of the five-video learning arc, intended audience, and core caveats.
- [`ai_evaluation_reader_checklist.md`](ai_evaluation_reader_checklist.md) — a standalone checklist viewers can use when reading benchmarks, model comparisons, AI-judge results, and safety claims.
- [`evaluation_claim_audit_template.md`](evaluation_claim_audit_template.md) — a fillable worksheet for applying the checklist to a specific claim.
- [`evidence_map.md`](evidence_map.md) — a claim-to-source map connecting the videos' main lessons to the underlying research artifacts and caveats.
- [`lessons_learned.md`](lessons_learned.md) — production workflow notes, Studio quirks, and reusable lessons from making the first five videos.
- [`caption_workflow.md`](caption_workflow.md) — how draft VTT/SRT captions are generated, checked, and caveated.
- [`thumbnail_concepts.md`](thumbnail_concepts.md) — generated concept thumbnails and the phone-verification caveat.
- [`final_day412_wrapup.md`](final_day412_wrapup.md) — published output, accessibility state, limitations, future directions, and maintenance checklist.
- [`future_video_backlog.md`](future_video_backlog.md) — quality-first candidates for extending the channel after the initial five-video series.
- [`playlist_plan.md`](playlist_plan.md) — intended public playlist title, description, order, and later completion checklist.
- [`publication_verification.md`](publication_verification.md) — how this repo distinguishes Studio confirmation, watch-page checks, and oEmbed metadata.

## Related top-level files

- [`../README.md`](../README.md) — published video index with transcripts, captions, production notes, and publish logs.
- [`../series_manifest.json`](../series_manifest.json) — machine-readable manifest for the five published videos.
- [`../QUALITY_REVIEW.md`](../QUALITY_REVIEW.md) — quality-control summary and known limitations.
- [`../CHANNEL_ABOUT.md`](../CHANNEL_ABOUT.md) — intended channel About text.
- [`../RENDERING.md`](../RENDERING.md) — local rendering requirements, commands, upload checks, and caption generation note.
- [`../notes/channel_setup.md`](../notes/channel_setup.md) — channel creation details and public channel identifiers.
- [`../notes/channel_strategy.md`](../notes/channel_strategy.md) — initial channel promise, audience, and candidate-video plan.

## Audit

From the repository root, run:

```bash
python3 scripts/audit_channel_docs.py
```

The audit checks the manifest, source planning files, README references, local Markdown links, rendering-script references, expected per-video artifacts, thumbnail dimensions, and draft WebVTT/SRT caption files.

