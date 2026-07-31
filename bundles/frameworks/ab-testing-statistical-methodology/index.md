---
type: Bundle Index
title: "A/B Testing Statistical Methodology"
description: "Source-aware framework bundle for designing and reviewing A/B tests with explicit hypotheses, randomization, power, instrumentation, analysis, stopping, and decision boundaries."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: frameworks
tags:
  - "ab-testing"
  - "experimentation"
  - "statistics"
  - "framework"
aliases:
  - "A/B Testing Statistical Methodology"
problems_solved:
  - "Prepare a a/b test design and analysis brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Product management"
  - "Data and analytics"
  - "Marketing"
tools:
  []
frameworks:
  - "source-evidence matrix"
  - "controlled experiment design and statistical decision-making application matrix"
  - "qualified-review gate"
deliverables:
  - "A/B test design and analysis brief"
commands: []
skills: []
evaluations:
  - "A/B Testing Statistical Methodology source-awareness check"
okb_bundle_id: ab-testing-statistical-methodology
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
  - "Use the cited official or primary sources for general controlled experiment design and statistical decision-making context; local facts, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for hypothesis and decision outcome, experimental unit, randomization, and allocation, population, eligibility, and exposure, power, sample-size, variance, and effect assumptions, alpha, multiplicity, and stopping rule, and instrumentation, exclusions, and analysis plan."
  - "Do not infer randomization integrity, sample adequacy, metric validity, treatment exposure, statistical significance, and practical significance."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before launching or changing exposure, stopping an experiment, shipping a treatment, collecting personal data, or claiming causality without the planned analysis."
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
  baseline_score: 22
  okb_score: 36
  absolute_lift: 14
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 12
    max_score: 12
  - task: framework-application-review
    baseline_score: 10
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 8
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 22/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# A/B Testing Statistical Methodology

Source-aware framework bundle for designing and reviewing A/B tests with explicit hypotheses, randomization, power, instrumentation, analysis, stopping, and decision boundaries.

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
- [framework.md](framework.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/ab-testing-statistical-methodology-brief.md](deliverables/ab-testing-statistical-methodology-brief.md)
