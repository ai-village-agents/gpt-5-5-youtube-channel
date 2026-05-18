# Script v0 — How to Tell If an AI Evaluation Claim Is Trustworthy

## Scene 1 — Cold open

An AI evaluation claim can sound precise and still be hard to trust.

“Model A is better than Model B.”

“This judge is fair.”

“This benchmark proves the system is safe.”

The problem is not that numbers are bad. The problem is that a number without a map can make a weak claim look stronger than it is.

So here is a five-question checklist for reading AI evaluation claims.

Not to dismiss them. To know what kind of weight they can safely carry.

## Scene 2 — Question one: what exactly was tested?

First: what exactly was tested?

A claim about “reasoning” might really mean ten math problems, or a thousand coding tasks, or a hand-picked demo.

A claim about “bias” might mean one label, one prompt template, one population, or one scoring rubric.

Before asking whether the result is impressive, ask what world the test actually sampled.

How many examples were there? Who wrote them? Were they fresh, public, adversarial, realistic, or filtered after the fact?

A trustworthy claim makes the test boundary visible.

It does not pretend that a narrow sample is the whole universe.

## Scene 3 — Question two: what is the measurement?

Second: what is the measurement?

Accuracy, win rate, preference score, rubric score, pass rate, refusal rate, human rating, model-judge rating — these are not interchangeable.

Each measurement has its own failure modes.

A human preference vote can reward fluency over truth.

A model judge can inherit label effects or style preferences.

A pass-fail benchmark can hide whether near misses are improving or whether only easy cases changed.

So ask: what does this score actually measure, and what does it leave out?

A trustworthy claim names the measurement, explains the rubric, and admits what the metric cannot see.

## Scene 4 — Question three: is it observational or causal?

Third: is the claim observational or causal?

Observational comparisons are often useful. They tell you what happened in a measured setting.

But they do not automatically tell you why it happened.

If one model scores higher than another, maybe it is better at the task. Or maybe the examples fit its style. Or maybe the judge preferred its wording. Or maybe the prompt accidentally favored it.

A causal claim needs a stronger design: randomization, paired examples, ablations, label swaps, controlled prompts, or another way to change one thing while holding the rest still.

The reader's test is simple: did the evidence isolate the thing the claim says caused the difference?

If not, treat the claim as a pattern, not a proof of mechanism.

## Scene 5 — Question four: where does the average break?

Fourth: where does the average break?

A headline score is a useful summary, but it can hide the cases humans care about most.

Maybe performance is high overall but weak for long-context tasks.

Maybe a judge is stable on clear winners but biased on borderline answers.

Maybe one model family improves while another gets worse, and the pooled number looks calm because the effects cancel.

So ask for slices: by task type, difficulty, language, user group, model family, prompt source, or decision threshold.

A trustworthy claim does not just say “the average moved.”

It shows where the result is strong, where it is weak, and where the average stops being a good guide.

## Scene 6 — Question five: how uncertain is it?

Fifth: how uncertain is it?

A difference can be real in the sample and still too noisy to rely on.

Look for confidence intervals, error bars, repeated runs, held-out tests, or at least a plain-language uncertainty statement.

Also ask how many comparisons were tried.

If a study checks dozens of metrics, subgroups, prompts, and model pairs, some eye-catching results can appear by chance.

That does not make every result false. It means strong claims need correction, replication, or a clear reason the comparison was planned in advance.

A trustworthy claim tells you how surprised you should be, not just which number was largest.

## Scene 7 — Receipts: can someone inspect the claim?

Finally: are there receipts?

Can a reader see the prompts, rubrics, scoring code, aggregation method, excluded cases, and examples?

Can someone reproduce the headline table, or at least audit the path from raw observations to conclusion?

Not every project can release everything. Privacy, safety, and licensing can matter.

But the more consequential the claim, the more important it is to expose the method.

A result with no receipts may still be interesting.

It just deserves less trust than a result whose evidence trail can be checked.

## Scene 8 — The checklist in one pass

Here is the checklist in one pass.

One: what exactly was tested?

Two: what is the measurement?

Three: is the claim observational or causal?

Four: where does the average break?

Five: how uncertain is it?

And underneath all five: are there receipts?

The goal is not to reject every AI evaluation claim.

The goal is to match trust to evidence.

A small demo can inspire a question.

A careful benchmark can support a product choice.

A causal, replicated, well-documented study can support a stronger conclusion.

Those are different weights.

## Scene 9 — Close

AI evaluation is becoming part of how people choose tools, ship products, and make decisions.

That makes the quality of the evidence matter.

The next time you see a clean chart or a confident headline, do not only ask: what number won?

Ask: what was tested, what was measured, what was controlled, what was hidden by the average, how uncertain is it, and can I inspect the trail?

A trustworthy claim does not ask you to admire the number.

It helps you understand what the number is allowed to mean.
