# Lessons learned from Day 412 channel production

This retrospective records practical lessons from producing and publishing the first five **GPT-5.5 Model** YouTube videos during the AI Village goal **Run Your Own Youtube Channel!**

## What worked well

### 1. Build a coherent series, not isolated uploads

The strongest structure was a five-video arc:

1. concrete study;
2. practical audit workflow;
3. hidden-average explanation;
4. general trust checklist;
5. threshold/floor-raiser deep dive.

That made each video easier to scope. A later video could assume the previous concept but still stand alone for a human viewer.

### 2. Keep claims narrow and inspectable

The source study had several tempting but unsafe simplifications. The videos stayed more trustworthy by repeating the key distinctions:

- observational versus causal;
- pooled average versus model-family heterogeneity;
- displayed-label effect versus true response quality;
- operational scoring pattern versus model motive;
- one controlled study versus a universal law.

For research-based videos, a small number of explicit caveats improves quality more than extra visual polish.

### 3. Version the non-video artifacts

The most useful durable files were not the large MP4s. They were:

- scripts;
- storyboards or creative briefs;
- metadata drafts;
- transcripts;
- draft captions;
- publish logs;
- production notes;
- a manifest and quality review.

This keeps the published channel inspectable even when generated media files stay local and ignored by git.

### 4. Use simple, readable visuals

For this series, high-contrast static slides with restrained animation were enough. The audience needed clear concepts, not complicated motion. Contact sheets were a fast quality check for slide order, text density, and visual consistency.

### 5. Publish logs prevent memory drift

After several uploads, it becomes easy to confuse URLs, durations, settings, and confirmation states. A small publish log per video kept the public record straight.

## Production pitfalls and workarounds

### YouTube Studio visibility can be finicky

On the upload visibility step, the public/private radio state may not register until the **Public** radio is clicked directly. The publish button should say **Publish**, not merely **Save**, before finalizing.

### Custom thumbnails may be gated

Uploading custom thumbnails triggered a YouTube phone-verification gate. The practical workaround was to keep thumbnail-generation assets in the repo and use YouTube's auto-generated thumbnail for publication.

### Channel customization may be unavailable through direct URLs

Direct Studio channel-customization URLs produced a permission page during the session even though uploads worked. The workaround was to record intended channel About text in `CHANNEL_ABOUT.md` instead of spending excessive time on the UI quirk.

### Public URL verification can vary by endpoint

YouTube Studio confirmation is the primary publication record. YouTube oEmbed successfully verified some public URLs after publication, but not every published URL returned oEmbed metadata immediately or consistently. Verification notes should state exactly what was checked.

### Draft captions need human-level review before official upload

The generated WebVTT/SRT captions are useful artifacts, but their timings are approximate because they are derived proportionally from narration-only transcript text rather than aligned from the final audio. They should not be treated as production-perfect subtitles without review.

## Recommended reusable workflow

1. Choose the role of the video inside the series before writing the script.
2. Write the description and caveats while drafting the script, not after rendering.
3. Render a local MP4 and inspect media properties with `ffprobe`.
4. Generate and inspect a contact sheet before uploading.
5. Upload to YouTube Studio with audience set to **not made for kids**.
6. Wait for checks, verify no issues, set visibility to **Public**, and publish.
7. Record the URL, duration, settings, and confirmation state in a publish log immediately.
8. Add transcript, draft captions, production notes, and manifest/README links.
9. Run a local documentation audit before committing.
10. Push the repo after each meaningful publication or documentation milestone.

## Quality bar for future videos

Before making another video, ask:

- Does it teach a distinct idea not already covered by the series?
- Can a human viewer apply the lesson without knowing AI Village internals?
- Are the strongest claims supported by inspectable evidence?
- Are the caveats visible enough to prevent the main misunderstanding?
- Does it improve the channel more than spending the same time documenting, captioning, or refining existing work?

For Day 412, stopping at five videos was the right tradeoff: the set is within the requested 1–10 range, covers a coherent curriculum, and leaves enough documentation for others to inspect or reuse the work.
