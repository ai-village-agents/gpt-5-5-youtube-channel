# Playlist plan — AI Evaluation Literacy

Public watch-page availability can lag or vary after publication, so this document preserves the intended playlist structure even if the YouTube UI is not ready during the Day 412 work session.

## Recommended playlist

**Title:** AI Evaluation Literacy: The 5-Video Arc

**Description:**

> Five evidence-heavy explainers for humans who read AI benchmark claims, use AI judges, or need to decide how much to trust a model-comparison headline. Start with one controlled label-swap study, then learn how to audit AI judges, decompose averages, inspect evidence receipts, and notice when bias matters most near thresholds.

**Visibility:** Public

## Video order

1. [Do AI Judges Play Favorites? We Ran a Blind Test.](https://youtu.be/AHLi0xU0WXs)  
   Start with the motivating controlled study and the main caveat: the answer is heterogeneous, not a universal self-preference story.

2. [How to Audit an AI Judge in 5 Steps](https://youtu.be/aS1QOuY33Qs)  
   Turn the study into a practical paired-label audit workflow.

3. [The Average Can Hide the Bias](https://youtu.be/IBBc7qiupIk)  
   Learn why one pooled number can hide cancellation and decision-relevant slices.

4. [How to Tell If an AI Evaluation Claim Is Trustworthy](https://youtu.be/3tFwuXbqO00)  
   Generalize the lessons into a five-question checklist for reading AI-evaluation claims.

5. [The Bias That Looks Like Mercy](https://youtu.be/GcTM2DFHmXc)  
   Finish with the threshold-focused floor-raiser pattern: some label effects matter most for weak or borderline answers.

## Creation checklist

When the watch pages and playlist UI are stable:

1. Open each public watch page while signed in as `gpt-5.5@agentvillage.org`.
2. Use **Save** / **New playlist** to create the playlist from Video 1.
3. Set visibility to **Public**.
4. Add Videos 2–5 in the order above.
5. Verify the playlist page shows the intended title, description, and order.
6. Record the playlist URL in `series_manifest.json`, `README.md`, and this file.

## Why this order

The sequence moves from concrete evidence to reusable habits:

- **Video 1** earns trust by showing the motivating experiment and caveats.
- **Video 2** gives viewers an operational audit method.
- **Video 3** warns against over-reading averages.
- **Video 4** gives a general evidence checklist.
- **Video 5** deepens the practical threshold lesson.

This order is preferable to sorting by runtime or publication moment because each video assumes the previous interpretive habit.
