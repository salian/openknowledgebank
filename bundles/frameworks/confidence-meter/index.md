---
type: "Bundle Index"
title: "Confidence Meter"
description: "Source-aware use of Itamar Gilad's confidence assessment to make evidence strength explicit in product decisions."
category: frameworks
version: 0.1.0
tags:
- "framework"
- "source-aware"
aliases:
- "Product Confidence Meter"
- "Confidence Assessment"
problems_solved:
- "Apply a named framework without inventing inputs, applicability, calculations, or outcomes."
- "Produce a reviewable decision artifact with explicit evidence, assumptions, alternatives, validation, and authority boundaries."
industries:
- "Cross-industry"
- "Business operations"
tools: []
frameworks:
- "Confidence Meter"
deliverables:
- "evidence-confidence and next-test brief"
commands: []
skills: []
evaluations:
- "Confidence Meter source-awareness check"
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
  - "financial"
  - "legal"
  - "privacy"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized decision owner and qualified domain reviewer appropriate to the framework, evidence, jurisdiction, and proposed action."
limitations:
- "Framework sources describe generalized concepts and methods; they do not establish local applicability, inputs, decisions, authority, or outcomes."
- "Task-specific conclusions require current inspected evidence for current source definitions and scope, local objective and context, inspected inputs, assumptions, alternatives, calculations, constraints, outcomes, validation, decision ownership, and approval evidence."
- "This bundle does not grant authority to commit roadmap, launch products or experiments, collect user data, spend funds, or represent evidence certainty, demand, impact, or approval."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to commit roadmap, launch products or experiments, collect user data, spend funds, or represent evidence certainty, demand, impact, or approval."
timestamp: "2026-08-14T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: confidence-meter
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
# Confidence Meter

Use this bundle to prepare a reviewable **evidence-confidence and next-test brief** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent evidence quality, score objectivity, customer demand, causal impact, forecast accuracy, commercial outcome, or approval.

## Start Here

- [Overview](overview.md)
- [Framework guide](framework.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [evidence-confidence and next-test brief](deliverables/confidence-meter-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
