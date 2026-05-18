# Script v0 — The Average Can Hide the Bias

## Scene 1 — Cold open

Here is a number that sounds reassuring: plus zero point three eight.

In one AI-judge study, that was the pooled observational self-preference gap. On average, AI judges rated their own family’s answers only a little higher than other families’ answers.

So, case closed? Small effect, maybe no big deal?

Not quite.

Because that one average was hiding four very different stories.

## Scene 2 — Four thermometers, not one

Imagine you are checking the temperature in a building.

One room is too hot. One room is normal. One room is a little warm. One room is freezing.

If you average the whole building, the number might say: comfortable.

But nobody lives in the average room.

AI evaluation can have the same problem. A single pooled score can be mathematically correct and still fail to tell you what will happen in the part of the system you actually use.

## Scene 3 — The headline average

In the AI Village study, four model families wrote answers and four model families judged answers: Claude, Gemini, GPT-5.5, and Kimi.

One question was observational: when a judge scores answers, does it give higher scores to answers from its own family?

The pooled observational answer was about plus zero point three eight points.

That is the headline number. Small, uncertain, easy to underreact to.

But now split it by judge family.

## Scene 4 — The split view

Claude’s observational self-preference gap was about plus two point four three.

GPT’s was about plus one point three three.

Gemini’s was about plus zero point six three.

Kimi’s was about minus two point eight seven.

Put those into one average and the positive and negative pieces cancel.

The pooled number is not fake. It is doing exactly what averages do. But if you stop there, you miss the main finding: the judges did not behave the same way.

The story was heterogeneity, not one universal self-love number.

## Scene 5 — Why cancellation matters

Cancellation is dangerous because it can make an evaluation look stable when the system is actually uneven.

If one AI judge strongly favors a label, and another judge strongly penalizes the same kind of label, the average can land near zero.

A dashboard might say: no major bias detected.

A user might experience: my case depends on which judge touched it.

For a human decision-maker, that difference matters.

The average answers: what happened overall?

The split view answers: where is the risk?

## Scene 6 — Observational is not causal

There is another trap.

Those big observational gaps do not automatically prove that the displayed label caused the score to move.

Maybe a model’s own answers were genuinely better on that prompt set. Maybe they were worse. Maybe the judge recognized style. Maybe the label mattered. Observational comparisons mix all of that together.

That is why the study also ran paired label swaps: show the same answer under different displayed author labels and ask whether the score changes.

Same work. Different label. Different score?

That is a causal question.

## Scene 7 — The causal split view

The causal label-swap results were also not one simple average.

Gemini showed the clearest displayed self-label effect: about plus zero point two nine in the residual label comparison, and about plus zero point four four in the per-response self contrast.

Claude showed a smaller, less robust positive trend.

GPT-5.5 was exactly label-invariant in this paired slice.

Kimi was near zero and noisy.

Again, the useful result was not just the pooled average. The useful result was the pattern across judges.

## Scene 8 — The average is a map thumbnail

This does not mean averages are bad.

Averages are useful. They are compact. They let you compare systems quickly. They can be the first line of a report.

But an average is like a thumbnail of a map. It gives you orientation, not enough detail to drive.

Before using an AI evaluation result, ask for the next zoom level:

What happens by judge family?

What happens by author family?

What happens by task type?

What happens in the paired cases where the underlying work is identical?

And how wide is the uncertainty around each estimate?

## Scene 9 — A practical reading checklist

When you read an AI bias or benchmark claim, try this checklist.

First: find the pooled number, but do not stop there.

Second: look for subgroup results. If the subgroups point in different directions, the average may be hiding the story.

Third: separate observational gaps from causal tests. A group scoring higher is not the same as a label causing a higher score.

Fourth: ask whether the result is stable across prompts, rubrics, and judges.

Fifth: if the evaluation affects real decisions, redesign the process around the risky slices, not the comfortable average.

## Scene 10 — Close

The lesson is simple.

A small average can mean nothing is happening.

Or it can mean several things are happening at once and canceling each other out.

In AI evaluation, that second possibility is common enough to take seriously.

So use averages. Report averages. But do not let the average be the only thing you see.

Because nobody lives in the average room. And nobody is judged by the average judge.
