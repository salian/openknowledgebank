---
type: Bundle Index
title: Azure AI Foundry
description: Source-aware tool bundle for project, model catalog, deployment, prompt, agent, evaluation, content filter, quota, identity, network, and monitoring review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: tools
version: 0.1.0
tags:
- azure-ai-foundry
- tool
- source-aware
aliases:
- Azure AI Foundry
problems_solved:
- Prepare a azure ai foundry review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools:
- Azure AI Foundry
frameworks:
- source-evidence matrix
- Azure AI Foundry application matrix
- qualified-review gate
deliverables:
- Azure AI Foundry review brief
commands: []
skills: []
evaluations:
- Azure AI Foundry source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- ai-ml-product-manager
- openai-chatgpt
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
limitations:
- Use the listed authoritative or identified source surfaces for general Azure AI Foundry guidance; local facts, configuration, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for Azure tenant, subscription, region, Foundry project, model and version, deployment type, quota, endpoint and authentication method, prompts, tools and data connections, evaluation dataset and metrics, content filters, networking, logging, costs, approvals, and rollback.
- Do not infer model availability, output quality, safety, quota, cost, data handling, deployment state, evaluation result, or production readiness.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that deploy or invoke models or agents, enable tools, change content filters, quotas, identities, networks, endpoints, or data connections; send sensitive data; expose credentials; or incur spend.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: azure-ai-foundry
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 15
  okb_score: 35
  absolute_lift: 20
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 5
    okb_score: 11
    max_score: 12
  - task: configuration-risk-review
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: source-or-state-reconciliation
    baseline_score: 5
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 35/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# Azure AI Foundry

Source-aware tool bundle for project, model catalog, deployment, prompt, agent, evaluation, content filter, quota, identity, network, and monitoring review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and domain actions prohibited without explicit approval.
5. **Source note** - name authoritative source URLs used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each supports. When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate a generic role.

Facts explicitly stated in the request belong under `Provided` as `Prompt-provided request`; do not move them to `Assumed`. Do not assign an owner, author, date, or version unless the request states it.

## Start Here

- [overview.md](overview.md)
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/azure-ai-foundry-brief.md](deliverables/azure-ai-foundry-brief.md)
