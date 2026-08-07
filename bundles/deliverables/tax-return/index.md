---
type: Bundle Index
title: Tax Return
description: Source-aware deliverable bundle for preparing and reviewing a U.S. federal individual income tax return from current instructions and taxpayer evidence.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- tax return
- federal income tax
- Form 1040
- tax preparation
- deliverable
aliases:
- Federal Individual Income Tax Return
- Individual Tax Return
problems_solved:
- Organize a reviewable return package from supplied evidence.
- Trace form and schedule decisions to current official instructions.
- Prevent invented taxpayer facts, unsupported filing positions, and false filing claims.
industries:
- accounting
- tax services
- financial services
tools: []
frameworks:
- evidence-status ledger
- form applicability map
- return reconciliation
deliverables:
- draft federal individual income tax return package
- evidence and exception register
- filing readiness review
commands: []
skills: []
evaluations:
- Tax Return quality check
okb_bundle_id: tax-return
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- tax-accountant-tax-specialist
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
- This bundle is a preparation and review aid, not tax or legal advice, an audit opinion, representation before a taxing authority, or proof that a return was filed or accepted.
- It covers a U.S. federal individual income tax return workflow; other return types and jurisdictions require their own current authority-specific sources.
- Taxpayer facts, filing positions, forms, schedules, calculations, elections, dates, signatures, payments, and acknowledgements require current instructions and supplied evidence.
safety_notes:
- Minimize, redact, and restrict access to tax return information and identity data.
- Require explicit taxpayer authorization before signing, filing, transmitting, paying, or disclosing return information.
- Route material uncertainty and filing-position decisions to a qualified tax professional.
timestamp: '2026-08-07T00:00:00Z'
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No reviewed public-safe benchmark task set, runnable evaluator configuration, or reviewer-scored aggregate results were available for this run.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Create and approve three public-safe tasks including an empty-evidence case, run identical baseline and bundle-assisted conditions, obtain reviewer-scored aggregate results, and build a listing scorecard.
---

# Tax Return

Use this bundle to prepare and review a U.S. federal individual income tax return package from current official instructions and taxpayer-authorized evidence.

Start with the [deliverable contract](deliverable.md), follow the [preparation and review workflow](workflow.md), and apply the [quality check](evaluations/quality-check.md).

This bundle does not file, sign, transmit, pay, or establish that a return has been accepted.
