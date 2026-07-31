---
type: Bundle Index
title: Content Creator / Social Media Producer
description: Source-aware role bundle for digital content creation and social production, evidence reconciliation, reviewable recommendations, and controlled consequential actions.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- "content-creator-social-media-producer"
- "digital"
- "role"
aliases:
- "Content Creator / Social Media Producer"
problems_solved:
- "Prepare a content production brief without fabricating local facts."
- "Separate verified, provided, assumed, and missing evidence."
- "Produce a review-ready recommendation with explicit verification and approval boundaries."
industries:
- "Media"
- "Marketing"
tools: []
frameworks:
- "source-evidence matrix"
- "digital content creation and social production review matrix"
- "qualified-review gate"
deliverables:
- "content production brief"
commands: []
skills: []
evaluations:
- "Content Creator / Social Media Producer source-awareness check"
okb_bundle_id: content-creator-social-media-producer
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- "adobe-photoshop"
- "adobe-premiere-pro"
- "content-calendar"
- "coppa"
- "ftc-endorsement-and-review-integrity-rules"
adjacent_bundles: []
contributors:
- "OpenKnowledgeBank"
maintainers:
- "OpenKnowledgeBank"
standard_mappings:
  onet_soc:
  - "27-3099.00"
  soc: []
  isco_08: []
  esco:
  - "http://data.europa.eu/esco/occupation/social-media-content-creator"
limitations:
- "Use the cited official, originator, standards, or professional sources for general digital content creation and social production context; local facts, records, values, states, and permissions require inspected evidence."
- "Task-specific work requires current evidence for objective, audience, channel, jurisdiction, and success criteria; creative brief, script, claims, and approvals; source assets, copyright, licenses, releases, and usage rights; sponsorships, material connections, disclosure requirements, and brand safety; accessibility, schedule, distribution, budget, and measurement definitions."
- "Do not infer asset rights, subject consent, claim substantiation, disclosure sufficiency, audience response, or content performance."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, and other sensitive data."
- "Require explicit confirmation before publishing content, using unclear-rights assets, targeting minors, entering sponsorships, or committing spend."
- "Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to an evidenced accountable reviewer."
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 17
  okb_score: 36
  absolute_lift: 19
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 1
    okb_score: 12
    max_score: 12
  - task: role-task-review
    baseline_score: 10
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 17/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Content Creator / Social Media Producer

Source-aware role bundle for digital content creation and social production, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

Do not assign an owner, author, date, or version to a provided artifact unless the request states it. Mark each absent field `Needs verification`.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/content-creator-social-media-producer-brief.md](deliverables/content-creator-social-media-producer-brief.md)
