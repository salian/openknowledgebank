---
type: "Workflow"
title: "SEC Reporting & Disclosure Source-Aware Triage"
description: "Workflow for converting SEC disclosure requests into evidence-backed, qualified-review-ready outputs."
okb_bundle_id: sec-disclosure
timestamp: "2026-07-11T00:00:00Z"
---

# Source-Aware Triage

## Inputs

- User request and intended decision.
- Official SEC source category already inspected, if any.
- Issuer-specific documents, disclosure controls, policies, filings, fiscal period, security class, transaction or event facts, committee materials, accounting/audit evidence, counsel notes, or other local evidence.
- Missing facts that block reliance.

## Steps

1. Classify the request by source category: periodic/current reporting, proxy/governance, ownership reporting, executive compensation, insider trading policy, conflict minerals, cybersecurity, EDGAR/Inline XBRL, Regulation FD, or adjacent/non-SEC.
2. Identify the current official SEC source that must be inspected before reliance.
3. Ask for only the minimum issuer evidence needed for the requested output.
4. Separate verified source facts, user-provided issuer facts, assumptions, and missing evidence.
5. Draft the [source-aware brief](../deliverables/source-aware-brief.md).
6. Mark qualified review and explicit confirmation requirements for any filing, public disclosure, investor communication, data export, policy change, trading-window, governance, accounting, audit, tax, or regulatory action.

## Output Contract

Include direct answer, source note, source category, evidence matrix, missing evidence, qualified-review gate, risk boundary, and next steps. If the answer depends on exact SEC rules, form items, EDGAR behavior, issuer status, deadlines, materiality, or disclosure text, state what source or issuer evidence must be inspected before the draft becomes a conclusion.
