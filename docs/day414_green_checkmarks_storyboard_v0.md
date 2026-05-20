# Day 414 storyboard v0 — A Green Check Is a Receipt, Not a Verdict

Status: visual storyboard only. Not a render plan, not proof assets, and not upload approval.

Script: [`day414_green_checkmarks_script_v1.md`](day414_green_checkmarks_script_v1.md)

## Visual principles

- Use large schematic cards, not dense terminal screenshots.
- Keep every frame readable at phone size.
- Show at most one code-like token per frame: `main`, `abc123`, `diff`, or `tests passed`.
- Use the green check as a useful signal, not a villain.
- Repeat the three-part checklist visually: **Fresh base / Right diff / Uncovered risk**.
- Avoid showing agent names, PR authors, or blame-like details. The examples should teach the habit, not make an internal postmortem.

## Palette

- Background: deep navy `#10131a` or `#121720`
- Primary text: warm white `#f4f1ea`
- Secondary text: muted gray-blue `#b9c0cf`
- Check accent: green `#86efac`
- Fresh base accent: blue `#7dd3fc`
- Right diff accent: amber `#fbbf24`
- Uncovered risk accent: pink `#fbcfe8`
- Warning/caveat outline: muted orange `#f59e0b`

## Scene plan

### Scene 01 — The comforting green check

Narration span:

> A green checkmark is one of the most comforting shapes in software... It is not a verdict.

Visual:

- Large green check centered.
- Text above: `All checks passed.`
- Text below initially: `Ready to merge?`
- Then a receipt card slides in over the question:

```text
Receipt, not verdict
check: passed
version: abc123
conditions: specific
```

Phone check:

- No more than four short text lines visible at once.
- The phrase **Receipt, not verdict** should be screenshot-readable.

### Scene 02 — The three questions

Narration span:

> Here are three questions that keep the signal in its lane: Fresh base. Right diff. Uncovered risk.

Visual:

Three large cards:

```text
Fresh base
current target?
```

```text
Right diff
actual change?
```

```text
Uncovered risk
what remains?
```

Motion:

- Cards appear one at a time, then settle into the footer order used for the rest of the video.

### Scene 03 — Fresh base

Narration span:

> Did the check run against the target you are about to merge or deploy into?... It is old evidence.

Visual:

A simple branch timeline:

```text
main at check time     main now
      ● ----------------- ●
       \                 
        ● PR checked
```

Then a label appears:

```text
Green on old base = old evidence
```

Source number moment:

- Show a small evidence tag, not a chart:

```text
Example trace:
144 / 610 PR heads
not descendants of recorded base
```

Caveat tag:

```text
triage signal, not failure label
```

Phone check:

- If the 144/610 tag feels dense, split into two beats.

### Scene 04 — Right diff

Narration span:

> Did the check inspect the exact change that will land?... Ask what diff the check was attached to.

Visual:

Two side-by-side panels:

Left:

```text
preview I remember
+ add at end
```

Right:

```text
current diff
+ inserted before tail
```

A highlighted arrow shows the difference between "append" and "insert before already-merged work."

Caveat/source tag:

```text
case appendix example
```

Avoid:

- Do not show PR number in the main frame unless later metadata needs it.
- Do not show a real code diff. Use schematic rows.

### Scene 05 — Uncovered risk

Narration span:

> What important failure could still happen even if the check result is correct?... What would still worry me if the robot is right?

Visual:

A ledger with three rows:

```text
Checked              Still ask
build passed          recent work removed?
tests passed          source shape preserved?
mergeable             user impact changed?
```

Motion:

- The left column gets green ticks.
- The right column gets question marks, not red Xs.

Phone check:

- If too dense, make this two frames: first "checked", then "still ask".

### Scene 06 — Signals are not verdicts

Narration span:

> A stale branch is not automatically unsafe... Each of those is a signal, not a verdict.

Visual:

Three stacked signal chips:

```text
stale base ≠ unsafe by itself
large deletion ≠ bad by itself
green check ≠ enough by itself
```

Bottom line:

```text
Signals point. Review decides.
```

Purpose:

- This scene protects the source caveat and keeps the video from becoming fear-based.

### Scene 07 — Checklist

Narration span:

> So before you treat a green check as approval, ask...

Visual:

Full-screen checklist:

```text
Fresh base
Did it run against today's target?

Right diff
Did it inspect the change that will land?

Uncovered risk
What important failure remains possible?
```

Motion:

- Each item highlights as narrated.
- Keep the wording shorter on screen than in narration.

### Scene 08 — Optional AI-assistant prompt

Narration span:

> If you are using an AI assistant during review, you can ask it the same thing...

Visual:

Prompt card with shortened text:

```text
Before I treat this check as approval:
1. What version and diff did it inspect?
2. What did it not inspect?
3. What decision remains mine?
```

Footer:

```text
Use the assistant to read the label, not to rubber-stamp the merge.
```

Potential cut:

- If runtime feels too long, this scene can become a description-only prompt rather than a narration section.

### Scene 09 — Ending

Narration span:

> Keep the green check... Do not let it replace the question.

Visual:

Large green check returns, now with labels around it:

```text
Useful signal
Limited scope
Human decision
```

Final line on screen:

```text
Let it speed up the review.
Do not let it replace the question.
```

## Rough duration allocation

- Scene 01: 35s
- Scene 02: 20s
- Scene 03: 50s
- Scene 04: 55s
- Scene 05: 55s
- Scene 06: 35s
- Scene 07: 45s
- Scene 08: 35s
- Scene 09: 25s

Total target: ~5 minutes.

## Open visual questions

1. Should the evidence tag show **144 / 610** or only say "many branches were stale enough to flag"? Prefer the number for credibility, but it must not feel like a fear statistic.
2. Should the PR case appendix be cited on-screen, in the description, or both? Prefer description plus a small "case appendix example" label on-screen.
3. Does "Uncovered risk" read clearly to non-developers? If not, test alternate label: **What remains?**
4. Should the AI prompt scene stay in the main video? It is useful but may feel like a second ending.

## Gate before proof assets

Before generating visuals:

- [ ] Confirm v1 script is the current active draft.
- [ ] Decide whether Scene 08 stays in narration.
- [ ] Pick final on-screen triplet wording.
- [ ] Verify no real PR author names appear in visuals.
- [ ] Keep the source caveat in metadata if this proceeds.
