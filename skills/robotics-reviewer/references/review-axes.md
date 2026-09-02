# Review axes

## Venue-first routing

Start with the target venue and track. Build a current policy packet from material supplied by the
user or official pages verified at runtime. Do not assume that a conference, journal, workshop, or
special issue shares another venue's rubric.

Record:

- venue, track, and policy edition or year;
- official author, reviewer, ethics, reproducibility, and supplementary-material sources used;
- verification or access date;
- policy gaps that remain unverified.

Map each official criterion to the generic axes below. Preserve the venue's own labels in the final
assessment when verified. If no current official rubric is available, label the review as generic
and do not fabricate venue-specific rules.

## Generic scholarly axes

- `contribution-and-novelty`
  - Is the claimed advance clear and distinguished from the closest relevant work?
  - Are improvements attributable to the proposed contribution rather than more data, compute,
    pretraining, tuning, or favorable evaluation?
- `technical-validity`
  - Do the method, assumptions, system design, and analysis support the central claims?
  - Are leakage, contamination, confounding, statistical dependence, and invalid comparisons
    controlled?
- `empirical-evidence`
  - Are baselines matched, ablations isolating, metrics appropriate, and uncertainty visible?
  - Does evaluation cover the environments, tasks, embodiments, and operating conditions implied
    by the claims?
- `generalization-and-deployment`
  - Are out-of-distribution, cross-dataset, sim-to-real, cross-robot, or cross-embodiment claims
    directly tested at the claimed scope?
  - Are latency, control rate, compute budget, failures, interventions, and safety reported when
    deployment is part of the contribution?
- `reproducibility-and-transparency`
  - Are code, data, checkpoints, prompts, configurations, hardware, seeds, evaluation protocols,
    and implementation details sufficiently specified for scrutiny?
- `significance-and-fit`
  - Is the contribution important for the target community and aligned with the verified venue
    remit?
  - Keep venue-fit judgment separate from technical validity.
- `clarity-and-presentation`
  - Can readers trace claims to methods, experiments, figures, tables, and limitations?
  - Are definitions, units, metrics, uncertainty, and system boundaries consistent?

## Venue mapping rules

- Do not turn a generic axis into an official venue requirement unless the policy packet supports
  that mapping.
- Distinguish a manuscript weakness from a policy violation.
- Treat current venue checklists as evidence requirements, not as proof of scientific quality.
- Do not infer scoring scales, acceptance thresholds, rebuttal opportunities, anonymity rules, or
  supplementary-material permissions from past editions.
- When official sources disagree, flag the conflict and prefer the current venue page or
  user-supplied authoritative packet. Do not silently resolve ambiguity.

## Weighting guidance for three reports

Assign these emphasis briefs before any reviewer receives the manuscript.

- `Reviewer 1` usually foregrounds technical validity, evaluation integrity, statistical
  independence, and claim-evidence alignment.
- `Reviewer 2` usually foregrounds novelty, matched baselines, ablations, reproducibility, and
  significance for the target community.
- `Reviewer 3` usually foregrounds generalization, embodied or systems evidence, failure and
  safety analysis, clarity, and verified venue fit.
- All reviewers still assess every applicable venue criterion. Emphasis changes weight, not access
  to evidence or scope.

These are analytical lenses, not invented reviewer identities or specialties.

## Missing-evidence handling

- If manuscript or policy material is incomplete, do not infer absent validation or requirements.
- Use explicit markers such as `Not assessable from provided material`,
  `AUTHOR_INPUT_NEEDED`, or `Current venue policy not verified`.
- A missing policy source limits venue-fit confidence. It is not itself a manuscript defect.
