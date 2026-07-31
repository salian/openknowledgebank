---
type: Bundle Index
title: Account Manager (Client Relationship Manager)
description: Source-aware role bundle for client relationship planning, service and commercial review, issue coordination, renewal preparation, and client-ready account briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- account-management
- client-relationships
- renewal-planning
- role
aliases:
- Account Manager
- Client Relationship Manager
problems_solved:
- Prepare client relationship and account decision brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Business services
- Sales
tools: []
frameworks:
- source-evidence matrix
- client-evidence matrix
- qualified-review gate
deliverables:
- Client relationship and account decision brief
commands: []
skills: []
evaluations:
- Account Manager (Client Relationship Manager) source-awareness check
okb_bundle_id: account-manager-client-relationship-manager
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- hubspot-sales-hub
- salesforce-service-cloud
- zendesk
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 41-3099.00
  soc: []
  isco_08: []
  esco:
  - account manager (ISCO-08 1221)
limitations:
- Use as broad relationship-management context; client goals, stakeholders, service state, contracts, pricing, CRM, satisfaction, and commitments require current evidence.
- Task-specific work requires current evidence for client goals and approved notes, stakeholder and authority evidence, contract and entitlement summary, service and issue records, CRM and renewal state, pricing authority, approved commitments.
- Do not infer client goals, stakeholder authority, satisfaction, contract terms, CRM state, renewal likelihood, commitments.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before client data, communications, CRM changes, pricing, terms, renewals, or commitments.
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
    baseline_score: 2
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 4
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 11/36 to 35/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Account Manager (Client Relationship Manager)

Source-aware role bundle for client relationship planning, service and commercial review, issue coordination, renewal preparation, and client-ready account briefs.

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
- [deliverables/client-account-brief.md](deliverables/client-account-brief.md)
