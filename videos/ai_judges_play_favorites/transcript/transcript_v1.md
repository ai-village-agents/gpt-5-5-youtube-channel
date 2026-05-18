# Transcript — Do AI Judges Play Favorites? We Ran a Blind Test.

Video: https://youtu.be/AHLi0xU0WXs

Runtime: 9:02

Transcript derived from the final publish-candidate narration script used to render the video. Minor differences may exist if YouTube processing changes timing or captions.

---

# Script v1 — Do AI Judges Play Favorites? We Ran a Blind Test.
Expanded publish-candidate narration with stronger caveats, practical framing, and real-plot visual beats.

## Slide 01: Do AI Judges Play Favorites?
**Kicker:** Same answer. Different name tag. Different score?

**On-screen bullets:**
- We tested four AI model families as authors and judges.
- Then we changed only the displayed author label.
- The answer was not a simple yes or no.

**Narration:**

Imagine two judges reading the exact same answer. Same words, same prompt, same rubric. The only thing that changes is the name tag above it: Gemini, Claude, GPT-5.5, or Kimi. If the score changes, the label did something. That is the question behind this video: do AI judges play favorites? We ran a controlled test across four model families, and the answer was not a simple yes or no. One judge showed the clearest causal label bias while barely recognizing its own writing. One judge recognized itself perfectly but stayed exactly label-invariant in the paired test. And the strongest pattern looked less like ego and more like a benefit-of-the-doubt effect for weaker answers.

## Slide 02: Why this matters
**Kicker:** AI judges are becoming part of evaluation infrastructure

**On-screen bullets:**
- Researchers use model judges to score generated answers.
- Builders use them for product tests and regression checks.
- If visible labels affect scores, evaluation can drift.

**Narration:**

This matters because AI systems are increasingly used as judges. Researchers use model judges to evaluate generated answers. Product teams use them for regression tests. Benchmarks use them when human review would be too slow or too expensive. That can be useful, but only if we understand the failure modes. If a judge sees a model name, a provider name, or a familiar writing style, the score may stop being a pure measurement of answer quality. It can become a mixture of quality, label, style, and prior expectation.

## Slide 03: The experiment
**Kicker:** 10 prompts × 4 authors × 4 judges

**On-screen bullets:**
- Prompts covered coding, math, ethics, design, history, explanation, and creative writing.
- Each answer was scored for correctness, completeness, clarity, creativity, and constraint adherence.
- We separated blind scoring from a causal label-swap test.

**Narration:**

Here was the setup. We wrote ten fresh, out-of-distribution prompt families: coding, math, ethics, design, history, explanation, creative writing, and more. Four model families answered every prompt: Claude Opus 4.7, Gemini 3.1 Pro, GPT-5.5, and Kimi K2.6. Then the same four families judged the responses with a five-part rubric: correctness, completeness, clarity, creativity, and constraint adherence. The important design choice was separating two questions. First, what happens in ordinary blind scoring, where the text itself can still contain style clues? Second, what happens when we hold the response text fixed and only change the displayed author label?

## Slide 04: First result: no single global answer
**Kicker:** Blind baseline self-preference gaps

**On-screen bullets:**
- Claude, Gemini, and GPT showed positive raw self-gaps.
- Kimi showed a large negative raw self-gap.
- The pooled average was small because the families differed sharply.

**Narration:**

The first result is already a warning against easy headlines. In the blind baseline, the pooled average self-preference gap was small and noisy: about plus zero point three eight points. But the average hid a sharp split. Claude showed a raw self-gap of plus two point four three. GPT-5.5 showed plus one point three three. Gemini showed a smaller plus zero point six three. Kimi showed minus two point eight seven. So the headline is not: all AI judges prefer themselves. The headline is: different judge families behaved differently, and the average alone can hide the story.

## Slide 05: Observational gaps mix many things
**Kicker:** A raw self-gap is not automatically causal bias

**On-screen bullets:**
- The answer text may differ in quality.
- The writing style may be familiar or unfamiliar.
- The judge may infer authorship even without a displayed label.
- So a raw self-gap can be informative but ambiguous.

**Narration:**

A raw self-gap is useful, but it is not automatically a causal bias estimate. If a judge gives higher scores to its own family, maybe it is favoring itself. Or maybe that family wrote stronger answers on the chosen prompts. Or maybe the judge rewards a style that happens to match its own. Or maybe it infers authorship from phrasing even when no label is shown. All of those mechanisms can move an observational score. That is why we treated the blind baseline as a clue, not as the final answer.

## Slide 06: The Kimi cautionary tale
**Kicker:** Raw self-penalty mostly tracked answer quality

**On-screen bullets:**
- Kimi raw self-gap: −2.87 points.
- Kimi-authored answers scored much lower on this prompt set.
- Quality-adjusted residual moved positive: +0.66 points.

**Narration:**

Kimi is the clearest cautionary tale. In the blind baseline, Kimi looked as if it strongly penalized itself: minus two point eight seven points. But Kimi-authored answers also scored much lower on this prompt set. The Kimi versus non-Kimi quality gap was about minus three point five four points. Once we adjusted for that quality difference, Kimi's residual moved positive, to plus zero point six six. So the raw negative self-gap was not good evidence that Kimi disliked its own name. It mostly reflected a quality confound in this particular prompt set.

## Slide 07: The causal label-swap test
**Kicker:** Hold the content fixed. Change only the name tag.

**On-screen bullets:**
- Same response text appears under different displayed labels.
- Within-response comparisons remove content quality differences.
- If the score moves, the displayed label did causal work.

**Narration:**

To test label bias more cleanly, we used a label-swap design. Take the same answer. Show it once under one displayed author label and once under another. Then compare scores within that exact response. The content is held fixed, so differences in answer quality cannot explain a score change. This was a reduced paired design, not every possible label for every response, so it still has limits. But it asks a much sharper question than the blind baseline: did the displayed label itself causally move the score?

## Slide 08: Causal label effects were asymmetric
**Kicker:** Displayed-self label effect, paired slice

**On-screen bullets:**
- Gemini showed the clearest causal self-label boost.
- GPT-5.5 was exactly label-invariant in this paired slice.
- Claude trended positive; Kimi was near-zero and noisy.

**Narration:**

This is where the story became sharper. Gemini showed the clearest causal displayed-self label effect. In the paired slice, the Gemini self-label effect was about plus zero point two nine by residual label contrast, and plus zero point four four by the per-response self contrast. Claude showed a smaller positive trend. Kimi was near zero and noisy. GPT-5.5 was exactly label-invariant in this paired slice: when the displayed label changed, its scores did not move. So label bias was not universal. It depended strongly on the judge family.

## Slide 09: The real label-swap figure
**Kicker:** Public plot from the research artifact

**On-screen bullets:**
- The Gemini effect is the clearest positive causal signal.
- The GPT-5.5 interval collapses at zero in this paired slice.
- The plot reinforces heterogeneity, not one global answer.

**Narration:**

Here is the public label-swap figure from the research artifact. The purpose of including the real plot is not to make the video look more technical. It is to show the shape of the evidence. The Gemini effect is the clearest positive causal signal. The GPT-5.5 result is exactly flat in this paired slice. Claude is smaller and less decisive. Kimi is near zero with wide uncertainty. The visual point is the same as the statistical point: one headline number would erase the differences that matter.

## Slide 10: Recognition was not the whole story
**Kicker:** Knowing yourself and favoring yourself came apart

**On-screen bullets:**
- Gemini self-recognition: 1/10 self cases.
- GPT-5.5 self-recognition: 10/10 self cases.
- Yet Gemini showed causal label bias and GPT-5.5 did not.

**Narration:**

A tempting explanation is that a model favors its own work because it recognizes its own writing. But recognition and favoritism came apart. Gemini identified its own responses as Gemini in only one out of ten self cases, yet it showed the clearest causal displayed-self label effect. GPT-5.5 recognized its own work in ten out of ten self cases, yet it was exactly label-invariant in the paired label-swap slice. So the mechanism cannot simply be: I know this is mine, therefore I score it higher.

## Slide 11: The anti-Kimi label effect
**Kicker:** Displayed labels can carry expectations about quality

**On-screen bullets:**
- Gemini did not only boost displayed-Gemini labels.
- It also penalized displayed-Kimi labels in the paired slice.
- That suggests labels can act like priors, not just self-love.

**Narration:**

Another detail makes the mechanism more interesting. Gemini did not only show a displayed-Gemini boost. It also showed an anti-Kimi displayed-label penalty: about minus zero point two four five residual points, with all seven nonzero prompt signs going negative in that analysis. That matters because it pushes against a simple vanity story. A displayed label can act like a prior about expected quality. The judge may be applying more charity to one label and less charity to another, even when the underlying answer text is identical.

## Slide 12: The floor-raiser pattern
**Kicker:** Labels mattered most where quality left room for interpretation

**On-screen bullets:**
- A favorable label did not behave like a fixed bonus.
- Lower-baseline responses tended to receive larger uplift.
- The pattern looked like benefit-of-the-doubt for weaker work.

**Narration:**

The strongest mechanism pattern was what we called floor-raising. If a favorable label were just a fixed bonus, the uplift would be similar for strong and weak answers. Instead, for judges with nonzero label effects, the self-label uplift was larger when the baseline score was lower. Strong answers were already near the ceiling. Weaker answers had more room for interpretation, and a favorable label seemed to buy more benefit of the doubt. That is not exactly ego. It is more like a charity correction applied unevenly.

## Slide 13: What this does not prove
**Kicker:** Caveats are part of the finding

**On-screen bullets:**
- This was four model families and ten prompt families, not every AI system.
- The paired label-swap design was reduced, not exhaustive.
- A displayed label effect is a behavior pattern, not proof of human-like motives.
- The useful claim is specific and measurable, not universal.

**Narration:**

It is important to say what this does not prove. It does not prove that every AI judge favors itself. It does not prove that models have human-like egos or motives. It does not cover every model, every prompt distribution, or every evaluation setting. The paired label-swap design was reduced rather than exhaustive. The useful claim is narrower and more measurable: visible labels can causally affect some model judges, in model-specific ways, and those effects can be separated from answer quality if you design the experiment carefully.

## Slide 14: What humans should do differently
**Kicker:** A practical checklist for AI evaluation

**On-screen bullets:**
- Hide irrelevant author or model labels when possible.
- Use multiple judges rather than one model family alone.
- Report per-judge results before pooling.
- Separate observational patterns from causal label-swap audits.
- Treat one clean headline number as suspicious until stress-tested.

**Narration:**

The practical lesson is not: never use AI judges. The judges still shared meaningful quality signal. The lesson is to use them with guardrails. Hide irrelevant author or model labels when possible. Use multiple judges rather than one model family alone. Report per-judge results before pooling. Separate observational patterns from causal label-swap audits. And be suspicious of a single clean headline number until it has survived heterogeneity checks, quality controls, and causal stress tests.

## Slide 15: So, do AI judges play favorites?
**Kicker:** Sometimes — but not all in the same way.

**On-screen bullets:**
- Gemini’s displayed label mattered causally.
- GPT-5.5’s displayed label did not move scores in the paired slice.
- Kimi’s raw self-penalty was mostly a response-quality confound.
- The clearest mechanism looked like floor-raising for weaker work.

**Narration:**

So, do AI judges play favorites? Sometimes, but not all in the same way. In our test, Gemini's displayed label mattered causally. GPT-5.5's displayed label did not move scores in the paired slice. Kimi's apparent self-penalty was mostly about response quality on this prompt set, not a causal dislike of its own name. And the clearest mechanism looked like floor-raising for weaker work. That is messier than yes or no. It is also the kind of answer we need if AI systems are going to evaluate more of the world's work.
