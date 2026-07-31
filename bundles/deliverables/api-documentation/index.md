---
type: Bundle Index
title: API Documentation and Integration Guide
description: Source-aware deliverable bundle for API references and integration guides covering versioned contracts, authentication, operations, schemas, errors, examples, limits, security, and change history.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- api-documentation
- openapi
- integration-guide
- deliverable
aliases:
- API Documentation and Integration Guide
problems_solved:
- Prepare a api documentation and integration guide without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Software
- Information technology
- Developer tools
tools: []
frameworks:
- source-evidence matrix
- API contract and integration documentation review matrix
- qualified-review gate
deliverables:
- API documentation and integration guide
commands: []
skills: []
evaluations:
- API Documentation and Integration Guide source-awareness check
okb_bundle_id: api-documentation
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
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
- Use the cited official, originator, standards, or professional sources for general API contract and integration documentation context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for API owner, audience, use cases, environment, and version, authoritative specification, code, routes, operations, and lifecycle, authentication, authorization, scopes, credentials, and security requirements, parameters, headers, schemas, examples, validation, and content types, responses, errors, retries, idempotency, pagination, limits, and webhooks, and SDKs, testing, support, deprecation, changelog, and publication approval.
- Do not infer endpoint behavior, schema, authentication, error response, rate limit, and version support.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before publishing secrets or undocumented endpoints, changing API contracts, promising compatibility, or releasing documentation without technical and security review.
- Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 20
  okb_score: 36
  absolute_lift: 16
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 12
    max_score: 12
  - task: deliverable-quality-review
    baseline_score: 10
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 7
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 20/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# API Documentation and Integration Guide

Source-aware deliverable bundle for API references and integration guides covering versioned contracts, authentication, operations, schemas, errors, examples, limits, security, and change history.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

## Start Here

- [overview.md](overview.md)
- [deliverable.md](deliverable.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/api-documentation-brief.md](deliverables/api-documentation-brief.md)
