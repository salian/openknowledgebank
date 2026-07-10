---
type: Bundle Index
title: Internal Auditor
description: Role bundle for internal audit planning, risk/control assessment, evidence requests, findings, and management-action tracking.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags:
  - internal-audit
  - controls
  - risk
  - assurance
  - governance
aliases:
  - Internal Audit Specialist
  - Corporate Auditor
problems_solved:
  - Route Internal Auditor work to the right source category and evidence set.
  - Separate verified source facts, user-provided facts, assumptions, and missing evidence.
  - Produce a internal audit finding brief suitable for professional review.
industries:
  - cross-industry
tools: []
frameworks:
  - source-evidence matrix
  - inspect-first workflow
  - professional-review gate
deliverables:
  - internal audit finding brief
commands: []
skills: []
evaluations:
  - Internal Auditor source-awareness check
okb_bundle_id: internal-auditor
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - soc-2
  - sox
  - compliance-officer
  - osh-act-general-safety
  - osha-hazard-communication
  - osha-injury-illness-recordkeeping
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
  - This bundle is not legal advice, professional certification, engineering approval, safety approval, or a substitute for licensed/qualified review.
  - Scenario-specific answers require current official sources, local evidence, and qualified review.
  - Do not infer facts about local systems, worksites, contracts, controls, people, hazards, or compliance status without evidence.
safety_notes:
  - Minimize sensitive personal, employee, customer, PHI/ePHI, security, payroll, and incident data in prompts and examples.
  - Require explicit confirmation before live operational, legal, safety, security, employment, reporting, disclosure, deployment, or contract actions.
  - Route final reliance to qualified professionals, licensed trades, counsel, auditors, safety staff, security leadership, or management as appropriate.
timestamp: "2026-07-10T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-10
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 18
  okb_score: 33
  absolute_lift: 15
  task_scores:
    -
      task: role-task-with-limited-evidence
      baseline_score: 7
      okb_score: 11
      max_score: 12
    -
      task: role-prioritization-review
      baseline_score: 7
      okb_score: 11
      max_score: 12
    -
      task: role-source-reconciliation
      baseline_score: 4
      okb_score: 11
      max_score: 12
  comparison_scores:

  display_summary: Improved measured rubric score from 18/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Internal Auditor

Role bundle for internal audit planning, risk/control assessment, evidence requests, findings, and management-action tracking.

## Required Answer Habit

Include a short **Source note** naming the official source category, local evidence used, and missing source or fact still needed before a conclusion is reliable.

## Start Here

- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)
