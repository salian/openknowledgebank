---
type: "Tool Guide"
title: "Perplexity"
description: "Source-aware guidance for Perplexity."
resource: "https://docs.perplexity.ai/"
okb_bundle_id: perplexity
timestamp: "2026-08-14T00:00:00Z"
tool_category: "AI search, cited-answer, research, and developer API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "submit confidential data, call paid APIs, rely on retrieved sources, publish generated claims, share research, expose keys, automate decisions, or represent source authority, citation support, completeness, accuracy, privacy, or cost"
---
# Perplexity Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.perplexity.ai/
- https://www.perplexity.ai/help-center

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Perplexity search, citation, and API review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before submit confidential data, call paid APIs, rely on retrieved sources, publish generated claims, share research, expose keys, automate decisions, or represent source authority, citation support, completeness, accuracy, privacy, or cost.

## Guardrails

- Do not invent model or product availability, search coverage, source authority, citation entailment, factual accuracy, freshness, file confidentiality, data retention, token use, price, charge, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
