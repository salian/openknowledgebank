---
type: "Bundle Index"
title: "OpenEMR"
description: "Source-aware guidance for OpenEMR electronic health records, practice management, scheduling, clinical documentation, prescribing, billing, interoperability, APIs, access, certification, and deployment."
category: tools
version: 0.1.0
tags:
- "tool"
- "source-aware"
aliases:
- "OpenEMR EHR"
problems_solved:
- "Review product use from current official sources and inspected local evidence."
- "Prepare a controlled decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "OpenEMR"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "OpenEMR clinical, interoperability, and deployment review brief"
commands: []
skills: []
evaluations:
- "OpenEMR source-awareness check"
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
  classification: "ymyl"
  domains:
  - "financial"
  - "legal"
  - "medical"
  - "privacy"
  - "regulatory"
  - "safety"
  - "security"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and domain, privacy, security, legal, financial, safety, employment, tax, healthcare, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for current product identity and lifecycle, account or deployment, plan and region, users and roles, configuration, source data, permissions, integrations, logs, controls, validation, rollback, and approval evidence."
- "This bundle does not grant authority to access or change patient records, prescribe, order or document care, exchange protected health information, submit claims, change billing or access, install modules, upgrade systems, or make clinical, eligibility, payment, or compliance decisions."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before access or change patient records, prescribe, order or document care, exchange protected health information, submit claims, change billing or access, install modules, upgrade systems, or make clinical, eligibility, payment, or compliance decisions."
timestamp: "2026-08-14T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: openemr
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
# OpenEMR

Use this bundle to prepare a reviewable **OpenEMR clinical, interoperability, and deployment review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent patient identity, diagnosis, medication, prescription, order, clinical status, eligibility, claim, payment, interoperability, certification applicability, privacy compliance, backup, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [OpenEMR clinical, interoperability, and deployment review brief](deliverables/openemr-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
