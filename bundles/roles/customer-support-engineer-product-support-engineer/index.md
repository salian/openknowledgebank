---
type: Bundle Index
title: Customer Support Engineer / Product Support Engineer
description: Source-aware role bundle for technical case triage, reproduction, log and configuration review, root-cause hypotheses, workaround validation, and escalation-ready support briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- technical-support
- product-support
- troubleshooting
- role
aliases:
- Customer Support Engineer
- Product Support Engineer
problems_solved:
- Prepare technical support investigation and escalation brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Software support
- Technology
tools: []
frameworks:
- source-evidence matrix
- technical-case evidence matrix
- qualified-review gate
deliverables:
- Technical support investigation and escalation brief
commands: []
skills: []
evaluations:
- Customer Support Engineer / Product Support Engineer source-awareness check
okb_bundle_id: customer-support-engineer-product-support-engineer
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
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
  - 15-1232.00
  soc: []
  isco_08: []
  esco:
  - '3512'
limitations:
- Use as occupational context; customer environment, product version, logs, configuration, access, incident state, root cause, and fixes require current evidence.
- Task-specific work requires current evidence for customer-reported symptoms and impact, authorized environment and version details, reproduction steps, sanitized logs and errors, configuration and recent changes, product documentation and known issues, case ownership and change authority.
- Do not infer environment, version, logs, configuration, root cause, fix status, product defect, case state.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before customer data, credentials, configuration changes, production actions, disclosures, or customer communication.
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
  baseline_score: 14
  okb_score: 32
  absolute_lift: 18
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 4
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 5
    okb_score: 10
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 5
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 14/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Customer Support Engineer / Product Support Engineer

Source-aware role bundle for technical case triage, reproduction, log and configuration review, root-cause hypotheses, workaround validation, and escalation-ready support briefs.

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
- [deliverables/technical-support-brief.md](deliverables/technical-support-brief.md)
