# Bundle Validator

The public repository includes a lightweight validator for bundle structure, registry metadata, internal links, and obvious public-safety issues.

Run it before opening a pull request:

```bash
python tools/validate-bundle/validate.py --root .
```

Current checks include:

- `registry/bundles.json` parses and contains valid bundle entries
- required registry fields are present
- bundle IDs use lowercase kebab-case
- categories, trust tiers, and statuses are recognized
- registry paths point to existing bundle directories
- each listed bundle has `index.md`, `log.md`, and a category core file
- every markdown concept has YAML frontmatter
- every concept has a `type`
- internal markdown links resolve
- related and adjacent bundle references point to known bundle IDs or emit warnings
- public bundle and registry files do not include obvious secrets, API key assignments, private keys, or local workspace paths

Warnings do not block CI, but should be addressed before a bundle is promoted from `draft` to `stable`.
