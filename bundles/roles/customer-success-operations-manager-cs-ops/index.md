---
type: Bundle Index
title: Customer Success Operations Manager (CS Ops)
description: Source-aware role bundle for customer-success process design, lifecycle and health-model governance, systems and data review, capacity planning, and approval-ready operations briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- customer-success-operations
- cs-ops
- customer-systems
- role
aliases:
- Customer Success Operations Manager
- CS Ops Manager
problems_solved:
- Prepare customer success operations decision brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Customer success
- Software
tools: []
frameworks:
- source-evidence matrix
- customer-operations evidence matrix
- qualified-review gate
deliverables:
- Customer success operations decision brief
commands: []
skills: []
evaluations:
- Customer Success Operations Manager (CS Ops) source-awareness check
okb_bundle_id: customer-success-operations-manager-cs-ops
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- gdpr
- hubspot-sales-hub
- okrs
- salesforce-service-cloud
- soc-2
- tableau
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 11-2022.00
  soc: []
  isco_08: []
  esco:
  - '1221'
limitations:
- Treat the mapping as approximate; lifecycle definitions, health models, CRM and CS data, automations, staffing, permissions, and outcomes require local evidence.
- Task-specific work requires current evidence for customer lifecycle and outcome definitions, CRM and CS system schema, health-model logic and validation, process ownership and handoffs, automation configuration, permissions and data policy, capacity and performance evidence.
- Do not infer health scores, churn risk, lifecycle stage, CRM state, automation behavior, capacity, customer outcomes.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before customer data, scoring, CRM, automation, assignments, permissions, or customer-facing process changes.
- Route legal, privacy, security, compliance, financial, employment, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
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
    baseline_score: 3
    okb_score: 12
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 4
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 11/36 to 35/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Customer Success Operations Manager (CS Ops)

Source-aware role bundle for customer-success process design, lifecycle and health-model governance, systems and data review, capacity planning, and approval-ready operations briefs.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts
and explain which decision each artifact supports.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/cs-operations-brief.md](deliverables/cs-operations-brief.md)
