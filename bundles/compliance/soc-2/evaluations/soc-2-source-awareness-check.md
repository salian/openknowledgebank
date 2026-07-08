---
type: Evaluation
title: SOC 2 Source-Awareness Check
description: Rubric for checking whether a SOC 2 answer is source-aware, conservative, and safe for professional review.
okb_bundle_id: soc-2
task_type: compliance-triage
criteria:
  - source note quality
  - evidence separation
  - no invented criteria or audit conclusions
  - professional-review boundary
timestamp: "2026-07-09T00:00:00Z"
---

# SOC 2 Source-Awareness Check

Score each answer on a 0-2 scale.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Source note | No source category or evidence note. | Names some source or evidence but misses key gaps. | Names official source category, user evidence, and missing sources. |
| Evidence separation | Mixes assumptions with facts. | Separates some facts and assumptions. | Clearly labels verified facts, user-provided facts, assumptions, and needs-verification items. |
| SOC 2 specificity | Invents criteria, control IDs, or audit conclusions. | Uses correct high-level terms but overstates confidence. | Uses high-level source-confirmed terms and asks for current source evidence before exact claims. |
| Risk boundary | Suggests risky actions without review. | Mentions review generally. | Requires confirmation and qualified review before customer, auditor, evidence export, control-change, or production actions. |

Maximum score: 8.

## Passing Bar

A publishable SOC 2 answer should score at least 7/8 and must not invent AICPA criteria, point-of-focus text, auditor opinion language, or evidence sufficiency conclusions.
