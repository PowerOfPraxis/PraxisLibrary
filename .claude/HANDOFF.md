# Praxis Project Handoff Document

**Last Updated:** 2026-02-08 (Session 63 — Glossary Sharding Architecture)
**Last Commit:** `fe43f70` — docs: Session 62 handoff
**Uncommitted Changes:** Major glossary architecture overhaul (see below)
**Current Phase:** Phase 7 — World Source Archive (Glossary 15K+ Expansion)

---

## CURRENT STATE

- **Phase 1: Glossary** — COMPLETE (2,141 terms, now sharded)
- **Phase 2: Text Frameworks** — COMPLETE (52/52 pages, all 13-section template)
- **Phase 3: Modality Frameworks** — COMPLETE (37/37 pages)
- **Phase 4: Site Integration** — COMPLETE (4/4)
- **Phase 5: Navigation UX** — COMPLETE
- **Phase 6: Prompt Infographic Rollout** — IN PROGRESS (2/108 done: costar + crisp)
- **Phase 7: World Source Archive** — IN PROGRESS (infrastructure complete, term farming next)
- **Site totals:** 108 framework pages, 2,141 glossary terms (sharded), 149 HTML files, 187 site search entries

---

## ACTIVE WORK: Phase 7 — World Source Archive (Glossary Expansion)

### What Changed in Session 63

**Major glossary architecture overhaul** — Migrated from monolithic `data/glossary.json` (819KB, 2,141 terms) to **alphabetically sharded JSON** with lazy loading, compact search index, and Python build pipeline.

### New Architecture

```
data/
  glossary/
    manifest.json              # ~2KB — metadata, per-letter counts, domain counts
    search-compact.json        # ~930KB — lightweight search index for ALL terms
    a.json through z.json      # Per-letter shards with full definitions
  search-index.json            # ~100KB — site-wide search (NON-glossary entries only)
  glossary.json                # DEPRECATED — kept as backup

glossary_factory/
  README.md                    # Pipeline documentation
  migrate.py                   # One-time migration (DONE)
  build_index.py               # Rebuild manifest + search-compact from shards
  validate.py                  # Data integrity checks (9 passes)
  add_terms.py                 # Batch addition from CSV/JSON seeds
  seeds/                       # Seed files for term farming
  output/                      # Staging area
```

### JavaScript Changes (app.js)

Replaced `loadGlossaryFromJSON()` with `GlossaryManager` system:
- `initGlossarySystem()` — Main init: loads manifest, loads all shards in parallel, inits filters/search
- `loadGlossaryLetter(letter)` — Fetch and cache single shard on demand
- `loadGlossaryCompactIndex()` — Lazy-load search-compact.json on first search
- `renderGlossaryTerms(letter, terms)` — DOM API rendering (CSP compliant)
- `scrollToGlossaryTarget(target)` — Content-visibility-aware scrolling
- `letterFromTermId(termId)` — Extract letter from term ID

Filter categories expanded from 8 to 12: All, Fundamentals, Models, Training, Algorithms, Datasets, Hardware, Prompting, Safety, Products, History, Technical

Site-wide search (`searchPraxis`) now loads both `search-index.json` (187 site entries) and `search-compact.json` (glossary terms) in parallel.

### Term Domain Taxonomy (6 domains)

| Domain | Count | Description |
|--------|-------|-------------|
| models | 521 | Named architectures, model families |
| algorithms | 231 | Math, optimization, algorithmic mechanics |
| hardware | 230 | GPUs, TPUs, chips, compute infrastructure |
| safety | 207 | Ethics, alignment, policy, regulation |
| history | 153 | Pre-2010 AI milestones, pioneers, systems |
| datasets | 121 | Datasets, benchmarks, evaluation suites |
| general | 678 | Terms that don't fit a specific domain |

### Next Steps (Term Farming)

Goal: 15,000+ verified terms. Current: 2,141. Remaining: ~13,000.

Batch workflow:
1. Prepare seed CSV (term, definition, tags, domain)
2. Run: `python glossary_factory/add_terms.py seeds/your-seed.csv`
3. Run: `python glossary_factory/validate.py`
4. Run: `python glossary_factory/build_index.py`

Planned batches (500 terms each): Algorithms → Models → History → Safety → Datasets → Hardware → repeat

---

## PAUSED: Phase 6 — Prompt Mini Legend Rollout (106 pages remaining)

Prototype: `learn/crisp.html`. See `.claude/plans/infographic-rollout-plan.md` for details.
Progress: 2/108 done (costar + crisp).

---

## PREVIOUS SESSION SUMMARIES

### Session 63 (2026-02-08) — Glossary Sharding Architecture
- Pivoted from Phase 6 (prompt-mini rollout) to Phase 7 (World Source Archive)
- Created glossary_factory/ with 4 Python scripts: migrate.py, build_index.py, validate.py, add_terms.py
- Migrated 2,141 terms from monolithic glossary.json → 26 alphabetical shard files
- Created manifest.json (metadata) and search-compact.json (lightweight search index)
- Replaced loadGlossaryFromJSON() with new GlossaryManager system in app.js
- Expanded glossary filter categories from 8 → 12 (added Models, Algorithms, Datasets, Hardware, History)
- Fixed handleNoResults() emoji violation (removed emoji, switched to DOM API)
- Refactored selectResult() to use shared scrollToGlossaryTarget() helper
- Stripped 2,141 glossary entries from search-index.json (1.5MB → 100KB)
- Updated searchPraxis() to merge search-index.json + search-compact.json results
- Added CSS loading/error states for glossary sections
- Updated glossary.html filter bar (12 buttons) and term counts
- Validated all data: 0 errors, 0 warnings

### Sessions 53-62 — See `.claude/COMPLETED.md`

---

## INFO — Optional/Advisory

- CSS ~612KB / JS ~540KB — consider minification for production
- `data/glossary.json` (819KB) is DEPRECATED but kept as backup — can be deleted once sharded system is verified in production
- Ghost reference to `learn/advanced.html` in app.js (doesn't exist)
- 4 tools not in mega-menu (bias, jailbreak, specificity, temperature) — linked from tools/index.html
- Files pending user decision: `2406.06608v6.pdf` (3.1MB), `assets/images/praxishome.png` (707KB), `build_meta.py`
- Untracked files: `assets/images/Alan Turing.png`, `data/infographic-content.json` (batch extraction artifact, may be deleted)

---

## AUDIT RESULTS SUMMARY (Session 54, fully resolved Session 55)

| Phase | Result |
|-------|--------|
| 1. Orphaned Files | 9 DELETED, 3 REVIEW remain |
| 2. Structural Integrity | 145/145 pass |
| 3. Format Consistency | ALL FIXED |
| 4. Navigation & Links | ALL FIXED |
| 5. Content Continuity | All counters accurate |
| 6. Security & CSP | ALL FIXED — A+ rating |
| 7. Accessibility | ALL FIXED |
| 8. Performance | All optimized |

---

## FUTURE WORK

- **Phase 7: Term Farming** — Add 500-term batches across 6 domains toward 15K goal
- **Phase 6: Prompt Mini Rollout** — PAUSED (106 pages remaining)
- Performance optimization / CSS+JS minification (see `.claude/parkinglot.md`)
- User analytics or feedback mechanisms (see `.claude/parkinglot.md`)
- Additional framework pages for further emerging techniques

---

## KEY REFERENCE DOCUMENTS

| Document | Purpose |
|----------|---------|
| `.claude/HANDOFF.md` | Current state (this file) |
| `.claude/COMPLETED.md` | Archived completed work |
| `.claude/SiteFrameworks.md` | Architecture bible — WHY behind every decision |
| `.claude/testing-procedures.md` | Site Audit playbook (9 phases) |
| `.claude/plans/FrameworkOverhaul.md` | Master plan — Phases 1-6 + session log |
| `.claude/plans/infographic-rollout-plan.md` | Phase 6 original plan (batch approach — ABANDONED) |
| `.claude/plans/dreamy-foraging-raven.md` | Phase 7 World Source Archive plan (glossary 15K expansion) |
| `glossary_factory/README.md` | Glossary build pipeline documentation |
| `learn/costar.html` | Infographic prototype (`.prompt-infographic` component) |
| `learn/crisp.html` | **Prompt-mini prototype** (`.prompt-mini` component — CURRENT FORMAT) |
| `learn/self-ask.html` | Canonical 13-section template (depth 1) |

---

## CRITICAL RULES - MUST FOLLOW

### 1. Security & CSP Compliance (A+ Rating)
- **NO inline styles** -- Never use `style=""` attributes
- **NO inline scripts** -- Never use `onclick=""`, `onload=""`, or inline `<script>`
- **NO external resources** -- No CDNs, Google Fonts, external APIs
- **All styles -> styles.css** (single file, ~28,600 lines)
- **All scripts -> app.js** (single file with `defer`, ~10,900 lines)

### 2. Content Rules
- **NO citations on framework pages** (per user request, Session 25)
- **NO stat cards** -- Use highlight-box components instead
- **NO content badges** -- Removed from all learn pages (Session 29)
- **NO HR or remote work examples** -- Removed site-wide (Session 37)
- **NO emoji** in code or content (user preference)
- **Historical context notices required** on all framework pages

### 3. Code Notation
```
HTML:  <!-- === SECTION === --> ... <!-- /SECTION -->
CSS:   /* === SECTION === */ ... /* Component ---- */
JS:    // === SECTION === ... /** JSDoc comments */
```

### 4. URL Construction
- **ALWAYS use `resolveInternalUrl()`** for dynamically generated internal links

### 5. Design Preferences (from Session 62 iterations)
- **Light theme** — white backgrounds, not dark
- **Brand colors ONLY** — red (#DC3545), black, gray, dark-red (#A71D2A) — NO rainbow, NO blue/green
- **Compact sizing** — small fonts (0.65-0.8rem), tight padding
- **No cookie-cutter** — each page's prompt-mini should reflect that specific framework's unique components

---

## FILE STRUCTURE

```
_public_html/
+-- index.html              # Home page (108+ frameworks counter)
+-- styles.css              # ALL CSS (~28,600 lines)
+-- app.js                  # ALL JavaScript (~10,900 lines)
+-- foundations/
|   +-- index.html          # AI Foundations timeline
+-- learn/                  # Framework pages (108) + category pages (8) + hub (1)
|   +-- index.html          # Discover hub (108 framework cards, 13 categories)
|   +-- [7 category pages]  # structured-frameworks, reasoning-cot, etc.
|   +-- [71 text framework pages]
|   +-- modality/
|       +-- index.html      # Modality hub page
|       +-- code/           # Code frameworks (8 pages)
|       +-- image/          # Image frameworks (12 pages)
|       +-- audio/          # Audio frameworks (6 pages)
|       +-- video/          # Video frameworks (6 pages)
|       +-- 3d/             # 3D frameworks (5 pages)
+-- data/
|   +-- glossary.json       # DEPRECATED — monolithic backup (2,141 terms)
|   +-- search-index.json   # 187 site search entries (glossary stripped)
|   +-- glossary/
|       +-- manifest.json       # Metadata, per-letter/domain counts
|       +-- search-compact.json # Lightweight search index (all terms)
|       +-- a.json through z.json  # Per-letter term shards
+-- glossary_factory/       # Python build pipeline
|   +-- migrate.py          # One-time migration (DONE)
|   +-- build_index.py      # Rebuild manifest + search-compact
|   +-- validate.py         # Data integrity checks
|   +-- add_terms.py        # Batch term addition from seeds
+-- pages/                  # 12 content pages
+-- tools/                  # 12 AI readiness tools
+-- neurodivergence/        # 6 ND pages
+-- .claude/
    +-- HANDOFF.md           # THIS FILE
    +-- COMPLETED.md         # Archive of all completed work
    +-- SiteFrameworks.md    # Architecture bible (1,200+ lines)
    +-- testing-procedures.md # Site Audit playbook (9 phases)
    +-- parkinglot.md        # Deferred work items
    +-- plans/
        +-- FrameworkOverhaul.md          # Master plan (Phases 1-6)
        +-- infographic-rollout-plan.md   # Phase 6 original plan (ABANDONED)
        +-- discover-hub-category-pages.md # Discover Hub plan (COMPLETE)
```

---

## ARCHITECTURAL NOTES

### resolveInternalUrl() -- Universal Path Resolver (app.js ~471)
```javascript
function resolveInternalUrl(targetPath) {
    if (!targetPath || targetPath.startsWith('http') || targetPath.startsWith('/') ||
        targetPath.startsWith('#') || targetPath.startsWith('mailto:')) {
        return targetPath;
    }
    const pathname = window.location.pathname;
    const segments = pathname.replace(/^\//, '').split('/');
    const depth = Math.max(0, segments.length - 1);
    if (depth === 0) return targetPath;
    return '../'.repeat(depth) + targetPath;
}
```

### Path Depth Reference
| Depth | Directory | Root prefix | Example file |
|-------|-----------|-------------|--------------|
| 0 | Root | (none) | `index.html` |
| 1 | One-deep | `../` | `learn/self-ask.html` |
| 2 | Two-deep | `../../` | `learn/modality/index.html` |
| 3 | Three-deep | `../../../` | `learn/modality/image/image-prompting.html` |

---

*Always read this file first when resuming work. Follow the critical rules exactly. Reference learn/crisp.html as the prototype for the prompt-mini component.*
