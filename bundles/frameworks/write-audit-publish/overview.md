---
type: "Bundle Overview"
title: "Write-Audit-Publish Pattern overview"
description: "Scope, evidence, and authority boundaries for Write-Audit-Publish Pattern."
---
# Write-Audit-Publish Pattern Overview

Verify the deployed Iceberg version and engine support, target table and branch semantics, write isolation, audit checks, promotion mechanism, concurrency, retention, rollback, access, monitoring, and ownership before proposing implementation.

## Evidence Contract

Relevant evidence includes Iceberg and engine versions, catalog and table configuration, branch state, write and audit queries, data-quality rules, concurrency behavior, retention policy, access controls, change plan, rollback evidence, and approvals. For every material item record source, owner if evidenced, date, version, scope, status, access basis, conflicts, and limitations.

When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None`. Put exact missing artifacts under `Needs verification`. A general disclaimer is not a substitute for requesting evidence.

## Boundary

Analysis and drafting do not establish engine support, catalog configuration, branch state, snapshot identity, audit result, data correctness, retention safety, rollback success, production readiness, or approval. Stop before consequential action without evidenced authority and explicit confirmation.
