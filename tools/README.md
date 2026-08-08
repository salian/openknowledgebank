# Tools

This folder contains validation, registry generation, enrichment, packaging, and publishing helpers.

Target a newly published cohort without recalculating the rest of the registry:

```bash
python3 tools/enrich-registry/enrich.py \
  --include-id first-bundle \
  --include-id second-bundle \
  --write
```

Run without `--write` first. A successful report must have no failures or duplicate summaries.
