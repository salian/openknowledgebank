---
type: Bundle Index
title: Board and Executive Product Update
description: Source-aware deliverable bundle for executive product updates connecting strategy, outcomes, customer evidence, delivery, economics, risks, decisions, and accountable next steps.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- product-update
- executive-reporting
- board-briefing
- deliverable
aliases:
- Board and Executive Product Update
problems_solved:
- Prepare a board or executive product update without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Product management
- Software
- Business services
tools: []
frameworks:
- source-evidence matrix
- executive product reporting and decisions review matrix
- qualified-review gate
deliverables:
- board or executive product update
commands: []
skills: []
evaluations:
- Board and Executive Product Update source-awareness check
okb_bundle_id: board-executive-product-update
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
- Use the cited official, originator, standards, or professional sources for general executive product reporting and decisions context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for audience, meeting, product scope, strategy, and requested decisions, customer problem, research, adoption, retention, and outcome evidence, roadmap, delivery, quality, reliability, and dependency status, financial, commercial, capacity, and investment evidence, risks, assumptions, options, tradeoffs, and forecast ranges, and owners, approvals, prior commitments, and follow-up.
- Do not infer customer outcome, delivery status, metric, forecast, risk, and executive decision.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before making board representations, committing roadmap, spend, headcount, forecasts, or customer claims without accountable review.
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
  baseline_score: 20
  okb_score: 36
  absolute_lift: 16
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 6
    okb_score: 12
    max_score: 12
  - task: deliverable-quality-review
    baseline_score: 8
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 20/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Board and Executive Product Update

Source-aware deliverable bundle for executive product updates connecting strategy, outcomes, customer evidence, delivery, economics, risks, decisions, and accountable next steps.

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
- [deliverable.md](deliverable.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/board-executive-product-update-brief.md](deliverables/board-executive-product-update-brief.md)
