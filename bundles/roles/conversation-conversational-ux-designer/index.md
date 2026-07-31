---
type: Bundle Index
title: Conversation / Conversational UX Designer
description: Source-aware role bundle for conversation design, intent coverage, safety, and experience validation, evidence reconciliation, reviewable recommendations, and controlled consequential actions.
category: roles
version: 0.1.0
tags:
- conversation-conversational-ux-designer
- conversation
- role
aliases:
- Conversation / Conversational UX Designer
problems_solved:
- Prepare a conversational experience brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Product design
- Digital products
tools: []
frameworks:
- source-evidence matrix
- conversation design, intent coverage, safety, and experience validation review matrix
- qualified-review gate
deliverables:
- conversational experience brief
commands: []
skills: []
evaluations:
- Conversation / Conversational UX Designer source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- figma
- gdpr
- wcag
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 15-1255.00
  soc: []
  isco_08: []
  esco:
  - user interface designer
limitations:
- Use the cited authoritative sources for general role, standards, or regulatory context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for users, channel, use cases, intents, entities, taxonomy, dialog states, prompts, fallback, and escalation; model or NLU version and data; privacy, consent, safety, accessibility, language, transcript, test, and metric evidence.
- Do not infer intent coverage, model behavior, user comprehension, safety, accessibility, or measured performance.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, and other sensitive data.
- Require explicit confirmation before actions that deploy prompts or a model, collect user data, send outbound messages, or claim safety, usability, or accessibility.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: conversation-conversational-ux-designer
okb_bundle_version: 0.1.0
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
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: role-task-review
    baseline_score: 9
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
# Conversation / Conversational UX Designer

Source-aware role bundle for conversation design, intent coverage, safety, and experience validation, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

Facts explicitly stated in the request belong under `Provided`, including the label `Prompt-provided request`. Do not move them to `Assumed`. Do not assign an owner, author, date, or version to a provided artifact unless the request states it. Mark each absent field `Needs verification`.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/conversation-conversational-ux-designer-brief.md](deliverables/conversation-conversational-ux-designer-brief.md)
