---
type: Bundle Index
title: OSHA Machine Guarding, Lockout/Tagout, and Process Safety Management
description: Source-aware compliance bundle for machine guarding, hazardous energy control, and process safety management triage.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - osha
  - machine-guarding
  - lockout-tagout
  - psm
  - process-safety
aliases:
  - machine guarding
  - LOTO
  - process safety management
  - 29 CFR 1910.147
  - 29 CFR 1910.119
problems_solved:
  - Route OSHA Machine Guarding, Lockout/Tagout, and Process Safety Management work to the right source category and evidence set.
  - Separate verified source facts, user-provided facts, assumptions, and missing evidence.
  - Produce a machine and process safety review brief suitable for professional review.
industries:
  - cross-industry
tools: []
frameworks:
  - source-evidence matrix
  - inspect-first workflow
  - professional-review gate
deliverables:
  - machine and process safety review brief
commands: []
skills: []
evaluations:
  - OSHA Machine Guarding, Lockout/Tagout, and Process Safety Management source-awareness check
okb_bundle_id: osha-machine-and-process-safety
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - osh-act-general-safety
  - osha-hazard-communication
  - osha-injury-illness-recordkeeping
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
  baseline_score: 15
  okb_score: 32
  absolute_lift: 17
  task_scores:
    -
      task: applicability-triage
      baseline_score: 4
      okb_score: 11
      max_score: 12
    -
      task: source-aware-checklist
      baseline_score: 8
      okb_score: 10
      max_score: 12
    -
      task: conflicting-evidence-review
      baseline_score: 3
      okb_score: 11
      max_score: 12
  comparison_scores:

  display_summary: Improved measured rubric score from 15/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# OSHA Machine Guarding, Lockout/Tagout, and Process Safety Management

Source-aware compliance bundle for machine guarding, hazardous energy control, and process safety management triage.

## Required Answer Habit

Include a short **Source note** naming the official source category, local evidence used, and missing source or fact still needed before a conclusion is reliable.

## Start Here

- [overview.md](overview.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)
