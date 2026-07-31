---
type: Bundle Index
title: Equal Opportunity / Fair Access Compliance Representative
description: Source-aware role bundle for objective equal-opportunity complaint, monitoring, and corrective-action support, evidence reconciliation, reviewable recommendations, and controlled consequential actions.
category: roles
version: 0.1.0
tags:
- equal-opportunity-fair-access-compliance-representative
- equal
- role
aliases:
- Equal Opportunity / Fair Access Compliance Representative
problems_solved:
- Prepare a equal-opportunity review brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Legal and compliance
- Regulated operations
tools: []
frameworks:
- source-evidence matrix
- objective equal-opportunity complaint, monitoring, and corrective-action support review matrix
- qualified-review gate
deliverables:
- equal-opportunity review brief
commands: []
skills: []
evaluations:
- Equal Opportunity / Fair Access Compliance Representative source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- ada
- salesforce-service-cloud
- section-508
- workday-hcm
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 13-1041.03
  soc: []
  isco_08: []
  esco:
  - '2422'
limitations:
- Use the cited authoritative sources for general role, standards, or regulatory context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for complaint, jurisdiction, scope, parties, allegations, and timeline; current law, policy, and coverage; evidence provenance, interviews, credibility factors, comparator and statistical analysis; confidentiality, retaliation, preservation, finding criteria, remedies, and qualified review.
- Do not infer discrimination, credibility, legal coverage, violation, liability, or required remedy.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, health, and other sensitive data.
- Require explicit confirmation before actions that contact parties, access sensitive records, issue a finding, impose discipline or remedy, or make a filing.
- Route legal, privacy, security, compliance, financial, employment, clinical, safety, and other qualified judgments to an evidenced accountable reviewer.
timestamp: '2026-07-31T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: equal-opportunity-fair-access-compliance-representative
okb_bundle_version: 0.1.0
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 22
  okb_score: 36
  absolute_lift: 14
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 6
    okb_score: 12
    max_score: 12
  - task: role-task-review
    baseline_score: 9
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 7
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 22/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---
# Equal Opportunity / Fair Access Compliance Representative

Source-aware role bundle for objective equal-opportunity complaint, monitoring, and corrective-action support, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

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
- [deliverables/equal-opportunity-fair-access-compliance-representative-brief.md](deliverables/equal-opportunity-fair-access-compliance-representative-brief.md)
