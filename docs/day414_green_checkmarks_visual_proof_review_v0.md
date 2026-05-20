# Day 414 visual proof review v0 — Green checkmarks candidate

Status: static visual proof review only. Not a render plan, not a full visual QA pass, and not upload approval.

Script reference: [`day414_green_checkmarks_script_v1.md`](day414_green_checkmarks_script_v1.md)
Storyboard reference: [`day414_green_checkmarks_storyboard_v0.md`](day414_green_checkmarks_storyboard_v0.md)
Generator:

```text
scripts/make_day414_green_checkmarks_visual_proofs.py
```

Generated contact sheet:

```text
assets/day414_green_checkmarks_mockups/green_checkmarks_contact_sheet_v0.png
```

Generated proof frames:

```text
assets/day414_green_checkmarks_mockups/visual_proofs/green_01_receipt_not_verdict.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_02_three_questions.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_03_fresh_base.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_04_right_diff.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_05_uncovered_risk.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_06_signals_not_verdicts.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_07_final_checklist.png
```

Each full-size frame also has a `_360p.png` downsized proof for phone-readability inspection.

## What the proof frames test

These frames test the visual language only:

- green check as useful signal rather than villain;
- dark high-contrast card style aligned with the thinking-partner candidate;
- the triplet **Fresh base / Right diff / Uncovered risk**;
- schematic diff/base/risk visuals instead of terminal dumps;
- source caveat language embedded in visuals where needed, especially "triage signal, not failure label" and "signals are not verdicts."

They do **not** test:

- narration timing;
- audio quality;
- motion pacing;
- caption readability in motion;
- final metadata/source caveats;
- upload readiness.

## Frame-by-frame notes

### 01 — Receipt, not verdict

Strengths:

- The main metaphor is immediately clear.
- The green check remains positive; the frame does not look anti-automation.
- The receipt fields are short and phone-readable.

Watch in a future render:

- Avoid over-animating the receipt card; the concept should land calmly.

### 02 — Three questions

Strengths:

- The triplet is clear and visually balanced.
- "Uncovered risk" reads more concrete than "Human risk."

Open question:

- Non-developer viewers may still need narration to understand "Right diff." The card subtitle "actual change?" helps.

### 03 — Fresh base

Strengths:

- Branch timeline is simple enough for non-experts.
- The evidence tag includes **144 / 610 PR heads** without turning it into a fear statistic.
- The caveat "triage signal, not failure label" is visible.

Risk:

- This is the densest frame. In a final render, the evidence tag may need to appear after the branch diagram, not simultaneously.

### 04 — Right diff

Strengths:

- Schematic "preview I remember" vs "current diff" conveys the mismatch without showing real code or PR authors.
- "case appendix example" avoids pretending a fresh adjudication happened here.

Risk:

- The phrase "inserted before tail" is compact but may be odd. Narration should explain it as "before already-merged work."

### 05 — Uncovered risk

Strengths:

- The checked/still-ask ledger keeps the green checks useful while making limits visible.
- Question marks rather than red Xs avoid panic framing.

Risk:

- Three rows may be a lot on small screens. If animated, reveal one row at a time.

### 06 — Signals are not verdicts

Strengths:

- This frame protects the main source caveat.
- "Signals point. Review decides." is a strong candidate line.

Risk:

- The frame is more conceptual; it should be short in a final cut.

### 07 — Final checklist

Strengths:

- The checklist is immediately reusable.
- The final line, "Let it speed up the review. Do not let it replace the question," is visually strong.

Risk:

- The footer duplicates the checklist cards; a final render may drop the footer on this scene.

## 360p readability check

Static 360p downsamples were generated for all seven frames. Based on the design constraints in the generator:

- titles and card headers should remain readable at 360p;
- code-like text is limited to a few large tokens;
- no real terminal dumps are present;
- the densest frames are Scene 03 and Scene 05 and should receive priority in any manual screenshot review.

This is not a substitute for an in-player phone-size review if the candidate proceeds to render.

## Source and privacy/blame check

The frames do not show:

- individual PR authors;
- agent names;
- real code excerpts;
- unverified incident claims;
- claims that stale branches are unsafe by default;
- claims that green checks are meaningless.

They do show the PR-drift number **144 / 610**, which is safe only with the narration/source caveat that non-descendant heads are triage signals, not automatic safety labels.

## Next visual step if this candidate continues

Before rendering, produce a rough motion plan that decides:

- whether Scene 08 from the storyboard, the AI-assistant prompt, stays in the main video or moves to the description;
- whether Scene 03's evidence tag appears after the branch diagram;
- whether Scene 05's ledger reveals row-by-row;
- whether the final checklist drops the footer to reduce redundancy.

## Gate state

This candidate is still pre-production. No audio, captions, render, watch/listen pass, metadata review, or publish rationale exists.

Do not upload.
