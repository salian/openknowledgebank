---
type: "Bundle Overview"
title: "Infrastructure as Code Template overview"
description: "Scope, evidence, and authority boundaries for Infrastructure as Code Template."
---
# Infrastructure as Code Template Overview

Verify tool, provider, module and API versions; inspect target environment, ownership and state; define resources, inputs, outputs, dependencies, naming and tags, secrets, identity and least privilege, network and data controls, policy, validation, tests, plan review, cost, drift, observability, rollout, rollback, and approvals.

## Evidence Contract

Relevant evidence includes tool and provider versions, target accounts and regions, current state and imports, approved architecture, resource schemas and quotas, module provenance, inputs and outputs, identity and access design, secrets handling, network and data controls, policy checks, formatting and validation, tests and plan output, cost estimate, drift and rollback plan, observability, and approvals. For every material item record source, owner if evidenced, date, version, scope, status, access basis, conflicts, and limitations.

When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None`. Put exact missing artifacts under `Needs verification`. A general disclaimer is not a substitute for requesting evidence.

## Boundary

Analysis and drafting do not establish tool or provider version, schema, account state, permission, quota, resource value, secret, plan effect, cost, policy result, security, compliance, rollback success, production readiness, or approval. Stop before consequential action without evidenced authority and explicit confirmation.
