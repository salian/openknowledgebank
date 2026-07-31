---
type: Bundle Index
title: Chief Information Officer (CIO)
description: Source-aware role bundle for enterprise technology strategy, architecture, governance, investment, resilience, and board support, evidence reconciliation, reviewable decisions, and controlled consequential actions.
category: roles
version: 0.1.0
tags:
- chief-information-officer-cio
- chief
- role
aliases:
- Chief Information Officer (CIO)
problems_solved:
- Prepare a technology strategy and governance brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready decision with explicit verification and approval boundaries.
industries:
- Enterprise management
- Technology
tools: []
frameworks:
- source-evidence matrix
- enterprise technology strategy, architecture, governance, investment, resilience, and board support review matrix
- qualified-review gate
deliverables:
- technology strategy and governance brief
commands: []
skills: []
evaluations:
- Chief Information Officer (CIO) source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- agile
- fda-qmsr-13485
- gdpr
- hipaa
- itil
- jira
- sap-s4hana
- soc-2
- sox
- tableau
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 11-3021.00
  soc: []
  isco_08: []
  esco:
  - '1330'
limitations:
- Use the listed authoritative sources for general role or tool behavior; local configuration, records, values, states, permissions, and results require inspected evidence.
- Task-specific work requires current evidence for business strategy, decision rights, risk appetite, and accountable owners; application, data, infrastructure, identity, security, vendor, and architecture inventories; portfolio costs, contracts, service levels, technical debt, controls, audit findings, incidents, continuity, regulation, roadmap, benefits, dependencies, and approvals.
- Do not infer current architecture, security posture, compliance, resilience, cost, ROI, vendor performance, or transformation outcome.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, student, and other sensitive data.
- Require explicit confirmation before actions that approve strategy or architecture, commit budget, select a vendor, change controls, access sensitive systems, or make board or public claims.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: chief-information-officer-cio
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 10
  okb_score: 34
  absolute_lift: 24
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 12
    max_score: 12
  - task: role-task-review
    baseline_score: 5
    okb_score: 11
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 4
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 10/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# Chief Information Officer (CIO)

Source-aware role bundle for enterprise technology strategy, architecture, governance, investment, resilience, and board support, evidence reconciliation, reviewable decisions, and controlled consequential actions.

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
- [deliverables/chief-information-officer-cio-brief.md](deliverables/chief-information-officer-cio-brief.md)
