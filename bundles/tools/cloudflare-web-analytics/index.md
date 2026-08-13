---
type: "Bundle Index"
title: "Cloudflare Web Analytics"
description: "Source-aware guidance for page-view and real-user performance analytics, core web vitals, dimensions, filters, and rules. and controlled Cloudflare Web Analytics use."
category: tools
version: 0.1.0
tags:
- "cloudflare-web-analytics"
- "tool"
- "source-aware"
aliases:
- "Cloudflare Analytics"
- "Cloudflare WebAnalytics"
problems_solved:
- "Review Cloudflare Web Analytics use from current official sources and inspected local evidence."
- "Prepare a controlled Cloudflare Web Analytics decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "Cloudflare Web Analytics"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "Cloudflare Web Analytics configuration and use review brief"
commands: []
skills: []
evaluations:
- "Cloudflare Web Analytics source-awareness check"
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
  - "legal"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and privacy, security, legal, financial, clinical, employment, records, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for Cloudflare account and plan, zone or site ownership, setup method and beacon version, tracked hostnames and paths, rules and filters, data origin and collection, privacy and consent requirements, dimensions and metric definitions, sampling or limits, time range, timezone, bot and cache effects, notifications, and change history."
- "This bundle does not grant authority to enable or disable collection, add or change beacon code, rules or filters, expose visitor data, change site configuration, export reports, or represent traffic, performance, privacy, or conversion outcomes."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before enable or disable collection, add or change beacon code, rules or filters, expose visitor data, change site configuration, export reports, or represent traffic, performance, privacy, or conversion outcomes."
timestamp: "2026-08-13T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: cloudflare-web-analytics
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
# Cloudflare Web Analytics

Use this bundle to prepare a reviewable **Cloudflare Web Analytics configuration and use review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent site ownership, collection state, visitor identity, consent applicability, metric definition, data completeness, bot treatment, Core Web Vital result, attribution, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Cloudflare Web Analytics configuration and use review brief](deliverables/cloudflare-web-analytics-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
