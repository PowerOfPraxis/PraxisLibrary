# Praxis Project Handoff Document

**Last Updated:** 2026-02-07 (Session 46)
**Last Commit:** `4bc69f5` (Session 45 push) — Session 46 changes UNCOMMITTED
**Current Phase:** Phase 3 Modality Frameworks — Sub-phase 3A Image Prompting COMPLETE (12/12)

---

## SESSION 46 SUMMARY

**Focus:** Phase 3 Modality Frameworks — Sub-phase 3A Image Prompting (12 pages) + Modality Hub

### Completed

1. **Session 45 Committed & Pushed** (`4bc69f5`):
   - All Phase 2 work (52/52 text frameworks) committed and pushed to remote

2. **12 Image Prompting Pages Created** (parallel background agents, 867-892 lines each):
   - `learn/modality/image/image-prompting.html` (883 lines) — Image Prompting Basics, 2023
   - `learn/modality/image/multimodal-cot.html` (878 lines) — Multimodal CoT, 2023 by Zhang et al.
   - `learn/modality/image/visual-cot.html` (884 lines) — Visual Chain of Thought, 2023
   - `learn/modality/image/image-as-text.html` (875 lines) — Image-as-Text Prompting, 2023
   - `learn/modality/image/vqa.html` (867 lines) — Visual Question Answering, 2015/2023
   - `learn/modality/image/image-gen-prompting.html` (879 lines) — Image Generation Prompting, 2022
   - `learn/modality/image/negative-prompting.html` (892 lines) — Negative Prompting, 2022
   - `learn/modality/image/controlnet-prompting.html` (892 lines) — ControlNet Prompting, 2023
   - `learn/modality/image/inpainting-prompting.html` (881 lines) — Inpainting Prompting, 2022
   - `learn/modality/image/style-transfer.html` (878 lines) — Style Transfer Prompting, 2015/2022
   - `learn/modality/image/image-to-image.html` (880 lines) — Image-to-Image Prompting, 2022
   - `learn/modality/image/composition-prompting.html` (881 lines) — Composition Prompting, 2023
   - All 13 sections, zero inline styles/scripts, historical context notices on all pages

3. **Modality Hub Page Created** (`learn/modality/index.html`):
   - Image Prompting section (12 cards), Code section (3 cards), Coming Soon (Audio, Video, 3D)
   - Full nav, footer, back-to-top, CTA

4. **Mega-Menu Navigation Updated** (127 HTML files via `update_nav_s46.py`):
   - New "Image" section with 12 links added after "Code" section
   - All 4 depth levels verified (root, one-deep, two-deep, three-deep)

5. **Search Index Updated** — 13 new entries added to `data/search-index.json` (12 image + 1 hub)

6. **Discover Hub Updated** (`learn/index.html`):
   - 12 new Image Prompting framework cards added in new section
   - Filter bar: +Image (12) button
   - Meta description: 62+ -> 79+

7. **Homepage Updated** (`index.html`):
   - Counter: 67+ -> 79+ frameworks
   - CTA text: "View All 79+ Frameworks"
   - Subtitle: "79+ proven prompting methodologies"

### Quality Checks Passed
- 0 inline styles across all 12 image pages
- 0 inline scripts across all 12 image pages
- 0 external resources
- Historical context notices on all 12 pages
- 867-892 lines per page (within target range)

---

## PHASE 3 MODALITY FRAMEWORKS: Progress

### Sub-phase 3A: Image Prompting — COMPLETE (12/12)

All 12 image prompting pages built and integrated.

### Sub-phase 3B: Audio/Speech — NOT STARTED (0/6)

| Framework | File | Priority |
|-----------|------|----------|
| Audio Prompting Basics | audio-prompting.html | MEDIUM |
| Speech-to-Text Prompting | stt-prompting.html | MEDIUM |
| Text-to-Speech Prompting | tts-prompting.html | MEDIUM |
| Audio Classification | audio-classification.html | LOW |
| Music Generation Prompting | music-gen.html | LOW |
| Voice Cloning Prompting | voice-cloning.html | LOW |

### Sub-phase 3C: Video — NOT STARTED (0/6)

| Framework | File | Priority |
|-----------|------|----------|
| Video Prompting Basics | video-prompting.html | MEDIUM |
| Video Generation Prompting | video-gen.html | MEDIUM |
| Temporal Reasoning | temporal-reasoning.html | LOW |
| Video QA | video-qa.html | LOW |
| Video Captioning | video-captioning.html | LOW |
| Video Editing Prompting | video-editing.html | LOW |

### Sub-phase 3D: Code/Structured — NOT STARTED (0/5 new, 3 exist)

| Framework | File | Priority |
|-----------|------|----------|
| Program Synthesis | program-synthesis.html | MEDIUM |
| Code Explanation | code-explanation.html | MEDIUM |
| Code Review Prompting | code-review.html | MEDIUM |
| Test Generation | test-generation.html | MEDIUM |
| SQL Generation | sql-generation.html | MEDIUM |

### Sub-phase 3E: 3D/Spatial — NOT STARTED (0/5)

| Framework | File | Priority |
|-----------|------|----------|
| 3D Prompting Basics | 3d-prompting.html | LOW |
| 3D Model Generation | 3d-model-gen.html | LOW |
| Scene Understanding | scene-understanding.html | LOW |
| Pose Estimation Prompting | pose-estimation.html | LOW |
| Point Cloud Prompting | point-cloud.html | LOW |

---

## NEXT TASKS

### Priority 1: Continue Phase 3 — Sub-phase 3B Audio/Speech (6 pages)

**Approach:**
- Same 13-section template, parallel background agents
- Directory: `learn/modality/audio/`
- After pages: update mega-menu, search index, discover hub, modality hub, homepage counter

### Priority 2: Phase 3 remaining sub-phases (3C-3E)

### Priority 3: Phase 4D Framework Matcher updates

---

## MEGA-MENU CSS ARCHITECTURE (Session 44)

Key CSS rules for the desktop mega-menu positioning:

```css
/* Container is centered on screen */
.header-container {
    max-width: 1400px;
    margin: 0 auto;
    position: relative;  /* positioning context for menus */
}

/* Wide menus (Discover) skip nav-item positioning */
.nav-item.has-dropdown:has(.mega-menu--multi-column) {
    position: static;
}

/* Discover menu: centered within header-container (= viewport center) */
.mega-menu--multi-column {
    left: 0; right: 0;
    margin-left: auto; margin-right: auto;
    width: max-content;
    max-width: calc(100vw - 2rem);
}

/* Resources menu: centered under its nav link */
.nav-item.has-dropdown:last-child:has(.mega-menu--multi-column) {
    position: relative;
}
.nav-item.has-dropdown:last-child .mega-menu--multi-column {
    left: 50%; right: auto;
    margin-left: 0; margin-right: 0;
    transform: translateX(-50%) translateY(10px);
}
```

---

## KEY REFERENCE DOCUMENTS

| Document | Purpose | Lines |
|----------|---------|-------|
| `.claude/SiteFrameworks.md` | **Architecture bible** — WHY behind every decision | 1,041 |
| `.claude/HANDOFF.md` | Current state (this file) | -- |
| `.claude/COMPLETED.md` | Archived completed work | -- |
| `.claude/plans/FrameworkOverhaul.md` | Master plan -- Phases 1-5 + session log | 1,769 |
| `learn/self-ask.html` | Canonical 13-section template | 899 |

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
**Usage:** `resolveInternalUrl('pages/glossary.html#term-foo')` -- always pass root-relative paths.

### Python Batch Script Pattern
Sessions 38/45/46 used Python scripts to batch-update navigation across all HTML files. Pattern: regex match Code section, insert Image section after it. Same approach for future modality additions.

---

## CRITICAL RULES - MUST FOLLOW

### 1. Security & CSP Compliance (A+ Rating)
- **NO inline styles** -- Never use `style=""` attributes
- **NO inline scripts** -- Never use `onclick=""`, `onload=""`, or inline `<script>`
- **NO external resources** -- No CDNs, Google Fonts, external APIs
- **All styles -> styles.css** (single file, ~27,600 lines)
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
- **ALWAYS use `resolveInternalUrl()`** for any dynamically generated internal links
- Pass root-relative paths: `resolveInternalUrl('pages/glossary.html#term-foo')`

### 5. Information Accuracy
- All historical/factual claims must be verified from .edu or .gov sources
- No fake, made up, or misleading information

---

## FILE STRUCTURE

```
_public_html/
+-- index.html              # Home page (79+ frameworks counter)
+-- styles.css              # ALL CSS (~27,600 lines)
+-- app.js                  # ALL JavaScript (~10,900 lines)
+-- foundations/
|   +-- index.html          # AI Foundations timeline
+-- learn/                  # Framework pages (79+) + category pages (7)
|   +-- index.html          # Discover hub (79 framework cards, 9 categories)
|   +-- [7 category pages]  # structured-frameworks, reasoning-cot, etc.
|   +-- [67 text framework pages]
|   +-- modality/
|       +-- index.html      # Modality hub page
|       +-- code/           # Code frameworks (3 pages)
|       +-- image/          # Image frameworks (12 pages) -- NEW Session 46
+-- data/
|   +-- glossary.json       # 2,141 AI terms
|   +-- search-index.json   # Search entries (79 frameworks + glossary + pages)
+-- pages/                  # 12 content pages
+-- tools/                  # 12 AI readiness tools
+-- neurodivergence/        # 6 ND pages
+-- patterns/               # 1 page
+-- quiz/                   # 1 page
+-- .claude/
    +-- HANDOFF.md           # THIS FILE
    +-- COMPLETED.md         # Archive of completed work
    +-- SiteFrameworks.md    # Architecture bible (1,041 lines)
    +-- plans/
        +-- FrameworkOverhaul.md          # Master plan (Phases 1-5)
        +-- discover-hub-category-pages.md # Discover Hub plan (COMPLETE)
```

---

## 10 FRAMEWORK CATEGORIES (79 frameworks)

| Category | Count | Category Page | Status |
|----------|-------|---------------|--------|
| Getting Started | 2 | -- | No category page needed |
| Structured Frameworks | 5 | `learn/structured-frameworks.html` | DONE |
| Reasoning & CoT | 15 | `learn/reasoning-cot.html` | DONE |
| Decomposition | 7 | `learn/decomposition.html` | DONE |
| Self-Correction | 7 | `learn/self-correction.html` | DONE |
| In-Context Learning | 13 | `learn/in-context-learning.html` | DONE |
| Ensemble Methods | 7 | `learn/ensemble-methods.html` | DONE |
| Prompting Strategies | 11 | `learn/prompting-strategies.html` | DONE |
| Code | 3 | -- | Uses `learn/modality/code/` hub |
| Image | 12 | -- | Uses `learn/modality/image/` via modality hub |

---

*Always read this file first when resuming work. Follow the critical rules exactly. Read SiteFrameworks.md for deep architectural understanding.*
