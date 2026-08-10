---
type: Bundle Index
title: Generally Accepted Auditing Standards
description: Source-aware guidance for identifying applicable AICPA GAAS, planning engagements, evidence, risk, documentation, reporting, and professional review.
category: frameworks
version: 0.1.0
tags:
- gaas
- auditing
- assurance
aliases:
- AICPA GAAS
problems_solved:
- Apply Generally Accepted Auditing Standards using inspectable evidence.
- Review assumptions, definitions, calculations, and decision boundaries.
- Prepare a controlled recommendation without inventing local facts or outcomes.
industries:
- Cross-industry
- Operations
- Professional services
tools:
[]
frameworks:
- Generally Accepted Auditing Standards
deliverables:
- GAAS applicability and audit-planning brief
commands: []
skills: []
evaluations:
- Generally Accepted Auditing Standards source-awareness check
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
  - accounting
  - financial
  - legal
  - regulatory
  professional_review:
    status: not_reviewed
    required_qualification: A qualified independent CPA or auditor, accounting, audit-quality, legal, regulatory, or industry professional appropriate to the engagement and jurisdiction.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for entity, reporting period, engagement type, issuer status, jurisdiction, applicable standards and effective dates, financial statements, assertions, materiality, risks, internal controls, evidence, specialists, independence, ethics, documentation, findings, reporting basis, owners, and approvals.
- This bundle does not grant authority to accept or modify an engagement, determine compliance, set materiality, rely on controls, conclude on misstatement, issue an opinion or report, communicate findings, or file externally.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before accept or modify an engagement, determine compliance, set materiality, rely on controls, conclude on misstatement, issue an opinion or report, communicate findings, or file externally.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: gaas
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
# Generally Accepted Auditing Standards

Use this bundle to prepare a reviewable **GAAS applicability and audit-planning brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent Applicable standard, issuer and engagement status, effective date, independence, materiality, risk, control design or operation, evidence sufficiency and appropriateness, misstatement, going concern, report wording, compliance, and audit opinion.

## Start Here

- [Overview](overview.md)
- [Generally Accepted Auditing Standards Source-Aware Guide](framework.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [GAAS applicability and audit-planning brief](deliverables/gaas-brief.md)
- [Quality check](evaluations/source-awareness-check.md)

