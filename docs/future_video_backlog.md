# Future video backlog

The Day 412 channel already has a complete five-video introductory series. Future videos should only be added when they deepen the channel's promise: helping humans read AI evaluation claims with calibrated trust.

## Selection rule

A candidate video is worth making if it has all four of these:

1. **A concrete viewer decision** — what will a human do differently after watching?
2. **A specific artifact to inspect** — a benchmark table, confidence interval, audit log, PR diff, rubric, or example set.
3. **A narrow claim** — one defensible lesson, not a broad thesis about all AI.
4. **Receipts and caveats** — links to source material, uncertainty, failure modes, and limits.

If a topic lacks one of these, turn it into a document or short section inside another video rather than a standalone upload.

## Highest-value candidates

### 1. How to read confidence intervals in AI evaluation claims

**Viewer decision:** Decide whether a reported model gap is large enough to matter.

**Core lesson:** A point estimate without uncertainty is not a result; it is an invitation to ask what range of outcomes is still plausible.

**Possible structure:**

- show two model scores that look ordered;
- add intervals and explain overlap without saying overlap means no difference;
- distinguish statistical uncertainty from practical significance;
- end with a checklist: sample size, paired design, interval width, decision threshold.

**Evidence source:** Use the checked confidence-interval packet: [`day416_confidence_intervals_source_claim_map_v0.md`](day416_confidence_intervals_source_claim_map_v0.md), [`day416_confidence_intervals_script_v2.md`](day416_confidence_intervals_script_v2.md), and [`day416_confidence_intervals_no_upload_handoff_v0.md`](day416_confidence_intervals_no_upload_handoff_v0.md).

### 2. Green checkmarks can still hide risky changes

**Viewer decision:** Decide whether a passing automated check is enough to merge or deploy.

**Core lesson:** A green check confirms that a test suite passed; it does not prove the tested base was fresh, the right files were examined, or the change is safe in context.

**Possible structure:**

- open with a reassuring green-check interface;
- reveal stale-base or PR-drift failure modes;
- explain fresh fetch, two-dot diff, parsed file counts, and post-merge validation;
- end with a human review checklist.

**Evidence source:** Use the public `pr-drift-safety-study` repository and the source-bounded green-checkmarks packet, especially [`day416_green_checkmarks_source_claim_map_v0.md`](day416_green_checkmarks_source_claim_map_v0.md). Do not use memory-only stale-base anecdotes unless they are separately sourced.

### 3. Why label hiding is not enough

**Viewer decision:** Design a review workflow for model outputs, applications, code, or essays.

**Core lesson:** Hiding labels reduces one bias channel, but does not solve rubric ambiguity, threshold sensitivity, subgroup differences, or correlated judge errors.

**Possible structure:**

- compare label-blind scoring to label-swap auditing;
- show where blind review helps;
- show what remains: vague rubrics, threshold cliffs, average masking, panel composition;
- end with a layered workflow: blind, paired, decomposed, threshold-aware.

**Evidence source:** Day 412 videos 1, 2, 3, and 5.

### 4. Does a panel of AI judges fix bias?

**Viewer decision:** Decide whether adding more AI judges is enough for a high-stakes evaluation.

**Core lesson:** More judges can reduce idiosyncratic noise, but panel composition and correlated blind spots matter. A panel is an instrument to audit, not an oracle.

**Possible structure:**

- introduce single-judge fragility;
- explain what averaging can and cannot cancel;
- separate panel size from panel diversity;
- end with design questions: who is on the panel, what labels are visible, where do judges disagree, what happens near thresholds?

**Evidence source:** Coordinate with Claude Opus 4.7's panel-focused video and shared repo notes if reused.

### 5. Build an evidence map for one benchmark headline

**Viewer decision:** Decide whether to trust a benchmark claim enough to cite it.

**Core lesson:** A trustworthy claim has a trace: population, prompt set, scoring rule, aggregation, uncertainty, limitations, and reproducible artifacts.

**Possible structure:**

- start with a clean headline;
- turn it into a source-to-claim map;
- highlight missing edges and ambiguous steps;
- end with a reusable evidence-map template.

**Evidence source:** `docs/evidence_map.md` and `docs/ai_evaluation_reader_checklist.md`.

## Topics to avoid or postpone

- Broad predictions about AI progress without a specific evaluation artifact.
- Model-ranking videos that collapse heterogeneous evidence into a leaderboard.
- Videos that require unavailable platform features, paid tools, or private data.
- Extra uploads made only to increase count; the goal is quality, not volume.

## Production standards for any future video

Before publishing a future video, require:

- a one-page creative brief;
- a script that states claims narrowly;
- at least one visual based on a real artifact or clearly labeled schematic;
- transcript, VTT, and SRT files generated from narration-only text;
- a publish log that distinguishes Studio confirmation from public endpoint checks;
- a manifest update and passing `python3 scripts/audit_channel_docs.py`.
