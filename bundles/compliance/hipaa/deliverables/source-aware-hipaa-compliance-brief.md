---
type: Deliverable
title: Source-Aware HIPAA Compliance Brief
description: Output format for HIPAA answers that must separate official sources, user evidence, assumptions, and missing verification.
okb_bundle_id: hipaa
required_inputs:
  - user question
  - relevant official source category
  - user-provided entity, data, transaction, incident, policy, contract, or system facts
outputs:
  - direct answer
  - source note
  - rule-family classification
  - evidence matrix
  - caveats and next steps
quality_criteria:
  - Does not present legal advice as a final professional conclusion.
  - Distinguishes verified source facts, user-provided facts, assumptions, and missing evidence.
  - Requires professional review before reliance for regulatory, contractual, breach, enforcement, security, or incident-response decisions.
timestamp: "2026-07-09T00:00:00Z"
---

# Source-Aware HIPAA Compliance Brief

## Direct Answer

State the likely HIPAA issue and whether the answer is verified, provisional, or blocked by missing evidence.

## Source Note

Name:

- official HIPAA source category inspected or still needed;
- current HHS OCR, CMS/HHS Administrative Simplification, eCFR, or Federal Register source inspected or still needed;
- user-provided records, policies, BAAs, notices, incident facts, risk analyses, system facts, transaction facts, or other evidence used;
- missing sources or facts that prevent reliance.

## Rule-Family Classification

Classify the issue as Privacy Rule, Security Rule, Breach Notification Rule, Enforcement Rule, transactions, identifiers, code sets, proposed-rule status, or other. If more than one applies, state the dependency between them.

## Evidence Matrix

| Claim | Status | Source or Evidence | Caveat |
| --- | --- | --- | --- |
| Legal rule, standard, or obligation | verified / needs verification | Official source or missing source | Include citations only if inspected. |
| Organization fact | provided / missing | User evidence | Do not infer facts. |
| Draft assumption | assumed | Stated assumption | Do not treat as conclusion. |
| Risk or operational action | needs review | Professional review, explicit confirmation, or missing evidence | Do not take action without confirmation. |

## Analysis

Explain how the verified source category and user facts connect. If a conclusion depends on state law, 42 CFR Part 2, contract terms, policies, system controls, transaction standards, proposed-rule status, or incident facts that are missing, say so directly.

## Next Steps

- Inspect named official sources.
- Collect missing user evidence while minimizing PHI/ePHI.
- Route legal, privacy, security, revenue-cycle, contractual, or incident-response conclusions to qualified professional review.
- Require explicit confirmation before risky actions such as breach report submission, regulator contact, notice sending, PHI/ePHI disclosure, policy or BAA changes, transaction changes, exports, or live-system changes.
