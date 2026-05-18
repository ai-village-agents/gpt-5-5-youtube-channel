# Caption workflow

The channel keeps draft captions for every published video in two formats:

- WebVTT (`.vtt`) for web-native caption tooling.
- SubRip (`.srt`) for broad video-platform compatibility.

Both formats are generated from the committed transcript files with:

```bash
python3 scripts/generate_narration_captions.py
```

The generator extracts narration-only prose before writing captions. This matters
because some transcripts, especially the first video, also contain production
material such as slide headings, on-screen bullets, and markdown labels that
should not appear as spoken captions.

Current timing is approximate. Cue durations are allocated in proportion to word
count across the published runtime, so these files are useful draft accessibility
artifacts and review aids, but they are not hand-aligned captions. Before using
these as final platform captions, a human or timing-aware tool should compare
them against the rendered audio.

Quality checks to run before committing caption changes:

```bash
python3 scripts/generate_narration_captions.py
python3 scripts/audit_channel_docs.py
for f in videos/*/captions/*.srt; do sed -n '1,24p' "$f"; done
```

The audit verifies that each video has both VTT and SRT files, that VTT files
start with `WEBVTT`, that SRT files start with a numbered timestamp cue, and
that the README links the manifest-listed caption paths.
