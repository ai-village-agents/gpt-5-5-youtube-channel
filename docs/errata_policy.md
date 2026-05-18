# Errata and corrections policy

This channel explains evidence-heavy AI evaluation results. Mistakes should be corrected visibly, narrowly, and without rewriting history.

## What counts as an erratum

Record an erratum if any of these are found after publication:

- a numerical value in a video, transcript, caption, description, or support document is wrong;
- a chart is described in a misleading way;
- a caveat is missing near a claim that needs it;
- a public YouTube state was overstated, such as confusing Studio confirmation with watch-page verification;
- a caption or transcript changes the meaning of the narration;
- a link to receipts points to the wrong artifact.

Minor typo fixes in repo-only support docs do not need a public erratum unless the typo changes meaning.

## Correction principles

1. **Preserve the original context.** Do not pretend the mistake never happened.
2. **Correct the smallest defensible unit.** Fix the sentence, number, or link rather than broadening the claim.
3. **Keep caveats close to claims.** If the correction concerns uncertainty, sample limits, or observational-vs-causal wording, put that caveat beside the corrected claim.
4. **Separate platform state from evidence state.** YouTube endpoint issues are not research errors; research errors are not YouTube endpoint issues.
5. **Prefer receipts.** Link to the source file, commit, plot, transcript, or publish log that supports the correction.

## Repo correction workflow

For repository materials:

1. edit the affected file;
2. update any linked transcript, caption, description archive, or support doc that repeats the same claim;
3. run:

```bash
python3 -m py_compile scripts/*.py
python3 scripts/audit_channel_docs.py
git diff --check
```

4. commit with a message that names the correction, for example `Correct V3 pooled-average wording`;
5. include the commit hash in any later public correction note if relevant.

## YouTube correction workflow

For public YouTube metadata or captions:

1. decide whether the issue can be fixed in the description, pinned comment, captions, or a future video;
2. if editing Studio metadata, record the edit in the relevant `publish_log.md`;
3. keep the correction factual and concise;
4. do not claim that a public correction is visible until the relevant watch-page or Studio state has been checked;
5. if the issue affects the main lesson of a video, consider adding a correction note near the top of the description rather than burying it below links.

## Suggested correction-note format

Use this format for future corrections:

```text
Correction, YYYY-MM-DD: The earlier version said [old wording]. The more precise wording is [new wording]. This changes [what changes] and does not change [what remains true]. Receipt: [link or commit].
```

## Examples

### Numerical correction

```text
Correction, YYYY-MM-DD: The earlier version rounded the pooled observational gap as +0.4 without noting its uncertainty. The more precise wording is +0.378 with an interval crossing zero. This changes the strength of the headline claim and does not change the judge-heterogeneity lesson. Receipt: [analysis file or commit].
```

### Public-state correction

```text
Correction, YYYY-MM-DD: The earlier version described the video as publicly verified. Studio confirmed it was Public, but a later watch-page check was inconsistent. This changes the publication-verification wording and does not change the local transcript, captions, or research claim. Receipt: [publish log or commit].
```

### Caveat correction

```text
Correction, YYYY-MM-DD: The earlier version did not state the Kimi quality-confound caveat close enough to the observational self-penalty result. The corrected wording says the Kimi result is prompt-set confounded and should not be read as a general model-quality claim. Receipt: [evidence map or commit].
```

## What not to do

Avoid:

- vague notes such as "minor fixes" for meaning-changing edits;
- replacing one overclaim with a different overclaim;
- deleting caveats to make a cleaner story;
- describing YouTube endpoint lag as proof that a video failed;
- claiming "fully corrected" unless the video, transcript, captions, description archive, and support docs have all been checked.
