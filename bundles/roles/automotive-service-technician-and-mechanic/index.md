---
type: Bundle Index
title: Automotive Service Technician and Mechanic
description: Evidence-grounded planning for vehicle diagnosis, repair options, parts and labor estimates, service records, quality checks, and customer authorization.
category: roles
version: 0.1.0
tags:
- automotive-service
- vehicle-repair
- diagnostics
aliases:
- Automotive technician
- Auto mechanic
problems_solved:
- Assess Automotive Service Technician and Mechanic scope and evidence.
- Prepare a reviewable work product without inventing local facts or conclusions.
industries:
- Automotive
- Maintenance and Repair
tools:
[]
frameworks:
- evidence-grounded role workflow
deliverables:
- automotive diagnostic and service-work brief
commands: []
skills: []
evaluations:
- Automotive Service Technician and Mechanic source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- osha
adjacent_bundles:
[]
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 49-3023.00
  soc:
  []
  isco_08:
  []
  esco: []
content_risk:
  classification: regulated
  domains:
  - employment
  - safety
  - legal
  - financial
  professional_review:
    status: not_reviewed
    required_qualification: A qualified role owner, operational reviewer, and legal, safety, or other professional appropriate to the task and jurisdiction.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for current authoritative sources, objective, scope, local records, constraints, decision criteria, conflicts, assumptions, approvals, validation evidence, and accountable ownership.
- This bundle does not grant authority to operate or move a vehicle, perform diagnosis or repair, disable safety or emissions controls, order parts, charge a customer, release a vehicle, or represent roadworthiness.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before taking any action to operate or move a vehicle, perform diagnosis or repair, disable safety or emissions controls, order parts, charge a customer, release a vehicle, or represent roadworthiness.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: automotive-service-technician-and-mechanic
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
# Automotive Service Technician and Mechanic

Use this bundle to prepare a reviewable **automotive diagnostic and service-work brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

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
- [Automotive Service Technician and Mechanic Source-Aware Guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [automotive diagnostic and service-work brief](deliverables/automotive-service-technician-and-mechanic-brief.md)
- [Quality check](evaluations/source-awareness-check.md)

