---
type: Deliverable
title: Source-Aware GDPR Compliance Brief
description: Output format for GDPR answers that must separate legal sources, regulator guidance, user evidence, assumptions, and missing verification.
okb_bundle_id: gdpr
required_inputs:
  - user question
  - relevant official legal source
  - regulator guidance source category
  - user-provided processing facts
outputs:
  - direct answer
  - source note
  - evidence matrix
  - caveats and next steps
quality_criteria:
  - Does not present legal advice as a final professional conclusion.
  - Distinguishes verified source facts, user-provided facts, assumptions, and missing evidence.
  - Requires professional review before reliance for regulatory, contractual, enforcement, or incident-response decisions.
timestamp: "2026-07-09T00:00:00Z"
---

# Source-Aware GDPR Compliance Brief

## Direct Answer

State the likely GDPR issue and whether the answer is verified, provisional, or blocked by missing evidence.

## Source Note

Name:

- official legal text inspected or still needed;
- regulator guidance source category inspected or still needed;
- national supervisory authority source inspected or still needed;
- user-provided records, policies, contracts, notices, incident facts, or processing facts used;
- missing sources or facts that prevent reliance.

## Evidence Matrix

| Claim | Status | Source or Evidence | Caveat |
| --- | --- | --- | --- |
| Legal rule or obligation | verified / needs verification | Official source or missing source | Include article/guidance only if inspected. |
| Organization fact | provided / missing | User evidence | Do not infer facts. |
| Draft assumption | assumed | Stated assumption | Do not treat as conclusion. |

## Analysis

Explain how the verified legal source and user facts connect. If a conclusion depends on national law, regulator guidance, a contract, a policy, a transfer mechanism, security facts, or incident facts that are missing, say so directly.

## Next Steps

- Inspect named official sources.
- Collect missing user evidence.
- Route legal conclusions to qualified professional review.
- Require explicit confirmation before risky actions such as regulator contact, notice submission, policy change, contract change, or external communication.
