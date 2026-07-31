---
type: Bundle Index
title: ICT System Developer
description: Source-aware role bundle for ICT system analysis, integration design, workflow and capability review, implementation planning, and validation-ready system briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- ict-systems
- systems-development
- systems-integration
- role
aliases:
- ICT System Developer
- Systems Developer
problems_solved:
- Design integrations without invented interfaces.
- Connect workflow requirements to testable system changes.
- Prepare operationally reviewable implementation plans.
industries:
- Information technology
tools: []
frameworks:
- source-evidence matrix
- system-evidence matrix
- qualified-review gate
deliverables:
- ICT system design and integration brief
commands: []
skills: []
evaluations:
- ICT System Developer source-awareness check
okb_bundle_id: ict-system-developer
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- agile
- docker
- fda-qmsr-13485
- gdpr
- jira
- scrum
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 15-1211.00
  soc: []
  isco_08: []
  esco:
  - ICT system developer
limitations:
- Environment-specific work requires current workflow, system, interface, control, and operations evidence.
- This bundle does not certify security or compliance.
- Do not infer integrations, fields, capacity, compatibility, or production state.
safety_notes:
- Protect credentials, personal data, and sensitive architecture.
- Require confirmation before access, integration, migration, or production changes.
- Route security, privacy, continuity, and compliance decisions to accountable reviewers.
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
  okb_score: 33
  absolute_lift: 19
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 5
    okb_score: 12
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 5
    okb_score: 10
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 14/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# ICT System Developer

Source-aware role bundle for ICT system analysis, integration design, workflow and capability review, implementation planning, and validation-ready system briefs.

## Required Answer Habit

Include a short **Source note** naming authoritative source categories and local
evidence used, assumptions made, and missing verification required before reliance.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name the source category, scope, date or version, and conflict checks required.
4. **Confirmation boundary** - identify the accountable reviewer and actions that must not occur without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not collapse missing evidence into a general disclaimer. Ask for the exact artifacts needed and explain which decision each artifact supports.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/ict-system-brief.md](deliverables/ict-system-brief.md)
