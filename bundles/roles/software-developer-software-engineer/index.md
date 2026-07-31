---
type: Bundle Index
title: Software Developer / Software Engineer
description: Source-aware role bundle for software requirements, architecture and code-change planning, implementation, testing, review, and production-readiness decisions.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- software-development
- software-engineering
- code-review
- role
aliases:
- Software Developer
- Software Engineer
problems_solved:
- Plan code changes without fabricated repository facts.
- Produce reviewable implementation and validation plans.
- Keep production claims tied to executed evidence.
industries:
- Software
- Information technology
tools: []
frameworks:
- source-evidence matrix
- software-change evidence matrix
- qualified-review gate
deliverables:
- Software change implementation and review brief
commands: []
skills: []
evaluations:
- Software Developer / Software Engineer source-awareness check
okb_bundle_id: software-developer-software-engineer
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
  - 15-1252.00
  soc: []
  isco_08: []
  esco:
  - '2512'
limitations:
- Codebase-specific work requires current repository, contract, dependency, test, telemetry, and environment evidence.
- This bundle does not prove security or reliability.
- Do not infer code paths, behavior, test outcomes, incidents, or deployment state.
safety_notes:
- Protect secrets, credentials, personal data, and proprietary source.
- Require confirmation before destructive changes, migrations, releases, or production actions.
- Route security, privacy, safety-critical, and architectural decisions to qualified reviewers.
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
    baseline_score: 2
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 6
    okb_score: 12
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 6
    okb_score: 10
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 14/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Software Developer / Software Engineer

Source-aware role bundle for software requirements, architecture and code-change planning, implementation, testing, review, and production-readiness decisions.

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
- [deliverables/software-change-brief.md](deliverables/software-change-brief.md)
