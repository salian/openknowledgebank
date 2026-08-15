---
type: "Bundle Index"
title: "Threat Model"
description: "Evidence-grounded threat model covering system scope, assets, trust boundaries, actors, abuse cases, controls, residual risk, and ownership."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "threat-modeling"
- "security"
aliases:
- "Threat Model"
problems_solved:
- "Model threats without inventing architecture, assets, adversary capability, vulnerabilities, control effectiveness, exploitability, or risk acceptance."
- "Prepare a reviewable threat model and mitigation decision record with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Cybersecurity"
- "Software"
tools: []
frameworks:
- "system, asset, trust-boundary, threat, control, residual-risk, and review analysis"
deliverables:
- "threat model and mitigation decision record"
commands: []
skills: []
evaluations:
- "Threat Model source-awareness check"
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
  - "security"
  - "privacy"
  - "legal"
  - "safety"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified system owner, security architect, threat modeler, privacy, legal, safety, operations, and risk-acceptance reviewers."
limitations:
- "NIST and OWASP sources describe threat-modeling approaches but do not establish local architecture, assets, threats, vulnerabilities, likelihood, control operation, residual risk, compliance, or risk-acceptance authority."
- "Task-specific conclusions require current inspected evidence for system and environment versions, architecture and data-flow diagrams, asset and data classifications, identity and trust boundaries, dependency and supplier evidence, threat intelligence scope and date, abuse cases, control design and test evidence, vulnerability records, ranking criteria and uncertainty, mitigations and owners, residual-risk decisions, reviews, and approvals."
- "This bundle does not grant authority to access or test systems without authorization, expose sensitive architecture, declare vulnerabilities, change controls, exploit weaknesses, accept risk, claim security or compliance, or publish the model."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access or test systems without authorization, expose sensitive architecture, declare vulnerabilities, change controls, exploit weaknesses, accept risk, claim security or compliance, or publish the model."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: threat-model
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
# Threat Model

Use this bundle to prepare a reviewable **threat model and mitigation decision record** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent system boundary, asset, data flow, trust relationship, actor capability, threat, vulnerability, exploitability, likelihood, control effectiveness, residual risk, security, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [threat model and mitigation decision record](deliverables/threat-model-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
