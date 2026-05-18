# Viewer FAQ: what this series is — and is not — claiming

## Are you saying AI judges are useless?

No. The study found meaningful shared quality signal across judges. The warning is narrower: if irrelevant labels or presentation details can move a score, then an evaluation needs safeguards before it is used for a serious decision.

A better conclusion is: AI judges can be useful measurement tools, but they should be audited like measurement tools.

## Are you saying every model favors itself?

No. The first study result is heterogeneity, not a universal self-preference law.

In the observational data, some judge families showed positive self-gaps while Kimi showed a large negative self-gap on this prompt set. In the paired label-swap slice, Gemini showed the clearest displayed-self-label boost, while GPT-5.5 was label-invariant in that paired slice.

## Does the Kimi result mean Kimi is generally worse?

No. The Kimi observational self-penalty was strongly confounded by the quality of Kimi-authored answers on this particular prompt set. It should not be generalized into a broad claim about Kimi in all tasks.

The careful wording is: in this study's prompt set, Kimi-authored responses were often scored lower by other judges, and that quality pattern explains much of the observational self-penalty.

## Why separate observational gaps from causal label swaps?

Because they answer different questions.

- An **observational gap** asks: in the data as collected, did a judge score one group differently?
- A **causal label-swap test** asks: if the answer stays the same and only the displayed label changes, does the score move?

The first can reveal a pattern. The second is closer to evidence that the label itself mattered.

## If labels matter, should we always hide them?

Often, yes — especially when authorship is irrelevant to the decision. But hiding labels is not the whole solution.

You still need a clear rubric, balanced examples, threshold checks, uncertainty, and audits for hidden proxies. A model may infer style, task source, or other signals even when the literal label is removed.

## Why focus on thresholds?

A small average score shift can be practically important if it moves a borderline case across a decision boundary. A change from 5.8 to 6.2 may matter more than a change from 9.4 to 9.8 if the decision threshold is 6.0.

That is why the series emphasizes where the bias appears, not just how large it is on average.

## What receipts should I expect from a trustworthy evaluation claim?

At minimum, look for:

1. the task population;
2. the scoring rubric;
3. examples of scored items;
4. who or what judged them;
5. aggregation choices;
6. uncertainty or robustness checks;
7. subgroup or slice results;
8. code, prompts, or enough procedural detail to reproduce the claim.

No single missing receipt automatically makes a claim false. But missing receipts should lower how much weight you put on it.

## Why make videos instead of only publishing the repo?

Most people encounter evaluation claims as summaries, leaderboards, or headlines. The videos translate the repo into reusable habits: separate observational from causal, inspect averages, ask for receipts, and test whether labels move scores.

The repo remains the source of record; the videos are an explanation layer.
