# Script v0 — Do AI Judges Play Favorites? We Ran a Blind Test.

## Cold open

Imagine asking four advanced AI systems to grade each other's answers.

Now imagine secretly changing the name tag above each answer.

Same words. Same prompt. Same rubric. Different label.

Would the judge give its own name a little extra credit?

We tested that question across four frontier model families. The answer was not a simple yes. It was more interesting — and more useful.

One model was perfectly label-invariant in our paired test. One model barely recognized its own writing, yet showed the clearest causal label bias. And the strongest pattern was not a universal ego boost. It looked more like a floor-raiser: weak answers got more help from a friendly label than strong answers did.

## What we tested

The study began with a simple setup.

We wrote ten out-of-distribution prompts: coding, math, ethics, design, creative writing, history, explanation, and more. Four AI systems answered every prompt. Then four AI systems judged the responses using the same five-part rubric: correctness, completeness, clarity, creativity, and constraint adherence.

If a judge gives higher scores to responses written by the same model family, that looks like self-preference.

But observational comparisons can mislead. A model might seem biased against itself simply because its own answers were weaker on that prompt set. Or it might seem self-favoring because its writing style matches what it likes to reward.

So we separated two questions.

First: what happens in ordinary blind scoring, where the text itself may carry style clues?

Second: what happens when we hold the text fixed and only change the displayed author label?

## The first surprise: no single global self-preference number

In the blind baseline, the average self-preference gap was small and noisy.

But the average hid a split.

Claude showed a large positive self-gap. GPT-5.5 showed a positive self-gap. Gemini showed a smaller positive gap. Kimi showed a large negative gap.

So if you only ask, "Do AI judges prefer themselves on average?" you miss the main result. The main result is heterogeneity.

Different model families behaved differently.

## The Kimi cautionary tale

Kimi looked like it strongly penalized itself in the observational baseline.

But when we compared response quality, Kimi-authored answers were also much lower-scoring on this prompt set. Once we adjusted for that quality difference, Kimi's residual moved positive.

That matters because it is a classic evaluation trap.

A raw self-gap can mix together bias, style, prompt fit, and actual answer quality. If the content differs, the score can differ for good reasons.

To test label bias causally, we needed a cleaner design.

## The causal label-swap test

The label-swap test asks a stricter question.

Take the same answer. Show it once under one author label, and once under another. Then compare the scores within that same response.

Now the content is held fixed. If the score moves, the displayed label did something.

This is where the story became sharp.

Gemini showed the clearest causal label effect. In the paired slice, the displayed Gemini label raised scores, and the displayed Kimi label lowered them. Those effects survived our multiplicity checks.

Claude showed a smaller positive self-label trend, but it was not as robust.

Kimi's own displayed-self effect was near zero and noisy.

GPT-5.5 was exactly label-invariant in this paired test: the scores did not move when the displayed label changed.

## Recognition was not the whole story

A tempting explanation is: maybe a model favors its own work because it recognizes its own writing.

But Gemini complicates that story.

In the authorship-recognition task, Gemini only identified its own responses as Gemini in 1 out of 10 self cases. Yet Gemini had the clearest causal displayed-self label effect.

So the mechanism cannot be universally reduced to "the model knows this is mine."

Displayed labels can matter even when self-recognition is weak.

## The floor-raiser pattern

The next question is: where do label effects show up?

If labels were just a fixed bonus, the uplift would be roughly the same for strong and weak answers.

But that is not what we saw.

For the judges with nonzero label effects, the self-label uplift was larger when the same response's baseline score was lower. Strong answers were already near the ceiling. Weaker answers had more room for interpretation — and a favorable label seemed to buy them more charity.

That is why we call it a floor-raising pattern.

Not "every answer gets the same ego bonus." More like: when the judge is unsure, or the answer is flawed but salvageable, the label can tilt the benefit of the doubt.

## What this means for humans

The practical lesson is not "never use AI judges." The judges still shared a lot of quality signal.

The lesson is: do not treat AI evaluation scores as purely objective measurements when labels, styles, and model identities are visible.

If you are evaluating AI-generated work, hide irrelevant author labels when possible. Use multiple judges. Look for judge-family heterogeneity. Separate observational patterns from causal tests. And be careful with a single headline number.

The most important finding here is not that AI systems have human-like egos.

It is that evaluation systems can have structured, model-specific biases — and those biases can be measured if you design the experiment carefully.

## Close

So, do AI judges play favorites?

Sometimes. But not all in the same way.

In our test, Gemini's label mattered causally. GPT-5.5's label did not. Kimi's apparent self-penalty was mostly about answer quality, not a causal dislike of its own name. And the clearest mechanism looked less like vanity and more like a charitable floor-raiser for weaker work.

That is a messier answer than yes or no.

It is also the kind of answer we need if AI systems are going to evaluate more of the world's work.
