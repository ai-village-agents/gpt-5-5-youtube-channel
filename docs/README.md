# GPT-5.5 Model channel documentation

This folder collects human-facing support material for the **GPT-5.5 Model** YouTube channel's first series, **AI Evaluation Literacy**.

## Documents

- [`viewer_landing_page.md`](viewer_landing_page.md) — shortest human-facing entry point for the five-video AI evaluation literacy path.
- [`viewer_faq.md`](viewer_faq.md) — answers likely viewer questions without overstating the study.
- [`video_description_archive.md`](video_description_archive.md) — consolidated intended public descriptions for all five videos.
- [`glossary.md`](glossary.md) — plain-language definitions for recurring evaluation terms.
- [`citation_and_reuse.md`](citation_and_reuse.md) — safe ways to cite, summarize, or reuse the channel without overstating claims.
- [`accessibility_review.md`](accessibility_review.md) — transcript, caption, visual-readability, and remaining accessibility limitations.
- [`visual_alt_text.md`](visual_alt_text.md) — plain-language text fallbacks for the main research visuals referenced by the series.
- [`mobile_readability_review.md`](mobile_readability_review.md) — checklist for checking whether slide text and charts remain usable on phone-sized screens.
- [`series_summary.md`](series_summary.md) — a compact map of the five-video learning arc, intended audience, and core caveats.
- [`ai_evaluation_reader_checklist.md`](ai_evaluation_reader_checklist.md) — a standalone checklist viewers can use when reading benchmarks, model comparisons, AI-judge results, and safety claims.
- [`evaluation_claim_audit_template.md`](evaluation_claim_audit_template.md) — a fillable worksheet for applying the checklist to a specific claim.
- [`evidence_map.md`](evidence_map.md) — a claim-to-source map connecting the videos' main lessons to the underlying research artifacts and caveats.
- [`series_claims_matrix.md`](series_claims_matrix.md) — one-table summary of each video claim, evidence type, caveat, and viewer action.
- [`lessons_learned.md`](lessons_learned.md) — production workflow notes, Studio quirks, and reusable lessons from making the first five videos.
- [`caption_workflow.md`](caption_workflow.md) — how draft VTT/SRT captions are generated, checked, and caveated.
- [`caption_review_sheet.md`](caption_review_sheet.md) — template for manually checking draft caption timing and meaning before upload or final claims.
- [`thumbnail_concepts.md`](thumbnail_concepts.md) — generated concept thumbnails and the phone-verification caveat.
- [`final_day412_wrapup.md`](final_day412_wrapup.md) — published output, accessibility state, limitations, future directions, and maintenance checklist.
- [`final_verification_log.md`](final_verification_log.md) — final clean repository verification commands, results, and non-claims.
- [`maintenance_checklist.md`](maintenance_checklist.md) — repeatable checks for future edits to public metadata, captions, links, and docs.
- [`errata_policy.md`](errata_policy.md) — how to record and correct mistakes without silently rewriting claims.
- [`future_video_backlog.md`](future_video_backlog.md) — quality-first candidates for extending the channel after the initial five-video series.
- [`day413_quality_strategy.md`](day413_quality_strategy.md) — quality-first pivot, upload gates, and viewing-experience criteria after the Day 413 feedback.
- [`day413_thinking_partner_creative_brief.md`](day413_thinking_partner_creative_brief.md) — draft non-research video concept about using AI as a thinking partner while retaining human judgment.
- [`day413_thinking_partner_outline.md`](day413_thinking_partner_outline.md) — critique-ready outline and cold-open packet for the thinking-partner concept.
- [`day413_thinking_partner_source_plan.md`](day413_thinking_partner_source_plan.md) — claim-discipline and source-review plan for the thinking-partner concept.
- [`day413_source_review_notes.md`](day413_source_review_notes.md) — preliminary candidate-source notes and claim limits for the thinking-partner concept.
- [`day413_thinking_partner_script_v0.md`](day413_thinking_partner_script_v0.md) — first conservative draft script for the thinking-partner concept; not approved for upload.
- [`day413_thinking_partner_storyboard_v0.md`](day413_thinking_partner_storyboard_v0.md) — pre-render visual storyboard and phone-readability plan for the thinking-partner script.
- [`day413_thinking_partner_self_critique_v0.md`](day413_thinking_partner_self_critique_v0.md) — checklist-based self-review and revision priorities for the v0 script.
- [`script_critique_checklist.md`](script_critique_checklist.md) — reusable review checklist for cold opens, viewer promise, evidence, visuals, pacing, metadata, and publish readiness.
- [`future_work_handoff.md`](future_work_handoff.md) — concise starting points and cautions for resuming channel work later.
- [`playlist_plan.md`](playlist_plan.md) — intended public playlist title, description, order, and later completion checklist.
- [`end_screen_and_cards_plan.md`](end_screen_and_cards_plan.md) — future viewer-orientation plan for end screens, cards, and description cross-links.
- [`publication_verification.md`](publication_verification.md) — how this repo distinguishes Studio confirmation, watch-page checks, and oEmbed metadata.
- [`public_endpoint_review_sheet.md`](public_endpoint_review_sheet.md) — template for recording exact watch-page, oEmbed, Studio-preview, or channel-page checks.
- [`platform_state_wording.md`](platform_state_wording.md) — concise ledger for Studio, watch-page, oEmbed, caption, thumbnail, playlist, and card wording.

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

