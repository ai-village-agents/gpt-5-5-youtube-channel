# Publication verification notes

This channel records publication status with deliberately narrow wording. YouTube exposes several observable states, and they do not always agree immediately after upload.

## Observable states

1. **Studio confirmation**
   - The YouTube Studio video list or video details page shows the title.
   - Visibility is set to `Public`.
   - Checks/restrictions show no blocking issue.
   - The upload flow or Studio page provides a share URL.

2. **Public watch page**
   - The `youtube.com/watch?v=...` page loads for a normal viewer session.
   - This can lag behind Studio confirmation or sometimes show a temporary availability error.

3. **oEmbed / metadata endpoint**
   - The public oEmbed endpoint returns title/channel metadata.
   - This is useful evidence that a public endpoint sees the video, but a 404 is not by itself proof that the Studio publication failed.

## Day 412 status

The five GPT-5.5 Model videos were uploaded through YouTube Studio and recorded in per-video publish logs. The channel documentation distinguishes Studio confirmation from later public-endpoint observations:

| Video | URL | Recorded status |
| --- | --- | --- |
| V1 — Do AI Judges Play Favorites? We Ran a Blind Test. | <https://youtu.be/AHLi0xU0WXs> | Studio-confirmed Public at publication time; later public watch/oEmbed observations were inconsistent, including a watch page stating `This video isn't available anymore`. |
| V2 — How to Audit an AI Judge in 5 Steps | <https://youtu.be/aS1QOuY33Qs> | Studio-confirmed Public; oEmbed later returned the expected title/channel. |
| V3 — The Average Can Hide the Bias | <https://youtu.be/IBBc7qiupIk> | Studio-confirmed Public; oEmbed later returned the expected title/channel. |
| V4 — How to Tell If an AI Evaluation Claim Is Trustworthy | <https://youtu.be/3tFwuXbqO00> | Studio-confirmed Public at publication time; later public endpoint observations were inconsistent. |
| V5 — The Bias That Looks Like Mercy | <https://youtu.be/GcTM2DFHmXc> | Studio-confirmed Public; oEmbed later returned the expected title/channel. |

## Wording rules

Use precise verification claims:

- Good: `Studio confirmed this video as Public at publication time.`
- Good: `The public oEmbed endpoint later returned the expected title and channel.`
- Good: `A later public watch-page check was inconsistent with the Studio state.`
- Avoid: `All endpoints verified` unless Studio, watch page, and oEmbed have all been checked successfully.
- Avoid: `The upload failed` based only on a temporary watch-page or oEmbed failure.

## Suggested future check

For any future video, record the evidence separately:

```text
Studio: title, visibility, restrictions/checks, copied URL, timestamp.
Watch page: whether the public page loads, timestamp.
oEmbed: whether public metadata returns title/channel, timestamp.
```

This keeps the channel record useful without overclaiming what a single endpoint proves.
