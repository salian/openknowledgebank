---
type: Bundle Index
title: Applications Programmer
description: Source-aware role bundle for application requirements, code-change planning, implementation review, testing, debugging, and release-ready engineering briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- application-development
- programming
- software-testing
- role
aliases:
- Applications Programmer
- Application Programmer
problems_solved:
- Plan application changes without fabricating codebase facts.
- Produce reviewable implementation and test plans.
- Separate proposed behavior from verified execution.
industries:
- Software
- Information technology
tools: []
frameworks:
- source-evidence matrix
- change-evidence matrix
- qualified-review gate
deliverables:
- Application change implementation brief
commands: []
skills: []
evaluations:
- Applications Programmer source-awareness check
okb_bundle_id: applications-programmer
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- agile
- docker
- jira
- scrum
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 15-1251.00
  soc: []
  isco_08: []
  esco:
  - '2514'
limitations:
- Codebase-specific work requires current repository, interface, dependency, test, and runtime evidence.
- This bundle does not prove security or production readiness.
- Do not infer files, symbols, API behavior, test outcomes, or deployment state.
safety_notes:
- Protect secrets, credentials, personal data, and proprietary code.
- Require confirmation before destructive migrations, dependency upgrades, releases, or production changes.
- Route security, privacy, and high-impact architecture decisions to qualified reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 11
  okb_score: 33
  absolute_lift: 22
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 10
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 5
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 11/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Applications Programmer

Source-aware role bundle for application requirements, code-change planning, implementation review, testing, debugging, and release-ready engineering briefs.

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
- [deliverables/application-change-brief.md](deliverables/application-change-brief.md)
