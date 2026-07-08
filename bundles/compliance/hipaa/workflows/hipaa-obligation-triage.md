---
type: Workflow
title: HIPAA Obligation Triage
description: Source-aware workflow for turning a HIPAA question into an evidence-backed compliance brief.
tags:
  - hipaa
  - triage
  - compliance
okb_bundle_id: hipaa
timestamp: "2026-07-09T00:00:00Z"
---

# HIPAA Obligation Triage

Use this workflow when the user asks whether HIPAA applies, what rule family is triggered, or what to do next.

## Inputs

- User question and intended decision.
- Entity role, relationship, and transaction facts.
- Data type, identifiability, source system, medium, use, disclosure, incident, or transaction facts.
- Relevant policies, notices, BAAs, incident reports, risk analysis records, transaction documentation, or other user-provided evidence.
- Current official sources from HHS OCR, CMS/HHS Administrative Simplification, eCFR, Federal Register, or other authority relevant to the rule family.

## Output Contract

The final answer should include:

- **Direct answer:** state the likely issue and whether the conclusion is verified, provisional, or blocked.
- **Source note:** name the official source category, user-provided evidence, and missing source or fact.
- **Rule-family classification:** map the question to Privacy, Security, Breach Notification, Enforcement, transactions, identifiers, code sets, proposed-rule status, or other.
- **Verified facts:** list what was checked against official sources.
- **User-provided facts:** list facts supplied by the user.
- **Assumptions:** label draft assumptions clearly.
- **Missing evidence:** name what blocks a conclusion.
- **Next steps:** identify source inspection, evidence collection, professional review, or operational action.

## Triage Steps

1. Classify the question using [rule-family-map.md](../requirements/rule-family-map.md).
2. Identify the official source category required for that class.
3. Ask for only the minimum user evidence needed; avoid collecting unnecessary PHI/ePHI.
4. Separate source-confirmed facts from user facts and assumptions.
5. Produce a brief using [source-aware-hipaa-compliance-brief.md](../deliverables/source-aware-hipaa-compliance-brief.md).
6. Mark any legal, regulatory, contractual, breach, security, reporting, disclosure, or live-system action as requiring professional review and explicit user confirmation.

## Quality Bar

A good answer does not guess the user's HIPAA status, breach reportability, or required action. It states what can be concluded from inspected sources and provided evidence, then names the missing evidence needed before relying on the answer.
