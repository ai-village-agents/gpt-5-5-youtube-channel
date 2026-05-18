# Public endpoint review sheet

Use this template when checking whether a YouTube public endpoint matches Studio or repository expectations. Public watch pages and oEmbed responses can lag or vary, so record exact observations rather than summarizing all endpoints at once.

## Per-check template

```text
Video title:
Video ID:
Check time and timezone:
Checker:
Endpoint checked: public watch page / oEmbed / Studio preview / channel page
URL:
Signed-in state: signed in / signed out / incognito / unknown
Observed title:
Observed channel:
Observed visibility or error message:
Runtime shown:
Captions visible:
Custom thumbnail visible:
Matches repo manifest: yes / no / partial
Matches Studio state: yes / no / not checked
Follow-up needed:
```

## Interpretation rules

- A successful oEmbed response for one video does not verify every video.
- A broken public watch page does not by itself prove the Studio upload failed.
- A Studio Public state does not by itself prove public watch-page propagation is complete.
- Caption, thumbnail, playlist, end-screen, card, and About-page state should each be checked separately.

## Safe summary wording

Use: “At [time], [endpoint] for [video] returned [observed result].”

Avoid: “all endpoints verified,” “the playlist is public,” “captions are published,” or “custom thumbnails are live” unless those exact states were checked and recorded.
