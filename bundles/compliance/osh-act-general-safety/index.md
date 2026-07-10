---
type: Bundle Index
title: OSH Act General Safety
description: Source-aware compliance bundle for OSH Act general duty, worker rights, employer duties, and OSHA posting/source triage.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - osha
  - osh-act
  - general-duty
  - workplace-safety
  - compliance
aliases:
  - Occupational Safety and Health Act general requirements
  - OSH Act general duty
  - OSHA general safety requirements
problems_solved:
  - Route OSH Act General Safety work to the right source category and evidence set.
  - Separate verified source facts, user-provided facts, assumptions, and missing evidence.
  - Produce a OSH Act source-aware safety brief suitable for professional review.
industries:
  - cross-industry
tools: []
frameworks:
  - source-evidence matrix
  - inspect-first workflow
  - professional-review gate
deliverables:
  - OSH Act source-aware safety brief
commands: []
skills: []
evaluations:
  - OSH Act General Safety source-awareness check
okb_bundle_id: osh-act-general-safety
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - osha-hazard-communication
  - osha-injury-illness-recordkeeping
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
  baseline_score: 15
  okb_score: 30
  absolute_lift: 15
  task_scores:
    -
      task: applicability-triage
      baseline_score: 4
      okb_score: 10
      max_score: 12
    -
      task: source-aware-checklist
      baseline_score: 7
      okb_score: 9
      max_score: 12
    -
      task: conflicting-evidence-review
      baseline_score: 4
      okb_score: 11
      max_score: 12
  comparison_scores:

  display_summary: Improved measured rubric score from 15/36 to 30/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# OSH Act General Safety

Source-aware compliance bundle for OSH Act general duty, worker rights, employer duties, and OSHA posting/source triage.

## Required Answer Habit

Include a short **Source note** naming the official source category, local evidence used, and missing source or fact still needed before a conclusion is reliable.

## Start Here

- [overview.md](overview.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)
