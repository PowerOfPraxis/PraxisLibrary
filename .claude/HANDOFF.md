# Praxis Project Handoff Document

**Last Updated:** 2026-02-08 (Session 62 — handoff prep)
**Last Commit:** `d395896` — Add prompt-mini legend component to CRISP concept section
**Uncommitted Changes:** None
**Current Phase:** Phase 6 — Prompt Infographic Rollout (106 pages remaining)

---

## CURRENT STATE

- **Phase 1: Glossary** — COMPLETE (2,141 terms)
- **Phase 2: Text Frameworks** — COMPLETE (52/52 pages, all 13-section template)
- **Phase 3: Modality Frameworks** — COMPLETE (37/37 pages)
- **Phase 4: Site Integration** — COMPLETE (4/4)
- **Phase 5: Navigation UX** — COMPLETE
- **Phase 6: Prompt Infographic Rollout** — IN PROGRESS (2/108 done: costar + crisp)
- **Site totals:** 108 framework pages (all 13-section), 2,141+ glossary terms, 149 HTML files, 2,328 search entries

---

## ACTIVE WORK: Phase 6 — Concept Section Redesign + Prompt Mini Legend

### What Changed in Session 62

**The original batch automation plan was ABANDONED.** User tested it (all 107 pages injected via Python scripts), but rejected the output as "cookie cutter" — 85/108 had identical 4-step structures with generic process descriptions instead of real prompt examples. All 107 injected pages were reverted via `git checkout`. The batch scripts were deleted.

**New approach: Hand-crafted, page-by-page redesign** with two components:

1. **Concept section layout redesign** — Restructured from original split-section to a new layout
2. **Prompt-mini legend** — A new compact CSS component inside the blue highlight-box

### Approved Prototype: learn/crisp.html

The CRISP page is the approved prototype for the new concept section format:

**Layout (top to bottom):**
```
┌─────────────────────────────────────────────────┐
│  Section Title (full width)                      │
│  Section Subtitle (full width)                   │
├────────────────────┬────────────────────────────┤
│  Paragraphs        │  Blue Highlight Box        │
│  (split-section    │  (split-section__media)    │
│   __content)       │                            │
│                    │  ┌── Title ──────────────┐ │
│  3 paragraphs of   │  │ Why Five Elements...  │ │
│  explanatory text   │  │                      │ │
│                    │  │ [paragraph text]      │ │
│                    │  │                      │ │
│                    │  │ ── prompt-mini ─────  │ │
│                    │  │ ● C  Context          │ │
│                    │  │    Background & sit.  │ │
│                    │  │ ● R  Role             │ │
│                    │  │    Who the AI...      │ │
│                    │  │ ● I  Instructions     │ │
│                    │  │    What you need...   │ │
│                    │  │ ● S  Scope            │ │
│                    │  │    Boundaries...      │ │
│                    │  │ ● P  Parameters       │ │
│                    │  │    Output format...   │ │
│                    │  └──────────────────────┘ │
├────────────────────┴────────────────────────────┤
```

**Key CSS classes:**
- `split-section--stretch` — Equal-height columns (not `--center` or `--align-start`)
- `split-section__media` — Right column (has existing `align-self: stretch` support)
- `.prompt-mini` — New component: vertical flex, fills remaining highlight-box space
- `.prompt-mini__item` — Card rows: badge + text group, white bg, color-matched left border
- `.prompt-mini__badge` — 32px circle, white letter, brand color bg, shadow
- `.prompt-mini__text` — Flex column wrapper for label + description
- `.prompt-mini__label` — 0.8rem bold label
- `.prompt-mini__desc` — 0.7rem muted description

**Key CSS additions (styles.css):**
- `.split-section--stretch .highlight-box` — `height: 100%; margin: 0;` (fill column)
- `.split-section--stretch .highlight-box__content` — `display: flex; flex-direction: column; height: 100%;`
- `.prompt-mini` — `flex: 1; flex-direction: column; justify-content: center;`
- `.prompt-mini__item` — Card with `background: rgba(255,255,255,0.7); border-left: 3px solid; border-radius;`
- Color cycling: `nth-child(5n+1)` through `5n+5` for 5-letter acronyms (uses 4 brand colors + repeat)

### What Each Page Needs (Rollout Pattern)

For each of the remaining 106 pages:

1. **Read the page** — Understand the framework (acronym? steps? how many components?)
2. **Restructure concept section** — Title/subtitle full-width above, `split-section--stretch`
3. **Move highlight-box** to `split-section__media` (right column) if not already there
4. **Craft prompt-mini HTML** — Letter badges for acronyms (CRISPE), number/icon badges for step-based frameworks
5. **Write definitions** — Short, plain-English description for each component/step
6. **Ensure equal-height columns** — Content fills naturally

### Two Types of Prompt-Mini

**Acronym frameworks (2 remaining):** CRISPE (6 letters), already have letter→label mappings
**Step-based frameworks (104 remaining):** Need creative adaptation — each step gets a badge, label, and short definition summarizing what that step contributes to the prompt

### Progress Tracker

| Category | Total | Done | Remaining |
|----------|-------|------|-----------|
| Structured Frameworks | 5 | 2 (costar, crisp) | 3 (crispe, constrained-output, context-structure) |
| Getting Started | 2 | 0 | 2 |
| Reasoning & CoT | 15 | 0 | 15 |
| Decomposition | 8 | 0 | 8 |
| Self-Correction | 7 | 0 | 7 |
| In-Context Learning | 13 | 0 | 13 |
| Ensemble Methods | 7 | 0 | 7 |
| Prompting Strategies | 14 | 0 | 14 |
| Code | 8 | 0 | 8 |
| Image | 12 | 0 | 12 |
| Audio | 6 | 0 | 6 |
| Video | 6 | 0 | 6 |
| 3D | 5 | 0 | 5 |
| **TOTAL** | **108** | **2** | **106** |

### Next Up
Start with remaining **Structured Frameworks** (3 pages), then Getting Started (2), then proceed category by category.

### Original Infographic Component (Still in CSS)
The `.prompt-infographic` BEM component (~line 25397 in styles.css, ~155 lines) from the CO-STAR prototype still exists and is used on `learn/costar.html`. This is a DIFFERENT component from `.prompt-mini` — it's the larger row-based infographic with header badge row, labeled fields, and footer. It may be adapted or replaced later as the rollout evolves.

---

## PREVIOUS SESSION SUMMARIES

### Session 62 (2026-02-08) — Concept Section Redesign + Prompt Mini
- Committed Session 61 uncommitted changes (styles.css, costar.html, about.html): `b993c8c`
- CSS generalization: cycling 4n color pattern for infographic component: `01c41e9`
- Attempted batch automation (Python scripts → inject all 107 pages) — user REJECTED as cookie-cutter
- Reverted all 107 injected pages, deleted batch scripts
- Pivoted to hand-crafted page-by-page approach
- Redesigned CRISP concept section: title/subtitle full-width, split-section--stretch, equal-height columns
- Created `.prompt-mini` CSS component: circular badges, card rows, color-matched borders, stacked label+desc
- Multiple layout iterations based on user feedback (stacked → side-by-side → stretch → mini legend in highlight-box)
- Committed: `d395896`

### Session 61 (2026-02-08) — Infographic Prototype + Plan
- Created `.prompt-infographic` CSS component
- Built CO-STAR prototype on learn/costar.html (6 rows, letter badges)
- Iterated design: dark→light, rainbow→neutral, large→compact, order swap
- Created infographic rollout plan for all 108 pages

### Session 60 (2026-02-08) — Split-Color Branding + Mobile Buttons
- Split-color branding across all mega-menu text (desktop + mobile)
- Glassy mobile quick link buttons (2x2 grid)
- Commit: `cb805e7`

### Sessions 53-59 — See `.claude/COMPLETED.md`

---

## INFO — Optional/Advisory

- CSS ~612KB / JS 533KB — consider minification for production
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

- **Phase 6: Prompt Mini Rollout** — ACTIVE (see above, 106 pages remaining)
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
|   +-- glossary.json       # 2,141 AI terms
|   +-- search-index.json   # 2,328 search entries
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
