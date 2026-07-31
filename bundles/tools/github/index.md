---
type: Bundle Index
title: "GitHub"
description: "Source-aware tool bundle for GitHub repository, pull request, issue, workflow, release, security, and permission evidence with review-ready change briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "github"
  - "software-collaboration"
  - "devops"
  - "tool"
aliases:
  - "GitHub"
problems_solved:
  - "Prepare a github repository change brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Software"
  - "Information technology"
tools:
  - "GitHub"
frameworks:
  - "source-evidence matrix"
  - "software-collaboration-and-repository-operations evidence matrix"
  - "qualified-review gate"
deliverables:
  - "GitHub repository change brief"
commands: []
skills: []
evaluations:
  - "GitHub source-awareness check"
okb_bundle_id: github
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "applications-programmer"
  - "customer-support-engineer-product-support-engineer"
  - "devops-engineer"
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
  - "Use official GitHub sources for general context; local software collaboration and repository operations, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for repository and organization scope, commit, branch, tag, and default-branch state, pull requests, reviews, issues, and discussions, checks, workflow runs, logs, and artifacts, rulesets, environments, secrets, and permissions, release and deployment evidence, and security and audit evidence."
  - "Do not infer repository state, branch protection, checks, workflow behavior, permissions, secrets, release state, security findings."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before pushing commits, merging, closing issues, changing workflows, permissions, secrets, rulesets, releases, or deployments."
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
      baseline_score: 10
      okb_score: 12
      max_score: 12
    - task: "metric-or-report-reconciliation"
      baseline_score: 5
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 16/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# GitHub

Source-aware tool bundle for GitHub repository, pull request, issue, workflow, release, security, and permission evidence with review-ready change briefs.

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
- [deliverables/github-brief.md](deliverables/github-brief.md)
