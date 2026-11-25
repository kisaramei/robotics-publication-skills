# Numerical audit

Use the [scope rules](../SKILL.md#numerical-audit) to select the evidence. For a whole
manuscript, start with numbers that support headline claims. For a specified table, follow
its caption and relevant definitions or claims in the text. Work from the supplied evidence.

- Recompute reported rates from successes and attempts where both counts are available.
  Keep tasks, episodes, training seeds and evaluation runs distinct. Check the stated
  weighting before comparing an overall result with per-task rates. For example, 8/10
  and 45/90 give a task-average success rate of 65% and a pooled rate of 53%.
  If the paper leaves the aggregation unspecified, give the alternatives.
- Check the direction of each metric and ties before verifying a ranking or a claim such
  as “best on every task.” Distinguish percentage-point gains from relative gains. Use
  the reported precision and allow for rounding in the inputs and the result.
- Compare repeated rows or identical intervals with their labels and evaluation protocol.
  A repeated value alone supports only a possible duplication. When seed counts, weights,
  or interval definitions are missing, identify the specific comparison they prevent.

For each finding, cite the table cell and the relevant caption or passage, show the
short calculation or comparison, and state its impact. Distinguish a confirmed internal
error, unclear aggregation, missing evidence, and possible duplication. If the checked
claims reconcile, say so briefly and identify what was checked.
