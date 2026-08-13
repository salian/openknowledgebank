---
type: "Bundle Index"
title: "Adobe Analytics"
description: "Source-aware guidance for digital analytics implementation, data collection, dimensions, metrics, attribution, reporting, and governance."
category: tools
version: 0.1.0
tags:
- "adobe-analytics"
- "tool"
- "source-aware"
aliases:
- "Adobe Analytics platform"

problems_solved:
- "Review Adobe Analytics use from current official sources and inspected local evidence."
- "Prepare a controlled Adobe Analytics decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "Adobe Analytics"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "Adobe Analytics configuration and use review brief"
commands: []
skills: []
evaluations:
- "Adobe Analytics source-awareness check"
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
  - "privacy"
  - "security"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and privacy, security, legal, financial, marketing, records, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for contract and product version, report suites, datastreams, variables, processing rules, identities, consent, segments, metrics, attribution settings, exports, and logs."
- "This bundle does not grant authority to change data collection or processing, publish segments, export person-level data, alter attribution, deploy tags, or represent findings as validated."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before change data collection or processing, publish segments, export person-level data, alter attribution, deploy tags, or represent findings as validated."
timestamp: "2026-08-12T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: adobe-analytics
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
# Adobe Analytics

Use this bundle to prepare a reviewable **Adobe Analytics configuration and use review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent implementation state, variable meaning, identity, consent, metric definition, segment, attribution result, data quality, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Adobe Analytics configuration and use review brief](deliverables/adobe-analytics-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
