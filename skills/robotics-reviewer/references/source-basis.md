# Source basis

## Authoritative sources

Venue requirements change. Establish the policy basis for every venue-aware review at runtime.

Use sources in this order:

1. current official venue policy documents supplied by the user;
2. current official venue pages verified during the task;
3. an official archived edition that exactly matches the submission cycle;
4. the generic scholarly axes in this skill, clearly labeled as non-venue-specific.

Record the venue, track, policy year or edition, source URLs or supplied filenames, access date,
and any unresolved gaps. User notes about preferences or lab practice may guide emphasis but must
not be represented as official venue policy.

## Policy packet

Include only verified, relevant material:

- scope and contribution criteria;
- reviewer rubric or assessment questions;
- anonymity and conflict-of-interest rules when they affect the review;
- ethics, responsible research, data, code, model, or reproducibility requirements;
- manuscript and supplementary-material rules that affect whether evidence is reviewable;
- track-specific requirements.

Do not hardcode or rely on memory for deadlines, page limits, scoring scales, acceptance
thresholds, rebuttal rules, code-release requirements, or supplementary-material permissions.

The bundled `editorial criteria and processes.md` is a local Nature reference. Load it only when
Nature is the target venue or the user explicitly asks for a Nature-style assessment. It is not
authority for robotics, ML, CV, NLP, or embodied-AI venues.

## Manuscript evidence basis

Reviewers may use only:

- manuscript, supplement, figures, tables, appendices, and author notes supplied by the user;
- code, data, logs, or artifacts the user explicitly places in scope;
- verified source anchors extracted from those materials;
- the shared policy packet.

Distinguish what is supported, weak, missing, and not assessable. Do not infer an absent
experiment, implementation detail, citation, dataset property, or venue requirement.

## Conservative implementation choices

- The default package contains three mutually blind reports plus a post-review synthesis. This is
  a workflow choice, not a claim about the target venue's actual review process.
- Every reviewer receives the same immutable manuscript and policy packet. Reviewers differ only
  by preassigned emphasis.
- Reviewer identities, institutions, seniority, and specialties are never invented.
- Every substantive concern has a claim pointer, evidence pointer, severity, and resolution test.
- The technical taxonomy and domain gates are internal coverage aids. They are not official venue
  taxonomies and must not manufacture concerns.
- Consensus is computed only after all reports are frozen and requires at least two independently
  raised concerns mapping to the same underlying issue.
- A recommendation posture is a simulated reviewer judgment, not an editorial decision or
  predicted acceptance probability.

## Unverified-policy fallback

If current policy cannot be supplied or verified:

- label the review `generic rubric; venue policy unverified`;
- omit claims about compliance, scoring, fit, or formal submission requirements;
- still assess the manuscript using the generic axes and claim-dependent technical gates;
- state what official material would be needed for a venue-specific pass.
