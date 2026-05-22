# Future upload log template (gate-closed uploads only)

This template is for a future upload only after all relevant publish gates have honestly closed. It is not upload approval, and filling it out must not substitute for full watch/listen, in-motion caption review, metadata review, source-caveat review, peer-feedback disposition, or publish-now rationale.

## Gate status before opening YouTube Studio

Record the exact candidate and the evidence that each required gate is closed.

- Video candidate path:
- Video SHA-256:
- Final rendered duration:
- Full start-to-finish watch/listen completed by:
- Playback method used for the full review:
- Audio decision:
- In-motion caption review completed by:
- Caption decision:
- Metadata/source-caveat review completed by:
- Peer feedback disposition or no-feedback rationale:
- Publish-now rationale:

If any line above is uncertain, stop and write the blocker plainly. Example: `Audio review incomplete. Do not upload.`

## Studio-confirmed facts

Only record these after seeing them in YouTube Studio. Do not infer them from local files, browser URLs, or RSS feeds.

- Channel:
- Upload started at:
- File uploaded:
- Title entered:
- Description entered:
- Visibility selected:
- Audience setting:
- License:
- Category:
- Language:
- Synthetic/altered-content setting:
- Caption file uploaded:
- Caption language:
- Caption processing status shown by Studio:
- Thumbnail selection:
- Playlist selection:
- End screens/cards:
- Checks/copyright status shown by Studio:
- Final publish/save button pressed at:
- Studio confirmation text or page state:
- Studio video ID / URL shown:

Safe wording after this section, if verified: `Studio-confirmed Public at publication time.`

## Public endpoint checks

Public endpoints can lag, personalize, or fail transiently. Keep this section separate from Studio-confirmed facts.

- Watch page URL checked:
- Time checked:
- Browser/session used:
- Visibility observed on watch page:
- Title observed:
- Description observed:
- Captions visible/selectable:
- Chapters visible:
- Thumbnail observed:
- RSS feed entry observed:
- Search/channel page observed:

Safe wording: `Public watch-page checks may lag or vary.`

Do not write that captions, chapters, thumbnails, playlists, cards, or end screens are live unless the specific public or Studio evidence was observed and logged.

## Post-publish repository backfill

- Published URL:
- Commit that records URL:
- Files updated:
- Checks run before commit:
- Push verification:

## Final caution

This template controls record-keeping only. It cannot open an upload gate, cannot repair an incomplete review, and cannot convert local artifacts into public facts.
