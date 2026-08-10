# OpenKnowledgeBank

[![Website](https://img.shields.io/badge/website-openknowledgebank.com-111827)](https://openknowledgebank.com)
[![Content license: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-0f766e)](LICENSE.md)
[![Code license: MIT](https://img.shields.io/badge/code-MIT-2563eb)](LICENSE-CODE.md)

Portable, inspectable knowledge bundles for LLM agents.

OpenKnowledgeBank gives agents role knowledge, workflows, safety rules, deliverable formats, commands, examples, and evaluations as plain markdown directories that can be reused across tools and models.

Use it when you want an agent to do specialized work with better structure, clearer source discipline, and more reusable operating guidance than a one-off prompt.

**Status:** early public preview. The current catalog and each bundle's publication and evaluation status are maintained in [registry/bundles.json](registry/bundles.json).

**Star this repo to follow the open library of reusable agent knowledge bundles.**

## See What A Bundle Changes

The [SEO Specialist / Consultant bundle](bundles/roles/seo-specialist-consultant) shows how reusable knowledge changes an agent's approach to a familiar problem.

**Task:** A founder says organic traffic fell and asks for an SEO audit, but provides no Search Console, analytics, crawl, URL, CMS, or date-range evidence.

**Without the bundle:** The agent jumps to a generic diagnosis and recommends titles, keywords, backlinks, sitemap submission, and content updates without knowing what caused the decline.

**With the bundle:** The agent explains that it cannot identify the cause yet, requests the evidence needed to investigate, and organizes the review around measurement, demand, crawling, indexing, relevance, internal links, and recent technical changes.

The assisted response is more useful because it separates what is known from what still needs verification and turns a vague request into an actionable investigation. You can inspect the [task, both responses, and evaluation](bundles/roles/seo-specialist-consultant/examples/before-after/technical-seo-triage) in the repository.

## Try It In 60 Seconds

Copy a bundle into your project or point your agent at it directly:

```text
Use the OpenKnowledgeBank bundle at bundles/roles/seo-specialist-consultant
to investigate an organic-traffic decline. Follow its audit workflow,
evidence checks, safety boundaries, and SEO audit brief format. Separate
verified facts from hypotheses and missing inputs. Do not diagnose the cause
or recommend changes to the live site until the necessary evidence is available.
```

Useful starting files:

- [registry/bundles.json](registry/bundles.json): machine-readable bundle catalog.
- [AGENT_USAGE.md](AGENT_USAGE.md): guidance for agents consuming bundles.
- [bundles/roles/seo-specialist-consultant/index.md](bundles/roles/seo-specialist-consultant/index.md): entry point for the SEO Specialist / Consultant bundle.
- [SEO technical-triage example](bundles/roles/seo-specialist-consultant/examples/before-after/technical-seo-triage): inspect the task, baseline response, bundle-assisted response, and evaluation.
- [docs/BUNDLE_SCHEMA.md](docs/BUNDLE_SCHEMA.md): current working bundle schema.

## Available Bundles

The catalog is maintained in [registry/bundles.json](registry/bundles.json), which is the source of truth for current bundle IDs, categories, publication status, trust tier, references, and evaluation summaries. It includes role, industry, capability, tool, framework, compliance, jurisdiction, deliverable, and dataset bundles.

Use the [website](https://openknowledgebank.com) to browse the catalog or inspect any bundle directly under [`bundles/`](bundles/).

### Write Descriptions For People

Registry descriptions appear on compact website cards, in search results, and in machine-readable discovery data. Put the subject, task, or outcome first so a reader can understand the bundle before the text is truncated.

Do not begin descriptions with internal quality labels or category names such as “source-aware guidance,” “evidence-first,” “evidence-grounded,” “role bundle,” or “framework bundle.” The registry already stores category, trust, source, and evaluation metadata separately. Describe what the bundle helps an agent understand, produce, investigate, or review.

## What Is Inside A Bundle?

Bundles are plain markdown directories with YAML frontmatter. Depending on the bundle type, they may include:

- role definitions and responsibilities
- operating principles and safety boundaries
- workflows, playbooks, and frameworks
- tool guidance and source requirements
- deliverable formats and quality bars
- commands and skill suggestions
- examples, references, and evaluations

Bundles can represent roles, industries, capabilities, tools, frameworks, compliance regimes, jurisdictions, deliverables, and datasets.

## Public Repository Boundary

This is a public repository. Everything committed here should be safe to inspect, reuse, and redistribute under the applicable license.

Publishable bundles, public registry data, schemas, validators, examples, and contributor documentation belong here. Do not commit secrets, credentials, private notes, personal or customer data, confidential examples, unpublished strategy, private workspace paths, or source material that cannot be publicly redistributed.

Run the public validator before opening a pull request:

```bash
python tools/validate-bundle/validate.py --root .
```

## Who This Is For

- Agent builders who want reusable domain knowledge instead of long prompt fragments.
- Teams evaluating whether specialized context improves agent output quality.
- Contributors who want to publish practical, inspectable knowledge for AI-assisted work.
- Tool builders who need a simple catalog format for agent-ready knowledge bundles.

## Contribute

OpenKnowledgeBank is free to use, inspect, remix, and contribute to.

Good contributions improve bundle quality, add useful role knowledge, strengthen evaluations, improve registry metadata, or make bundles easier for agents and humans to use.

Start with:

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [docs/BUNDLE_CREATION_PROCESS.md](docs/BUNDLE_CREATION_PROCESS.md)
- [docs/BUNDLE_SCHEMA.md](docs/BUNDLE_SCHEMA.md)

## Repository Structure

```text
bundles/
  roles/
  industries/
  capabilities/
  tools/
  frameworks/
  compliance/
  jurisdictions/
  deliverables/
  datasets/
registry/
schemas/
tools/
examples/
docs/
```

## License

Knowledge bundles, documentation, and examples are licensed under [Creative Commons Attribution 4.0 International](LICENSE.md).

Code and tooling are licensed under [MIT](LICENSE-CODE.md).
