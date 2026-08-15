---
type: "Bundle Index"
title: "SLO and Error Budget Document"
description: "Evidence-grounded reliability specification covering user journeys, indicators, objectives, budgets, policy, measurement, and governance."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "site-reliability"
- "error-budget"
aliases:
- "SLO and Error Budget Document"
problems_solved:
- "Define SLOs and error budgets without inventing user needs, telemetry, baselines, targets, consumption, policy decisions, or approval."
- "Prepare a reviewable SLO and error budget specification with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Site reliability engineering"
- "Software"
tools: []
frameworks:
- "user-journey, indicator, objective, budget, policy, and measurement review"
deliverables:
- "SLO and error budget specification"
commands: []
skills: []
evaluations:
- "SLO and Error Budget Document source-awareness check"
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
  classification: "ymyl"
  domains:
  - "security"
  - "privacy"
  - "financial"
  - "safety"
  professional_review:
    status: not_reviewed
    required_qualification: "Accountable product, service, reliability, data, security, privacy, finance, safety, and incident-management reviewers."
limitations:
- "Google SRE material provides practitioner guidance and examples, not universal SLO targets or proof of local user needs, telemetry quality, baseline performance, budget consumption, release policy, or readiness."
- "Task-specific conclusions require current inspected evidence for service and user-journey research, ownership and dependencies, indicator specification and telemetry lineage, event taxonomy and exclusions, historical baseline and missingness, calculation code and windows, product and reliability risk decisions, proposed targets and budget, alert tests, incident and release policy, exceptions, reviews, and approvals."
- "This bundle does not grant authority to change telemetry, set targets unilaterally, stop or authorize releases, suppress alerts, waive incidents, claim reliability, or approve production policy."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to change telemetry, set targets unilaterally, stop or authorize releases, suppress alerts, waive incidents, claim reliability, or approve production policy."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: slo-error-budget-doc
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
# SLO and Error Budget Document

Use this bundle to prepare a reviewable **SLO and error budget specification** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent user need, service boundary, event validity, telemetry completeness, baseline, objective, error budget, burn rate, release decision, reliability, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [SLO and error budget specification](deliverables/slo-error-budget-doc-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
