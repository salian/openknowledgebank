---
type: Bundle Index
title: Freight Forwarder
description: Evidence-grounded planning for routing, carrier and agent selection, bookings, consolidation, documentation, customs handoffs, charges, tracking, and exceptions.
category: roles
version: 0.1.0
tags:
- freight-forwarding
- international-logistics
- shipment-coordination
aliases:
- International freight forwarder
- Forwarding agent
problems_solved:
- Plan and review Freight Forwarder work from inspected evidence.
- Prepare a controlled work brief without inventing role facts, authority, or outcomes.
industries:
- Logistics
- Transportation
- International Trade
tools: []
frameworks:
- evidence-grounded role workflow
deliverables:
- freight forwarding routing and documentation brief
commands: []
skills: []
evaluations:
- Freight Forwarder source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- bill-of-lading
- c-tpat
- incoterms
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 43-5011.01
  soc: []
  isco_08: []
  esco: []
content_risk:
  classification: regulated
  domains:
  - employment
  - legal
  - financial
  - regulatory
  - safety
  professional_review:
    status: not_reviewed
    required_qualification: A qualified role owner, operational reviewer, and legal, safety, clinical, financial, or other professional appropriate to the task and jurisdiction.
limitations:
- Occupational sources describe generalized work activities; they do not establish a specific person's role, competence, credentials, authority, employer procedures, records, permissions, outcomes, or approval.
- Task-specific conclusions require current inspected evidence for current occupational and professional sources, objective, actual role, jurisdiction, qualifications, local procedures, systems, records, constraints, conflicts, assumptions, approvals, validation evidence, and accountable ownership.
- This bundle does not grant authority to book or consolidate cargo, select or bind a carrier, issue or alter transport documents, make a customs declaration, approve charges, handle dangerous goods, or represent shipper authority.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before taking any action to book or consolidate cargo, select or bind a carrier, issue or alter transport documents, make a customs declaration, approve charges, handle dangerous goods, or represent shipper authority.
timestamp: '2026-08-11T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: freight-forwarder
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard.
---
# Freight Forwarder

Use this bundle to prepare a reviewable **freight forwarding routing and documentation brief** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent the person's role, competence, credentials, authority, employer procedures, system state, records, decisions, outcomes, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [freight forwarding routing and documentation brief](deliverables/freight-forwarder-brief.md)
- [Quality check](evaluations/source-awareness-check.md)

