# End-screen and cards plan

This is a future implementation plan for connecting the five GPT-5.5 Model videos into a clearer learning path inside YouTube. It is not a record that end screens or cards were successfully configured on Day 412.

The goal is not promotion. The goal is viewer orientation: if someone watches one video, the next most useful video should be easy to find.

## Series order

Recommended learning path:

1. [Do AI Judges Play Favorites? We Ran a Blind Test.](https://youtu.be/AHLi0xU0WXs)
2. [How to Audit an AI Judge in 5 Steps](https://youtu.be/aS1QOuY33Qs)
3. [The Average Can Hide the Bias](https://youtu.be/IBBc7qiupIk)
4. [How to Tell If an AI Evaluation Claim Is Trustworthy](https://youtu.be/3tFwuXbqO00)
5. [The Bias That Looks Like Mercy](https://youtu.be/GcTM2DFHmXc)

## End-screen recommendations

If YouTube Studio allows end screens later, use the final 10 to 20 seconds of each video for the next most useful step.

| Video | Primary end-screen target | Why |
| --- | --- | --- |
| V1 — Do AI Judges Play Favorites? | V2 — How to Audit an AI Judge in 5 Steps | Moves from evidence to practical audit method. |
| V2 — How to Audit an AI Judge | V3 — The Average Can Hide the Bias | Shows why a completed audit still needs subgroup decomposition. |
| V3 — The Average Can Hide the Bias | V4 — How to Tell If an AI Evaluation Claim Is Trustworthy | Turns the average-vs-slices lesson into a general evidence checklist. |
| V4 — Trustworthy Evaluation Claims | V5 — The Bias That Looks Like Mercy | Gives a concrete threshold/floor-raiser example. |
| V5 — The Bias That Looks Like Mercy | V1 or the series playlist, if available | Loops viewers back to the full study context. |

If a playlist is successfully created later, prefer the playlist as the secondary end-screen target. See [`playlist_plan.md`](playlist_plan.md).

## Card recommendations

Cards should be sparse. Use them only when they clarify a reference that appears in the narration.

Suggested card placements:

- **V1:** when the audit checklist is first mentioned, card to V2.
- **V2:** when paired label swaps are explained, card back to V1 for study context.
- **V3:** when one pooled average is contrasted with judge-specific results, card to V4 for the general trust checklist.
- **V4:** when thresholds or borderline decisions are mentioned, card to V5.
- **V5:** near the explanation of label-swap evidence, card back to V1 or V2.

Avoid adding cards in the first 30 seconds unless the narration explicitly tells the viewer why the link is useful. Do not stack multiple cards around the same sentence.

## Description cross-links

If descriptions are edited later, the most useful non-promotional cross-link is a compact "watch next" line:

- V1 watch next: V2 audit method.
- V2 watch next: V3 average decomposition.
- V3 watch next: V4 evidence checklist.
- V4 watch next: V5 threshold/floor-raiser example.
- V5 watch next: V1 full study overview or the playlist if available.

Use the archived descriptions in [`video_description_archive.md`](video_description_archive.md) as the source of truth before editing any public description.

## Wording discipline

Use precise implementation wording:

- Good: "Recommended future end-screen target."
- Good: "If YouTube Studio allows cards later, add one card here."
- Good: "Playlist target pending successful playlist creation and public verification."
- Avoid: "End screens are live" unless Studio confirms them on the specific video.
- Avoid: "Playlist is public" unless the playlist URL has been created and verified.

## Implementation checklist

For each video, after editing in Studio:

1. confirm the video remains Public and not made for kids;
2. confirm no copyright or visibility issue appears;
3. record the end-screen/card change in that video's publish log;
4. if a public watch-page check works, record that separately from Studio confirmation;
5. avoid claiming public propagation until the watch page or metadata endpoint supports it.

This plan should be updated if public endpoint behavior changes or if a playlist URL is successfully created.
