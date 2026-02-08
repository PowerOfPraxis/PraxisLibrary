# Glossary Factory — Build Pipeline

This directory contains Python scripts for managing the Praxis Library glossary data.

## Architecture

The glossary is stored as **alphabetically sharded JSON files** in `data/glossary/`:
- `manifest.json` — Metadata, per-letter counts, domain counts
- `search-compact.json` — Lightweight search index for all terms (lazy-loaded)
- `a.json` through `z.json` — Full term definitions, one file per letter
- `_other.json` — Terms starting with numbers or special characters

## Scripts

| Script | Purpose | When to Run |
|--------|---------|-------------|
| `migrate.py` | One-time: convert legacy `glossary.json` to sharded format | Once during initial migration |
| `build_index.py` | Rebuild `manifest.json` + `search-compact.json` from shards | After any shard modification |
| `add_terms.py` | Add new terms from a CSV/JSON seed file | Each time new terms are ready |
| `validate.py` | Check data integrity across all shards | Before every git commit |

## Workflow

1. Prepare seed file in `seeds/` (CSV format: term, definition, tags, domain)
2. Run: `python add_terms.py seeds/your-seed-file.csv`
3. Run: `python validate.py`
4. Run: `python build_index.py`
5. Verify on glossary page, then git commit

## Term Schema

```json
{
  "id": "term-example-name",
  "term": "Example Name",
  "definition": "A clear, factual definition of the term...",
  "tags": ["Category1", "Category2"],
  "domain": "algorithms",
  "link": "learn/related-page.html",
  "related": ["term-related-concept"]
}
```

## Domains

- `models` — Named architectures and model families
- `hardware` — Physical compute layer (GPUs, TPUs, chips)
- `datasets` — Datasets, benchmarks, evaluation suites
- `algorithms` — Math, optimization, algorithmic mechanics
- `history` — Pre-2010 AI milestones, pioneers, systems
- `safety` — Ethics, alignment, policy, regulation
- `general` — Terms that don't fit a specific domain
