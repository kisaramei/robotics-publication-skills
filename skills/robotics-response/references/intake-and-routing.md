# Intake and routing

## Contents

- [Publication route](#publication-route)
- [Journal-only decision-type gate](#journal-only-decision-type-gate)
- [Task modes](#task-modes)
- [Readiness states](#readiness-states)
- [Editor instruction handling](#editor-instruction-handling)
- [Pasted editorial email handling](#pasted-editorial-email-handling)
- [Minimum information by output type](#minimum-information-by-output-type)
- [Clarifying question rules](#clarifying-question-rules)
- [Routing shortcuts](#routing-shortcuts)


Use this file before splitting comments or drafting prose. Its job is to decide what task the
user is asking for, whether the supplied information is enough, and what output state is honest.

## Publication route

Select one route before drafting:

- `journal-revision` for post-decision revision packages, marked manuscripts, revision cover
  letters, and point-by-point journal correspondence;
- `conference-rebuttal` for a bounded author-response window before the final conference
  decision.

If a conference route is selected, load `conference-rebuttal.md`, verify the current venue/year
rules, and skip the Major/Minor gate. If the route is unclear and the requested output depends on
it, ask whether this is a journal revision or conference author response.

## Journal-only decision-type gate

For journal work, resolve the editorial decision only when it affects the requested strategy or
deliverable. Use the supplied letter and explicit author statements already in context first.

- If an editor letter explicitly says `Major Revision` or `Minor Revision`, use that value and do
  not ask a redundant question.
- If the user explicitly says 大修、小修, major review, minor review, major revision, or minor
  revision, normalize it to the corresponding revision type.
- If neither source resolves it and the task does not depend on the label, use
  `decision type: unknown` and proceed. This includes local `audit`, `revise`, and `triage-only`
  tasks whose wording, evidence checks, or comment classification are independent of the decision.
- If the requested strategy or deliverable does depend on the label, ask one concise question
  explaining the dependency and request the decision type or letter. Defer only the dependent
  work; continue independent analysis or drafting with explicit placeholders for missing facts.
- Never guess from the number or apparent difficulty of reviewer comments. Reviewer requests and
  editor instructions can be serious even when the package is labelled Minor Revision.
- `revise-and-resubmit` and `transfer after review` remain distinct decision types; do not force
  either into Major or Minor Revision. Follow the explicit editor instructions for those routes.

When relevant to the task, apply the supplied decision's strategy from `static/core/workflow.md`.
Record the decision type, or `unknown`, when returning a response strategy summary. An unknown
decision does not justify inventing results, manuscript changes, or an editorial instruction.

## Task modes

| Mode | Use when | Minimum useful input | Default output |
|---|---|---|---|
| `draft` | User wants a new point-by-point response package | Reviewer comments plus any author actions or manuscript-change notes | Internal/editor master plus separate reviewer-specific responses with placeholders where needed |
| `audit` | User provides an existing response draft and asks whether it is good enough | Response draft; reviewer comments when available | Findings first, then revised or annotated response sections |
| `revise` | User wants a draft rewritten for tone, traceability, or Nature-style response | Existing draft plus target change request | Revised response text plus changed-risk notes |
| `triage-only` | User wants strategy, action list, or missing inputs before writing prose | Reviewer comments or editor letter | Tracker, action map, missing-input list, no final letter |
| `cover-letter` | User asks for a revision cover letter only | Manuscript metadata plus revision summary or change notes | Concise editor-facing cover letter |
| `revision-package` | User asks for a complete revision package or pastes a decision email and wants the agent to begin | Decision email or reviewer/editor comments plus available author actions | Internal/editor master, reviewer-separated response files, cover letter when useful, change checklist, and placeholders |
| `latex-template` | User asks for LaTeX templates or filled `.tex` files | Desired output type; manuscript metadata if filling templates | Template paths or filled `.tex` content |
| `appeal-like` | User wants to challenge rejection or process rather than revise | Decision letter and disputed points | Route out of default workflow and explain separate appeal handling |
| `conference-rebuttal` | User is in a bounded conference author-response phase | Reviews plus current venue/year rules or their official URL | Rule record, prioritized issue ledger, and one compact response or required platform fields |

If the mode is unclear, infer the safest useful mode. Prefer `triage-only` when drafting would
require many unsupported facts.

## Readiness states

Use one readiness state for each comment and one package-level state:

| State | Meaning | Allowed output |
|---|---|---|
| `ready_to_submit` | Direct answer, supplied action, and traceable manuscript location are all present | Final response wording without unresolved placeholders |
| `draft_with_placeholders` | A useful draft can be written, but visible placeholders remain | Draft wording with bracketed placeholders and risk flags |
| `needs_author_input` | Final text would require facts the user has not supplied | Tracker, questions, partial draft only if placeholders are explicit |
| `blocked` | Ethics, compliance, data integrity, missing central evidence, or appeal-like routing prevents credible revision response | Blocking issue first; do not produce confident final wording |

Do not call a package `ready_to_submit` if any comment remains `draft_with_placeholders`,
`needs_author_input`, or `blocked`.

## Editor instruction handling

When editor instructions are supplied:

- Assign editor-level IDs before reviewer IDs: `E.1`, `E.2`, `E.3`.
- Address editor instructions before Reviewer 1, Reviewer 2, etc.
- If editor instructions conflict with reviewer suggestions, surface the conflict in the strategy summary.
- Treat explicit editor constraints as higher priority than reviewer-level preference.

Example:

```text
E.1: Focus on clarifying the central claim without substantial manuscript expansion.
R1.1: Make the causal claim stronger.
R2.1: Soften unsupported causal language.
```

The response strategy should explain that the editor's constraint and the observational design
support claim softening rather than stronger causal language.

## Pasted editorial email handling

When the user pastes an editorial decision email or revision invitation, do not ask them to
separate the email manually. Start by extracting:

- journal name;
- manuscript title and manuscript ID;
- decision type and revision deadline;
- required files, such as clean manuscript, marked manuscript, response to reviewers, cover letter, graphical abstract, data availability update, or supplementary files;
- editor instructions and portal-specific constraints;
- reviewer-report boundaries and comment numbering.
- reviewer-visibility rules and whether the portal accepts separate reviewer-response files.

Ignore boilerplate only after checking it for required files, deadlines, formatting constraints,
and resubmission instructions. If the email contains reviewer reports, enter `revision-package`
or `draft` mode automatically depending on whether the user requested a full package or only a
response letter. If reviewer boundaries are ambiguous, keep the original ordering visible in the
internal package and flag the ambiguity instead of inventing identities. Do not create outward-facing
reviewer files until their boundaries can be separated safely.

## Minimum information by output type

### Full draft response

Requires:

- reviewer comments or editor comments;
- enough author notes to know which actions were taken;
- manuscript locations or placeholders for claimed changes.

If locations are missing, use section names or bracketed placeholders. Do not invent line numbers.

### Final submission-ready response

Requires:

- all reviewer and editor comments identified;
- all claimed actions supplied by the author;
- traceable locations for every manuscript change;
- real details for experiments, analyses, statistics, citations, figures, tables, supplements, ethics, and data availability.

If any required fact is missing, the output is not `ready_to_submit`.

### Audit

Requires:

- user draft;
- reviewer comments when available.

If reviewer comments are absent, audit only the visible draft and flag that completeness cannot be verified.

## Clarifying question rules

Check existing conversation context and supplied materials first. Usually proceed with placeholders
and risk flags. Ask concise questions only for missing information that changes the requested work:

- the task may be either a journal revision or conference rebuttal and the distinction changes
  the deliverable;
- the journal decision type remains unknown and the requested strategy or deliverable depends on it;
- conference venue/year rules cannot be verified and the user asks for compliant final text;
- the user explicitly asks for final submission-ready text and required facts are missing;
- the draft would otherwise fabricate data, locations, approvals, statistics, citations, or figure panels;
- reviewer boundaries are too ambiguous to assign stable IDs;
- the case appears appeal-like or outside normal revision response.

When asking, group the facts needed for the dependent part of the requested output and explain why
they matter. Continue work that does not depend on the answer. Do not ask about the decision type
merely because it is unknown:

```text
I need three facts before final wording: the validation result summary, the Methods/Results location,
and whether Fig. 5 is a main or supplementary figure.
```

## Routing shortcuts

- Vague author note such as "we fixed it" -> `needs_author_input`.
- Existing response with hostile language -> `audit` or `revise`.
- Reviewer asks for impossible new work -> normal revision mode with `PARTIAL` or `OUT_OF_SCOPE`, not appeal.
- Rejection challenge -> `appeal-like`.
- User asks only "what should we do?" -> `triage-only`.
- Pasted decision/revision email with reviewer reports -> auto-parse the email and begin `draft` or `revision-package`; do not wait for the user to reformat the email.
- Conference author-response notice or reviews -> select `conference-rebuttal`, skip the
  Major/Minor gate, and load `conference-rebuttal.md`.
