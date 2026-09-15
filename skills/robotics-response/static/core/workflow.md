# Workflow and output format

## Accepted inputs

The skill may receive: pasted editorial decision or revision-invitation email; conference author-response instructions; editor, reviewer, area-chair, or meta-reviewer comments; previous response draft; manuscript change notes; tracked-change summary; line or page numbers; figure, table, and supplement list; author notes in Chinese or English; venue, track, year, article type, manuscript title, author list, manuscript ID, original manuscript text or LaTeX source; requested output format; and portal instructions governing visibility and permitted changes.

If reviewer boundaries or comment segmentation are ambiguous, flag the ambiguity instead of inventing reviewer structure.

## Publication route and decision strategy

Select `journal-revision` or `conference-rebuttal` before drafting. If the route is genuinely
unclear and changes the deliverable, ask one concise question.

For `conference-rebuttal`, load `references/conference-rebuttal.md`, verify the current
venue/year rules, skip the Major/Minor gate below, and use the compact conference output. The
conference reference overrides every journal-specific instruction about reviewer-separated
files, cover letters, redlines, manuscript edits, and LaTeX revision packages.

### Journal-only decision gate

For journal revision-response work, resolve the editorial decision when it affects the requested
strategy or deliverable:

1. Use an explicit label in the editor decision letter, revision invitation, or author statement
   already supplied in context. Do not ask again for a known decision.
2. Normalize informal author wording such as `major review` and `minor review` to `Major Revision`
   and `Minor Revision` when the meaning is unambiguous.
3. If the decision remains unknown, assess whether knowing it changes this task. Local audits,
   wording revisions, and comment triage can proceed with `decision type: unknown` when they do
   not depend on the label. Preserve missing-evidence placeholders and verified work status.
4. If the requested strategy or deliverable does depend on it, ask one concise question explaining
   which part needs the decision letter or explicit decision type. Defer that part and continue
   useful independent work. Keep `revise-and-resubmit` and `transfer after review` distinct;
   follow their explicit editor instructions instead of forcing a Major/Minor classification.
5. Do not infer the decision type from comment count, reviewer tone, requested workload, or the
   apparent severity of individual comments.

When a supplied decision calls for a Major/Minor package strategy, use the corresponding default:

| Decision type | Default revision strategy |
|---|---|
| `Major Revision` | Build an evidence-first work plan. Prioritize central-claim support, experiments or analyses, methods and statistics, validation, figures, limitations, and any structural rewriting. Treat unresolved central evidence or integrity/compliance items as finalization blockers. Responses should explain both the action and the evidence that resolves each concern. |
| `Minor Revision` | Use a bounded correction plan. Prioritize precise wording, definitions, citations, reporting details, figure/table presentation, and localized clarifications. Keep replies concise and avoid unnecessary redesign of the study or expansion of claims unless an editor or reviewer request genuinely requires it. |

The decision label sets the package-level posture, not the severity of every comment. A substantive
evidence, statistics, ethics, or data-integrity concern remains major or blocking even inside a
Minor Revision. Journal instructions and explicit editor directions override these defaults.

## Workflow

1. Select publication route, task mode, and input readiness. Journal modes are `draft`, `audit`,
   `revise`, `triage-only`, `cover-letter`, `revision-package`, `latex-template`, or
   `appeal-like`; conference work uses `conference-rebuttal`, `audit`, or `triage-only`.
2. Parse the supplied decision email, conference reviews, or platform instructions. Extract the
   venue, track, year, manuscript metadata, decision or response stage, official constraints,
   reviewer/chair IDs, deadline and time zone, visibility, and required deliverables.
3. For `journal-revision`, retain any supplied decision and apply the decision gate only to work
   that depends on it. If the decision is missing, independent work can proceed with
   `decision type: unknown`. For
   `conference-rebuttal`, skip that gate, verify the current rules, and follow
   `references/conference-rebuttal.md`.
4. Preserve item-level severity and distinguish verified completed work from planned work.
5. Extract editor instructions first and assign IDs such as `E.1`, then split reviewer comments with IDs such as `R1.1`, `R1.2`, and `R2.1`.
6. Classify each item by category, severity, action label, work status, required input, expected output, finalization-blocking state, package readiness, and risk.
7. Create an internal/editor master strategy and tracker before drafting prose. It may record duplicates and conflicts across reviewers, but label it clearly as not reviewer-facing.
8. In a journal route, treat reviewer reports as mutually blind by default and draft standalone
   privacy-filtered responses unless official instructions require a combined file. In a
   conference route, produce one compact response or the platform's required fields, retain the
   supplied reviewer/chair IDs, and follow verified visibility rules.
9. When reviewers repeat the same concern, answer it fully in every relevant reviewer-specific file. When their requests conflict, reconcile the scientific and manuscript action in the master strategy, then explain the chosen revision independently to each reviewer using only that reviewer's concern and the manuscript evidence.
10. When a reviewer asks about material that already existed in the submitted manuscript, use `CLARIFY_EXISTING` and treat the missed point as a presentation problem. Answer directly, acknowledge that the original wording or placement did not make the point sufficiently clear, make or propose a small clarification, and cite the revised location. Do not say that the reviewer should have seen it or that it was already stated.
11. If explicit current journal or portal instructions require one combined response document, follow that submission requirement and flag its visibility implications. Otherwise default to an editor/internal master plus separate reviewer-specific files. Never silently treat the master tracker as reviewer-facing.
12. Only for a journal `cover-letter` or `revision-package`, draft a concise editor-facing cover
   letter. Do not create one for a conference unless its current rules require it.
13. Map each claimed change to manuscript location, figure, table, supplement, citation, or explicit placeholder. For every main-text edit, load `../../../nature-shared/core/main-text-discipline.md`, classify the result or explanation, and decide whether it belongs in the main text, caption, Methods/source data, SI, or response letter. Answer the reviewer fully in the letter while keeping the manuscript change to the shortest reader-facing text that preserves the central inference. Every addition triggers a deletion check across the affected paragraph; prefer replacement or compression before appending.
14. In a journal route, if editing manuscript text, use a backed-up copy and mark changed text in
   red. In a conference route, edit or promise manuscript changes only when the verified rules
   permit them. For journal LaTeX, use `\revised{...}` from
   `templates/revised-manuscript-redline.tex`.
15. If pasting revised manuscript text after a response, format it in italics. For LaTeX response files, use `\RevisedExcerpt{...}` from `templates/response-to-reviewers.tex`.
16. In a journal route, create requested LaTeX reviewer files and other permitted package
   artifacts. Preserve visible placeholders for missing facts. The conference route defaults to
   platform-ready text, not journal LaTeX templates.
17. Mark a claimed change `VERIFIED_DONE` only after matching it to supplied revised manuscript text, analysis output, figure/table content, or another inspectable artifact. Treat an unsupported author report as `REPORTED_DONE_UNVERIFIED`.
18. Flag missing author input rather than fabricating details.
19. Run QA for completeness, decision-strategy consistency, reviewer isolation, per-item status calibration, blocking-state consistency, traceability, factuality, tone, unresolved risk, red-marked changes, italic revised excerpts, and LaTeX placeholder visibility.
20. Derive package readiness from the item statuses and return one of: `ready_to_submit`, `draft_with_placeholders`, `needs_author_input`, or `blocked`.

## Conference rebuttal output format

For `conference-rebuttal`, use the output contract in
`references/conference-rebuttal.md`. Do not append the journal package below.

## Journal revision output format

Unless the user asks for another format, return:

```text
Response strategy summary
- Decision type:
- Task mode:
- Overall posture:
- Major risks:
- Parsed email metadata:
- Suggested ordering:
- Package readiness:

Internal/editor master tracker (not reviewer-facing)
| ID | Reviewer concern | Type | Severity | Proposed action | Work status | Required input | Expected output | Blocks finalization? |
|---|---|---|---|---|---|---|---|---|

Reviewer-specific response files
- Reviewer 1: [standalone response containing Reviewer 1 comments only]
- Reviewer 2: [standalone response containing Reviewer 2 comments only]

Draft revision cover letter
[only when requested or when returning a revision package]

Marked manuscript changes
- [red-marked changed passages or path to marked backup copy]

LaTeX files
- cover letter: [path or template-filled text when requested]
- response to Reviewer 1: [path or template-filled text when requested]
- response to Reviewer 2: [path or template-filled text when requested]
- red-marked manuscript: [path or template-filled text when requested]

Manuscript change checklist
- [specific manuscript changes or placeholders]
- Main-text discipline audit: [result/explanation class; destination; appended,
  replaced, compressed, relocated, or deleted; before/after paragraph word count]

Missing information / risk flags
- [specific unresolved items or "None"]

中文核对
- [when the user writes in Chinese; otherwise omit unless useful]
```
