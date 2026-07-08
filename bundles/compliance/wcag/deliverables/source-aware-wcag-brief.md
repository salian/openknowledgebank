---
type: Deliverable
title: Source-Aware WCAG Brief
description: Output format for WCAG answers that must separate W3C/WAI source facts, user evidence, assumptions, missing verification, and review needs.
okb_bundle_id: wcag
required_inputs:
  - user question
  - relevant W3C/WAI source category
  - target WCAG version and level
  - user-provided product or policy evidence
outputs:
  - direct answer
  - source note
  - conformance target and scope
  - evidence matrix
  - caveats and next steps
quality_criteria:
  - Does not present accessibility, conformance, procurement, or legal advice as a final professional conclusion.
  - Distinguishes verified source facts, user-provided facts, scanner output, assumptions, and missing evidence.
  - Requires professional review before reliance for regulatory, contractual, procurement, litigation, public conformance, or live-product decisions.
timestamp: "2026-07-09T00:00:00Z"
---

# Source-Aware WCAG Brief

## Direct Answer

State the likely WCAG issue and whether the answer is verified, provisional, or blocked by missing evidence.

## Source Note

Name:

- W3C/WAI WCAG source inspected or still needed;
- WCAG version and conformance level requested or assumed;
- exact success-criterion or conformance language inspected or still needed;
- user-provided product, code, design, audit, scanner, VPAT/ACR, procurement, contract, or legal evidence used;
- missing sources or facts that prevent reliance.

## Conformance Target and Scope

State:

- target WCAG version and level;
- product, page, component, content, document, or journey scope;
- test method and evidence reviewed;
- date or release scope;
- whether jurisdictional, contractual, or procurement requirements were inspected.

## Evidence Matrix

| Claim | Status | Source or Evidence | Caveat |
| --- | --- | --- | --- |
| WCAG rule or source fact | verified / needs verification | W3C/WAI source or missing source | Include exact criterion only if inspected. |
| Product or content fact | provided / missing | User evidence | Do not infer facts. |
| Scanner or audit finding | provided / needs verification | Tool output or audit report | Treat as evidence, not complete proof. |
| Draft assumption | assumed | Stated assumption | Do not treat as conclusion. |

## Analysis

Explain how the verified WCAG source and user evidence connect. If a conclusion depends on exact criterion wording, content scope, manual testing, assistive-technology review, remediation evidence, jurisdictional law, procurement terms, or contractual language that is missing, say so directly.

## Next Steps

- Inspect named W3C/WAI sources.
- Collect missing product and testing evidence.
- Validate scanner findings with manual review where needed.
- Route conformance, legal, procurement, or public-claim conclusions to qualified professional review.
- Require explicit confirmation before risky actions such as publishing accessibility statements, submitting VPAT/ACR materials, changing live products, or sending legal/compliance communications.
