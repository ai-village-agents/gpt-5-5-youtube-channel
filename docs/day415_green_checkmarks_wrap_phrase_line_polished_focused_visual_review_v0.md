# Day 415 green-checkmarks wrap phrase line-polished focused visual review v0

Status: narrow focused visual review only. This is not a final in-motion
caption pass, not an audio approval, and not upload readiness.

## Reviewed artifacts

These files are ignored production artifacts and are not intended to be
committed:

- Full burn-in used as the source for clips:
  `production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_line_polished_burnin.mp4`
  - size: 5,363,686 bytes
  - ffprobe duration observed during render check: 269.323000 seconds
- Focus clip 1:
  `production/day415_green_checkmarks_rough_v11_caption_band_clearance/phrase_line_polished_focus/01_that_is_line_polished_from_full.mp4`
  - extraction: `-ss 19.0 -t 10.5` from the full line-polished burn-in
  - size: 218,849 bytes
  - ffprobe duration: 10.500000 seconds
- Focus clip 2:
  `production/day415_green_checkmarks_rough_v11_caption_band_clearance/phrase_line_polished_focus/02_stale_branch_not_line_polished_from_full.mp4`
  - extraction: `-ss 186.5 -t 9.5` from the full line-polished burn-in
  - size: 199,829 bytes
  - ffprobe duration: 9.500000 seconds

Method note: the focused clips were cut from the full caption-burned timeline,
not made by burning full-timeline captions onto already-trimmed clips. This
avoids the earlier invalid-review failure mode where the captions were offset.

## Caption edits under review

The line-polished draft changes only line breaks, not wording or timings.

Cue 7 was changed from:

```text
this version, under these conditions. That
is
```

to:

```text
this version, under these conditions.
That is
```

Cue 50 was changed from:

```text
This is also the caveat. A stale branch is
not
```

to:

```text
This is also the caveat.
A stale branch is not
```

## Focused observations

### Clip 1: `That is`

In Firefox, the focused clip showed the revised caption as:

```text
this version, under these conditions.
That is
```

The line break reads more naturally than the earlier function-word ending.
The caption sits in the lower caption band without colliding with the green
check panel, receipt card, bottom navigation chips, or other scene-01 visual
material. The following cue:

```text
useful evidence. It is not a verdict.
```

also remained readable and clear.

### Clip 2: `A stale branch is not`

In Firefox, the focused clip showed the revised caption as:

```text
This is also the caveat.
A stale branch is not
```

This removes the previous `is / not` line break and keeps the caveat readable.
The scene-06 signal rows (`stale base`, `large deletion`, `green check`) remain
well above the caption band, with no apparent collision. The following unedited
cue remained readable:

```text
automatically unsafe. A large deletion
count is
```

This confirms that the narrow line-break edit did not introduce an obvious
visual problem at the transition into the signal-caveat section.

## Decision

The wrap phrase line-polished caption draft is a plausible successor to the
wrap phrase-polished draft for these two focused points. It removes two
function-word line endings without changing timing, wording, cue count, or the
machine-QA risk profile documented in the caption experiment note.

## Remaining gate status

Gate remains closed. Do not upload.

Incomplete items include:

- audio review incomplete;
- no reliable full watch/listen of the final candidate;
- no full final in-motion caption review of the line-polished burn-in;
- captions remain draft-only;
- no final public-link/chapter verification;
- no peer-feedback disposition or explicit no-feedback rationale;
- no publish-now rationale.

This document supports only a narrow focused visual decision about two caption
line breaks. It does not approve the video for publication.
