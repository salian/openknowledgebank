---
type: Workflow
title: GDPR Obligation Triage
description: Source-aware workflow for turning a GDPR question into an evidence-backed compliance brief.
tags:
  - gdpr
  - triage
  - compliance
okb_bundle_id: gdpr
timestamp: "2026-07-09T00:00:00Z"
---

# GDPR Obligation Triage

Use this workflow when the user asks whether GDPR applies, what obligation is triggered, or what to do next.

## Inputs

- User question and intended decision.
- Jurisdiction, establishment, and data-subject facts.
- Controller, processor, joint-controller, or recipient role facts.
- Processing purpose, data categories, data-subject categories, and transfer facts.
- Current official legal text, relevant EDPB guidance, national supervisory authority guidance, and user-provided documents.

## Output Contract

The final answer should include:

- **Direct answer:** state the likely issue and confidence level.
- **Source note:** name the official legal text, regulator guidance category, user-provided evidence, and missing source or fact.
- **Verified facts:** list what was checked against official sources.
- **User-provided facts:** list facts supplied by the user.
- **Assumptions:** label draft assumptions clearly.
- **Missing evidence:** name what blocks a conclusion.
- **Next steps:** identify source inspection, document review, professional review, or operational action.

## Triage Steps

1. Classify the question as applicability, lawful basis, transparency, rights request, processor contract, records, security, breach, DPIA, DPO, transfer, representative, supervisory authority, or other.
2. Identify the official source category required for that class.
3. Ask for user evidence needed to decide the issue.
4. Separate source-confirmed facts from user facts and assumptions.
5. Produce a brief using [source-aware-compliance-brief.md](../deliverables/source-aware-compliance-brief.md).
6. Mark any legal, regulatory, contractual, or incident-response action as requiring professional review and explicit user confirmation.

## Quality Bar

A good answer does not guess the user's compliance status. It states what can be concluded from inspected sources and provided evidence, then names the missing evidence needed before relying on the answer.
