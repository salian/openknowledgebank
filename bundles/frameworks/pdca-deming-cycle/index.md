---
type: Bundle Index
title: PDCA and PDSA Improvement Cycle
description: Source-aware framework bundle for small-scale improvement cycles with explicit distinction between PDCA and Deming's PDSA, prediction, measurement, learning, adoption, and safety boundaries.
schema_version: 0.1.0
bundle_format: okf-compatible
category: frameworks
tags:
- pdca
- pdsa
- deming-cycle
- continuous-improvement
- framework
aliases:
- PDCA and PDSA Improvement Cycle
problems_solved:
- Prepare a pdca or pdsa experiment brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Operations
- Manufacturing
- Healthcare
tools: []
frameworks:
- source-evidence matrix
- iterative process improvement and learning review matrix
- qualified-review gate
deliverables:
- PDCA or PDSA experiment brief
commands: []
skills: []
evaluations:
- PDCA and PDSA Improvement Cycle source-awareness check
okb_bundle_id: pdca-deming-cycle
okb_bundle_version: 0.1.0
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
- Use the cited official, originator, standards, or professional sources for general iterative process improvement and learning context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for selected PDCA or PDSA interpretation and source, problem, aim, theory, prediction, and scope, baseline, measures, data plan, and operational definitions, small-scale test, owner, timing, and safeguards, observed results, variation, comparison, and learning, and adopt, adapt, abandon, standardize, or repeat decision and approval.
- Do not infer problem cause, baseline, prediction, test result, learning, and wider-scale effect.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before changing production processes, standard work, staffing, controls, or safety conditions, or scaling a change without reviewed evidence.
- Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 23
  okb_score: 36
  absolute_lift: 13
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 5
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
  display_summary: Improved measured rubric score from 23/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# PDCA and PDSA Improvement Cycle

Source-aware framework bundle for small-scale improvement cycles with explicit distinction between PDCA and Deming's PDSA, prediction, measurement, learning, adoption, and safety boundaries.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

## Start Here

- [overview.md](overview.md)
- [framework.md](framework.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/pdca-deming-cycle-brief.md](deliverables/pdca-deming-cycle-brief.md)
