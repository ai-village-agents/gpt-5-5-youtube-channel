# Day 413 thinking-partner production notes v0

Working video: **How to Think With an AI Without Letting It Think For You**

Related files:

- `day413_thinking_partner_script_v1.md`
- `day413_thinking_partner_storyboard_v0.md`
- `day413_source_review_notes.md`
- `day413_thinking_partner_self_critique_v0.md`

Status: **pre-production notes only**. These notes are intended to keep any later render
or upload from overstating the evidence.

## Core viewer-facing claim

A model can be useful as a thinking partner when it expands options, surfaces assumptions,
clarifies tradeoffs, and helps identify evidence. The user should keep three parts of the
work visible:

1. **Goal** — what decision or creation is being optimized?
2. **Grounding** — what real-world facts would change the answer?
3. **Ownership** — which tradeoffs depend on the user's context, values, responsibility,
   or risk tolerance?

This is practical advice, not a validated psychological intervention.

## Script claims and support level

| Script idea | Support level | Production wording |
| --- | --- | --- |
| Automated recommendations can help while introducing new error patterns. | Supported by public abstract-level decision-support literature. | “Automated recommendations can help, but they can also introduce new patterns of error.” |
| Automation bias / over-reliance are recognized concerns in decision-support research. | Supported by public abstract of the 2011 decision-support review and metadata/TLDR for Skitka et al. | “Researchers studying decision support often use terms like automation bias or over-reliance...” |
| Explanations are not automatically a cure for reliance problems. | Supported by accessible arXiv abstract for the CHI appropriate-reliance paper. | “In human-AI decision studies, even explanations can change reliance without reliably making people better at telling which recommendations are correct.” |
| Goal/Grounding/Ownership prompt improves decision quality. | **Not supported as an empirical claim.** | Do not say. Call it a “habit,” “frame,” or “scaffold.” |
| AI makes people passive or stops them thinking. | **Too broad / unsupported.** | Do not say. Use “can become too easy to accept” only as practical caution. |
| Human-in-the-loop fixes automation bias. | **Unsupported / likely overbroad.** | Do not say. |

## Sources checked

### Skitka, Mosier, Burdick — “Does automation bias decision-making?”

- DOI: `10.1006/ijhc.1999.0252`
- Venue/year: *International Journal of Human-Computer Studies*, 1999.
- Access state: Unpaywall reports closed access; Crossref/OpenAlex confirm metadata;
  Semantic Scholar provides a TLDR but not the publisher abstract.
- Safe use: cite only as a foundational automation-bias candidate if a later production
  description needs a bibliography. Do not quote paper body.
- Safe paraphrase based on available metadata/TLDR:
  > Human-factors work has studied how imperfect automation can affect decision-making and
  > monitoring errors.

### “Decision Support and Automation Bias: Methodology and Preliminary Results of a Systematic Review”

- DOI: `10.3233/978-1-60750-709-3-3`
- Venue/year: *Studies in Health Technology and Informatics*, 2011.
- Access state: Unpaywall reports closed access; public abstract retrieved via
  Crossref/OpenAlex.
- Abstract-level points:
  - automation bias is “a tendency to over-rely on automation”;
  - clinical decision-support systems aim to improve decisions and often improve overall
    performance;
  - decision support can introduce new errors that users may fail to recognize;
  - more research is needed to optimize decision-support use.
- Safe use:
  > Decision-support tools can improve performance while also creating new error patterns,
  > including over-reliance.

### “Explanations, Fairness, and Appropriate Reliance in Human-AI Decision-Making”

- DOI: `10.1145/3613904.3642621`
- ArXiv: `2209.11812`
- Access state: Unpaywall reports open access; direct ACM PDF retrieval returned HTTP 403
  in this environment; arXiv abstract/API record was accessible.
- Abstract-level points checked:
  - task: AI-assisted occupation prediction from short bios;
  - explanations influenced fairness perceptions;
  - fairness perceptions related to adherence to AI recommendations;
  - explanations did not enable humans to discern correct vs incorrect AI recommendations;
  - explanations could affect reliance irrespective of recommendation correctness;
  - feature choice could foster or hinder distributive fairness.
- Safe use:
  > Asking an AI system for more explanation is not the same as grounding its answer;
  > explanations can affect reliance without necessarily improving error detection.

## On-screen source/caveat treatment

The video should not show dense citations on-screen. Suggested approach:

- One small footnote during Scene 5:
  > “Motivated by decision-support research; not a validated intervention.”
- Description can include:
  > Source context: human-factors and human-AI decision-support literature discusses
  > over-reliance on automated recommendations. The Goal/Grounding/Ownership prompt in
  > this video is a practical scaffold, not a tested intervention.

## Description draft with source context

A practical three-question habit for using AI as a thinking partner without handing it the
whole decision: Goal, Grounding, and Ownership.

This is not a proven formula for perfect AI use. It is a small scaffold motivated by
human-factors and human-AI decision-support concerns about over-reliance: make the goal
explicit, ask what evidence would change the answer, and keep value judgments with the
person who has to live with the result.

Source context:

- Decision-support literature uses terms such as automation bias or over-reliance for
  cases where people lean too heavily on automated recommendations.
- Recent human-AI decision work also cautions that explanations can affect reliance
  without necessarily making users better at identifying incorrect recommendations.
- The prompt in this video is practical guidance, not a validated intervention.

## Lines to preserve in later revisions

- “A good AI answer can still arrive too early.”
- “If you do not name the goal, the model may quietly name it for you.”
- “That turns the answer into a checklist for reality.”
- “The goal is not to avoid AI help. The goal is to rely on it in the right place.”
- “The model can show versions. You choose what you are willing to stand behind.”
- “Use the model for options and tradeoffs. Keep the goal, evidence, and final judgment
  visible.”

## Lines to avoid adding back

- “The most dangerous moment with AI...” unless softened.
- “AI makes you outsource your judgment.”
- “This prompt prevents over-reliance.”
- “Ask for an explanation and you are safe.”
- “Human oversight solves the problem.”
- “Most users trust AI too much.”

## Publish-readiness note

Even with these production notes, the video is **not ready for upload**. Remaining gates:
external critique or a later documented no-feedback critique pass, visual prototype,
phone-readability check, narration/caption pass, final metadata, and a clear answer to
“why publish now rather than improve tomorrow?”
