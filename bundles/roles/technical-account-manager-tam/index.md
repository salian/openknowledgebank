---
type: Bundle Index
title: Technical Account Manager (TAM)
description: Source-aware role bundle for technical account planning, adoption and risk review, escalation coordination, architecture discussions, and customer-ready technical briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- technical-account-management
- customer-success
- technical-advisory
- role
aliases:
- Technical Account Manager
- TAM
problems_solved:
- Prepare account guidance without fabricating environment facts.
- Coordinate escalations with traceable evidence.
- Separate recommendations from binding commitments.
industries:
- Software
- Technology services
tools: []
frameworks:
- source-evidence matrix
- account-technical-evidence matrix
- qualified-review gate
deliverables:
- Technical account health and action brief
commands: []
skills: []
evaluations:
- Technical Account Manager (TAM) source-awareness check
okb_bundle_id: technical-account-manager-tam
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- confluence
- gdpr
- jira
- salesforce-service-cloud
- soc-2
- zendesk
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 41-4011.00
  soc: []
  isco_08: []
  esco:
  - '2433.1'
limitations:
- Customer-specific advice requires current architecture, product, entitlement, case, and account evidence.
- This bundle does not establish contractual or security assurances.
- Do not infer customer configuration, adoption, health, incident cause, or product commitments.
safety_notes:
- Minimize customer, security, credential, and incident data.
- Require confirmation before customer communications, escalations, production changes, or commitments.
- Route architecture, security, legal, and contractual reliance to qualified owners.
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
  okb_score: 32
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 10
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 5
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 11/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Technical Account Manager (TAM)

Source-aware role bundle for technical account planning, adoption and risk review, escalation coordination, architecture discussions, and customer-ready technical briefs.

## Required Answer Habit

Include a short **Source note** naming authoritative source categories and local
evidence used, assumptions made, and missing verification required before reliance.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name the source category, scope, date or version, and conflict checks required.
4. **Confirmation boundary** - identify the accountable reviewer and actions that must not occur without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not collapse missing evidence into a general disclaimer. Ask for the exact artifacts needed and explain which decision each artifact supports.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/technical-account-brief.md](deliverables/technical-account-brief.md)
