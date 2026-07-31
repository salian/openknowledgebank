---
type: Bundle Index
title: Net Promoter System
description: Source-aware framework bundle for operating a Net Promoter feedback system across survey design, scoring, sampling, qualitative learning, closed-loop follow-up, governance, and improvement.
schema_version: 0.1.0
bundle_format: okf-compatible
category: frameworks
tags:
- net-promoter-system
- customer-experience
- closed-loop-feedback
- framework
aliases:
- Net Promoter System
problems_solved:
- Prepare a net promoter system operating brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Customer experience
- Retail
- Business services
tools: []
frameworks:
- source-evidence matrix
- customer feedback and closed-loop improvement review matrix
- qualified-review gate
deliverables:
- Net Promoter System operating brief
commands: []
skills: []
evaluations:
- Net Promoter System source-awareness check
okb_bundle_id: net-promoter-system
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
- Use the cited official, originator, standards, or professional sources for general customer feedback and closed-loop improvement context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for survey wording, scale, trigger, channel, and timing, population, sample, response, consent, and nonresponse evidence, score definition, exclusions, segments, period, and uncertainty, qualitative feedback and issue taxonomy, closed-loop contact, escalation, ownership, and resolution evidence, and improvement experiments, outcomes, governance, privacy, and approvals.
- Do not infer respondent representativeness, score accuracy, feedback meaning, customer identity, follow-up outcome, and improvement effect.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before contacting customers, exposing personal data, publishing scores, changing incentives, or claiming loyalty, growth, or causality without supporting evidence.
- Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to accountable reviewers.
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
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: framework-application-review
    baseline_score: 8
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 5
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 18/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Net Promoter System

Source-aware framework bundle for operating a Net Promoter feedback system across survey design, scoring, sampling, qualitative learning, closed-loop follow-up, governance, and improvement.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

## Start Here

- [overview.md](overview.md)
- [framework.md](framework.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/net-promoter-system-brief.md](deliverables/net-promoter-system-brief.md)
