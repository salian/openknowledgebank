---
type: Tool Guide
title: "Kubernetes"
description: "Defines source-aware container orchestration and cluster operations, evidence handling, and action boundaries."
tool_category: "Container orchestration"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review container orchestration and cluster operations from supplied evidence."
  - "Draft a kubernetes operations and change brief with explicit evidence states."
confirmation_required:
  - "applying or deleting resources, changing images, configuration, secrets, access, scaling, networking, storage, or production traffic"
okb_bundle_id: kubernetes
timestamp: "2026-07-31T00:00:00Z"
---

# Kubernetes

Source-aware tool bundle for Kubernetes workload, service, configuration, access, rollout, reliability, and incident evidence with controlled implementation briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- cluster version and context
- namespaces and ownership
- manifests and applied objects
- workloads, services, ingress, storage, and configuration
- RBAC and service-account evidence
- events, status, logs, metrics, and rollout history
- backup, policy, and change approvals

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before applying or deleting resources, changing images, configuration, secrets, access, scaling, networking, storage, or production traffic.
