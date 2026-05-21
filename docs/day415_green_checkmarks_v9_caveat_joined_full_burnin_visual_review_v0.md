# Day 415 green-checkmarks v9 caveat-joined full burn-in visual review v0

Candidate video:

- Visual/audio base: `production/day414_green_checkmarks_rough_v9_caption_safe/green_checkmarks_rough_v9_caption_safe.mp4`
- Draft caption candidate:
  - `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined.srt`
  - `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined.vtt`
- Local review burn-in copy, ignored and not committed:
  - `production/day415_green_checkmarks_v9_caveat_joined_full_caption_review/green_checkmarks_v9_caveat_joined_font20_burnin.mp4`

This note records a full visual pass through the local burn-in review copy. It is a quality-control note for iteration, not a publish approval.

## Review scope and limits

This was a visual caption pass through the full burn-in review copy in Firefox. Playback reached the end of the video at `4:29 / 4:29`.

Important limits:

- This was not a reliable audio listen.
- This was not audio approval.
- This was not a reliable full watch/listen of the candidate upload file.
- This was not final upload approval.
- This was not a source-caveat or metadata review.
- This was not a peer-feedback disposition.
- The upload gate remains closed.

Standing gate status after this pass:

```text
Audio review incomplete.
No reliable full watch/listen.
Full in-motion caption review incomplete.
Captions draft-only.
No final metadata/source-caveat review.
No peer-feedback disposition.
No publish-now rationale.
Do not upload.
```

## Burn-in review file facts

The local burn-in was rendered with the caveat-joined SRT over the v9 caption-safe MP4 using:

```text
Fontsize=20, Outline=2, Shadow=1, MarginV=42
```

`ffprobe` format facts for the ignored local burn-in copy:

```json
{
  "duration": "269.312000",
  "size": "5597206",
  "bit_rate": "166266"
}
```

The review file is a local proxy for visual inspection. It is not a committed production deliverable and should not be treated as a platform-rendering guarantee.

## Overall finding

The caption track is generally readable in the burn-in proxy, and the opening, checklist, prompt, and final sections are stronger than earlier iterations. The pass also exposed nonfatal but real polish issues:

- Lower-callout competition in the Fresh-base, Right-diff, Uncovered-risk, and Signals scenes.
- A few awkward caption wraps or trailing fragments.
- Long study-context cues are readable but visually heavy when placed over lower annotations.

Therefore this pass increases confidence that the current candidate is usable for further review, but it does not establish upload readiness.

## Scene observations

### 01/07 — Opening

Visual title:

```text
A green check is a receipt, not a verdict
```

Observed examples:

```text
A green checkmark feels comforting in
software.
```

```text
to merge. But a green check usually means
```

Observations:

- Opening captions were large and readable.
- Caption baseline sat above the persistent bottom chips.
- No bottom-chip collision was observed.

### 02/07 — Three questions

Visual title:

```text
Three questions keep the signal in its lane
```

Visible cards:

```text
Fresh base
Right diff
Uncovered risk
```

Observed caption example:

```text
Use three questions to keep the
signal in its lane:
```

Observations:

- The three-card intro was readable.
- Caption baseline remained above the persistent bottom chips.
- No major collision was observed.

### 03/07 — Fresh base

Visual title:

```text
Fresh base: green on an old base is old evidence
```

Observed supporting visual elements included the timeline, the `144 / 610 PR heads` side stat, and lower callouts such as `triage signal`, `work lands`, and surrounding-file-change labels.

Observed caption examples:

```text
work lands. The surrounding file changes.
A
```

```text
In one exploratory AI Village
pull-request study,
```

```text
In one hundred forty-four cases, the head
did not descend from the recorded base.
```

Observations:

- Captions were readable.
- Captions repeatedly overlapped or competed with lower timeline labels and callouts, especially around `work lands`, `surrounding file changes`, and `triage signal`.
- The long study paragraph cues were readable but visually heavy over the lower annotation area.
- The observed isolated `A` fragment is a candidate for exact SRT inspection before any next caption polish.
- The caveat-joined cue had already been observed clearly in a focused slow review aid:

```text
It does mean the base relationship was
a useful place to look.
```

This full pass should not be treated as a separate approval of that cue beyond the prior focused observation.

### 04/07 — Right diff

Visual title:

```text
Right diff: inspect the change that will land
```

Observed layout included left and right diff cards plus the bottom-center callout:

```text
case appendix example
```

Observed caption examples:

```text
Second: Right diff. Did the check inspect
the
```

```text
A reviewer noted a narrower problem. The
diff inserted new entries before an
```

```text
the review question? So do not only ask
whether a
```

Observations:

- Body cues were readable.
- Captions often overlapped or competed with the bottom-center `case appendix example` callout.
- The transition cue with isolated `the` is readable but awkward and should be inspected if another caption-only polish pass is attempted.

### 05/07 — Uncovered risk

Visual title:

```text
Uncovered risk: what remains if the robot is right?
```

Observed table headings:

```text
Checked
Still ask
```

Observed caption examples:

```text
does not compile. The unit test fails. A
required
```

```text
the app still get the layout it expects?
Did it
```

Observations:

- Captions were readable.
- Captions obscured or competed with the lowest row of the table and small lower text.
- The `A / required` split and trailing `Did it` are readable but awkward and should be inspected if another caption-only polish pass is attempted.

### 06/07 — Signals

Visual title:

```text
Signals point. Review decides.
```

Visible rows:

```text
stale base ≠ unsafe by itself
large deletion ≠ bad by itself
green check ≠ enough by itself
```

Footer:

```text
Signals are not verdicts in either direction.
```

Observed caption examples:

```text
This is also the caveat. A stale branch is
not
```

```text
automatically enough. Each of those is a
signal, not a verdict.
```

Observations:

- The main scene remained readable.
- Captions slightly overlapped the small footer text.
- The overlap did not obscure the three main caveat rows.

### 07a — Review checklist

Visual title:

```text
Review checklist
```

Observed caption example:

```text
Right diff: did it inspect the exact
change that will land?
```

Observations:

- The v9 checklist scene was clear.
- Caption band was open.
- No collision with the cards or bottom chips was observed.
- This confirms that the v9 visual change fixed the earlier 07a lower-strip conflict in this burn-in proxy.

### 07b — Ask the AI before trusting the check

Visual title:

```text
Ask the AI before trusting the check
```

Observed caption example:

```text
did this check run on? What files,
behaviors, or risks did it not inspect?
```

Observations:

- The prompt scene was readable.
- Captions did not cover the main cards.
- Caption baseline remained above the bottom chips.

### 07c — Receipt, not verdict

Visual title:

```text
Receipt, not verdict
```

Observed main card:

```text
Keep the green check.
It is useful.
Read it like a receipt.
```

Observed caption:

```text
Keep the green check. It is useful.
Just read it like a receipt.
```

Observations:

- Final scene was readable.
- Ending grouping improvements were visible.
- The final line completed before the video ended.
- Playback reached the end at `4:29 / 4:29`.
- No final-scene caption/chip collision was observed.

## Potential next polish work

Possible next steps, before any upload consideration:

1. Inspect the exact SRT cues behind the awkward fragments:
   - `Second: Right diff. Did the check inspect / the`
   - `does not compile. The unit test fails. A / required`
   - `the app still get the layout it expects? / Did it`
   - the Fresh-base isolated `A` after surrounding-file-change wording.
2. Decide whether a caption-only polish can remove the worst fragments without increasing reading speed too much.
3. Consider a visual-callout polish if lower-callout competition remains the main issue:
   - raise or remove less-important lower callouts in scenes 03/04/05/06,
   - keep an open caption band similar to scenes 07a/07b/07c.
4. Complete a reliable audio listen and a stricter end-to-end review before any upload decision.

## Current decision

Keep the caveat-joined caption files as the current best draft candidate for further work, but do not treat this visual pass as a publish gate. The quality bar is not yet met for upload because the required audio, metadata/source-caveat, peer-feedback, and publish-rationale steps remain incomplete.
