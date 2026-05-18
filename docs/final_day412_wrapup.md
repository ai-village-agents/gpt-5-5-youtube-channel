# Final Day 412 channel wrap-up

Day 412 goal: **Run Your Own Youtube Channel!**

Channel: **GPT-5.5 Model** (`@GPT-5.5Model`)  
Series: **AI Evaluation Literacy**  
Published date: **2026-05-18 / AI Village Day 412**

## Published videos

1. [Do AI Judges Play Favorites? We Ran a Blind Test.](https://youtu.be/AHLi0xU0WXs) — why label-swap audits matter and why a single headline number is not enough.
2. [How to Audit an AI Judge in 5 Steps](https://youtu.be/aS1QOuY33Qs) — a practical workflow for testing whether irrelevant labels move scores.
3. [The Average Can Hide the Bias](https://youtu.be/IBBc7qiupIk) — why aggregate evaluation results need subgroup checks.
4. [How to Tell If an AI Evaluation Claim Is Trustworthy](https://youtu.be/3tFwuXbqO00) — a five-question checklist for benchmarks, model comparisons, and AI-judge claims.
5. [The Bias That Looks Like Mercy](https://youtu.be/GcTM2DFHmXc) — how a displayed label can matter most near decision thresholds.

## What the channel is trying to offer

The first five videos form a small curriculum for humans who read AI benchmark reports, compare models, or rely on AI judges. The central message is calibrated skepticism: evaluation can be useful, but only when claims keep their scope, show their receipts, and separate observational patterns from causal tests.

The videos intentionally avoid the strongest-sounding but least defensible version of the research result. They do **not** claim that all AI judges always favor themselves, that model behavior reveals motives, or that one pooled average captures the study. Instead, the series emphasizes heterogeneity, paired comparisons, uncertainty, threshold effects, and evidence trails.

## Quality and accessibility state

Completed artifacts include:

- public YouTube uploads for all five videos;
- transcripts for every video;
- narration-only WebVTT and SRT caption drafts for every video;
- production notes and publish logs for every video;
- a series manifest with URLs, runtimes, caption paths, and documentation paths;
- concept thumbnail PNGs at 1280×720 for future use if phone verification becomes available;
- an audit script that checks manifest consistency, source planning files, rendering-script references, local Markdown links, docs-index coverage, README references, captions, and thumbnail dimensions, plus a [`final_verification_log.md`](final_verification_log.md) record of the last clean checks;
- viewer-support docs for caveats, glossary terms, safe citation/reuse wording, archived descriptions, accessibility status, visual alt text, end-screen/card planning, and future maintenance.

Important caveat: the caption files are cleaned narration-only text, but their cue timing is generated proportionally from word counts rather than manually aligned to audio. They are suitable as draft accessibility artifacts and as a starting point for future upload/review, not as hand-verified subtitles.

## Known platform limitations

- Custom thumbnails could not be uploaded because YouTube required phone verification.
- The channel customization/About route repeatedly showed a permission error, so `CHANNEL_ABOUT.md` records the intended About text instead of a confirmed live About page.
- YouTube public URL and oEmbed availability can lag behind Studio publication confirmations; the repo distinguishes Studio confirmation from public endpoint checks.
- Production MP4s and local render intermediates are intentionally ignored in Git to keep the repository lightweight.

## Maintenance checklist

If this channel is revisited later:

1. Run `python3 scripts/audit_channel_docs.py` before publishing repo changes.
2. Regenerate captions with `python3 scripts/generate_narration_captions.py` after transcript edits.
3. Inspect beginning, middle, and end of every caption file for leaked production markers.
4. Upload or manually align captions in YouTube Studio if time allows.
5. Add custom thumbnails only if verification is available and the public video state can be checked afterward.
6. Preserve the research caveats from `docs/evidence_map.md` when writing new videos.
7. Use [`maintenance_checklist.md`](maintenance_checklist.md), [`accessibility_review.md`](accessibility_review.md), and [`publication_verification.md`](publication_verification.md) before making future public-state claims.

## Future video directions

The strongest next videos would extend the same evidence-literacy mission rather than chase volume:

- how to read confidence intervals in AI evaluation claims;
- why green checkmarks can still hide stale or risky changes;
- how to design a label-blind review workflow for model outputs;
- why a panel of AI judges can reduce some bias but not make evaluation automatic;
- how to build a public evidence map for a benchmark claim.
