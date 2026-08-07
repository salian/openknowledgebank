---
type: Evaluation
---

# Section 508 Federal ICT Accessibility Quality Check

## Rubric

- **Authority:** Separates statute, 36 CFR standards, FAR, guidance, agency policy, and contract terms.
- **Applicability:** Establishes federal, ICT, lifecycle, user, date, and acquisition context.
- **Standards:** Maps WCAG 2.0 and non-WCAG requirements by component.
- **Exceptions:** Requires the correct authority, basis, documentation, and alternative-access evidence.
- **Conformance:** Treats ACRs and tests as scoped evidence, not certification or automatic proof.
- **Procurement:** Traces requirements and evidence through the acquisition lifecycle.
- **Safety:** Protects sensitive records and stops before consequential action or claim.

## Public-safe scenarios

1. A commercial website with no federal agency or contract evidence is labeled “Section 508 noncompliant.” A passing review rejects the blanket legal conclusion and requests coverage evidence.
2. A product is tested only against WCAG 2.2 AA and reported fully Section 508 conformant. A passing review preserves WCAG 2.0 as the incorporated edition and checks all applicable non-WCAG provisions and contract overlays.
3. A vendor ACR says “supports” and an agency record asserts undue burden without an authorized determination. A passing review records both as incomplete evidence and makes no conformance or exemption claim.

## Evaluation status

Blocked. No approved benchmark task set, runnable matched evaluator configuration, or qualified Section 508 and federal acquisition reviewer scorecard was available. No measured score is claimed. The exact next action is to approve the three scenarios above, create `operations/evaluations/configs/section-508-v1.json`, run baseline and candidate under the same configuration, obtain qualified reviewer scoring, and aggregate the results.
