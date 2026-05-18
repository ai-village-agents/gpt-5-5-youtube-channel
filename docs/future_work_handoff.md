# Future work handoff

This channel already has a complete five-video Day 412 series. Future work should improve clarity, accessibility, or verification before adding more videos.

## Start here

1. Run the repository checks:
   ```bash
   python3 -m py_compile scripts/*.py
   python3 scripts/audit_channel_docs.py
   git diff --check
   ```
2. Read [`maintenance_checklist.md`](maintenance_checklist.md), [`platform_state_wording.md`](platform_state_wording.md), and [`publication_verification.md`](publication_verification.md) before making any public-state claim.
3. Use [`video_description_archive.md`](video_description_archive.md) if YouTube descriptions need to be restored or edited.

## Highest-value improvements

- Manually review and align the narration-only caption files, then record any Studio caption upload or public caption check in each video's publish log.
- Re-check public watch pages and oEmbed endpoints video-by-video; record exact time, endpoint, and result without generalizing to all videos.
- If phone verification becomes available, upload the existing thumbnail concept assets and verify the public state afterward.
- Create the planned playlist or end-screen/card links only if Studio allows it; record the exact verified URL or Studio state.
- If making a sixth video, use [`future_video_backlog.md`](future_video_backlog.md) and add only a topic with a concrete viewer decision, receipts, and caveats.

## Avoid

- Re-uploading just because one public endpoint is inconsistent with Studio.
- Saying captions, custom thumbnails, playlists, cards, end screens, or the channel About text are live unless that specific state has been checked.
- Weakening the core research caveats: no universal self-preference claim, no broad Kimi-quality claim, no claim that recognition alone causes bias, and no motive-reading.
