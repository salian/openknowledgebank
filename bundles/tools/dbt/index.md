---
type: Bundle Index
title: "dbt (Data Build Tool)"
description: "Source-aware tool bundle for dbt projects, models, sources, tests, lineage, runs, artifacts, environments, and controlled transformation briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "dbt"
  - "analytics-engineering"
  - "data-transformation"
  - "tool"
aliases:
  - "dbt (Data Build Tool)"
problems_solved:
  - "Prepare a dbt transformation and review brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Data and analytics"
  - "Software"
tools:
  - "dbt (Data Build Tool)"
frameworks:
  - "source-evidence matrix"
  - "analytics-engineering-and-data-transformation evidence matrix"
  - "qualified-review gate"
deliverables:
  - "dbt transformation and review brief"
commands: []
skills: []
evaluations:
  - "dbt (Data Build Tool) source-awareness check"
okb_bundle_id: dbt
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "ai-data-platform-engineer"
  - "business-intelligence-analyst"
  - "business-intelligence-bi-developer"
  - "data-architect"
  - "data-engineer"
  - "data-product-manager"
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
  - "Use official dbt (Data Build Tool) sources for general context; local analytics engineering and data transformation, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for dbt product and version, project, packages, adapter, profile, and target, models, sources, seeds, snapshots, macros, and exposures, properties, contracts, tests, and documentation, selection syntax and invocation parameters, manifest, run results, catalog, logs, and lineage, and warehouse permissions, deployment, and approval evidence."
  - "Do not infer project structure, models, sources, tests, lineage, target, run status, warehouse state."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before running production jobs, changing models or contracts, modifying targets, deploying packages, or altering warehouse objects."
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
  baseline_score: 19
  okb_score: 36
  absolute_lift: 17
  task_scores:
    - task: "empty-evidence-integrity"
      baseline_score: 3
      okb_score: 12
      max_score: 12
    - task: "configuration-risk-review"
      baseline_score: 10
      okb_score: 12
      max_score: 12
    - task: "metric-or-report-reconciliation"
      baseline_score: 6
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 19/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# dbt (Data Build Tool)

Source-aware tool bundle for dbt projects, models, sources, tests, lineage, runs, artifacts, environments, and controlled transformation briefs.

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
- [deliverables/dbt-data-build-tool-brief.md](deliverables/dbt-data-build-tool-brief.md)
