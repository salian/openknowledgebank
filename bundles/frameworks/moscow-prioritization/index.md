---
type: Bundle Index
title: MoSCoW Prioritization
description: Source-aware framework bundle for MoSCoW prioritization with explicit deadline, scope, definitions, dependencies, acceptance criteria, capacity, contingency, and decision ownership.
schema_version: 0.1.0
bundle_format: okf-compatible
category: frameworks
tags:
- moscow
- prioritization
- requirements
- framework
aliases:
- MoSCoW Prioritization
problems_solved:
- Prepare a moscow priority decision brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Project management
- Software
- Business services
tools: []
frameworks:
- source-evidence matrix
- timeboxed requirement prioritization review matrix
- qualified-review gate
deliverables:
- MoSCoW priority decision brief
commands: []
skills: []
evaluations:
- MoSCoW Prioritization source-awareness check
okb_bundle_id: moscow-prioritization
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
- Use the cited official, originator, standards, or professional sources for general timeboxed requirement prioritization context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for decision scope, deadline, outcome, and constraints, agreed Must, Should, Could, and Won't definitions, requirements and acceptance criteria, dependencies, compliance, safety, and minimum viable outcome, effort, capacity, uncertainty, and contingency, and decision owner, rationale, change control, and review cadence.
- Do not infer requirement necessity, effort, dependency, deadline feasibility, priority agreement, and tradeoff effect.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before committing scope, deadlines, resources, contractual obligations, or dropping safety, compliance, or critical requirements without accountable approval.
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
  baseline_score: 17
  okb_score: 36
  absolute_lift: 19
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 12
    max_score: 12
  - task: framework-application-review
    baseline_score: 9
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 7
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 17/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# MoSCoW Prioritization

Source-aware framework bundle for MoSCoW prioritization with explicit deadline, scope, definitions, dependencies, acceptance criteria, capacity, contingency, and decision ownership.

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
- [deliverables/moscow-prioritization-brief.md](deliverables/moscow-prioritization-brief.md)
