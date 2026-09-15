---
name: robotics-response
description: >-
  Draft, audit, or revise peer-review responses for robotics, computer vision, and
  machine-learning papers. Route explicitly between journal revision packages and
  time-bounded conference author responses or rebuttals for venues such as ICRA, CoRL,
  CVPR, NeurIPS, and ICLR. For journals, prepare reviewer-separated point-by-point letters,
  revision cover letters, marked-manuscript excerpts, and LaTeX packages. For conferences,
  verify the current venue/year rules and produce one compact, evidence-grounded response
  within the allowed word or character budget. Use for reviewer comments, editor decision
  letters, author response, rebuttal, revision packages, 修回信, 审稿意见回复, 逐点回复,
  大修回复, 小修回复, 会议 rebuttal, 作者回复, or 标红修改. Do not use for
  pre-submission simulated review.
---

# Robotics Publication Response — Router

This skill is split into two layers:

- A **static layer** under `static/` that holds versioned, reusable content fragments (the default stance and red lines, and the response workflow with output format).
- A **dynamic layer** (this file plus `manifest.yaml`) that loads the core every time and reaches for the deeper response references or templates only when a step needs them.

Do not try to apply the response logic from memory or from this router. Always load fragments from disk as described below.

## Routing protocol

Follow these four steps every time the skill is invoked.

### 1. Load the manifest and the core layer

Read [manifest.yaml](manifest.yaml). Then read every file listed under `always_load`:

- `static/core/stance.md` — the editor-facing purpose, the default stance, the red lines, and the source hierarchy that apply to every response job.
- `static/core/workflow.md` — accepted inputs, the revision correspondence workflow, and the output package format.

### 2. Select the publication route before drafting

Choose exactly one publication route:

- **`journal-revision`**: a journal editor has invited a revision, or the user needs a
  point-by-point revision package, marked manuscript, or revision cover letter.
- **`conference-rebuttal`**: a conference provides a bounded author-response or rebuttal
  window before the final decision, normally with venue/year-specific limits.

If the input does not establish the route and the distinction changes the deliverable, ask one
concise question. Do not treat every use of the word "rebuttal" as a journal revision.

Then identify the runtime variation:

- **task mode** — `draft` / `audit` / `revise` / `triage-only` / `cover-letter` / `revision-package` / `latex-template` / `appeal-like`.
- **decision type** — for `journal-revision` only: minor revision, major revision,
  revise-and-resubmit, transfer after review, or unclear.
- **venue rules** — for `conference-rebuttal` only: venue, year, official rule source,
  deadline/time zone, response budget and counting method, visibility, permitted changes,
  and submission constraints.
- **user language** — if the user writes Chinese, also produce the 中文核对 block.

The Major/Minor (`Major Revision` / `Minor Revision`) decision gate applies only when the requested `journal-revision` strategy or
deliverable depends on the decision type. First use the editor letter or an explicit author
statement already in context. If the decision remains unknown and changes the requested work,
ask one concise question and defer only the dependent part. Local `audit`, `revise`, and
`triage-only` work can proceed with `decision type: unknown` when the label does not affect it.
Never infer the decision from comment count or tone, or fill missing evidence with invented
results. **Skip this gate entirely for `conference-rebuttal`.** Instead, load
[references/conference-rebuttal.md](references/conference-rebuttal.md) and verify the current
venue/year rules from an official source before claiming that a response satisfies them. If
verification is unavailable, ask the user for the official instructions or URL. Triage may
continue, but final budget/compliance claims may not.

Use `references/intake-and-routing.md` to fix the task mode, minimum inputs, and readiness state before drafting. Route appeal-like cases separately; do not draft an appeal as the default path.

### 3. Run the workflow

Follow `static/core/workflow.md` and the selected route:

- For `journal-revision`, apply the workflow to the requested task: parse any supplied decision
  letter, resolve the decision type when the strategy depends on it, classify editor and reviewer items, build an internal
  tracker, prepare privacy-filtered reviewer-specific responses, map real changes to manuscript
  locations, and add cover-letter, marked-manuscript, or LaTeX deliverables when requested or
  required.
- For `conference-rebuttal`, apply the verified current rules, retain the platform's reviewer
  and AC/meta-reviewer identifiers, rank decision-critical issues before minor clarifications,
  and draft one compact author response within the verified budget. Do not create a cover
  letter, redline, or revision package unless the current rules explicitly require or permit it.
  Do not state or promise that an experiment, analysis, citation, figure, release, or manuscript
  change will be completed when it has not been performed and verified. Use current evidence,
  correct a factual misunderstanding, narrow a claim, or state a limitation instead.

In either route, when a reviewer missed material already present in the manuscript, treat that
as a clarity signal rather than rebuking the reviewer. Classify each item by response action and
independently verified work status, flag missing author input, run QA, and derive readiness from
the per-item statuses and blocking state.

Whenever a response proposes or performs a manuscript main-text edit, also load
`../nature-shared/core/main-text-discipline.md`. Answer the reviewer completely
in the letter, but keep the manuscript change to the shortest text needed for
the reader. Prefer replacement or compression over appending, and route
non-central robustness or reconciliation detail to SI unless it changes the
central interpretation.

Never invent experiments, citations, line numbers, figure panels, supplementary items, editor instructions, or manuscript changes. Mark anything the author must supply as `AUTHOR_INPUT_NEEDED`.

### 4. Reach for references only when needed

The files under `references/` and `templates/` are deep resources, not defaults. Open them on demand per the `references.on_demand` table in the manifest. In particular, load
`references/conference-rebuttal.md` for every conference route,
`references/comment-taxonomy.md` to classify comments, `references/action-mapping.md` for
tracker fields, `references/tone-and-stance.md` for disagreement wording,
`references/difficult-cases.md` for impossible experiments, conflicts, or appeal-like cases,
`references/chinese-author-alignment.md` for Chinese author notes,
`references/latex-templates.md` for journal `.tex` outputs,
`../nature-shared/core/main-text-discipline.md` for reviewer-driven manuscript additions,
`references/package-consistency-audit.md` for a journal package edited alongside the manuscript,
and `references/qa-checklist.md` before finalizing.

`qa-checklist.md` and `package-consistency-audit.md` are complementary and both apply to a final package: the first asks whether the response is complete, honest, and well-toned; the second asks whether the marked manuscript, the clean manuscript, and the letter agree. For a LaTeX package, run `scripts/check_package_consistency.py` after the first complete draft, after a batch of related edits affecting package consistency, and before delivery. Synchronize affected quotes within the batch and recheck locations when pagination or numbering may change. Complete the full compilation and consistency checks before delivery; a passing check on unchanged files remains valid. Stop once checks pass and no new edit, failed check, or unresolved issue requires follow-up.

## Why this split

- The static layer is versioned and reviewable; the core stays small for a normal response.
- The dynamic layer keeps each invocation cheap: the difficult-case, taxonomy, and QA depth load only when a step needs them.
- The router itself is short on purpose. Update fragments and references, not this file, when adding scope.
- The separate conference reference keeps current, venue-specific checks out of the journal
  revision path until they are needed.
