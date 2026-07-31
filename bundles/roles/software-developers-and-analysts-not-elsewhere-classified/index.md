---
type: Bundle Index
title: Software Developers and Analysts Not Elsewhere Classified
description: Source-aware role bundle for atypical software development and analysis work that does not fit a narrower taxonomy, with explicit scope classification and review boundaries.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- software-analysis
- software-development
- taxonomy
- role
aliases:
- Software Developers and Analysts NEC
- Software Specialists NEC
problems_solved:
- Handle residual software roles without pretending the title defines the work.
- Classify scope before implementation.
- Route high-risk or specialist work explicitly.
industries:
- Software
- Information technology
tools: []
frameworks:
- source-evidence matrix
- scope-and-evidence matrix
- qualified-review gate
deliverables:
- Software role classification and implementation brief
commands: []
skills: []
evaluations:
- Software Developers and Analysts Not Elsewhere Classified source-awareness check
okb_bundle_id: software-developers-and-analysts-not-elsewhere-classified
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- agile
- confluence
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
  - 15-1299.00
  soc: []
  isco_08: []
  esco:
  - '2519'
limitations:
- This residual classification does not define a specific software discipline or grant expertise.
- Task-specific work requires current scope, system, code, data, test, and owner evidence.
- Do not infer responsibilities, technology, behavior, or production state.
safety_notes:
- Protect secrets, credentials, personal data, and proprietary source.
- Require confirmation before changes, migrations, releases, or production actions.
- Route security, privacy, regulated, safety-critical, and domain-specialist work appropriately.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 15
  okb_score: 32
  absolute_lift: 17
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 10
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 6
    okb_score: 10
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 7
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Software Developers and Analysts Not Elsewhere Classified

Source-aware role bundle for atypical software development and analysis work that does not fit a narrower taxonomy, with explicit scope classification and review boundaries.

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
- [deliverables/software-role-classification-brief.md](deliverables/software-role-classification-brief.md)
