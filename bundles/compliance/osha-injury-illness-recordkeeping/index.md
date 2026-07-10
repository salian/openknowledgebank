---
type: Bundle Index
title: OSHA Injury and Illness Recordkeeping and Reporting
description: Source-aware compliance bundle for OSHA injury and illness recording, reporting, and electronic submission triage.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - osha
  - recordkeeping
  - injury-reporting
  - illness-reporting
  - part-1904
aliases:
  - OSHA 300 Log
  - OSHA 301
  - OSHA 300A
  - 29 CFR Part 1904
problems_solved:
  - Route OSHA Injury and Illness Recordkeeping and Reporting work to the right source category and evidence set.
  - Separate verified source facts, user-provided facts, assumptions, and missing evidence.
  - Produce a recordkeeping and reporting decision brief suitable for professional review.
industries:
  - cross-industry
tools: []
frameworks:
  - source-evidence matrix
  - inspect-first workflow
  - professional-review gate
deliverables:
  - recordkeeping and reporting decision brief
commands: []
skills: []
evaluations:
  - OSHA Injury and Illness Recordkeeping and Reporting source-awareness check
okb_bundle_id: osha-injury-illness-recordkeeping
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - osh-act-general-safety
  - osha-hazard-communication
  - osha-machine-and-process-safety
  - osha-occupational-exposure-limits
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
      task: applicability-triage
      baseline_score: 3
      okb_score: 11
      max_score: 12
    -
      task: source-aware-checklist
      baseline_score: 8
      okb_score: 11
      max_score: 12
    -
      task: conflicting-evidence-review
      baseline_score: 7
      okb_score: 11
      max_score: 12
  comparison_scores:

  display_summary: Improved measured rubric score from 18/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# OSHA Injury and Illness Recordkeeping and Reporting

Source-aware compliance bundle for OSHA injury and illness recording, reporting, and electronic submission triage.

## Required Answer Habit

Include a short **Source note** naming the official source category, local evidence used, and missing source or fact still needed before a conclusion is reliable.

## Start Here

- [overview.md](overview.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)
