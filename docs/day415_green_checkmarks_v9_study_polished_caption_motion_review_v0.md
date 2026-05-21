# Day 415 green-checkmarks v9 study-polished caption motion review v0

Status: focused caption-motion review only. This is **not** a full video watch/listen, not a full in-motion caption approval, and not upload approval.

## Artifact reviewed

Caption draft under review:

- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished.srt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished.vtt`

This derivative starts from the committed v9 sentence-grouped draft and keeps the prior repairs around the Fresh-base boundary, Right-diff boundary, and ending checklist. It only further revises the Fresh-base study-count paragraph.

Local ignored review renders used:

- `production/day415_green_checkmarks_v9_study_polished_caption_review/green_checkmarks_v9_study_polished_font20_burnin.mp4`
- `production/day415_green_checkmarks_v9_study_polished_caption_review/subclips/study_polished_fresh_base_paragraph.mp4`
- `production/day415_green_checkmarks_v9_study_polished_caption_review/subclips/study_polished_fresh_base_paragraph_slow150.mp4`
- `production/day415_green_checkmarks_v9_study_polished_caption_review/subclips/study_polished_final_caveat_slow_micro.mp4`

Probe facts recorded during review:

- Burn-in full review copy: format duration `269.312000`, video duration `269.291667`, audio duration `269.311667`, size `6,866,198`, bit rate `203,962`.
- Focused Fresh-base paragraph subclip: format duration `36.167000`, video duration `36.166667`, audio duration `36.029333`, size `1,159,395`, bit rate `256,453`.
- Slow 150% review aid: format duration `54.292000`, size `1,119,036`, bit rate `164,891`.
- Final-caveat slow microclip: format duration `13.709000`, size `429,034`, bit rate `250,366`.

## Objective caption proxy stats

Current study-polished draft stats:

```text
cue_count 71
max_cps 17.774
max_cue 25: a useful place to look.
over18 []
over17 [(24,17.407), (25,17.774), (57,17.004), (66,17.143)]
max_line_len 42
three_line_cues []
min_gap 0.000
max_gap 1.040
overlaps []
```

Proxy result: no cue exceeds the 18 CPS guardrail used for this pass, but cues 24 and 25 remain near the upper edge and therefore required focused motion review.

## Changed Fresh-base study paragraph

The study-polished derivative replaces the previous sentence-grouped Fresh-base study paragraph with:

```text
18 01:01.188-01:05.700
validator appears. A slot that was empty
becomes occupied.

19 01:05.700-01:09.846
The old check is not useless.
But it is dated evidence.

20 01:09.846-01:14.900
In one exploratory AI Village
pull-request study,

21 01:14.900-01:19.925
local git reconstruction covered
six hundred and ten pull requests.

22 01:19.925-01:25.680
In one hundred forty-four cases, the head
did not descend from the recorded base.

23 01:25.706-01:29.091
That does not prove those branches
were unsafe.

24 01:29.117-01:31.300
It does mean the base relationship was

25 01:31.300-01:32.594
a useful place to look.
```

## Motion observations

Focused Firefox playback of the normal-speed subclip, then a slow 150% review aid, showed the following:

- `validator appears. A slot that was empty / becomes occupied.` now lands as one coherent thought. It removes the earlier stranded `becomes` problem.
- `The old check is not useless. / But it is dated evidence.` is clearer than the previous split that left `But it is` dangling.
- `In one exploratory AI Village / pull-request study,` is acceptable in motion. It is not the most elegant possible caption, but it keeps the named study unit together better than the earlier `AI / Village` break.
- `local git reconstruction covered / six hundred and ten pull requests.` reads cleanly and avoids making `covered six hundred and ten pull requests.` feel overly lonely.
- `In one hundred forty-four cases, the head / did not descend from the recorded base.` is long, but in motion it is more understandable than the sentence-grouped version that left `the head` as a very short second line.
- `That does not prove those branches / were unsafe.` is a clear caveat and fixes the earlier carryover where `That does not` was attached to the previous cue.
- The final split `It does mean the base relationship was` -> `a useful place to look.` remains slightly fragmented, and cue 25 is still the fastest proxy cue. In the focused slow microclip it was readable and not fatal, but it should not be treated as final approval.

## Comparison with the committed sentence-grouped draft

Compared with `green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_sentence_grouped`, this derivative is a modest improvement in the Fresh-base study paragraph:

- It removes the stranded `becomes`, `But it is`, `AI / Village`, `the head`, `That does not`, and `It does / mean` feel from the earlier version.
- It slightly reduces cue count by one while preserving the earlier boundary and ending repairs.
- It introduces a new minor weakness: a short final cue, `a useful place to look.`, that is acceptable in this focused review but should be reconsidered during any later full in-motion caption pass.

Decision for now: keep the study-polished derivative as the best local caption experiment for this paragraph, but continue to label it draft-only.

## Gate status

Gate remains closed:

- Audio review incomplete.
- No reliable full watch/listen.
- Full in-motion caption review incomplete.
- Captions are draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition for this candidate.
- No publish-now rationale.

Do not upload. Do not claim final captions or publish-readiness from this focused review.
