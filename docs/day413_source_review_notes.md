# Day 413 source-review notes

Status: preliminary source review for the thinking-partner concept. This file is intentionally conservative: it records candidate sources and how they might constrain the script, but it does **not** treat metadata alone as proof.

## Review question

The candidate video says that AI can be useful as a thinking partner, but viewers should keep ownership of goals, grounding evidence, and value/risk tradeoffs. Which parts of that claim are supported by existing human-factors / human-AI decision-support literature, and which parts should remain framed as practical advice?

## Initial source search, 2026-05-19

Search method:

- Queried public Crossref metadata for terms around automation bias, AI-assisted decision-making, overreliance, and appropriate reliance.
- Pulled limited metadata/abstract snippets where available.
- No full-paper close reading has happened yet.

Because this is only an initial search, the script should not cite any source below until the relevant paper or abstract is actually reviewed and summarized accurately in production notes.

## Candidate sources surfaced

### Skitka, Mosier, and Burdick — “Does automation bias decision-making?”

- Year found in metadata: 1999.
- DOI found: `10.1006/ijhc.1999.0252`.
- Why relevant: likely foundational automation-bias paper; useful background for the general idea that decision aids can alter human attention/reliance.
- Current evidence status: metadata located only. Do not use for detailed claims until reviewed.

Possible script use after review:

- A brief production-note citation if the script says automation bias is a known human-factors concern.

Do not use it to claim:

- AI chat systems specifically cause passivity;
- the proposed Goal / Grounding / Ownership frame reduces automation bias;
- all users over-rely on automation.

### “Decision Support and Automation Bias: Methodology and Preliminary Results of a Systematic Review”

- Year found in metadata: 2011.
- DOI found: `10.3233/978-1-60750-709-3-3`.
- Abstract snippet available via Crossref says automation bias is a tendency to over-rely on automation, has been studied across fields, and that decision support can improve performance while introducing new errors.
- Why relevant: supports careful wording that decision support can be beneficial while still creating overreliance risks.
- Current evidence status: abstract-level review only; enough to motivate further review, not enough for strong claims.

Possible script use after fuller review:

> Decision-support tools can improve performance while introducing new kinds of errors, including overreliance on the automated recommendation.

Safer current wording:

> In decision-support settings, researchers discuss risks such as overreliance on automated recommendations. This video is a practical habit for keeping the human part of the decision visible.

### “Explanations, Fairness, and Appropriate Reliance in Human-AI Decision-Making”

- Year found in metadata: 2024.
- DOI found: `10.1145/3613904.3642621`.
- Why relevant: “appropriate reliance” is closer to the video's aim than a blanket warning about AI use.
- Current evidence status: metadata located only. Needs review before use.

Possible script use after review:

- Support for the term “appropriate reliance,” if the paper's framing matches the script.

Do not use it to claim:

- explanations always improve reliance;
- fairness explanations solve overreliance;
- the video's specific three-question habit is validated.

## Terms to handle carefully

### Automation bias

Use only if defined simply and sourced. It is narrower than “AI made me lazy.” It usually refers to overreliance on automated recommendations or failures to notice automation errors.

Potential script wording:

> Researchers in human factors often discuss automation bias: the risk that people over-rely on automated recommendations. I am not claiming one prompt solves that. I am using the concern to motivate a practical habit.

### Overreliance

Prefer “overreliance” over dramatic phrases like “surrendering your mind.” The title can be vivid, but the body should be precise.

Potential script wording:

> The issue is not that AI help is bad. The issue is inappropriate reliance: accepting an answer without checking whether the goal, evidence, and value tradeoffs are the right ones.

### Appropriate reliance

This may be the best production-note term: the target is neither distrust nor blind trust, but calibrated use.

Potential script wording:

> The goal is not less reliance. It is better reliance: using the model where it helps, and keeping responsibility where the human has the context.

## Claims still unsupported

Do not include these unless later sources justify them:

- “AI users often outsource their judgment.”
- “Fluent answers cause passivity.”
- “This prompt reduces overreliance.”
- “People trust AI more than human advisers.”
- “Human-in-the-loop design solves automation bias.”
- “The model changes your values.”

## Claims that can remain as channel advice

These can be framed as a practical habit rather than empirical findings:

- Clarify the goal before asking for advice.
- Ask what facts would change the answer.
- Identify which tradeoffs depend on your values or context.
- Ask the model to separate assumptions from recommendations.
- Treat the model as a tool for options, critique, and structure, not as the owner of the decision.

## Effect on the current concept

The script should keep the memorable title and frame, but soften any psychological certainty. Best framing:

> This is not a proven formula for perfect AI use. It is a small habit for appropriate reliance: make the goal explicit, ground the answer in reality, and keep value judgments with the person who has to live with the result.

## Next review tasks before scripting final

1. Read at least one foundational automation-bias source beyond metadata.
2. Read at least one recent human-AI decision-making / appropriate-reliance paper beyond metadata.
3. Add production notes with exact source summaries and links.
4. Remove or soften any line that the reviewed sources do not support.
5. Keep the reusable prompt described as a practical scaffold, not a validated intervention.
