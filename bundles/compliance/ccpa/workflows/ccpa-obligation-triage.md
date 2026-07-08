---
type: Workflow
title: CCPA Obligation Triage
description: Source-aware workflow for turning a CCPA or CPRA question into an evidence-backed compliance brief.
tags:
  - ccpa
  - cpra
  - triage
  - compliance
okb_bundle_id: ccpa
timestamp: "2026-07-08T21:51:32Z"
---

# CCPA Obligation Triage

Use this workflow when the user asks whether CCPA applies, what obligation is triggered, or what to do next.

## Inputs

- User question and intended decision.
- California consumer, business, service-provider, contractor, and third-party relationship facts.
- Products, services, sites, apps, data categories, consumer categories, purposes, retention, recipients, contracts, and opt-out mechanisms.
- Current statutory text, current CPPA regulations and rulemaking status, relevant Attorney General material, and user-provided documents.
- Technical evidence when the question involves tags, SDKs, cookies, GPC, opt-out signals, ADMT, cybersecurity audits, risk assessments, or data disclosures.

## Output Contract

The final answer should include:

- **Direct answer:** state the likely issue and confidence level.
- **Source note:** name the official statute or regulation source category, California agency material checked, user-provided evidence, and missing source or fact.
- **Verified facts:** list what was checked against official sources.
- **User-provided facts:** list facts supplied by the user.
- **Assumptions:** label draft assumptions clearly.
- **Missing evidence:** name what blocks a conclusion.
- **Risk boundary:** state whether professional review or explicit user confirmation is needed.
- **Next steps:** identify source inspection, document review, technical verification, professional review, or operational action.

## Triage Steps

1. Classify the question as applicability, notice, access, deletion, correction, opt-out, sale, sharing, sensitive personal information, GPC, data minimization/retention, service-provider/contractor terms, consumer request handling, ADMT, risk assessment, cybersecurity audit, enforcement, or other.
2. Identify the official source category required for that class.
3. Ask for user evidence needed to decide the issue.
4. Separate source-confirmed facts from user facts and assumptions.
5. Produce a brief using [source-aware-ccpa-compliance-brief.md](../deliverables/source-aware-ccpa-compliance-brief.md).
6. Mark any legal, regulatory, contractual, consumer-response, or live-system action as requiring professional review and explicit user confirmation.

## Quality Bar

A good answer does not guess the user's CCPA status. It states what can be concluded from inspected sources and provided evidence, then names the missing evidence needed before relying on the answer.
