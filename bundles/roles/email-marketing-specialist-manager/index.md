---
type: Bundle Index
title: Email Marketing Specialist / Manager
description: Source-aware role bundle for email strategy, segmentation and lifecycle planning, consent and suppression review, content QA, experiment design, and approval-ready send briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- email-marketing
- lifecycle-marketing
- marketing-operations
- role
aliases:
- Email Marketing Specialist
- Email Marketing Manager
problems_solved:
- Prepare sends without pretending to inspect a platform.
- Protect consent and suppression boundaries.
- Measure campaigns with explicit definitions and uncertainty.
industries:
- Marketing
- Digital commerce
tools: []
frameworks:
- source-evidence matrix
- send-evidence matrix
- qualified-review gate
deliverables:
- Email campaign and send-readiness brief
commands: []
skills: []
evaluations:
- Email Marketing Specialist / Manager source-awareness check
okb_bundle_id: email-marketing-specialist-manager
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- can-spam
- ccpa
- gdpr
- hubspot-sales-hub
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 13-1161.00
  soc: []
  isco_08: []
  esco:
  - dc97adbe-f807-4ad8-8f3c-c24b3416cdef
limitations:
- Program-specific work requires current list, consent, suppression, segment, content, sender, automation, and performance evidence.
- This bundle does not establish legal compliance or deliverability.
- Do not infer consent, membership, list size, sender state, delivery, or results.
safety_notes:
- Minimize personal and subscriber data.
- Require confirmation before sending, scheduling, enrollment, imports, exports, or consent and suppression changes.
- Route privacy, communications-law, security, and regulated-claim decisions to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 9
  okb_score: 32
  absolute_lift: 23
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
    baseline_score: 3
    okb_score: 11
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 9/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Email Marketing Specialist / Manager

Source-aware role bundle for email strategy, segmentation and lifecycle planning, consent and suppression review, content QA, experiment design, and approval-ready send briefs.

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
- [deliverables/email-send-readiness-brief.md](deliverables/email-send-readiness-brief.md)
