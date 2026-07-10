---
type: "Bundle Index"
title: "SEC Reporting & Disclosure (US Public Companies)"
description: "Source-aware compliance bundle for SEC reporting and disclosure source triage, evidence collection, and review-ready decision support for US public companies."
schema_version: "0.1.0"
bundle_format: "okf-compatible"
category: "compliance"
tags:
  - "sec"
  - "disclosure"
  - "reporting"
  - "public-companies"
  - "exchange-act"
  - "edgar"
  - "xbrl"
  - "regulation-fd"
  - "compliance"
aliases:
  - "SEC Reporting & Disclosure"
  - "SEC public company reporting"
  - "Exchange Act reporting"
  - "US Public Companies"
problems_solved:
  - "Route SEC reporting and disclosure questions to the right official source category and issuer evidence set."
  - "Separate verified SEC source facts, user-provided issuer facts, assumptions, and missing evidence."
  - "Produce an SEC disclosure source-aware brief suitable for qualified legal, accounting, audit, governance, or disclosure committee review."
industries:
  - "Public companies and SEC-reporting issuers"
tools:
  - "SEC.gov"
  - "EDGAR"
  - "Inline XBRL"
frameworks:
  - "source-evidence matrix"
  - "inspect-first workflow"
  - "qualified-review gate"
  - "disclosure control handoff"
deliverables:
  - "SEC disclosure source-aware brief"
commands:
  []
skills:
  []
evaluations:
  - "SEC disclosure source-awareness check"
okb_bundle_id: sec-disclosure
okb_bundle_version: "0.1.0"
trust_tier: "trusted"
status: "beta"
license: "CC-BY-4.0"
related_bundles:
  - "auditor-external"
  - "beneficial-ownership-13d-13g"
adjacent_bundles:
  []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc:
    []
  soc:
    []
  isco_08:
    []
  esco:
    []
limitations:
  - "This bundle is not legal, securities, accounting, audit, tax, investment, governance, or disclosure advice."
  - "Scenario-specific answers require current SEC sources, issuer-specific evidence, disclosure controls, and qualified review."
  - "Do not infer issuer status, filing deadlines, form items, materiality, disclosure text, EDGAR behavior, or compliance status without evidence."
safety_notes:
  - "Minimize sensitive issuer, financial, personal, security, incident, trading, compensation, customer, and employee data in prompts and examples."
  - "Require explicit confirmation before live filing, public disclosure, investor communication, trading-policy, governance, financial reporting, data export, or regulatory actions."
  - "Route final reliance to qualified counsel, accounting or audit professionals, disclosure committee members, governance leaders, or management as appropriate."
timestamp: "2026-07-11T00:00:00Z"
evaluation_summary:
  status: "blocked"
  last_evaluated: "2026-07-11"
  method: "baseline-vs-okb-rubric"
  display_summary: "Measured evaluation is blocked pending generated baseline and bundle-assisted outputs plus reviewer scoring."
  evidence_note: "No measured performance claim is made for this bundle."
---

# SEC Reporting & Disclosure (US Public Companies)

Source-aware compliance bundle for SEC reporting and disclosure source triage, evidence collection, and review-ready decision support for US public companies.

## Required Answer Habit

Include a short **Source note** naming the official SEC source category, current source inspected, issuer evidence used, and missing source or fact still needed before a conclusion is reliable.

## Start Here

- [overview.md](overview.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)

## Core Source Categories

- Exchange Act periodic and current reporting, including Form 10-K, Form 10-Q, and Form 8-K source inspection.
- Proxy statement and shareholder governance disclosure, including Regulation 14A source inspection.
- Beneficial ownership and insider reporting, including Section 16 and Schedules 13D/13G source inspection.
- Executive compensation, insider trading policy and trading arrangement, conflict minerals, cybersecurity, EDGAR, Inline XBRL, and Regulation FD source inspection.

## Use Boundary

Use this bundle to prepare reviewable source triage, evidence checklists, and draft briefs. Do not use it to make final filing, materiality, disclosure, securities-law, accounting, audit, tax, governance, or investor-communication decisions without current official sources, issuer evidence, explicit user confirmation, and qualified review.
