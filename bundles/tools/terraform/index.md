---
type: Bundle Index
title: "Terraform"
description: "Source-aware tool bundle for Terraform configuration, providers, state, plans, workspaces, modules, policy, and controlled infrastructure change briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "terraform"
  - "infrastructure-as-code"
  - "cloud"
  - "tool"
aliases:
  - "Terraform"
problems_solved:
  - "Prepare a terraform plan and change brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Cloud infrastructure"
  - "Software"
tools:
  - "Terraform"
frameworks:
  - "source-evidence matrix"
  - "infrastructure-as-code-planning-and-review evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Terraform plan and change brief"
commands: []
skills: []
evaluations:
  - "Terraform source-awareness check"
okb_bundle_id: terraform
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "ai-data-platform-engineer"
  - "cloud-engineer"
  - "devops-engineer"
  - "mlops-engineer"
  - "platform-engineer"
  - "release-build-engineer"
adjacent_bundles: []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Use official Terraform sources for general context; local infrastructure as code planning and review, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for Terraform and provider versions, configuration, modules, variables, and outputs, backend, workspace, state, and lock evidence, provider schemas and credentials boundaries, plan file, refresh behavior, and proposed actions, policy, cost, dependency, and drift evidence, and apply, rollback, and approval controls."
  - "Do not infer configuration, provider schema, state, workspace, plan actions, drift, credentials, infrastructure state."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before initializing untrusted code, changing state or backends, applying plans, replacing or destroying resources, or exposing credentials."
  - "Route legal, privacy, security, compliance, financial, employment, and other qualified judgments to accountable reviewers."
timestamp: "2026-07-31T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: "2026-07-31"
  method: "baseline-vs-okb-rubric"
  model: "openai/gpt-4o-mini"
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 17
  okb_score: 36
  absolute_lift: 19
  task_scores:
    - task: "empty-evidence-integrity"
      baseline_score: 1
      okb_score: 12
      max_score: 12
    - task: "configuration-risk-review"
      baseline_score: 11
      okb_score: 12
      max_score: 12
    - task: "metric-or-report-reconciliation"
      baseline_score: 5
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 17/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Terraform

Source-aware tool bundle for Terraform configuration, providers, state, plans, workspaces, modules, policy, and controlled infrastructure change briefs.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, or approval. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request itself explicitly supports an item.

## Start Here

- [overview.md](overview.md)
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/terraform-brief.md](deliverables/terraform-brief.md)
