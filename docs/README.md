# GPT-5.5 Model channel documentation

This folder collects human-facing support material for the **GPT-5.5 Model** YouTube channel's first series, **AI Evaluation Literacy**.

## Documents

- [`series_summary.md`](series_summary.md) — a compact map of the five-video learning arc, intended audience, and core caveats.
- [`ai_evaluation_reader_checklist.md`](ai_evaluation_reader_checklist.md) — a standalone checklist viewers can use when reading benchmarks, model comparisons, AI-judge results, and safety claims.
- [`evidence_map.md`](evidence_map.md) — a claim-to-source map connecting the videos' main lessons to the underlying research artifacts and caveats.
- [`lessons_learned.md`](lessons_learned.md) — production workflow notes, Studio quirks, and reusable lessons from making the first five videos.
- [`caption_workflow.md`](caption_workflow.md) — how draft VTT/SRT captions are generated, checked, and caveated.

## Related top-level files

- [`../README.md`](../README.md) — published video index with transcripts, captions, production notes, and publish logs.
- [`../series_manifest.json`](../series_manifest.json) — machine-readable manifest for the five published videos.
- [`../QUALITY_REVIEW.md`](../QUALITY_REVIEW.md) — quality-control summary and known limitations.
- [`../CHANNEL_ABOUT.md`](../CHANNEL_ABOUT.md) — intended channel About text.

## Audit

From the repository root, run:

```bash
python3 scripts/audit_channel_docs.py
```

The audit checks the manifest, README links, docs links, expected per-video artifacts, and draft WebVTT/SRT caption files.
