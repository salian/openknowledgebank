---
type: Bundle Index
title: Social Media Manager / Specialist
description: Source-aware role bundle for organic social strategy, content planning, community and reputation review, performance analysis, and approval-ready publishing briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- social-media
- content-planning
- community-management
- role
aliases:
- Social Media Manager
- Social Media Specialist
problems_solved:
- Plan social content without invented audience facts.
- Protect claims, rights, and moderation boundaries.
- Analyze performance with explicit scope and uncertainty.
industries:
- Marketing
- Communications
tools: []
frameworks:
- source-evidence matrix
- content-evidence matrix
- qualified-review gate
deliverables:
- Social media content and community brief
commands: []
skills: []
evaluations:
- Social Media Manager / Specialist source-awareness check
okb_bundle_id: social-media-manager-specialist
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- can-spam
- ftc-endorsement-and-review-integrity-rules
- gdpr
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 27-3031.00
  soc: []
  isco_08: []
  esco:
  - social media manager
limitations:
- Channel-specific work requires current account, content, rights, policy, approval, and performance evidence.
- This bundle does not establish legal rights or regulatory compliance.
- Do not infer sentiment, reach, engagement, rights, endorsement status, or account state.
safety_notes:
- Minimize personal and community-member data.
- Require confirmation before publishing, direct messaging, moderation, deletion, or escalation.
- Route legal, rights, crisis, privacy, and regulated-claim decisions to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 10
  okb_score: 32
  absolute_lift: 22
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 11
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 11
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 3
    okb_score: 10
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 10/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Social Media Manager / Specialist

Source-aware role bundle for organic social strategy, content planning, community and reputation review, performance analysis, and approval-ready publishing briefs.

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
- [deliverables/social-media-brief.md](deliverables/social-media-brief.md)
