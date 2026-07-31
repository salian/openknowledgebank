---
type: Bundle Index
title: ChatGPT / OpenAI API
description: Source-aware tool bundle for ChatGPT and OpenAI API use-case, model, tool, data, evaluation, and deployment review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: tools
version: 0.1.0
tags:
- openai-chatgpt
- openai
- tool
aliases:
- ChatGPT / OpenAI API
problems_solved:
- Prepare a OpenAI implementation and risk brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools:
- ChatGPT / OpenAI API
frameworks:
- source-evidence matrix
- ChatGPT and OpenAI API use-case, model, tool, data, evaluation, and deployment review review matrix
- qualified-review gate
deliverables:
- OpenAI implementation and risk brief
commands: []
skills: []
evaluations:
- ChatGPT / OpenAI API source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
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
- Use the listed authoritative sources for general role or tool behavior; local configuration, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for product surface, organization, project, account, environment, API and SDK versions; model ID or snapshot, inputs, outputs, prompts, tools, function schemas, files, vector stores, external services, authentication, permissions, retention and data controls, regional requirements, safety policy, eval data and results, latency, usage, cost, monitoring, fallback, and approvals.
- Do not infer current capability, model behavior, output accuracy, safety, retention setting, regional eligibility, cost, tool result, or production readiness.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that send sensitive data, call external tools, upload files, create or delete resources, change retention controls, expose credentials, deploy, or incur usage charges.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: openai-chatgpt
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 11
  okb_score: 36
  absolute_lift: 25
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 12
    max_score: 12
  - task: configuration-risk-review
    baseline_score: 4
    okb_score: 12
    max_score: 12
  - task: metric-or-state-reconciliation
    baseline_score: 5
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 11/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# ChatGPT / OpenAI API

Source-aware tool bundle for ChatGPT and OpenAI API use-case, model, tool, data, evaluation, and deployment review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name authoritative source URLs used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each supports. When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate a generic role.

Facts explicitly stated in the request belong under `Provided` as `Prompt-provided request`; do not move them to `Assumed`. Do not assign an owner, author, date, or version unless the request states it.

## Start Here

- [overview.md](overview.md)
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/openai-chatgpt-brief.md](deliverables/openai-chatgpt-brief.md)
