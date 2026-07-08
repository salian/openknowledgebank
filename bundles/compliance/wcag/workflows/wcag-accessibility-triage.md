---
type: Workflow
title: WCAG Accessibility Triage
description: Source-aware workflow for turning a WCAG question into an evidence-backed accessibility brief.
tags:
  - wcag
  - accessibility
  - triage
okb_bundle_id: wcag
timestamp: "2026-07-09T00:00:00Z"
---

# WCAG Accessibility Triage

Use this workflow when the user asks whether WCAG applies, what conformance target to use, what a finding means, whether a product is compliant, or what to do next.

## Inputs

- User question and intended decision.
- Target WCAG version and conformance level, if known.
- Product, page, component, content, or document scope.
- W3C/WAI source material for exact WCAG wording and conformance framing.
- User-provided audit reports, scanner output, code, designs, test notes, assistive-technology observations, VPAT/ACR material, contracts, procurement requirements, or legal source excerpts.

## Output Contract

The final answer should include:

- **Direct answer:** state the likely WCAG issue and confidence level.
- **Source note:** name the W3C/WAI source category, target version and level, user-provided evidence, jurisdictional or contractual source category if relevant, and missing source or fact.
- **Conformance target and scope:** identify the version, level, content/product scope, test method, and date/version assumptions.
- **Verified facts:** list what was checked against official W3C/WAI sources.
- **User-provided facts:** list facts supplied by the user.
- **Assumptions:** label draft assumptions clearly.
- **Missing evidence:** name what blocks a product conformance, legal, procurement, or public-claim conclusion.
- **Next steps:** identify source inspection, manual testing, assistive-technology review, remediation evidence, professional review, or operational action.

## Triage Steps

1. Classify the question as version/level selection, success-criterion interpretation, scanner finding, design/content review, remediation planning, conformance claim, VPAT/ACR/procurement issue, accessibility statement, or jurisdiction-specific legal question.
2. Identify the official source category required for that class.
3. Ask for user evidence needed to decide the issue.
4. Separate source-confirmed WCAG facts from user evidence, assumptions, scanner output, and legal/procurement materials.
5. Produce a brief using [source-aware-wcag-brief.md](../deliverables/source-aware-wcag-brief.md).
6. Mark any public conformance statement, VPAT/ACR submission, legal/procurement response, external communication, or live product change as requiring professional review and explicit user confirmation.

## Quality Bar

A good answer does not guess product conformance. It states what can be concluded from inspected WCAG sources and provided evidence, then names the missing evidence needed before relying on the answer.
