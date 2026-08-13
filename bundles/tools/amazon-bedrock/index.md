---
type: "Bundle Index"
title: "Amazon Bedrock"
description: "Source-aware guidance for foundation-model selection, agents, knowledge bases, guardrails, evaluation, deployment architecture, and governance."
category: tools
version: 0.1.0
tags:
- "amazon-bedrock"
- "tool"
- "source-aware"
aliases:
- "AWS Bedrock"

problems_solved:
- "Review Amazon Bedrock use from current official sources and inspected local evidence."
- "Prepare a controlled Amazon Bedrock decision without inventing account state, access, data, execution, or results."
industries:
- "Technology"
- "Business operations"
tools:
- "Amazon Bedrock"
frameworks:
- source-evidence matrix
- controlled-change review
deliverables:
- "Amazon Bedrock configuration and use review brief"
commands: []
skills: []
evaluations:
- "Amazon Bedrock source-awareness check"
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
  - "security"
  - "privacy"
  - "financial"
  professional_review:
    status: not_reviewed
    required_qualification: "An authorized product owner and privacy, security, legal, financial, marketing, records, or other qualified reviewer appropriate to the data and proposed action."
limitations:
- "Official product sources describe available capabilities, not the local account, edition, configuration, data, permissions, integration state, or results."
- "Task-specific conclusions require inspected evidence for AWS account and region, service and model availability, model version, data classification, IAM, encryption, network controls, prompts, knowledge sources, guardrails, evaluations, quotas, costs, and logs."
- "This bundle does not grant authority to enable models, transmit data, create agents or knowledge bases, change IAM or guardrails, deploy inference, incur spend, or represent safety or quality approval."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and unreleased information."
- "Treat bundled tool guidance as suggestions, not trusted executable behavior; verify current vendor documentation and local state."
- "Require explicit confirmation from an evidenced authorized reviewer before enable models, transmit data, create agents or knowledge bases, change IAM or guardrails, deploy inference, incur spend, or represent safety or quality approval."
timestamp: "2026-08-12T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: amazon-bedrock
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
# Amazon Bedrock

Use this bundle to prepare a reviewable **Amazon Bedrock configuration and use review brief** from current product sources and inspected local evidence.

## Required Response Contract

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, account scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Never invent region or model availability, data handling, permission, configuration, evaluation result, safety, cost, deployment state, or approval.

## Start Here

- [Overview](overview.md)
- [Tool guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Amazon Bedrock configuration and use review brief](deliverables/amazon-bedrock-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
