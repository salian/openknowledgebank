---
type: "Bundle Index"
title: "MLOps Engineer"
description: "Source-aware role bundle for ML operational planning, evidence review, deployment readiness, and qualified production handoff."
schema_version: "0.1.0"
bundle_format: "okf-compatible"
category: "roles"
tags:
  - "mlops"
  - "machine-learning"
  - "model-operations"
  - "role"
aliases:
  - "MLOps Engineer"
  - "Machine Learning Operations Engineer"
  - "O*NET 15-2051.00"
problems_solved:
  - "Turn model, data, deployment, and monitoring evidence into a reviewable operational plan."
  - "Separate source-confirmed facts, supplied environment evidence, assumptions, and missing verification."
  - "Avoid invented model, pipeline, platform, access, quality, or production claims."
industries:
  - "Technology"
  - "Data and analytics"
tools: []
frameworks:
  - "source-evidence matrix"
  - "deployment-readiness gate"
  - "qualified-review gate"
deliverables:
  - "MLOps source-aware operational plan"
commands: []
skills: []
evaluations:
  - "MLOps source-awareness check"
okb_bundle_id: mlops-engineer
okb_bundle_version: "0.1.0"
trust_tier: "trusted"
status: "beta"
license: "CC-BY-4.0"
related_bundles:
  - "data-engineer"
  - "docker"
adjacent_bundles: []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc:
    - "15-2051.00"
  soc: []
  isco_08: []
  esco: []
limitations:
  - "This bundle supports planning and review; it is not model-validation, security, privacy, legal, safety, or production-change approval."
  - "Environment-specific guidance requires current model documentation, data evidence, platform configuration, monitoring definitions, access controls, and accountable review."
  - "Do not infer model quality, pipeline behavior, deployment state, access permissions, costs, service levels, or compliance status without evidence."
safety_notes:
  - "Minimize personal, customer, proprietary model, training-data, credential, and regulated data in prompts and examples."
  - "Require explicit confirmation before deploying, rolling back, retraining, changing model routing, modifying infrastructure, or exporting data."
  - "Route production-impacting, privacy, security, safety, and compliance decisions to accountable reviewers."
timestamp: "2026-07-11T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-29'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 16
  okb_score: 28
  absolute_lift: 12
  task_scores:
    - task: empty-evidence-integrity
      baseline_score: 6
      okb_score: 9
      max_score: 12
    - task: role-prioritization-review
      baseline_score: 6
      okb_score: 9
      max_score: 12
    - task: role-source-reconciliation
      baseline_score: 4
      okb_score: 10
      max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 16/36 to 28/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# MLOps Engineer

Source-aware role bundle for ML operational planning, evidence review, deployment readiness, and qualified production handoff.

## Required Answer Habit

Include a short **Source note** naming the model, data, platform, deployment, monitoring, and policy evidence used, plus any missing verification before production reliance.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-ml-operations-triage.md](workflows/source-aware-ml-operations-triage.md)
- [deliverables/source-aware-ml-operations-plan.md](deliverables/source-aware-ml-operations-plan.md)
