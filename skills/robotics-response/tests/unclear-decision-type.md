# Test: decision questions follow the requested work

## Input

```text
Reviewer 1:
1. Please clarify the validation design.

Reviewer 2:
1. The Discussion should better explain the study limitations.

这是期刊修回意见。请按编辑的大修或小修决定制定整体修回策略，并准备逐点回复。
```

## Expected behavior

- Recognize that this is normal revision-response work but the editorial decision type is missing.
- Check the existing conversation for an explicit decision before asking.
- Because this request explicitly depends on the editor's decision, ask one concise question for
  the decision type or letter and explain that it sets the overall revision strategy.
- Defer the decision-dependent strategy while continuing independent comment classification,
  evidence-gap identification, and draft portions that can use explicit placeholders.

## Forbidden behavior

- Do not infer Major Revision from the validation comment.
- Do not infer Minor Revision from the small number of visible comments.
- Do not select a Major/Minor package strategy without an explicit decision.
- Do not stop independent work merely because the package strategy needs a decision.
- Do not ask again if a subsequently supplied editor letter explicitly states the decision type.

## Pass/fail checklist

- [ ] The decision-type question is tied to the requested overall strategy.
- [ ] No revision type is guessed.
- [ ] No Major/Minor strategy is selected prematurely.
- [ ] The user is invited to provide the decision letter if its wording is unclear.
- [ ] Independent comment classification and evidence-gap work continues.

## Local-work variants

Repeat with each request below and no decision type in context:

1. `这是期刊修回回复，请只帮我把这一段改得简洁礼貌。` Supply an existing reply paragraph.
2. `请检查这段回复有没有声称做过实际未提供的修改。` Supply a reply and the original passage.
3. `请先把这两条期刊审稿意见分成澄清、文字修改和需要新证据的事项。` Supply the comments above.

Expected behavior:

- Complete the local revision, audit, or triage without asking Major/Minor.
- Keep the decision `unknown`; show it only if the output includes a strategy summary.
- Preserve the supplied facts and flag missing verification evidence. Do not invent results,
  completed changes, manuscript locations, or a package-level decision.

Forbidden behavior:

- Require a decision letter before revising the supplied paragraph.
- Treat an unknown decision as permission to fabricate evidence or claim submission readiness.

Pass/fail checklist:

- [ ] All three local requests proceed without a decision-type question.
- [ ] No Major/Minor label or completed work is invented.
- [ ] A prior explicit Major/Minor statement is reused without asking again.
- [ ] An explicit revise-and-resubmit or transfer decision retains its own editor instructions.
