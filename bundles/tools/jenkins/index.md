---
type: Bundle Index
title: "Jenkins"
description: "Source-aware tool bundle for Jenkins controller, agent, job, pipeline, plugin, credential, build, release, and controlled automation briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "jenkins"
  - "ci-cd"
  - "automation"
  - "tool"
aliases:
  - "Jenkins"
problems_solved:
  - "Prepare a jenkins pipeline and change brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Software"
  - "Information technology"
tools:
  - "Jenkins"
frameworks:
  - "source-evidence matrix"
  - "continuous-integration-and-delivery-automation evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Jenkins pipeline and change brief"
commands: []
skills: []
evaluations:
  - "Jenkins source-awareness check"
okb_bundle_id: jenkins
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "applications-programmer"
  - "devops-engineer"
  - "ict-system-developer"
  - "release-build-engineer"
  - "software-developer-software-engineer"
  - "software-developers-and-analysts-not-elsewhere-classified"
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
  - "Use official Jenkins sources for general context; local continuous integration and delivery automation, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for Jenkins version and controller scope, agents, labels, executors, and node state, job, pipeline, multibranch, and Jenkinsfile definitions, plugins, dependencies, and compatibility evidence, credentials references and permission boundaries, build parameters, logs, artifacts, and test results, and environment, deployment, rollback, and approval evidence."
  - "Do not infer controller state, agents, pipeline definition, plugins, credentials, build results, artifacts, deployment state."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before running jobs, changing pipelines, plugins, credentials, permissions, agents, artifacts, releases, or deployments."
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
  baseline_score: 16
  okb_score: 36
  absolute_lift: 20
  task_scores:
    - task: "empty-evidence-integrity"
      baseline_score: 1
      okb_score: 12
      max_score: 12
    - task: "configuration-risk-review"
      baseline_score: 9
      okb_score: 12
      max_score: 12
    - task: "metric-or-report-reconciliation"
      baseline_score: 6
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 16/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Jenkins

Source-aware tool bundle for Jenkins controller, agent, job, pipeline, plugin, credential, build, release, and controlled automation briefs.

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
- [deliverables/jenkins-brief.md](deliverables/jenkins-brief.md)
