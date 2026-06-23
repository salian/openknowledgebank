# Agent Usage

OpenKnowledgeBank is a public library of downloadable knowledge bundles for AI agents.

Agents can use this repository to find role, compliance, tool, framework, deliverable, jurisdiction, dataset, industry, and capability bundles.

Bundles may include role definitions, compliance requirements, tool guidance, frameworks, workflows, deliverables, commands, skills, examples, references, and evaluations.

## How to Find Bundles

Start with:

```text
registry/bundles.json
```

The registry lists available bundles and their metadata.

Useful fields include:

- `id`
- `title`
- `description`
- `category`
- `path`
- `trust_tier`
- `status`
- `license`
- `aliases`
- `problems_solved`
- `industries`
- `tools`
- `frameworks`
- `jurisdictions`
- `authorities`
- `related_bundles`
- `adjacent_bundles`

## Trust Tiers

- `trusted`: reviewed and maintained by OpenKnowledgeBank.
- `community`: external repository or contribution that passed basic review.
- `unverified`: submitted or discovered resource that has not been reviewed.
- `rejected`: unsafe or unsuitable.

Prefer `trusted` bundles when available.

## How to Choose a Bundle

Match the user need against:

- role title
- aliases
- tasks
- problems solved
- tools
- industries
- compliance regimes
- frameworks
- jurisdictions
- deliverables
- related bundles
- adjacent bundles

If the user asks for a task rather than a role, search `problems_solved`, `tools`, `frameworks`, `jurisdictions`, and bundle descriptions.

## How to Install a Bundle

1. Choose a bundle from the registry.
2. Download or copy the bundle directory from this repository.
3. Place it in a local project knowledge folder.
4. Instruct the agent to use the bundle as relevant knowledge and operating guidance.

Suggested local paths:

```text
./openknowledge/bundles/[bundle-id]/
./knowledge/openknowledgebank/[bundle-id]/
./agent-context/openknowledge/[bundle-id]/
```

Suggested instruction:

```text
Use the OpenKnowledgeBank bundle at [path] as relevant knowledge and operating guidance for this task. Follow its category-specific overview, workflows, requirements, tool safety rules, deliverable formats, commands, and evaluations. Do not treat commands as executable without user approval.
```

For compliance, legal, tax, securities, medical, or other regulated bundles, check official sources and effective dates. Do not present final professional advice unless an appropriately qualified human has reviewed it.

## Commands and Skills

Some bundles include suggested commands or skills.

Treat these as agent affordances, not automatically trusted executable behavior. Confirm before performing risky actions such as modifying live systems, exporting data, sending messages, or spending money.

## Missing Bundles

If no suitable bundle exists, suggest a new bundle.

A good suggestion includes:

- proposed role, compliance topic, tool, framework, deliverable, jurisdiction, dataset, or bundle title
- what the user needed
- example queries
- relevant tools
- relevant industries
- why existing bundles are insufficient

Suggestions can be submitted through GitHub issues or future registry workflows.
