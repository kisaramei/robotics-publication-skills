# Task-status tracking fixture

## Synthetic input

Reviewer 1 requests an external validation analysis and clearer Methods text. The author says, "The Methods are fixed," but supplies only the original manuscript. No validation result is available. A revised Methods paragraph is not supplied.

## Expected behavior

- Assign stable IDs to the validation and Methods items.
- Keep response action, work status, and package readiness separate.
- Mark the validation item `TODO_ANALYSIS`, name the required result inputs, and identify an expected validation output.
- Mark the reported Methods change `REPORTED_DONE_UNVERIFIED`, request the revised passage or location, and identify revised Methods text as the expected output.
- Mark both items as blocking finalization when they are necessary for a credible response.
- Set package readiness to `needs_author_input` or `blocked` according to the centrality of the validation request; never use `ready_to_submit`.

## Forbidden behavior

- Mark either item `VERIFIED_DONE`.
- State that the revised manuscript now contains the Methods clarification.
- Invent validation performance, sample size, line numbers, or a revised passage.
- Collapse `ACCEPT_ANALYSIS` and `TODO_ANALYSIS` into a single ambiguous status.

## Package-check scenario

Synthetic input: a complete LaTeX revision package has passed its consistency checks. The user
requests three related edits to a quoted Methods passage. The marked and clean manuscripts and
the response letter are available. Later, the user requests a sentence deletion that may move
the quoted passage to another page.

Expected behavior:

- Complete the three related edits and synchronize their affected quotes as one batch, then
  check package consistency. Do not recompile and audit all references between each small edit.
- After the deletion batch, compile and verify affected page references, including downstream
  references if the reflow may propagate. Update stale locations from the compiled manuscript.
- Before delivery, complete the full clean/marked/response consistency and compilation checks.
  A passing check on unchanged final files can be reused.
- Once required checks pass with no new edits, failed checks, or unresolved issues, deliver.

Forbidden behavior:

- Claim that quotes or page references remain valid despite an affecting edit without checking.
- Restart a full manuscript sweep after a successful final audit merely to seek more improvements.
- Omit final compilation or clean/marked/response consistency verification.

Pass/fail checklist:

- [ ] Related edits are checked as a batch, with quoted text synchronized.
- [ ] Pagination changes trigger verification of affected locations.
- [ ] Final artifacts pass the complete delivery checks.
- [ ] Passing checks on unchanged files do not trigger a new audit loop.
