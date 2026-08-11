---
type: Bundle Index
title: Dietitian and Nutritionist
description: Evidence-grounded preparation for nutrition assessment, care goals, education, monitoring, documentation, coordination, and referral within verified professional scope.
category: roles
version: 0.1.0
tags:
- dietitian
- nutrition
- clinical-care
aliases:
- Registered dietitian
- Nutritionist
problems_solved:
- Assess Dietitian and Nutritionist scope and evidence.
- Prepare a reviewable work product without inventing local facts or conclusions.
industries:
- Healthcare
- Public Health
- Food and Nutrition
tools:
[]
frameworks:
- evidence-grounded role workflow
deliverables:
- nutrition assessment and care-planning brief
commands: []
skills: []
evaluations:
- Dietitian and Nutritionist source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- epic
- hipaa
- fda-dietary-supplement-cgmp-ndi
adjacent_bundles:
[]
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 29-1031.00
  soc:
  []
  isco_08:
  []
  esco: []
content_risk:
  classification: ymyl
  domains:
  - medical
  - employment
  - privacy
  - safety
  - legal
  - regulatory
  professional_review:
    status: not_reviewed
    required_qualification: A qualified role owner, operational reviewer, and legal, safety, or other professional appropriate to the task and jurisdiction.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for current authoritative sources, objective, scope, local records, constraints, decision criteria, conflicts, assumptions, approvals, validation evidence, and accountable ownership.
- This bundle does not grant authority to diagnose or treat, prescribe or order, change a medical record or care plan, recommend unsafe restriction or supplementation, disclose health information, contact a patient or clinician, or represent clinical approval.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before taking any action to diagnose or treat, prescribe or order, change a medical record or care plan, recommend unsafe restriction or supplementation, disclose health information, contact a patient or clinician, or represent clinical approval.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: dietitian-nutritionist
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
# Dietitian and Nutritionist

Use this bundle to prepare a reviewable **nutrition assessment and care-planning brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

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
- [Dietitian and Nutritionist Source-Aware Guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [nutrition assessment and care-planning brief](deliverables/dietitian-nutritionist-brief.md)
- [Quality check](evaluations/source-awareness-check.md)

