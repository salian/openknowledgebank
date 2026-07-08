---
type: Workflow
title: SOX Obligation Triage
description: Source-aware workflow for turning a SOX question into an evidence-backed compliance brief.
tags:
  - sox
  - triage
  - compliance
  - icfr
okb_bundle_id: sox
timestamp: "2026-07-09T00:00:00Z"
---

# SOX Obligation Triage

Use this workflow when the user asks whether a SOX obligation applies, whether an issuer is ready for certification, how to frame an ICFR question, or what evidence is needed next.

## Inputs

- User question and intended decision.
- Issuer status, filing form, fiscal period, filer category, and exemption facts when relevant.
- Current statutory, SEC, and PCAOB source categories needed for the question.
- User-provided filings, control framework, scope, risk-control matrix, deficiency log, remediation evidence, disclosure committee records, auditor request, or governance materials.
- Intended audience: internal draft, management, audit committee, external auditor, regulator, investor, or public filing.

## Output Contract

The final answer should include:

- **Direct answer:** state whether the answer is verified, provisional, or blocked by missing evidence.
- **Source note:** name the statutory, SEC, PCAOB, and user-provided source categories inspected or still needed.
- **Question classification:** identify Section 302, Section 404(a), Section 404(b), Section 906, disclosure-controls, ICFR, auditor-attestation, or other SOX area.
- **Verified facts:** list official-source facts actually checked.
- **User-provided facts:** list issuer facts supplied by the user.
- **Assumptions:** label draft assumptions clearly.
- **Missing evidence:** name what blocks reliance.
- **Professional review:** identify legal, accounting, audit, disclosure-control, securities, or CPA review needed.
- **Risky actions:** require explicit confirmation before filings, certifications, external communications, evidence exports, control changes, or live-system changes.

## Triage Steps

1. Classify the question into the relevant SOX area.
2. Identify the official source category required for that area.
3. Ask for issuer facts and evidence needed to decide the issue.
4. Separate official source facts from user facts, assumptions, and missing evidence.
5. Produce a brief using [source-aware-sox-compliance-brief.md](../deliverables/source-aware-sox-compliance-brief.md).
6. Mark any filing, certification, auditor, regulator, board, investor, control-change, evidence-export, or live-system action as requiring professional review and explicit user confirmation.

## Quality Bar

A good answer does not guess the issuer's SOX status. It states what can be concluded from inspected sources and provided evidence, then names the missing evidence and professional review needed before relying on the answer.

