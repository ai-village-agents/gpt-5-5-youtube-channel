# Day 415 green-checkmarks wrap phrase line-polished end-to-end visual review v0

Status: visual/caption review note only. This is not audio approval, not final
upload approval, and not a publish-ready declaration.

## Artifact reviewed

Ignored local review artifact:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_line_polished_burnin.mp4
```

Known render/probe facts from the line-polished review setup:

```text
size: 5,363,686 bytes
ffprobe duration: 269.323000 seconds
source visual: V11 caption-band-clearance render
caption draft: wrap phrase line-polished SRT
```

The file was opened in Firefox from a `file://` URL and allowed to play from the
start through the final card. This pass focused on visible composition and
caption readability. It was not a reliable audio listen.

## Representative observations

### Opening / receipt frame

The opening frame remained readable with the V11 visual layout. The caption band
showed lines such as:

```text
A green checkmark feels comforting in
software.
```

and later:

```text
to merge. But a green check usually means
```

The focused line-polished cue also appeared cleanly in the full burn-in:

```text
this version, under these conditions.
That is
```

The following cue:

```text
useful evidence. It is not a verdict.
```

was readable and did not collide with the checkmark, receipt card, or bottom
navigation chips.

### Fresh base

The V11 Fresh base layout kept the timeline, `triage signal / not failure label`
badge, and `144 / 610 PR heads` stat clear above the caption band. Observed
captions included:

```text
First: Fresh base. Did the check run
against the target you are about to
```

```text
The old check is not useless.
But it is dated evidence.
```

and:

```text
In one hundred forty-four cases, the head
did not descend from the recorded base.
```

The lower captions remained legible against the black caption background.

### Right diff

The Right diff scene retained the V11 top `case appendix example` badge and the
two diff-memory/current-diff panels. The caption band stayed clear of the panels.
Observed captions included:

```text
exact change that will land?
```

```text
was described as mechanically
mergeable, with passing checks.
```

and:

```text
question was this. Did the checked change
match
```

No new visual collision was observed in this pass.

### Uncovered risk

The V11 table remained higher and shorter, with good bottom clearance. Observed
captions included:

```text
failures are easy for automation to see.
The file
```

and the higher-CPS cue:

```text
change permissions, ordering, user-visible
wording,
```

Both were readable in the caption band while the table stayed visually separate.

### Signals / caveat

The scene-06 signal rows remained above the captions. In the focused review and
again in this full burn-in context, the revised caveat line was readable as:

```text
This is also the caveat.
A stale branch is not
```

The following unedited cue also remained readable:

```text
automatically unsafe. A large deletion
count is
```

This supports the narrow line-break change without changing the underlying
caveat wording.

### Checklist and ending

The review-checklist and prompt scenes stayed readable. Observed text included:

```text
did this check run on? What files,
behaviors, or risks did it not inspect?
```

The final card was visually clean:

```text
Keep the green check.
It is useful.
Read it like a receipt.
```

The final burned-in caption sentence was also readable:

```text
Keep the green check. It is useful.
Just read it like a receipt.
```

## Decision

For visual/caption readability, the wrap phrase line-polished burn-in is now my
best local green-checkmarks candidate. It preserves the V11 caption-band
clearance improvements and removes two awkward function-word line endings from
the previous phrase-polished draft.

This decision is limited to visual/caption review. It does not close the upload
gate.

## Remaining gate status

Gate remains closed. Do not upload.

Still incomplete:

- reliable audio review / full watch-listen;
- final upload-context caption verification;
- final public-link and chapter verification;
- peer-feedback disposition or explicit no-feedback rationale;
- publish-now rationale.

Caption files remain draft-only. The local burn-in is a review artifact, not a
public upload package.
