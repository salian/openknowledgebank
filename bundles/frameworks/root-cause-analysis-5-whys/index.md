---
type: Bundle Index
title: Root Cause Analysis and Five Whys
description: Source-aware framework bundle for problem statement, causal chain, evidence, contributing causes, verification, corrective action, and learning review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: frameworks
version: 0.1.0
tags:
- root-cause-analysis-5-whys
- framework
- source-aware
aliases:
- Root Cause Analysis and Five Whys
problems_solved:
- Prepare a root cause analysis and five whys review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools: []
frameworks:
- Root Cause Analysis and Five Whys
- source-evidence matrix
- qualified-review gate
deliverables:
- Root Cause Analysis and Five Whys review brief
commands: []
skills: []
evaluations:
- Root Cause Analysis and Five Whys source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- toyota-production-system
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
- Use the listed authoritative or identified source surfaces for general Root Cause Analysis and Five Whys guidance; local facts, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for event and impact definition, timeline, affected scope, logs and observations, process and system changes, causal hypotheses, each why-answer and supporting evidence, alternative causes, human factors, experiments or recurrence tests, corrective and preventive actions, owners, dates, approvals, and follow-up results.
- Do not infer root cause, causal link, fault, recurrence risk, corrective-action effectiveness, closure, or accountability.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that assign blame or root cause, change production processes or controls, stop operations, close incidents or corrective actions, communicate findings, or make safety, legal, or disciplinary determinations.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-08-01T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: root-cause-analysis-5-whys
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 15
  okb_score: 33
  absolute_lift: 18
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 5
    okb_score: 11
    max_score: 12
  - task: framework-application-review
    baseline_score: 5
    okb_score: 11
    max_score: 12
  - task: source-or-state-reconciliation
    baseline_score: 5
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# Root Cause Analysis and Five Whys

Source-aware framework bundle for problem statement, causal chain, evidence, contributing causes, verification, corrective action, and learning review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and domain actions prohibited without explicit approval.
5. **Source note** - name source URLs used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each supports. For an empty-evidence task, write `None` under Verified, Provided, and Assumed. Set `Accountable reviewer` to `Needs verification`; do not nominate a generic role. Facts explicitly stated in a non-empty request belong under `Provided` as `Prompt-provided request`; do not invent owner, author, date, version, or provenance.

## Start Here

- [overview.md](overview.md)
- [framework.md](framework.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/root-cause-analysis-5-whys-brief.md](deliverables/root-cause-analysis-5-whys-brief.md)
