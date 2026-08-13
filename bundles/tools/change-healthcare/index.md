---
type: "Bundle Index"
title: "Optum APIs (formerly Change Healthcare)"
description: "Source-aware guidance for current optum developer apis and healthcare administrative, clinical, payment, eligibility, claims, and interoperability workflows formerly associated with change healthcare. and controlled Optum APIs (formerly Change Healthcare) use."
category: tools
version: 0.1.0
tags:
- "change-healthcare"
- "tool"
- "source-aware"
aliases:
- "Change Healthcare"
- "Optum Developer"
- "Optum healthcare APIs"
problems_solved:
- "Review Optum APIs (formerly Change Healthcare) use from current official sources and inspected local evidence."
- "Prepare a controlled Optum APIs (formerly Change Healthcare) decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "Optum APIs (formerly Change Healthcare)"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "Optum APIs (formerly Change Healthcare) configuration and use review brief"
commands: []
skills: []
evaluations:
- "Optum APIs (formerly Change Healthcare) source-awareness check"
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
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
content_risk:
  classification: "regulated"
  domains:
  - "medical"
  - "privacy"
  - "security"
  - "financial"
  - "regulatory"
  - "legal"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and privacy, security, legal, financial, clinical, employment, records, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for current product ownership and migration status, API product and version, environment, organization and trading partners, credentials and scopes, patient and member identity, consent and authorization, transaction formats, claims and eligibility data, payer rules, mappings, acknowledgments, errors, integrations, security controls, and audit logs."
- "This bundle does not grant authority to access or transmit protected health information, query eligibility, submit or alter claims or payments, change trading-partner configuration, issue credentials, call production APIs, or represent clinical, coverage, payment, or compliance outcomes."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before access or transmit protected health information, query eligibility, submit or alter claims or payments, change trading-partner configuration, issue credentials, call production APIs, or represent clinical, coverage, payment, or compliance outcomes."
timestamp: "2026-08-13T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: change-healthcare
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
# Optum APIs (formerly Change Healthcare)

Use this bundle to prepare a reviewable **Optum APIs (formerly Change Healthcare) configuration and use review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent current product applicability, patient or member identity, authorization, eligibility or coverage, code or claim accuracy, payer adjudication, payment status, API result, regulatory compliance, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Optum APIs (formerly Change Healthcare) configuration and use review brief](deliverables/change-healthcare-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
