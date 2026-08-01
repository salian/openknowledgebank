---
type: Evaluation
title: Backlog Item Quality Check
description: Reviews whether a backlog item is grounded, outcome-focused, testable, ordered transparently, and safe to act on.
okb_bundle_id: product-backlog-user-stories
task_type: deliverable review
criteria: [direct answer, evidence separation, Product Goal alignment, coherent scope, observable acceptance criteria, ordering rationale, dependencies and risks, explicit unknowns, source note, confirmation boundary]
---

# Backlog Item Quality Check

Score each criterion as `pass`, `partial`, or `fail`, with evidence:

- Direct answer is easy to find.
- Verified, provided, assumed, and missing evidence are separated.
- The item connects to a supplied Product Goal or clearly names the gap.
- Scope is coherent and non-goals are explicit.
- Acceptance criteria are observable and cover relevant edge cases.
- Ordering rationale names the basis, inputs, scope, and uncertainty.
- Dependencies, risks, and open questions are visible.
- No unsupported dates, owners, metrics, estimates, customer claims, or tool fields are invented.
- Source note names official sources, local evidence, and missing sources.
- Live modifications are behind an explicit confirmation boundary.

## Adversarial Check

When no local product evidence is supplied, `Verified`, `Provided`, and `Assumed` should be `None` unless the prompt itself supplies facts. The output should put missing artifacts under `Needs verification` and should not nominate an accountable reviewer without evidence.
