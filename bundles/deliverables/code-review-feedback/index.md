---
type: Bundle Index
title: Code Review Feedback
description: Source-aware deliverable bundle for change intent, correctness, security, reliability, test, compatibility, maintainability, severity, evidence, suggestion, and review-decision feedback, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: deliverables
version: 0.1.0
tags:
- code-review-feedback
- deliverable
- source-aware
aliases:
- Code Review Feedback
problems_solved:
- Prepare a code review feedback review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Technology
- Business operations
tools: []
frameworks:
- source-evidence matrix
- qualified-review gate
deliverables:
- Code Review Feedback review brief
commands: []
skills: []
evaluations:
- Code Review Feedback source-awareness check
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
- Use the listed authoritative or identified source surfaces for general Code Review Feedback guidance; local facts, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for repository and branch, change request and acceptance criteria, full diff and surrounding code, language and runtime, architecture and threat context, tests and results, static or security analysis, logs, backward-compatibility requirements, deployment and rollback plan, ownership and review policy, exact file and line, reproduction evidence, confidence, and approvals.
- Do not infer change intent, runtime behavior, defect, exploitability, severity, test result, compatibility, merge eligibility, or deployment safety.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that submit review comments, approve or request changes, apply suggestions, edit code, run commands or tests, merge changes, expose private code or secrets, or deploy software.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-08-01T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: code-review-feedback
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
  okb_score: 36
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: deliverable-quality-review
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: source-or-state-reconciliation
    baseline_score: 5
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# Code Review Feedback

Source-aware deliverable bundle for change intent, correctness, security, reliability, test, compatibility, maintainability, severity, evidence, suggestion, and review-decision feedback, evidence reconciliation, reviewable decisions, and controlled consequential actions.

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
- [deliverable.md](deliverable.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/code-review-feedback-brief.md](deliverables/code-review-feedback-brief.md)
