---
type: Bundle Index
title: Epic
description: Source-aware guidance for Epic interoperability, FHIR apps, clinical data, authorization, validation, and governed implementation.
category: tools
version: 0.1.0
tags:
- epic
- ehr
- healthcare-interoperability
aliases:
- EpicCare
- Epic on FHIR
problems_solved:
- Plan evidence-grounded Epic work.
- Review configuration, data, control, and operational constraints.
- Prepare controlled changes without inventing local state or outcomes.
industries:
- Technology
- Operations
- Cross-industry
tools:
- Epic
frameworks:
- evidence-grounded system change
deliverables:
- Epic interoperability and clinical-safety brief
commands: []
skills: []
evaluations:
- Epic source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
[]
adjacent_bundles:
[]
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  []
  soc:
  []
  isco_08:
  []
  esco: []
content_risk:
  classification: ymyl
  domains:
  - medical
  - privacy
  - security
  - safety
  - legal
  professional_review:
    status: not_reviewed
    required_qualification: A qualified Epic, clinical informatics, interoperability, healthcare, patient-safety, privacy, security, or legal professional appropriate to the organization and use case.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for organization, Epic version, environment, endpoint, supported FHIR resources, SMART launch, OAuth scopes, patient and encounter context, clinical workflow, data mappings, consent, validation, monitoring, owners, and approvals.
- This bundle does not grant authority to access or alter health records, register or launch apps, use credentials, make clinical interpretations, change workflows, transmit protected data, or deploy integrations.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before access or alter health records, register or launch apps, use credentials, make clinical interpretations, change workflows, transmit protected data, or deploy integrations.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: epic
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
# Epic

Use this bundle to prepare a reviewable **Epic interoperability and clinical-safety brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent Environment and endpoint state, supported resources, patient identity, clinical facts, authorization, consent, mapping validity, app behavior, safety, and implementation approval.

## Start Here

- [Overview](overview.md)
- [Epic Source-Aware Guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Epic interoperability and clinical-safety brief](deliverables/epic-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
