---
type: Deliverable
title: Source-Aware ADA Compliance Brief
description: Review-ready brief format for ADA Title III and digital accessibility questions that separates source-confirmed law, technical standards, user facts, assumptions, and missing evidence.
okb_bundle_id: ada
required_inputs:
  - user question and intended decision
  - current DOJ, ADA, W3C/WAI, and WCAG source categories
  - user-provided business, website, app, audit, testing, policy, vendor, or remediation evidence
outputs:
  - direct answer
  - source note
  - evidence table
  - Title III / Title II / WCAG distinction
  - missing evidence
  - risk boundary
  - next steps
quality_criteria:
  - separates official-source facts, technical-standard facts, user facts, assumptions, and missing evidence
  - avoids legal or conformance conclusions from incomplete facts
  - requires professional review for reliance
timestamp: "2026-07-09T00:00:00Z"
---

# Source-Aware ADA Compliance Brief

Use this deliverable when the user needs a concise ADA Title III or digital accessibility analysis for review.

## Required Sections

### Direct Answer

State the likely issue, confidence level, and whether the answer is a triage view or a reliance-ready conclusion. Most outputs should be triage unless current sources, user evidence, accessibility testing, and qualified review have all been completed.

### Source Note

Name:

- the DOJ, ADA.gov, ADA legal/regulatory, or other legal source category used;
- the W3C/WAI or WCAG technical source category checked, if digital accessibility or conformance is involved;
- the user-provided business, website, app, audit, testing, policy, vendor, communication, or remediation evidence used for this specific answer;
- any missing source or fact still needed before the answer can be relied on.

### Evidence Table

| Claim | Status | Source or Evidence | Caveat |
| --- | --- | --- | --- |
| Official ADA source fact | Verified / needs verification | DOJ, ADA.gov, ADA statute/regulation, or current legal source | Include access date or source date when available |
| Technical standard fact | Verified / needs verification | W3C/WAI WCAG source or accessibility test method | Identify WCAG version and level when known |
| Organization or product fact | Provided / missing | User document, audit, scanner result, manual test, code, screenshot, contract, or statement | Identify owner, scope, and freshness when known |
| Draft assumption | Assumed | Stated assumption | Do not treat as conclusion |

### Applicability and Obligation Analysis

Classify the issue. Explain whether it concerns Title III public accommodation, Title II public entity, digital accessibility, effective communication, auxiliary aids and services, WCAG target, product conformance, accessibility statement, remediation, vendor responsibility, legal demand, state law, procurement, or another ADA topic.

### Title III / Title II / WCAG Distinction

If the user asks about websites or mobile apps, state whether the question concerns a private business open to the public, a state/local government public entity, a technical WCAG target, or a mix. Do not apply the DOJ Title II web/mobile rule to a private Title III business without current legal authority.

### Missing Evidence

List missing official sources, user documents, technical evidence, accessibility test evidence, business facts, legal authority, or reviewer decisions. If exact obligations, deadlines, case-law rules, state-law rules, accessibility standards, or remediation commitments matter, require current source inspection and professional review.

### Risk Boundary

State whether professional legal, accessibility, procurement, compliance, or product review is required before reliance. Require explicit user confirmation before any accessibility statement publication, legal or regulator communication, remediation commitment, live product change, public conformance claim, or user-data export.

### Next Steps

Give the smallest useful next actions: inspect source, collect evidence, test affected user journeys, identify WCAG target, prepare reviewer questions, draft a remediation review packet, or route to legal/accessibility review.

## Quality Bar

The brief should be useful to an accessibility or legal reviewer because it exposes source status and evidence gaps. It should not sound more certain than the inspected sources and user evidence support.
