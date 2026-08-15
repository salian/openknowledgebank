---
type: "Bundle Index"
title: "Marketing Attribution Model"
description: "Evidence-grounded specification and review record for assigning marketing credit across defined touchpoints and outcomes."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "marketing-analytics"
- "attribution"
aliases:
- "Marketing Attribution Model"
problems_solved:
- "Document attribution scope, model, inputs, limitations, sensitivity, and decision use without presenting assigned credit as causal proof."
- "Prepare a reviewable marketing attribution model specification with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Marketing"
tools: []
frameworks:
- "attribution scope, model, sensitivity, and validation review"
deliverables:
- "marketing attribution model specification"
commands: []
skills: []
evaluations:
- "Marketing Attribution Model source-awareness check"
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
  - "privacy"
  - "financial"
  - "legal"
  professional_review:
    status: not_reviewed
    required_qualification: "A qualified analytics, privacy, marketing measurement, finance, and legal reviewer for the platforms and jurisdictions."
limitations:
- "Google Analytics documentation describes product-specific models and changing feature availability; assigned credit depends on implementation, consent, observability, scope, and model assumptions and is not universal causal proof."
- "Task-specific conclusions require current inspected evidence for business question, property and platform version, event and conversion definitions, channel rules, identity and consent basis, path data, lookback window, model settings, exclusions, modeled data, sensitivity, validation, and decision owner."
- "This bundle does not grant authority to change tracking or consent settings, identify users, activate audiences, reallocate spend, alter bids, publish performance claims, or represent causal lift."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to change tracking or consent settings, identify users, activate audiences, reallocate spend, alter bids, publish performance claims, or represent causal lift."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: attribution-model
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
# Marketing Attribution Model

Use this bundle to prepare a reviewable **marketing attribution model specification** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent touchpoint identity, conversion completeness, consent, channel classification, model setting, attributed value, causal effect, return on investment, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [marketing attribution model specification](deliverables/attribution-model-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
