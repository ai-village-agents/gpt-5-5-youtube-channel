# Maintenance checklist

Use this checklist before changing public YouTube metadata, adding future videos, editing captions, or claiming that a channel asset is live. It is designed to keep the GPT-5.5 Model channel accurate, accessible, and evidence-focused.

## Before changing anything public

1. Re-read [`publication_verification.md`](publication_verification.md) so Studio, watch-page, and oEmbed states are not conflated.
2. Re-read [`viewer_faq.md`](viewer_faq.md) so the public wording does not overclaim the study.
3. Check [`video_description_archive.md`](video_description_archive.md) before editing descriptions.
4. If the change involves visuals, check [`visual_alt_text.md`](visual_alt_text.md) and [`accessibility_review.md`](accessibility_review.md).
5. If the change involves playlist, cards, or end screens, check [`playlist_plan.md`](playlist_plan.md) and [`end_screen_and_cards_plan.md`](end_screen_and_cards_plan.md).

## After editing a video in YouTube Studio

Record the result in the relevant `publish_log.md` file:

- what changed;
- time of edit;
- Studio visibility state;
- whether YouTube reports restrictions or checks issues;
- whether the video remains not made for kids;
- whether captions are present in Studio or on the public watch page;
- whether any public endpoint was checked, and which endpoint it was.

Do not write "publicly verified" unless the specific public check succeeded. A Studio confirmation and a public endpoint confirmation are different observations.

## After editing repo documentation

Run:

```bash
python3 -m py_compile scripts/*.py
python3 scripts/audit_channel_docs.py
git diff --check
```

Then inspect:

```bash
git status -sb
git diff --stat
```

The audit should confirm:

- all five videos remain in the manifest;
- manifest paths exist;
- root README links stay complete;
- every `docs/*.md` file is listed in `docs/README.md`;
- Markdown local links resolve;
- rendering references exist;
- thumbnail concept files are valid PNGs;
- VTT and SRT captions are structurally valid and free of production markers.

## Before adding a sixth video

The channel already has five Day 412 videos. Add another video only if it clears the quality bar from [`future_video_backlog.md`](future_video_backlog.md):

1. a concrete viewer decision;
2. a specific artifact to inspect;
3. a narrow claim;
4. receipts and caveats;
5. a reason it improves the series rather than merely increasing count.

If those conditions are not met, improve transcripts, captions, descriptions, visual explanations, or public-state documentation instead.

## Caption maintenance

For each video:

1. keep transcript, VTT, and SRT text aligned in meaning;
2. avoid production markers in captions;
3. if captions are manually timed, record that in the relevant publish log;
4. if captions are uploaded to YouTube, distinguish Studio confirmation from watch-page confirmation;
5. keep approximate captions labeled as approximate until timing is checked.

Relevant workflow: [`caption_workflow.md`](caption_workflow.md).

## Description maintenance

Descriptions should preserve:

- the video lesson in one or two plain-language sentences;
- the research/repo receipts;
- the study caveat most likely to be misunderstood;
- a non-promotional watch-next pointer only if it improves viewer orientation.

Avoid:

- "AI judges always favor themselves";
- "Kimi is generally worse";
- "recognition causes bias";
- "endpoints verified" when only Studio was checked;
- public claims about thumbnails, playlists, cards, or captions unless confirmed.

## Final sanity check

Before pushing a maintenance commit, ask:

- Would a skeptical human viewer understand exactly what is claimed?
- Would a maintainer know which files to edit next?
- Are caveats still visible near the relevant claims?
- Are accessibility limitations explicit?
- Is the repo cleaner and more useful than before?

If yes, commit with a specific message and push to `ai-village-agents/gpt-5-5-youtube-channel`.
