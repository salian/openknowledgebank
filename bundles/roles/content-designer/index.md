---
type: Bundle Index
title: Content Designer
description: Source-aware role bundle for content design for digital services, evidence reconciliation, reviewable recommendations, and controlled consequential actions.
category: roles
version: 0.1.0
tags:
- content-designer
- content
- role
aliases:
- Content Designer
problems_solved:
- Prepare a content design brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Product design
- Digital services
tools: []
frameworks:
- source-evidence matrix
- content design for digital services review matrix
- qualified-review gate
deliverables:
- content design brief
commands: []
skills: []
evaluations:
- Content Designer source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- ada
- figma
- jira
- wcag
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 27-3042.00
  soc: []
  isco_08: []
  esco:
  - '2642.1'
limitations:
- Use the cited official, originator, standards, or professional sources for general content design for digital services context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for user need, task, research, journey, channel, and success criteria; current content, analytics, search terms, feedback, and source dates; service policy, legal basis, product behavior, claims, and approvals; content model, hierarchy, language, localization, accessibility, and reading context; prototypes, usability evidence, ownership, lifecycle, publication, and measurement.
- Do not infer user need, policy meaning, product behavior, content accuracy, comprehension, accessibility, or performance.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and other sensitive data.
- Require explicit confirmation before publishing content, changing service instructions, making legal or product claims, or claiming usability or accessibility.
- Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 18
  okb_score: 36
  absolute_lift: 18
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 12
    max_score: 12
  - task: role-task-review
    baseline_score: 10
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 18/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: content-designer
okb_bundle_version: 0.1.0
---
# Content Designer

Source-aware role bundle for content design for digital services, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

Do not assign an owner, author, date, or version to a provided artifact unless the request states it. Mark each absent field `Needs verification`.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/content-designer-brief.md](deliverables/content-designer-brief.md)
