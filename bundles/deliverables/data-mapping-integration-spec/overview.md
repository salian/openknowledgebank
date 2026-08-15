---
type: "Bundle Overview"
title: "Data Mapping and Integration Specification overview"
description: "Scope, evidence, and authority boundaries for Data Mapping and Integration Specification."
---
# Data Mapping and Integration Specification Overview

Inspect source and target schemas and versions; define business meaning, keys, grain, types, nullability, mappings, transformations, code sets, filters, joins, timing, lineage, quality checks, reconciliation, security, failure handling, observability, rollback, ownership, and approval.

## Evidence Contract

Relevant evidence includes source and target systems and versions, inspected schemas and samples, field definitions and owners, keys and grain, types and constraints, mapping and transformation rules, code sets, timing and volumes, lineage, quality and reconciliation rules, privacy and security controls, failure handling, tests, and approvals. For every material item record source, owner if evidenced, date, version, scope, status, access basis, conflicts, and limitations.

When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None`. Put exact missing artifacts under `Needs verification`. A general disclaimer is not a substitute for requesting evidence.

## Boundary

Analysis and drafting do not establish system access, schema, field meaning, key, grain, type, transformation, data quality, permission, compatibility, runtime result, reconciliation, or approval. Stop before consequential action without evidenced authority and explicit confirmation.
