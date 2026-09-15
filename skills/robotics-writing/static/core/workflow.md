# Writing workflow

Use the relevant steps for the requested drafting or restructuring scope. Keep routine planning internal; apply step 3b only when missing information materially affects the draft. Steps 4-6 guide drafting, 7-8 cover checking and delivery, and step 9 applies to subsequent revisions.

## 1. Build a one-sentence argument

> In [system/problem], we show [advance] using [approach], supported by [evidence], with [boundary].

Force every section to serve this sentence. If the sentence cannot be written, the paper does not yet have an argument — surface that to the user.

## 1b. Build the Terminology Ledger

Reuse known canonical terms and extract recurring terms, abbreviations, notation, and proper names relevant to the requested scope. Keep this lightweight for a short passage; show a Terminology Ledger for a full manuscript, on request, or when important ambiguity needs resolution. Do not require an empty table or reconfirm established terms. See `../../../nature-shared/core/terminology-ledger.md`.

## 2. Choose section architecture

Pick the section structure from the relevant `section/*.md` fragment and, if needed, deeper patterns from `references/article-architecture.md`.

## 3. Map each paragraph to one central message

Give each paragraph one central message. Context, gap, approach, result, comparison, mechanism, implication, and limitation are useful function labels, not mutually exclusive paragraph types.

Evidence, comparison, explanation, and a qualification may support the same message in one paragraph. Split only when the central message changes; preserve a coherent single-paragraph abstract when the requested format calls for one.

## 3a. Allocate Results evidence before drafting

When the task includes Results, a full manuscript, main-text compression, or
main-versus-SI placement, load
`../../../nature-shared/core/main-text-discipline.md`. Classify each result as
core discovery, necessary support, qualification, robustness, heterogeneity,
provenance detail, alternative inference, or edge case. Build the shortest
sufficient main-text evidence chain and record the destination of everything
else. Do not bury conclusion-changing evidence in SI.

## 3b. Resolve material ambiguity

Use the user's request, supplied material, and prior decisions first. When the claim, supporting evidence, and relevant boundary are clear enough for the requested scope, draft directly. A full section, Method section, or major rewrite does not by itself require approval of an outline.

Ask only when an unresolved fact or framing choice would materially change the scientific claim or requested deliverable and cannot be recovered from the supplied material. Briefly state the affected argument or assumption and ask at most 2–3 focused questions; do not repeat questions already answered.

Wait for the answer before asserting the affected scientific content. Continue independent parts when useful, or provide an explicitly marked scaffold or placeholder if the missing fact can be isolated. Never guess an experimental detail, result, mechanism, or release commitment.

For an outline-only request, deliver the outline. For a prose request, choose a reasonable structure and deliver the prose without an extra outline-approval round. If the user explicitly requests staged approval, follow that workflow.

If style feedback is too vague to apply and no suitable writing sample is already available, ask for a short sample. Match its rhythm, hedging, transitions, voice, and terminology without importing its claims or facts.

## 4. Draft from evidence outward

Keep claims near the data that support them. Do not stack claims at the top of a section then leave evidence at the bottom.

## 5. Calibrate verbs to evidence strength

`show` / `demonstrate` need strong direct evidence. `suggest` / `indicate` are for trend-level or indirect evidence. `may` / `could` are for plausible but unverified mechanisms.

## 6. Remove unsupported novelty and universal claims

Sweep for `first`, `unique`, `unprecedented`, `comprehensive`, `complete`, `always`, `never`. Replace with bounded claims or delete.

## 7. Run a paragraph-flow check

- One paragraph, one message.
- The first sentence is the topic / claim.
- Each subsequent sentence has an explicit relation to the previous one (cause, comparison, restriction, example).

For full reverse-outlining, open `references/paragraph-flow.md`.

## 8. Return prose plus notes

Return the requested prose with only the material assumptions, missing inputs, or evidence gaps the user needs to understand it. Scale additional notes to the task; see `output-format.md`.

## 9. Revise by targeted edit, not full rewrite

When the user reacts to a draft, "this is not what I meant" is usually local — a wrong claim, a mis-framed paragraph, the wrong result leading. Do not silently re-draft the whole section: a full rewrite breaks the paragraphs that were already right and forces the user to re-check everything.

- Change **only** the paragraphs or claims the user flagged; keep the rest verbatim.
- Make structural changes needed to complete the requested fix and briefly explain material reordering. Ask only if the change requires an unresolved scientific or scope decision under step 3b.
- Keep the Terminology Ledger (step 1b) stable across revisions unless the user changes a term; never let a revision reintroduce a variant of a locked term.
- After revising, re-run only the checks relevant to what changed (steps 5-7), not the whole workflow.
- If the user corrects the original premise, use the correction directly. Apply step 3b only to material ambiguity that remains.
- Every proposed addition triggers the main-text deletion check: identify the
  new sentence's function, find existing text with the same function, and prefer
  replacement or compression before appending. Re-run the paragraph necessity
  and claim-repetition checks after the edit.
