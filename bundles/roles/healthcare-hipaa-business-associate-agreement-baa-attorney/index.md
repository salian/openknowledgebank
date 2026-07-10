---
type: Bundle Index
title: Healthcare / HIPAA BAA Attorney
description: Micro-role bundle for HIPAA business associate agreement issue spotting, source-aware clause review, and professional legal review boundaries.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags:
  - hipaa
  - baa
  - healthcare-law
  - contracts
  - privacy
aliases:
  - HIPAA BAA Attorney
  - Business Associate Agreement Lawyer
problems_solved:
  - Route Healthcare / HIPAA BAA Attorney work to the right source category and evidence set.
  - Separate verified source facts, user-provided facts, assumptions, and missing evidence.
  - Produce a BAA source-aware issue brief suitable for professional review.
industries:
  - cross-industry
tools: []
frameworks:
  - source-evidence matrix
  - inspect-first workflow
  - professional-review gate
deliverables:
  - BAA source-aware issue brief
commands: []
skills: []
evaluations:
  - Healthcare / HIPAA BAA Attorney source-awareness check
okb_bundle_id: healthcare-hipaa-business-associate-agreement-baa-attorney
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - hipaa
  - hipaa-privacy-rule
  - hipaa-security-rule
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
  baseline_score: 23
  okb_score: 33
  absolute_lift: 10
  task_scores:
    -
      task: role-task-with-limited-evidence
      baseline_score: 10
      okb_score: 11
      max_score: 12
    -
      task: role-prioritization-review
      baseline_score: 6
      okb_score: 11
      max_score: 12
    -
      task: role-source-reconciliation
      baseline_score: 7
      okb_score: 11
      max_score: 12
  comparison_scores:

  display_summary: Improved measured rubric score from 23/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Healthcare / HIPAA BAA Attorney

Micro-role bundle for HIPAA business associate agreement issue spotting, source-aware clause review, and professional legal review boundaries.

## Required Answer Habit

Include a short **Source note** naming the official source category, local evidence used, and missing source or fact still needed before a conclusion is reliable.

## Start Here

- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)
