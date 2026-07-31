---
type: Bundle Index
title: Chief Product Officer (CPO)
description: Source-aware role bundle for product vision, portfolio strategy, operating model, prioritization, and executive review, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: roles
version: 0.1.0
tags:
- chief-product-officer-cpo
- chief
- role
aliases:
- Chief Product Officer (CPO)
problems_solved:
- Prepare a product portfolio decision brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Digital products
- Technology
tools: []
frameworks:
- source-evidence matrix
- product vision, portfolio strategy, operating model, prioritization, and executive review review matrix
- qualified-review gate
deliverables:
- product portfolio decision brief
commands: []
skills: []
evaluations:
- Chief Product Officer (CPO) source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- amplitude
- confluence
- figma
- jira
- jobs-to-be-done
- mixpanel
- okrs
- product-requirements-document
- product-roadmap
- rice-prioritization
- scrum
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 11-1011.00
  soc: []
  isco_08: []
  esco:
  - '1120'
limitations:
- Use the listed authoritative sources for general role or tool behavior; local configuration, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for company strategy, users, markets, research, product evidence, and decision criteria; product portfolio, lifecycle, metrics, experiments, economics, competitive evidence, capacity, dependencies, roadmap, risks, accessibility, privacy, security, legal review, and approvals.
- Do not infer customer need, product-market fit, metric result, priority, forecast, competitive position, roadmap feasibility, or business impact.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that approve strategy or roadmap, commit capacity or budget, launch or retire a product, change customer commitments, or make investor or market claims.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: chief-product-officer-cpo
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 11
  okb_score: 35
  absolute_lift: 24
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 11
    max_score: 12
  - task: role-task-review
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 4
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 11/36 to 35/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# Chief Product Officer (CPO)

Source-aware role bundle for product vision, portfolio strategy, operating model, prioritization, and executive review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name authoritative source URLs used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each supports. When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate a generic role.

Facts explicitly stated in the request belong under `Provided` as `Prompt-provided request`; do not move them to `Assumed`. Do not assign an owner, author, date, or version unless the request states it.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/chief-product-officer-cpo-brief.md](deliverables/chief-product-officer-cpo-brief.md)
