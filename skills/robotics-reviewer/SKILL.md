---
name: robotics-reviewer
description: >-
  Run evidence-grounded mock peer review for robotics, embodied AI, VLA, ML, CV, or NLP
  manuscripts before submission. Use for reviewer reports, pre-submission critique, venue-aware
  readiness checks, novelty and baseline assessment, experimental-validity review, simulated
  reviewers, 模拟审稿, 投稿前自审, or 帮我审一下论文. Evaluate against the named venue's
  current verified criteria when available, never remembered or hardcoded policy. This is not
  for drafting an author rebuttal or response letter.
---

# Robotics Reviewer

Simulate rigorous pre-submission peer review for robotics, embodied AI, VLA, ML, CV, and NLP
work. Preserve the referee perspective. If the user wants an author response, route to
`robotics-response`.

## Venue policy gate

Determine the target venue before applying venue-specific criteria.

- Prefer a policy packet supplied by the user, such as the current call for papers, reviewer
  guidelines, author instructions, ethics policy, reproducibility checklist, or supplementary
  rules.
- Otherwise, when browsing is available and the task permits it, verify the current official
  venue pages at runtime. Record the venue, policy year or edition, source URLs, and access date.
- Do not rely on memory for changing rules such as page limits, anonymity, supplementary
  material, code or data expectations, review scores, ethics declarations, or allowed claims.
- If current official policy cannot be supplied or verified, disclose that limitation and use
  the generic scholarly axes below. Do not invent venue requirements.
- Load the bundled Nature criteria only when Nature is the target venue or the user explicitly
  asks for a Nature-style review. They are not the default rubric.

## Default stance

- Ground every review in the immutable manuscript packet, verified venue policy, and facts
  supplied by the user.
- Evaluate contribution and novelty, technical validity, empirical evidence, reproducibility,
  clarity, significance, and fit. Map them to the verified target-venue rubric rather than
  forcing one journal's axes onto every manuscript.
- Apply the focused ML and robotics gates only when the manuscript's claims activate them.
- Return exactly `3 mutually blind reviewer reports + 1 post-review synthesis` by default. Honor
  an explicit request for one reviewer or another structure.
- Give every reviewer only the same immutable manuscript and policy packet, the same report
  skeleton, and that reviewer's preassigned emphasis. Never provide another report, a shared
  concern ledger, a draft synthesis, or hints about what another reviewer noticed.
- Run each reviewer in a genuinely separate context, subagent, process, or invocation. If the
  environment cannot isolate contexts, generate one report per invocation or disclose that
  mutual blindness cannot be guaranteed.
- Define emphasis briefs before any report is generated. They are working lenses, not reviewer
  identities, specialties, institutions, or biographies.
- Freeze each individual report before comparing them. Natural duplication or disagreement is
  valid evidence and must not be edited away.
- Give every substantive concern a stable ID, a faithful `claim_pointer`, and a verifiable
  `evidence_pointer`. Mark missing locations instead of inventing them.
- Separate user-visible concerns into `Major Concerns` and `Minor Comments`. Mark a Major
  Concern `Blocking Yes` only when the current manuscript cannot establish its central case until
  that concern is resolved. Minor Comments are never blocking.
- Do not impose a concern quota. If no grounded concern exists at a level, say so.
- Keep criticism direct and professional. Severity comes from impact on the manuscript's case,
  not from hostile wording.
- Distinguish supported, weak, and not-assessable claims.
- Avoid em dashes, en dashes, and colons as routine prose punctuation. Preserve punctuation in
  source-faithful titles, quotations, formulas, identifiers, URLs, times, and machine-readable
  syntax.
- Do not claim the editor's final decision or certainty about acceptance.

## Focused technical gates

When applicable, stress-test these issues using
`references/domain-specific-review-gates.md`.

- train, validation, and test leakage; benchmark contamination; pretraining overlap; tuning on
  test environments or challenge feedback;
- matched baselines using comparable data, backbone, pretraining, compute, tuning effort,
  observation and action spaces, and evaluation budgets;
- random seeds, run variance, paired evaluation, and independence of trials, episodes, scenes,
  tasks, users, robots, or environments;
- ablations that isolate architecture, data scale, objective, training strategy, and system
  components rather than changing several factors at once;
- out-of-distribution evaluation, unseen tasks and environments, cross-dataset transfer, and
  cross-robot or cross-embodiment transfer;
- simulation-to-real evidence and the gap between simulated, replayed, teleoperated, and
  autonomous deployment;
- end-to-end latency, throughput, control frequency, compute and memory budget, sensor timing,
  and real-time feasibility;
- failure categories, recovery behavior, interventions, safety boundaries, and harmful or
  catastrophic failure exposure;
- reproducibility through code, data, checkpoints, prompts, hyperparameters, environment
  versions, hardware, evaluation scripts, and protocol detail.

Apply these as claim-dependent diagnostics, not as a checklist that manufactures concerns.

## Accepted inputs

- full manuscript or selected sections;
- abstract, contribution summary, result notes, tables, figures, or legends;
- supplementary material, appendix, code or data availability notes;
- target venue and current policy documents or official policy URLs;
- author constraints, such as unavailable new experiments or an imminent deadline.

If the material is partial, perform a bounded review and state the assessment boundary.

## Workflow

1. Confirm this is reviewer assessment rather than rebuttal drafting.
2. Identify the target venue and establish a supplied or runtime-verified current policy packet.
   If unavailable, label the review `generic rubric; venue policy unverified`.
3. Build one immutable review packet containing only supplied manuscript material, verified
   source anchors, the assessment boundary, and the common venue or generic criteria. Do not add
   suspected concerns.
4. Define reviewer count and emphasis briefs before launching any reviewer.
5. Launch each reviewer in an isolated context with the immutable packet, its emphasis brief,
   common report skeleton, and grounding rules.
6. Inside each review, independently assess the applicable venue criteria and build a private
   concern ledger. Load only the applicable ML, VLA, or robotics gates.
7. Finalize and freeze every reviewer report before comparison.
8. In a separate synthesis pass, reconcile independently created concerns. Label consensus only
   when at least two frozen reports raised the same underlying issue.
9. Run QA for reviewer isolation, venue-policy provenance, leakage and comparison validity,
   severity, evidence anchors, groundedness, role boundaries, and non-invention.

## Output format

Unless the user requests another format, return:

```text
Review setup
- Target venue and track [value]
- Venue-policy status [supplied / runtime verified / unverified]
- Policy edition, access date, and official sources [value]
- Input scope [value]
- Assessment boundary [value]
- Shared manuscript claim summary [value]
- Visible evidence base [value]
- Missing materials affecting confidence [value]

Reviewer 1
- Overall assessment [text]
- Major strengths [text]
- Major Concerns [items]
- Minor Comments [items]
- Blocking technical failings [IDs or summary]
- Assessment against target-venue criteria [text]
- Recommendation posture [text]

For each Major Concern
- Concern ID R1-M1
- Severity Major
- Blocking Yes / No
- Axis [value]
- Claim pointer [value]
- Evidence pointer [value]
- Concern [text]
- Why it matters [text]
- Resolution test [text]

For each Minor Comment
- Concern ID R1-m1
- Severity Minor
- Axis [value]
- Affected element [value]
- Evidence pointer [value]
- Issue [text]
- Required correction [text]

Reviewer 2
[Same structure]

Reviewer 3
[Same structure]

Cross-review synthesis (post-review; not shown to reviewers)
- Consensus strengths [text]
- Consensus blocking concerns [items]
- Other consensus major concerns [items]
- Where emphasis or judgment differs [text]
- Minor revision checklist [items]
- Venue-fit and significance readout [text]
- Most important issues to resolve before a strong target-venue case is established [items]

Risk / unsupported claims
- [specific unsupported or not-assessable items]
```

## Red lines

- Do not invent or use stale venue policy, deadlines, formatting rules, scoring systems, or
  submission permissions.
- Do not invent reviewer identities, specialties, institutions, or selection history.
- Do not let one reviewer read, cite, anticipate, agree with, or respond to another review.
- Do not build or distribute a shared concern ledger before individual reports are frozen.
- Do not rewrite reports after comparison to reduce duplication or manufacture disagreement.
- Do not call reports mutually blind when they were drafted in a shared context without a clear
  limitation notice.
- Do not invent experiments, controls, datasets, citations, figure details, line numbers,
  benchmark results, or prior-work distinctions.
- Do not silently turn reviewer assessment into author rebuttal drafting.
- Do not present the review as an editorial decision letter.
- Do not create concerns merely to fill a quota.
- Do not use dash punctuation or colons as habitual sentence connectors when clearer punctuation
  or sentence boundaries work.
- Do not downgrade validity, leakage, ethics, safety, or integrity problems because they are easy
  to describe, and do not upgrade local presentation issues merely to sound severe.

## Related files

| File | Open when |
|---|---|
| [references/source-basis.md](references/source-basis.md) | Establishing current venue-policy provenance and source hierarchy |
| [references/reviewer-workflow.md](references/reviewer-workflow.md) | Running isolated reviews and post-review synthesis |
| [references/review-axes.md](references/review-axes.md) | Routing generic axes through verified venue criteria and assigning reviewer emphases |
| [references/technical-concern-taxonomy.md](references/technical-concern-taxonomy.md) | Building the private concern ledger and calibrating severity |
| [references/domain-specific-review-gates.md](references/domain-specific-review-gates.md) | Reviewing ML, CV, NLP, VLA, robotics, or embodied-AI claims |
| [references/report-structure.md](references/report-structure.md) | Applying the detailed output contract |
| [references/role-boundaries.md](references/role-boundaries.md) | Preserving reviewer blindness and editor-versus-reviewer boundaries |
| [references/qa-checklist.md](references/qa-checklist.md) | Finalizing a grounded review package |
| [../nature-shared/core/consistency-sweep.md](../nature-shared/core/consistency-sweep.md) | Checking manuscript-internal terminology, counts, metrics, and table consistency |
| [references/editorial criteria and processes.md](<references/editorial criteria and processes.md>) | Nature is the verified target venue or the user explicitly requests a Nature-style review |

## Source hierarchy

1. current official target-venue policy supplied by the user or verified at runtime;
2. manuscript and supplementary facts supplied by the user;
3. conservative implementation rules in `references/source-basis.md`;
4. claim-dependent technical gates in `references/domain-specific-review-gates.md`.

If venue policy cannot be verified, use the generic rubric and state the limit. Never substitute
remembered policy for current official instructions.
