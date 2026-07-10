---
type: Bundle Index
title: OSHA PPE and Worker Protection Programs
description: Source-aware compliance bundle for OSHA PPE hazard assessment, selection, training, and worker-protection program triage.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - osha
  - ppe
  - worker-protection
  - hazard-assessment
  - safety-program
aliases:
  - personal protective equipment
  - PPE hazard assessment
  - 29 CFR 1910 Subpart I
problems_solved:
  - Route OSHA PPE and Worker Protection Programs work to the right source category and evidence set.
  - Separate verified source facts, user-provided facts, assumptions, and missing evidence.
  - Produce a PPE program evidence brief suitable for professional review.
industries:
  - cross-industry
tools: []
frameworks:
  - source-evidence matrix
  - inspect-first workflow
  - professional-review gate
deliverables:
  - PPE program evidence brief
commands: []
skills: []
evaluations:
  - OSHA PPE and Worker Protection Programs source-awareness check
okb_bundle_id: osha-ppe-and-worker-protection
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - osh-act-general-safety
  - osha-hazard-communication
  - osha-injury-illness-recordkeeping
  - osha-machine-and-process-safety
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
  baseline_score: 14
  okb_score: 31
  absolute_lift: 17
  task_scores:
    -
      task: applicability-triage
      baseline_score: 5
      okb_score: 10
      max_score: 12
    -
      task: source-aware-checklist
      baseline_score: 7
      okb_score: 10
      max_score: 12
    -
      task: conflicting-evidence-review
      baseline_score: 2
      okb_score: 11
      max_score: 12
  comparison_scores:

  display_summary: Improved measured rubric score from 14/36 to 31/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# OSHA PPE and Worker Protection Programs

Source-aware compliance bundle for OSHA PPE hazard assessment, selection, training, and worker-protection program triage.

## Required Answer Habit

Include a short **Source note** naming the official source category, local evidence used, and missing source or fact still needed before a conclusion is reliable.

## Start Here

- [overview.md](overview.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)
