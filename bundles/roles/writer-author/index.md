---
type: "Bundle Index"
title: "Writer and Author"
description: "Evidence-grounded planning and review for Writer and Author work, with explicit source, local-evidence, qualification, and authority boundaries."
category: roles
version: 0.1.0
tags:
- "writer"
- "role"
- "source-aware"
aliases:
- "Author"

problems_solved:
- "Prepare reviewable Writer and Author work from inspected evidence."
- "Separate occupational guidance from local role, qualification, records, decisions, and authority."
industries:
- "Publishing"
- "Media"
- "Communications"
tools: []
frameworks:
- "evidence-grounded role workflow"
deliverables:
- "writing assignment and publication review brief"
commands: []
skills: []
evaluations:
- "Writer and Author source-awareness check"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
[]
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - "27-3043.00"
  soc: []
  isco_08: []
  esco: []
content_risk:
  classification: "regulated"
  domains:
  - "legal"
  - "privacy"
  professional_review:
    status: not_reviewed
    required_qualification: "A qualified role owner and legal, clinical, safety, privacy, financial, public-sector, or other professional appropriate to the task and jurisdiction."
limitations:
- "Occupational sources describe generalized work activities; they do not establish a specific person's role, competence, credentials, authority, employer procedures, records, permissions, outcomes, or approval."
- "Task-specific conclusions require current inspected evidence for current sources, actual role, jurisdiction, qualifications, local procedures, systems, records, constraints, conflicts, approvals, validation evidence, and accountable ownership."
- "This bundle does not grant authority to publish or submit work, claim authorship or rights, disclose confidential information, make legal representations, or represent editorial approval."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to publish or submit work, claim authorship or rights, disclose confidential information, make legal representations, or represent editorial approval."
timestamp: "2026-08-12T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: writer-author
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: "No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available."
  evidence_note: "No measured score is claimed."
evaluation_detail:
  status: blocked
  next_action: "Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard."
---
# Writer and Author

Use this bundle to prepare a reviewable **writing assignment and publication review brief** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent brief, source, quote, rights, authorship, fact, confidentiality status, editorial decision, publication state, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [writing assignment and publication review brief](deliverables/writer-author-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
