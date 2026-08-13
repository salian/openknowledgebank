---
type: "Bundle Index"
title: "Customer.io"
description: "Source-aware guidance for profiles, events, objects, segments, campaigns, broadcasts, journeys, messaging, surveys, and metrics. and controlled Customer.io use."
category: tools
version: 0.1.0
tags:
- "customer-io"
- "tool"
- "source-aware"
aliases:
- "CustomerIO"
- "Customer.io Journeys"
problems_solved:
- "Review Customer.io use from current official sources and inspected local evidence."
- "Prepare a controlled Customer.io decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "Customer.io"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "Customer.io configuration and use review brief"
commands: []
skills: []
evaluations:
- "Customer.io source-awareness check"
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
- "Task-specific conclusions require inspected evidence for workspace and region, API and SDK versions, credentials, profiles and identifiers, event and object schemas, consent and suppression, segments, campaigns and workflows, channels and senders, rate limits, AI or MCP scopes, integrations, reporting webhooks, metrics, and logs."
- "This bundle does not grant authority to ingest or export profiles and events, merge identities, change consent, activate campaigns or workflows, send messages, connect AI or MCP, use credentials, or represent delivery or conversion."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before ingest or export profiles and events, merge identities, change consent, activate campaigns or workflows, send messages, connect AI or MCP, use credentials, or represent delivery or conversion."
timestamp: "2026-08-13T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: customer-io
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
# Customer.io

Use this bundle to prepare a reviewable **Customer.io configuration and use review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent profile identity, consent, event accuracy, segment membership, personalization, AI action, message delivery, conversion, attribution, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Customer.io configuration and use review brief](deliverables/customer-io-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
