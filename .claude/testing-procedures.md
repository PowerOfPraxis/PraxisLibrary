# Praxis Site Audit — Testing Procedures

**Living Document** | Created: Session 53 (2026-02-07)
**Trigger Prompt:** See [Audit Trigger Prompt](#audit-trigger-prompt) at bottom of document.

---

## PURPOSE

This document is the **single source of truth** for comprehensive site auditing. It is a repeatable, procedural playbook executed from a single prompt. Every audit run produces a findings report, tracks resolutions, and updates this document with new patterns discovered.

**Connected Documents:**
| Document | Role in Audit |
|----------|---------------|
| `.claude/SiteFrameworks.md` | Architecture bible — defines WHY standards exist |
| `.claude/HANDOFF.md` | Current state — tracks audit results session-to-session |
| `.claude/plans/FrameworkOverhaul.md` | Standards reference (CSP, performance, accessibility) |
| `CLAUDE.md` | Critical rules — the audit enforces these |
| `styles.css` | Single stylesheet — audit target |
| `app.js` | Single script — audit target |

---

## SITE BASELINE (Update each audit)

| Metric | Current Value | Last Verified |
|--------|---------------|---------------|
| Total HTML files | 145 | Session 55 |
| Framework pages | 104 (all 13-section) | Session 55 |
| Glossary terms | 2,141 | Session 54 |
| Mega-menu tabs | 13 | Session 54 |
| CSS file | 1 (styles.css, ~612KB) | Session 55 |
| JS file | 1 (app.js, 533KB) | Session 54 |
| JSON data files | 2 (glossary.json, search-index.json) | Session 54 |
| Image assets | 2 (praxishome.png 707KB, me2.webp 35KB) | Session 54 |
| Python batch scripts | 8 | Session 54 |
| Orphan files identified | 9 DELETED + 3 (REVIEW) | Session 55 |

---

## AUDIT EXECUTION ORDER

Run phases in this exact order. Each phase produces a findings list. Findings get resolved before moving to the next phase, or get logged for user review.

```
Phase 1: Orphaned File Scan .............. (cleanup first)
Phase 2: Structural Integrity ........... (HTML validity, notation)
Phase 3: Format Consistency .............. (component patterns, templates)
Phase 4: Navigation & Link Integrity .... (dead links, mega-menu, breadcrumbs)
Phase 5: Content Continuity .............. (fact-check, accuracy, consistency)
Phase 6: Security & CSP Compliance ...... (inline styles/scripts, externals)
Phase 7: Accessibility & UD/UDL ......... (WCAG AA, universal design)
Phase 8: Performance ..................... (render-blocking, unused code, DOM)
Phase 9: Findings Report & Resolution ... (present to user, resolve together)
```

---

## PHASE 1: ORPHANED FILE SCAN

**Goal:** Identify files that are not linked, referenced, or needed. Present list to user for approval before deletion.

### Procedure

1. **Glob all files** in the project root (exclude `.git/`, `.claude/`, `.vscode/`, `.github/`)
2. **For each file**, check if it is:
   - Linked from any HTML file (href, src, or content reference)
   - Referenced in `app.js` or `styles.css`
   - Referenced in `data/search-index.json`
   - A Python batch script (these are OK to keep — utility scripts)
   - A configuration file (`.htaccess`, `LICENSE`, `CLAUDE.md`, etc.)
3. **Known orphan patterns to check:**
   - Files ending in `-new.html` (old draft duplicates)
   - Files with `_temp` or `_mmi_temp` prefix
   - `nul` file (Windows null device artifact)
   - PDF files in root (working reference materials)
   - Files not in the mega-menu navigation AND not linked from any page
4. **Output:** Orphaned file list with recommended action (delete/keep/review)

### Known Orphans (Session 53 Baseline)

| File | Status | Action |
|------|--------|--------|
| `nul` | Windows artifact | DELETE (user approved) |
| `2406.06608v6.pdf` | Research reference PDF | KEEP (non-git-tracked OK) |
| `learn/_mmi_temp.html` | Temporary build artifact | REVIEW with user |
| `learn/mot_new.html` | Duplicate of memory-of-thought | REVIEW with user |
| `learn/analogical-reasoning-new.html` | Duplicate of analogical-reasoning | REVIEW with user |
| `learn/graph-of-thought-new.html` | Duplicate of graph-of-thought | REVIEW with user |
| `pages/animation-features.html` | Not in navigation | REVIEW with user |

### Acceptance Criteria
- [ ] All orphaned files identified
- [ ] User has reviewed and approved each action
- [ ] Deleted files removed from git tracking
- [ ] No needed files were removed

---

## PHASE 2: STRUCTURAL INTEGRITY

**Goal:** Every HTML file is valid, well-formed, and follows project notation standards.

### Procedure

1. **HTML structure check** (all 151 files):
   - `<!DOCTYPE html>` present
   - `<html lang="en">` present
   - `<meta charset="UTF-8">` present
   - `<meta name="viewport">` present
   - `<meta name="description">` present and non-empty
   - `<title>` present and contains "Praxis"
   - `<link rel="icon">` pointing to correct `favicon.svg` path
   - `<link rel="stylesheet">` pointing to correct `styles.css` path
   - `<script src="...app.js" defer>` present with correct path
   - `<a href="#main-content" class="skip-link">` present
   - `<main id="main-content">` present
   - Proper `<header>`, `<main>`, `<footer>` structure

2. **Section notation check**:
   - HTML comments follow: `<!-- === SECTION === -->` ... `<!-- /SECTION -->`
   - Every opened section comment has a closing comment

3. **Heading hierarchy check**:
   - Exactly one `<h1>` per page
   - No skipped levels (h1 -> h3 without h2)
   - Headings follow logical document outline

4. **Path depth validation**:
   | Depth | Directory | Expected prefix |
   |-------|-----------|----------------|
   | 0 | Root (`index.html`) | (none) |
   | 1 | `learn/`, `pages/`, `tools/`, etc. | `../` |
   | 2 | `learn/modality/` | `../../` |
   | 3 | `learn/modality/image/`, etc. | `../../../` |

   - Verify every `href` and `src` uses correct relative path for its depth
   - Verify `favicon.svg`, `styles.css`, and `app.js` paths match depth

### Acceptance Criteria
- [ ] All files pass DOCTYPE/meta/structure check
- [ ] All section comments properly opened and closed
- [ ] Heading hierarchy is valid (no skips)
- [ ] All asset paths correct for file depth

---

## PHASE 3: FORMAT CONSISTENCY

**Goal:** All pages using shared components follow the identical format pattern.

### Component Patterns to Validate

#### 3A. Comparison Panel (Standard: "See the Difference")
```
Expected pattern across ALL framework pages:
  <h2 class="section-title">See the Difference</h2>
  Before side: <h3 class="comparison-panel__title">[Framework-specific before]</h3>
  After side: <h3 class="comparison-panel__title">[Framework-specific after]</h3>
```
**Check:** Grep all HTML files for `comparison-panel`. Verify the section h2 is "See the Difference" — NOT a custom title.

**Known violations (Session 53):**
- `learn/self-verification.html` — h2 says "Unverified vs. Self-Verified Output" (should be "See the Difference")
- `learn/self-refine.html` — h2 says "First Draft vs. Self-Refined Output" (should be "See the Difference")

#### 3B. 13-Section Template (Framework Pages)
All framework pages must contain these 13 sections in order:
1. Hero (with breadcrumb, hero-badge, h1, subtitle)
2. Historical Context (highlight-box--warning)
3. The Concept (split-section)
4. Why It Works (pillar-grid--3)
5. How It Works (element-timeline)
6. Comparison Panel ("See the Difference")
7. Examples (accordion)
8. Implementation Patterns / Feedback Strategies
9. When to Use / Limitations (split-section with check/cross lists)
10. Use Cases (use-case-showcase)
11. Framework Positioning (evolution-timeline)
12. Related Frameworks (evolution-callout links)
13. CTA Section (cta-corporate--dark)

**Check:** For each framework page, verify all 13 sections exist. Flag missing sections.

#### 3C. Hero Badge Category
Every framework page hero-badge must match its mega-menu category.
```
<div class="hero-badge">
    <span class="hero-badge__text">[CATEGORY NAME]</span>
</div>
```

#### 3D. Breadcrumb Pattern
```
Home / Discover / [Page Name]       (depth 1)
Home / Discover / [Hub] / [Page]    (depth 2-3, modality pages)
```

#### 3E. Historical Context Notice
Every framework page must have the historical context warning box with:
- `Framework Context: [YEAR]` title
- `Background:` paragraph
- `Modern LLM Status:` paragraph

#### 3F. CTA Section
All framework pages must end with the dark CTA with neural canvas background.

### Acceptance Criteria
- [ ] All comparison panels use "See the Difference" h2
- [ ] All framework pages have 13 sections
- [ ] Hero badges match categories
- [ ] Breadcrumbs are correct for depth
- [ ] Historical context present on all framework pages
- [ ] CTA sections present and consistent

---

## PHASE 4: NAVIGATION & LINK INTEGRITY

**Goal:** Every link on the site resolves. Navigation is consistent across all files.

### Procedure

#### 4A. Mega-Menu Consistency
1. Extract the mega-menu HTML from a reference file (e.g., `learn/self-ask.html` for depth 1)
2. For each of the 4 depth levels (0, 1, 2, 3):
   - Verify all files at that depth have identical mega-menu structure
   - Verify all 13 tab sections present with correct `data-tab` slugs
   - Verify all framework links are present in correct categories
   - Verify path prefixes match depth level

**13 Required Tab Slugs:**
`getting-started`, `structured-frameworks`, `in-context-learning`, `reasoning-cot`, `decomposition`, `self-correction`, `ensemble-methods`, `prompting-strategies`, `code`, `image`, `audio`, `video`, `3d`

#### 4B. Internal Link Scan
For every `<a href="...">` in every HTML file:
1. Resolve the relative path to an absolute file path
2. Verify the target file exists on disk
3. If the link includes an anchor (`#section-id`), verify the target ID exists in the target file
4. Flag dead links with file + line number

#### 4C. Footer Consistency
Verify all files have identical footer structure with correct relative paths for their depth.

#### 4D. Search Index Completeness
1. Read `data/search-index.json`
2. Verify every framework page has a search index entry
3. Verify every search index URL resolves to an existing file
4. Flag orphaned search entries (pointing to deleted pages) or missing entries

#### 4E. Glossary Cross-Reference
1. Verify `data/glossary.json` is valid JSON
2. Check for duplicate term entries
3. Spot-check 10 random terms for accuracy

### Acceptance Criteria
- [ ] Mega-menu identical across all files at each depth level
- [ ] Zero dead internal links
- [ ] Footer consistent across all files
- [ ] Search index complete and accurate
- [ ] Glossary JSON valid with no duplicates

---

## PHASE 5: CONTENT CONTINUITY

**Goal:** All content is factually accurate, consistent, and free of errors.

### Procedure

#### 5A. Content Accuracy Spot-Check
For each framework page, verify:
1. Framework name matches title, h1, breadcrumb, and meta description
2. Category assignment is correct (matches the research paper taxonomy)
3. Historical dates are plausible (paper publication years)
4. "Modern LLM Status" sections are current (mention 2025-2026)
5. No HR or remote work examples (banned per site rules)
6. No emoji in content (banned per site rules)
7. No citations on framework pages (banned per site rules, Session 25)
8. No stat cards (banned — use highlight-box instead)
9. No content badges (removed Session 29)

#### 5B. Cross-Page Consistency
1. When framework A references framework B, verify the description matches B's actual content
2. Related framework links point to correct pages
3. Category pages list the correct frameworks for their category
4. Discover hub (`learn/index.html`) cards match actual framework pages

#### 5C. Counter Verification
1. `index.html` homepage counter says "101+ frameworks" — verify actual count
2. HANDOFF.md framework count matches actual file count
3. Glossary term count matches actual `glossary.json` entry count

### Acceptance Criteria
- [ ] All framework names consistent across title/h1/breadcrumb/meta
- [ ] No banned content patterns (HR examples, emoji, citations, stat cards)
- [ ] Cross-references between pages are accurate
- [ ] All counters match actual counts

---

## PHASE 6: SECURITY & CSP COMPLIANCE

**Goal:** A+ Content Security Policy rating. Zero violations.

### CSP Policy Reference
```
default-src 'none';
connect-src 'self';
form-action 'none';
base-uri 'none';
font-src 'self';
img-src 'self' data:;
style-src 'self';
script-src 'self';
```

### Procedure

#### 6A. Inline Style Scan
```
Grep ALL HTML files for: style="
Expected: ZERO matches in framework/content pages
```
**Known violations (Session 53):** `pages/security.html`, `pages/performance.html`, `pages/animation-features.html`

#### 6B. Inline Script/Event Handler Scan
```
Grep ALL HTML files for: onclick=|onload=|onerror=|onmouseover=|onsubmit=|onfocus=|onblur=
Grep ALL HTML files for: <script> (that is NOT <script src=)
Expected: ZERO matches
```

#### 6C. External Resource Scan
```
Grep ALL HTML files for: googleapis|cdnjs|cdn\.|cloudflare|jsdelivr|unpkg|fonts\.google
Grep ALL HTML files for: http://|https:// (in href/src attributes, excluding anchor links)
Expected: ZERO external resource URLs
```

#### 6D. JavaScript Security Scan
```
Grep app.js for: eval\(|new Function\(|setTimeout\("|setInterval\("
Expected: ZERO matches
```

#### 6E. .htaccess Verification
Read `.htaccess` and verify:
- CSP headers are set correctly
- Security headers present (X-Frame-Options, X-Content-Type-Options, etc.)
- HTTPS redirect configured

### Acceptance Criteria
- [ ] Zero inline styles in content pages
- [ ] Zero inline event handlers
- [ ] Zero external resource URLs
- [ ] Zero dangerous JS patterns
- [ ] .htaccess security headers correct

---

## PHASE 7: ACCESSIBILITY & UD/UDL

**Goal:** WCAG AA compliance. Universal Design for Learning principles met.

### Procedure

#### 7A. WCAG AA Checklist
For ALL HTML files, verify:
1. **Skip link** — `<a href="#main-content" class="skip-link">` present
2. **Language** — `<html lang="en">` present
3. **Alt text** — All `<img>` tags have meaningful `alt` attributes
4. **Heading hierarchy** — h1 > h2 > h3, no skips (covered in Phase 2)
5. **Focus indicators** — All interactive elements have visible `:focus` styles (check CSS)
6. **Color contrast** — Text meets 4.5:1 ratio against backgrounds (check CSS variables)
7. **Keyboard navigation** — All interactive elements reachable via Tab
8. **ARIA attributes** — Proper use of `role`, `aria-label`, `aria-expanded`, `aria-controls`
9. **Form labels** — All form inputs have associated labels
10. **Link purpose** — Link text is descriptive (no "click here")

#### 7B. Accessibility Dashboard Check
Verify the ADL (Accessibility Dashboard Layer) is present on ALL pages:
- `adl-toggle` button present
- `adl-panel` with text size, contrast, read aloud, dimming controls
- `adl-dim-overlay` present
- All ADL controls have proper ARIA attributes

#### 7C. Universal Design for Learning (UDL)
1. **Multiple means of representation** — Content available in text, visual (diagrams/timelines), and interactive (accordions, tools) formats
2. **Multiple means of engagement** — Varied examples (technical, creative, business), progressive disclosure (accordions)
3. **Multiple means of action/expression** — Interactive tools, quiz, glossary search, framework matcher
4. **Neurodivergent support** — ND hub pages present and linked, text size controls, read aloud, screen dimming

#### 7D. Anchor Link Offset Check
```css
/* Standard pages: */
:target { scroll-margin-top: 100px; }
/* Glossary pages: */
[id^="letter-"], [id^="term-"] { scroll-margin-top: 160px; }
```
Verify CSS contains proper scroll-margin-top values so anchor-linked content is not hidden behind sticky headers.

### Acceptance Criteria
- [ ] Skip links on all pages
- [ ] All images have alt text
- [ ] Heading hierarchy valid
- [ ] Focus styles visible
- [ ] Color contrast meets 4.5:1
- [ ] ADL dashboard on all pages
- [ ] UDL principles met across site
- [ ] Anchor offsets correct

---

## PHASE 8: PERFORMANCE

**Goal:** 100% Lighthouse scores (Performance, Accessibility, Best Practices, SEO).

### Procedure

#### 8A. Render-Blocking Check
1. Verify `app.js` has `defer` attribute on ALL pages
2. Verify no additional `<script>` tags without `defer` or `async`
3. Verify CSS is loaded via `<link rel="stylesheet">` (not `@import`)

#### 8B. Unused Code Scan
1. Check for CSS classes defined in `styles.css` but never used in any HTML file
2. Check for JS functions defined in `app.js` but never called
3. Flag large unused sections for potential cleanup

#### 8C. DOM Depth Check
Spot-check 5 representative pages for excessive DOM nesting (target: max 15 levels deep).

#### 8D. Image Optimization
1. Verify all images are in optimized formats (WebP, SVG preferred)
2. Check image file sizes — flag anything over 500KB
3. Verify images have explicit width/height or aspect-ratio to prevent layout shift

#### 8E. Meta/SEO Check
Every page must have:
- `<meta name="description" content="...">` (non-empty, unique per page)
- `<title>` tag (unique per page)
- Proper heading hierarchy (h1 only once)

### Acceptance Criteria
- [ ] All scripts deferred
- [ ] No significant unused CSS/JS
- [ ] DOM depth reasonable
- [ ] Images optimized
- [ ] Meta descriptions present and unique

---

## PHASE 9: FINDINGS REPORT & RESOLUTION

**Goal:** Present all findings to user. Resolve together.

### Report Format

```markdown
# Praxis Site Audit — Session [N] Findings

**Date:** [DATE]
**Auditor:** Claude Code (Session [N])
**Phases Completed:** 1-8

## Summary
- Total issues found: [N]
- Critical (must fix): [N]
- Warning (should fix): [N]
- Info (optional): [N]

## Critical Issues
[List with file:line, description, recommended fix]

## Warnings
[List with file:line, description, recommended fix]

## Info
[List with file:line, description]

## Orphaned Files for Review
[Table with file, status, recommended action]

## Resolutions Applied This Session
[List of fixes made with before/after]

## Deferred Items
[Items requiring user decision or future work]
```

### Post-Audit Checklist
- [ ] All critical issues resolved
- [ ] Orphaned file list reviewed with user
- [ ] HANDOFF.md updated with audit results
- [ ] This document updated with any new patterns discovered
- [ ] Session number incremented

---

## AUDIT HISTORY LOG

| Session | Date | Issues Found | Resolved | Deferred | Notes |
|---------|------|-------------|----------|----------|-------|
| 53 | 2026-02-07 | -- | -- | -- | Document created, first audit pending |
| 54 | 2026-02-07 | 20+ | 8 | 12+ | First full audit. Fixed: 4 dead links, 2 comparison h2s, 296 aria-labels. Deferred: 4 h2 fixes, 2 inline styles, 58 search entries, 8 orphan deletions, heading hierarchy, focus-visible, ADL gaps |
| 55 | 2026-02-07 | 0 new | 12 | 8 | All critical items resolved. Fixed: 3 remaining h2s (+1 already OK), 2 inline styles, 58 search entries added, 8 orphan files deleted. Remaining: warnings only (heading hierarchy, focus-visible, ADL gaps, incomplete Code pages) |

---

## KNOWN PATTERN REGISTRY

Patterns discovered during audits that should be checked in future runs.

### Format Patterns
| Pattern | Standard | Violation Example |
|---------|----------|-------------------|
| Comparison panel h2 | "See the Difference" | Custom titles like "Unverified vs. Self-Verified Output" |
| Framework page sections | 13-section template | Missing sections |
| Hero badge text | Must match category name | Wrong category |

### Security Patterns
| Pattern | Rule | Violation Example |
|---------|------|-------------------|
| Inline styles | NEVER in content pages | `style=""` attributes |
| Inline scripts | NEVER anywhere | `onclick=""` handlers |
| External resources | NEVER anywhere | CDN links, Google Fonts |

### Content Patterns
| Pattern | Rule | Violation Example |
|---------|------|-------------------|
| No emoji | Site-wide | Emoji in page content |
| No citations | Framework pages only | Citation blocks |
| No stat cards | Site-wide | Use highlight-box instead |
| No HR/remote work examples | Site-wide | Removed in Session 37 |
| Historical context | Required on all framework pages | Missing context box |

---

## AUDIT TRIGGER PROMPT

Copy and paste this prompt to start a full audit:

---

```
Run the Praxis Site Audit. Read .claude/testing-procedures.md and execute all 9 phases in order.

For each phase:
1. Run the checks described in the procedure
2. Log all findings (critical/warning/info)
3. Fix critical issues immediately where safe to do so
4. Collect items needing my review

At the end, present the Phase 9 findings report and the orphaned files list for my review.

Update testing-procedures.md audit history log and HANDOFF.md when complete.
```

---

*This is a living document. Update the Known Pattern Registry, Site Baseline table, and Audit History Log after every audit run.*
