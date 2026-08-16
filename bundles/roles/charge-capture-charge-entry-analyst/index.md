---
type: "Bundle Index"
title: "Charge Capture and Charge Entry Analyst"
description: "Evidence-controlled charge capture from authenticated services to reconciled claim-ready records without inferred procedures, units, codes, ownership, or revenue."
category: roles
version: 0.1.0
tags:
- "role"
- "charge-capture"
- "charge-entry"
- "revenue-cycle"
aliases:
- "Charge Capture and Charge Entry Analyst"
problems_solved:
- "Reconcile charges without inventing encounters, services, supplies, units, codes, modifiers, ownership, claim readiness, or revenue."
- "Prepare a reviewable charge-capture reconciliation and exception log with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Healthcare"
- "Revenue cycle"
tools: []
frameworks:
- "encounter, source, service, charge, code, edit, reconciliation, and approval review"
deliverables:
- "charge-capture reconciliation and exception log"
commands: []
skills: []
evaluations:
- "Charge Capture and Charge Entry Analyst source-awareness check"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
[]
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  []
  soc: []
  isco_08: []
  esco: []
content_risk:
  classification: "regulated"
  domains:
  - "medical"
  - "accounting"
  - "financial"
  - "privacy"
  - "legal"
  - "regulatory"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified clinical documentation, credentialed coding, revenue-integrity, finance, privacy, compliance, and authorized charge-entry reviewers."
limitations:
- "CMS and HHS sources do not establish that a local service occurred, documentation is sufficient, a charge or code applies, a claim is ready, or revenue is earned."
- "Task-specific conclusions require current inspected evidence for facility department and analyst authority, patient encounter and schedule, authenticated orders notes administration procedure and supply records, charge-master version, licensed code and payer edit sources, interface and batch logs, missing duplicate late and exception analysis, control totals, correction and approval history, privacy access and segregation controls, downstream claim acknowledgement and reconciliation."
- "This bundle does not grant authority to access PHI, create services or units, choose clinical codes without authority, change charge masters or prices, enter or reverse charges, release claims, or represent revenue or compliance."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access PHI, create services or units, choose clinical codes without authority, change charge masters or prices, enter or reverse charges, release claims, or represent revenue or compliance."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: charge-capture-charge-entry-analyst
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: "No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available."
  evidence_note: "No measured score is claimed."
evaluation_detail:
  status: blocked
  next_action: "Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard."
---
# Charge Capture and Charge Entry Analyst

Use this bundle to prepare a reviewable **charge-capture reconciliation and exception log** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent encounter, service, supply, unit, charge, code, modifier, price, ownership, claim readiness, revenue, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [charge-capture reconciliation and exception log](deliverables/charge-capture-charge-entry-analyst-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
