---
type: Bundle Index
title: "MLflow"
description: "Source-aware tool bundle for MLflow experiments, runs, metrics, parameters, artifacts, datasets, model registry, storage, access, and controlled model changes."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "mlflow"
  - "machine-learning"
  - "model-governance"
  - "tool"
aliases:
  - "MLflow"
problems_solved:
  - "Prepare a mlflow experiment and model-governance brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Artificial intelligence"
  - "Software"
  - "Data and analytics"
tools:
  - "MLflow"
frameworks:
  - "source-evidence matrix"
  - "machine-learning lifecycle tracking and model governance evidence matrix"
  - "qualified-review gate"
deliverables:
  - "MLflow experiment and model-governance brief"
commands: []
skills: []
evaluations:
  - "MLflow source-awareness check"
okb_bundle_id: mlflow
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
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
  - "Use the cited official or primary sources for general machine-learning lifecycle tracking and model governance context; local facts, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for MLflow version, deployment, and tracking URI, experiments, runs, metrics, parameters, artifacts, and datasets, model registry records, versions, aliases, and deployment references, backend and artifact stores, authentication and access controls, and promotion, deployment, and deletion approvals."
  - "Do not infer run reproducibility, metric comparability, artifact contents, model lineage, registry state, and deployment outcome."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before logging sensitive data, registering, promoting, deploying, or deleting models, or changing storage and access configuration."
  - "Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to accountable reviewers."
timestamp: "2026-07-31T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 18
  okb_score: 36
  absolute_lift: 18
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 12
    max_score: 12
  - task: configuration-risk-review
    baseline_score: 10
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 7
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 18/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# MLflow

Source-aware tool bundle for MLflow experiments, runs, metrics, parameters, artifacts, datasets, model registry, storage, access, and controlled model changes.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, or approval. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request itself explicitly supports an item.

For an empty-evidence request, set the accountable reviewer to `Needs verification`. Do not nominate, designate, or invent a reviewer role.

## Start Here

- [overview.md](overview.md)
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/mlflow-brief.md](deliverables/mlflow-brief.md)
