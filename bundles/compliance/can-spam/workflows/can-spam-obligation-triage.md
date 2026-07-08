---
type: Workflow
title: CAN-SPAM Obligation Triage
description: Source-aware workflow for turning a CAN-SPAM question into an evidence-backed compliance brief.
tags:
  - can-spam
  - triage
  - email-marketing
  - compliance
okb_bundle_id: can-spam
timestamp: "2026-07-08T22:23:14Z"
---

# CAN-SPAM Obligation Triage

Use this workflow when the user asks whether a commercial email campaign, message, opt-out flow, sender practice, or vendor send raises a CAN-SPAM issue.

## Inputs

- User question and intended decision.
- Email copy, subject line, from and reply-to identity, available header evidence, footer, physical address, and unsubscribe mechanism.
- Campaign purpose, audience, list source, sender or advertiser identity, vendor or affiliate involvement, and suppression-list process.
- Current FTC guidance, current eCFR Part 316, current statutory source text when section-level claims matter, and user-provided campaign evidence.
- ESP screenshots, suppression exports, unsubscribe test evidence, vendor documentation, or policy documents when operational behavior matters.

## Output Contract

The final answer should include:

- **Direct answer:** state the likely issue and confidence level.
- **Source note:** name the official FTC, statutory, or regulatory source category checked, user-provided evidence, and missing source or fact.
- **Verified facts:** list what was checked against official sources.
- **User-provided facts:** list facts supplied by the user.
- **Assumptions:** label draft assumptions clearly.
- **Missing evidence:** name what blocks a conclusion.
- **Risk boundary:** state whether professional review or explicit user confirmation is needed.
- **Next steps:** identify source inspection, document review, technical verification, professional review, or operational action.

## Triage Steps

1. Classify the question as message purpose, sender identity, subject line, ad identification, physical postal address, opt-out mechanism, opt-out timing, suppression-list use, third-party sender responsibility, sexually oriented material labeling, enforcement risk, or adjacent law/platform issue.
2. Identify the official source category required for that class.
3. Ask for user evidence needed to decide the issue.
4. Separate source-confirmed facts from user facts and assumptions.
5. Produce a brief using [source-aware-can-spam-compliance-brief.md](../deliverables/source-aware-can-spam-compliance-brief.md).
6. Mark any legal, campaign-send, list-upload, contact-export, suppression-change, automation-change, or vendor-instruction action as requiring professional review and explicit user confirmation.

## Quality Bar

A good answer does not approve a campaign from incomplete evidence. It states what can be concluded from inspected sources and provided evidence, then names the missing evidence needed before relying on the answer.
