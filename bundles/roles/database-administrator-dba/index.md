---
type: Bundle Index
title: Database Administrator (DBA)
description: Source-aware role bundle for database administration and reliability, evidence reconciliation, reviewable recommendations, and controlled consequential actions.
category: roles
version: 0.1.0
tags:
- database-administrator-dba
- database
- role
aliases:
- Database Administrator (DBA)
problems_solved:
- Prepare a database change brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Data and analytics
- Technology operations
tools: []
frameworks:
- source-evidence matrix
- database administration and reliability review matrix
- qualified-review gate
deliverables:
- database change brief
commands: []
skills: []
evaluations:
- Database Administrator (DBA) source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- gdpr
- hipaa
- itil
- soc-2
- sox
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 15-1242.00
  soc: []
  isco_08: []
  esco:
  - '2521'
limitations:
- Use the cited official, originator, standards, or professional sources for general database administration and reliability context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for database purpose, owners, environments, engine, version, topology, and dependencies; schemas, data classification, volume, workload, queries, indexes, and statistics; identities, roles, privileges, encryption, keys, audit, and network controls; backups, retention, restore tests, replication, recovery objectives, and incidents; change plan, migration, capacity, monitoring, maintenance, rollback, and approvals.
- Do not infer schema meaning, privilege, backup validity, recoverability, performance cause, replication state, capacity, or production health.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and other sensitive data.
- Require explicit confirmation before querying or exporting sensitive data, changing schemas or privileges, restoring backups, failing over, or modifying production.
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
  baseline_score: 17
  okb_score: 36
  absolute_lift: 19
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
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
  display_summary: Improved measured rubric score from 17/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: database-administrator-dba
okb_bundle_version: 0.1.0
---
# Database Administrator (DBA)

Source-aware role bundle for database administration and reliability, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

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
- [deliverables/database-administrator-dba-brief.md](deliverables/database-administrator-dba-brief.md)
