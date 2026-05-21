# Day 415 green-checkmarks v11 full burn-in visual review v0

Date: 2026-05-21  
Candidate: `green_checkmarks_rough_v11_caption_band_clearance_wrap_polished_burnin.mp4`  
Source path: `production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_polished_burnin.mp4`

## Scope

This note records a full Firefox pass of the v11 caption-band-clearance burn-in file. Playback reached the end of the file at `4:29 / 4:29`.

This was a **visual/caption pass only**. It is useful for judging scene composition, caption-band clearance, and obvious burn-in readability issues, but it is not enough to approve the candidate for upload.

## Gate status

The upload gate remains closed.

Not done:

- Audio review incomplete.
- No reliable full watch/listen.
- This pass is not audio approval.
- This pass is not final in-motion caption approval.
- Captions remain draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition.
- No publish-now rationale.
- Do not upload.

## Overall finding

V11 is the best visual direction so far for this candidate. Compared with the earlier v9/v10 burn-ins, the lower caption band is materially cleaner in scenes 03-06. Scene 05's table is higher and shorter, and scene 06's signal rows are more compact, leaving more breathing room for captions.

The pass did not reveal a major visual collision that would force reverting v11. Remaining issues are mostly caption-polish and final-review issues rather than obvious visual-band collisions. The most visible caption-polish concern remains the phrase boundary around `A required`, and `A file list is not` is readable but not elegant.

## Scene observations

### Scene 01 — opening receipt frame

Visible title:

```text
01/07 A green check is a receipt, not a verdict
visual proof v0
```

The scene opened correctly. Captions were readable, including:

```text
A green checkmark feels comforting in
software.
```

Later in the scene, the caption:

```text
to read that as a bigger sentence: This is
safe
```

was also readable. No collision was observed.

### Scene 02 — three questions

Visible title:

```text
02/07 Three questions keep the signal in its lane
visual proof v0
```

The three cards were visible:

```text
Fresh base
current target?

Right diff
actual change?

Uncovered risk
what remains?
```

The caption:

```text
Use three questions to keep the
signal in its lane:
```

was readable. No collision was observed.

### Scene 03 — Fresh base

Visible title:

```text
03/07 Fresh base: green on an old base is old evidence
visual proof v11
```

The timeline labels were visible:

```text
main at check time
main now
PR checked
```

The compact badge remained out of the lower caption band:

```text
triage signal
not failure label
```

The stat card remained visible:

```text
144 / 610 PR heads
not descendants
of recorded base
```

Captions were readable with a cleaner lower band than the older v9 lower-label design. Observed captions included:

```text
while a pull request waits. The check may
have
```

The wrap-polished fix read well:

```text
A validator appears. A slot that was empty
becomes occupied.
```

The dense study cue was readable:

```text
In one hundred forty-four cases, the head
did not descend from the recorded base.
```

The badge and stat card remain visually present mid-scene, but no lower caption-band conflict was observed during this pass.

### Scene 04 — Right diff

Visible title:

```text
04/07 Right diff: inspect the change that will land
visual proof v11
```

The top badge was visible and clear of the captions:

```text
case appendix example
```

The two-panel comparison remained legible:

```text
preview I remember
+ add at end

current diff
+ inserted before tail
already-merged tail
```

The lower caption band was much cleaner than the old lower-badge design. Observed captions included:

```text
exact change that will land?
A file list is not
```

This was readable, though the phrase boundary is not especially elegant.

Other readable captions included:

```text
A reviewer noted a narrower problem. The
diff inserted new entries before an
```

and:

```text
Parsing was not the whole issue. The real
```

Body captions were readable; moving the badge to the top avoided the earlier bottom-band competition.

### Scene 05 — Uncovered risk

Visible title:

```text
05/07 Uncovered risk: what remains if the robot is right?
visual proof v11
```

The top badge was visible:

```text
What would still worry me if the robot is right?
```

The higher, shorter table was visible:

```text
Checked
build passed
tests passed
mergeable

Still ask
recent work removed?
source shape preserved?
user impact changed?
```

Observed captions included:

```text
failures are easy for automation to see.
The file
```

and:

```text
about meaning. Did this remove recent
work?
```

The scene no longer presses as close to the captions as v10/v9. The related re-encoded focused review also confirmed improved clearance on later scene-05 captions:

```text
Did the app still get the layout
it expects? Did it
```

and:

```text
or a hidden invariant? The most useful
question
```

The main remaining concern here is the caption phrase boundary:

```text
A required
```

That is a caption-polish issue, not a newly observed visual collision.

### Scene 06 — Signals

Visible title:

```text
06/07 Signals point. Review decides.
visual proof v11
```

The top badge was visible:

```text
Signals are not verdicts in either direction.
```

The compact rows were visible:

```text
stale base     ≠ unsafe by itself
large deletion ≠ bad by itself
green check    ≠ enough by itself
```

The full pass saw the opening caption:

```text
This is also the caveat. A stale branch is
not
```

The full pass advanced quickly into scene 07a before a still observation of the later target cue, but the re-encoded focused review confirmed the target caption with improved clearance:

```text
automatically enough. Each of those is a
signal, not a verdict.
```

The compact rows leave a clearer caption area than v10. This remains a visual aid, not a final caption or audio approval.

### Scene 07a — Review checklist

Visible title:

```text
07a/09 Review checklist
rough v9 visual
```

The three checklist cards were visible:

```text
Fresh base
Right diff
Uncovered risk
```

The caption:

```text
Before treating a green check as approval,
ask:
```

was readable. No collision was observed.

### Scene 07b — Ask the AI

Visible title:

```text
07b/09 Ask the AI before trusting the check
rough v7 visual
```

The three cards were visible:

```text
1 Version / base / diff
2 Uninspected risks
3 Human decision left
```

Observed captions included:

```text
If you are using an AI assistant during
review,
```

and:

```text
What human decision remains
if the check is correct?
```

No collision was observed.

### Scene 07c — Receipt, not verdict

Visible title:

```text
07c/09 Receipt, not verdict
rough v8 visual
```

The final card was clear:

```text
Keep the green check.
It is useful.
Read it like a receipt.
```

The caption:

```text
What version did it check?
What diff did it inspect?
```

was readable. Playback ended cleanly at `4:29 / 4:29`.

## Decision

Preserve v11 as the current best visual successor for green-checkmarks. It materially improves the caption-band clearance problem that remained after the wrap-polished caption pass and the v10 visual experiment.

Do not upload yet. Useful next steps are either:

1. a small caption-only polish pass for awkward phrase boundaries such as `A required` and possibly `A file list is not`, or
2. a stricter reliable full watch/listen protocol that can actually evaluate audio and pacing, followed by full caption, metadata/source-caveat, peer-feedback, and publish-now reviews.
