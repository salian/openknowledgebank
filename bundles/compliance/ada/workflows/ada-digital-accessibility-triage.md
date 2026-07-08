---
type: Workflow
title: ADA Digital Accessibility Triage
description: Source-aware workflow for turning an ADA Title III or digital accessibility question into an evidence-backed compliance brief.
tags:
  - ada
  - accessibility
  - triage
  - compliance
okb_bundle_id: ada
timestamp: "2026-07-09T00:00:00Z"
---

# ADA Digital Accessibility Triage

Use this workflow when the user asks whether ADA applies, what digital accessibility obligation is triggered, whether a website or app is compliant, or what to do next.

## Inputs

- User question and intended decision.
- Business type, public-facing goods or services, website/app scope, customer journey, and affected content.
- User-provided audits, scanner results, manual testing, assistive-technology notes, screenshots, code/design scope, vendor contracts, accessibility policy, remediation plan, and accessibility statement.
- Current DOJ, ADA.gov, ADA legal/regulatory, W3C/WAI, WCAG, case-law, state-law, procurement, or contractual source categories as relevant.

## Output Contract

The final answer should include:

- **Direct answer:** state the likely issue and confidence level.
- **Source note:** name the DOJ/ADA source category, W3C/WAI or WCAG source category if relevant, user-provided evidence, and missing source or fact.
- **Issue classification:** identify Title III public accommodation, Title II public entity, WCAG technical question, product conformance, accessibility statement, remediation, legal demand, state-law, procurement, or other issue.
- **Verified facts:** list what was checked against official or technical sources.
- **User-provided facts:** list facts supplied by the user.
- **Assumptions:** label draft assumptions clearly.
- **Missing evidence:** name what blocks a conclusion.
- **Risk boundary:** state whether professional review or explicit user confirmation is needed.
- **Next steps:** identify source inspection, product evidence collection, accessibility testing, reviewer questions, or operational action.

## Triage Steps

1. Classify the question as Title III public accommodation, Title II public entity, digital accessibility, effective communication, auxiliary aids and services, WCAG target, public statement, remediation, vendor responsibility, legal demand, state-law, procurement, or other.
2. Identify the source category required for that class.
3. If the question involves a private business, distinguish Title III guidance from the Title II web/mobile rule for state and local governments.
4. Ask for product and business evidence needed to decide the issue.
5. Separate source-confirmed facts from user facts and assumptions.
6. Produce a brief using [source-aware-ada-compliance-brief.md](../deliverables/source-aware-ada-compliance-brief.md).
7. Mark any legal, regulatory, public-statement, remediation-commitment, user-data, or live-product action as requiring professional review and explicit user confirmation.

## Quality Bar

A good answer does not guess ADA compliance or WCAG conformance. It states what can be concluded from inspected sources and provided evidence, explains the Title III/Title II/WCAG distinction when relevant, and names the missing evidence needed before relying on the answer.
