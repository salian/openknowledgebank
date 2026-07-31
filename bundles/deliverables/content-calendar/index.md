---
type: Bundle Index
title: Content Calendar
description: Source-aware deliverable bundle for creating a channel-aware content calendar with evidenced audience, objective, asset, owner, approval, rights, schedule, dependency, and measurement fields.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- content-calendar
- editorial-planning
- content-marketing
- deliverable
aliases:
- Content Calendar
problems_solved:
- Prepare a review-ready content calendar without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Marketing
- Publishing
- Media
tools: []
frameworks:
- source-evidence matrix
- content planning and publication scheduling review matrix
- qualified-review gate
deliverables:
- review-ready content calendar
commands: []
skills: []
evaluations:
- Content Calendar source-awareness check
okb_bundle_id: content-calendar
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
- Use the cited official, originator, standards, or professional sources for general content planning and publication scheduling context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for audience, objective, campaign, and channel strategy, content inventory, themes, formats, and source material, asset owner, creator, reviewer, and approval status, publication date, timezone, cadence, dependency, and status, rights, claims, privacy, accessibility, and brand requirements, and distribution, measurement definitions, and retrospective evidence.
- Do not infer audience need, asset readiness, approval, publication date, content rights, and performance.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before publishing, scheduling, changing approved content, using unclear-rights material, making unsupported claims, or committing media spend.
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
  baseline_score: 15
  okb_score: 36
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 12
    max_score: 12
  - task: deliverable-quality-review
    baseline_score: 7
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Content Calendar

Source-aware deliverable bundle for creating a channel-aware content calendar with evidenced audience, objective, asset, owner, approval, rights, schedule, dependency, and measurement fields.

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
- [deliverables/content-calendar-brief.md](deliverables/content-calendar-brief.md)
