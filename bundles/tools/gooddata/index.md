---
type: "Bundle Index"
title: "GoodData"
description: "Source-aware guidance for GoodData semantic models, metrics, analytics, dashboards, embedding, APIs, permissions, and governance."
category: tools
version: 0.1.0
tags:
- "gooddata"
- "tool"
- "source-aware"
aliases:
- "GoodData Cloud"
- "GoodData Analytics"
problems_solved:
- "Review GoodData use from current official sources and inspected local evidence."
- "Prepare a controlled analytics decision without inventing schema, metric, data, permission, or result state."
industries:
- "Technology"
- "Business operations"
tools:
- "GoodData"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "GoodData semantic analytics review brief"
commands: []
skills: []
evaluations:
- "GoodData source-awareness check"
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
  - "financial"
  - "privacy"
  - "security"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized analytics owner and data, privacy, security, financial, or other qualified reviewer appropriate to the data and decision."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for deployment and edition, workspaces, data sources and lineage, semantic model, metric definitions, filters, permissions, dashboards, embeds, APIs, schedules, logs, validation, rollback, and approvals."
- "This bundle does not grant authority to connect or expose data, change models or metrics, publish dashboards, embed analytics, schedule exports, change access, or represent analytical or business results."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before connect or expose data, change models or metrics, publish dashboards, embed analytics, schedule exports, change access, or represent analytical or business results."
timestamp: "2026-08-13T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: gooddata
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
# GoodData

Use this bundle to prepare a reviewable **GoodData semantic analytics review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent schema, lineage, metric definition, filter context, data freshness, access, dashboard state, calculation accuracy, forecast, business conclusion, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [GoodData semantic analytics review brief](deliverables/gooddata-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
