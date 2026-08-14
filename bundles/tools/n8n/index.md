---
type: "Bundle Index"
title: "n8n"
description: "Source-aware guidance for n8n workflow automation, nodes, credentials, triggers, executions, code, AI workflows, human review, APIs, Cloud, and self-hosted deployment."
category: tools
version: 0.1.0
tags:
- "tool"
- "source-aware"
aliases:
- "n8n Workflow Automation"
- "n8n AI Workflow Automation"
problems_solved:
- "Review product use from current official sources and inspected local evidence."
- "Prepare a controlled decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "n8n"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "n8n workflow, credential, and deployment review brief"
commands: []
skills: []
evaluations:
- "n8n source-awareness check"
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
  - "legal"
  - "privacy"
  - "safety"
  - "security"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and domain, privacy, security, legal, financial, safety, employment, tax, healthcare, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for current product identity and lifecycle, account or deployment, plan and region, users and roles, configuration, source data, permissions, integrations, logs, controls, validation, rollback, and approval evidence."
- "This bundle does not grant authority to store credentials, call external or production systems, execute code or AI tools, activate schedules or webhooks, process personal data, install community nodes, change access, deploy or upgrade instances, or represent execution, delivery, security, or business results."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before store credentials, call external or production systems, execute code or AI tools, activate schedules or webhooks, process personal data, install community nodes, change access, deploy or upgrade instances, or represent execution, delivery, security, or business results."
timestamp: "2026-08-14T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: n8n
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
# n8n

Use this bundle to prepare a reviewable **n8n workflow, credential, and deployment review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent credential scope, node behavior, input or output data, workflow execution, AI tool action, human review, webhook exposure, community-node safety, API result, deployment, availability, compliance, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [n8n workflow, credential, and deployment review brief](deliverables/n8n-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
