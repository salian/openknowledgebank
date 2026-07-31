---
type: Bundle Index
title: Customer Service Representative
description: Source-aware role bundle for customer inquiry triage, account and order evidence review, policy-bounded resolution, escalation, and approval-ready response drafts.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- customer-service
- case-resolution
- customer-communications
- role
aliases:
- Customer Service Representative
- Customer Care Representative
problems_solved:
- Prepare customer case resolution and response brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Customer service
tools: []
frameworks:
- source-evidence matrix
- case-evidence matrix
- qualified-review gate
deliverables:
- Customer case resolution and response brief
commands: []
skills: []
evaluations:
- Customer Service Representative source-awareness check
okb_bundle_id: customer-service-representative
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- gdpr
- hipaa
- salesforce-service-cloud
- tcpa
- zendesk
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 43-4051.00
  soc: []
  isco_08: []
  esco:
  - '4222'
limitations:
- Use as occupational context; identity, account, order, entitlement, policy, communication, refund, and case state require current authorized evidence.
- Task-specific work requires current evidence for verified customer identity under policy, case and communication history, order, account, or service state, current policy and entitlement, product or service evidence, refund and exception authority, escalation and communication approval.
- Do not infer customer identity, account state, order status, policy terms, entitlement, refund authority, case outcome.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before personal data, identity, account changes, refunds, exceptions, disclosures, or customer communication.
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
  baseline_score: 13
  okb_score: 34
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 12
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 5
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 4
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 13/36 to 34/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Customer Service Representative

Source-aware role bundle for customer inquiry triage, account and order evidence review, policy-bounded resolution, escalation, and approval-ready response drafts.

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
- [deliverables/customer-service-brief.md](deliverables/customer-service-brief.md)
