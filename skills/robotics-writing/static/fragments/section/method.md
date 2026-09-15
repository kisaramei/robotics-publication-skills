# Section: Method (writing)

## Default structure

`task formulation -> overview (pipeline / system / approach) -> per-module detail -> implementation notes -> assumptions and boundary`

## The three-element pattern (per module)

Each module should answer:

1. **Motivation** — what problem this module solves, and why the obvious alternative fails
2. **Mechanism** — what the module actually does, to a level a peer could re-implement
3. **Evidence / role** — how this module contributes to the overall result (ablation hook)

If any element is missing, the module reads as a black box. Flag the gap.

## Pre-writing checklist

Before drafting Method, extract the following from the supplied material and prior decisions. Apply `static/core/workflow.md` step 3b only to material gaps; this checklist does not create a separate confirmation round:

- Task formulation: inputs, outputs, scope.
- Overview figure / pipeline diagram: does one exist? It anchors the section.
- Notation: defined once and consistent.
- Reproducibility scope: code, weights, data — what will be released.

Use an explicit placeholder for an isolated missing detail or release commitment. If a missing fact determines the method itself, ask before asserting it; do not infer an implementation from a familiar method name.

## Forbidden vague phrases

Never leave:

- `under standard conditions`
- `using routine methods`
- `data were analyzed statistically`
- `the method was validated`
- `samples were randomly assigned` (without saying how)

Replace with the actual reproducible information.

## Deeper reference

For module-motivation templates, three-elements examples, and overview-template patterns, open `references/method.md` and `references/examples/method/`.
