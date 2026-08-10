---
type: Bundle Overview
title: Star and Snowflake Schema Design overview
description: Scope, evidence, and authority boundaries for Star and Snowflake Schema Design.
---
# Star and Snowflake Schema Design Overview

Source-aware guidance for grain, facts, dimensions, normalization choices, conformance, performance, and governed schema design.

## Evidence Contract

Relevant evidence includes business process, query use cases, source schemas, grain, facts, dimensions, hierarchies, keys, cardinalities, history, conformance, platform behavior, data volumes, security classifications, performance evidence, tests, owners, and approvals. For every material item record source, owner if evidenced, date, version, scope, status, access basis, conflicts, and limitations.

When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None`. Put exact missing artifacts under `Needs verification`. A general disclaimer is not a substitute for requesting evidence.

## Boundary

Analysis and drafting do not establish Source semantics, grain, fact additivity, dimension meaning, hierarchy validity, key behavior, history, conformance, effective access, query correctness, performance, and migration impact. Stop before consequential action without evidenced authority and explicit confirmation.

