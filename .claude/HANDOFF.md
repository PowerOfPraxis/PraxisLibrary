# Praxis Project Handoff Document

**Last Updated:** 2026-02-05 (Session 24)
**Last Commit:** b51e757 - feat: Phase 2 start - zero-shot and zero-shot-cot framework pages
**Current Phase:** Framework Overhaul - Phase 2 IN PROGRESS

---

## CURRENT SESSION STATUS (Session 24)

### Completed This Session
- [x] Created `learn/zero-shot.html` - Foundation technique page
- [x] Created `learn/zero-shot-cot.html` - Reasoning technique with interactive elements
- [x] Added CSS for new comparison-tabs component (styles.css)
- [x] Added JS for comparison-tabs interactivity (app.js)

### Files Modified (Uncommitted)
| File | Changes |
|------|---------|
| `learn/zero-shot.html` | NEW - Foundation technique page (CSP compliant, verifiable sources) |
| `learn/zero-shot-cot.html` | NEW - Reasoning technique with interactive before/after tabs |
| `styles.css` | Added comparison-tabs, comparison-grid, comparison-card variants |
| `app.js` | Added comparison-tabs JS handler (lines ~6869-6894) |
| `.claude/plans/FrameworkOverhaul.md` | Updated Session 24 log, Phase 2 progress |

### Immediate Next Steps (Resume Here)
1. **Create remaining HIGH priority pages (10 more):**
   - [ ] one-shot.html
   - [ ] example-selection.html
   - [ ] least-to-most.html
   - [ ] plan-and-solve.html
   - [ ] tree-of-thought.html
   - [ ] self-refine.html
   - [ ] self-verification.html
   - [ ] code-prompting.html (goes in learn/modality/code/)
   - [ ] self-debugging.html (goes in learn/modality/code/)
   - [ ] structured-output.html (goes in learn/modality/code/)

2. **After ALL pages created:** Update navigation & footer links in all 48+ HTML files

---

## ACTIVE PROJECT: Framework Overhaul

**Master Plan:** `.claude/plans/FrameworkOverhaul.md`

**Overall Scope:**
- ✅ 33 glossary terms (Phase 1 COMPLETE)
- 🔄 52 text framework pages (Phase 2 IN PROGRESS - 2/52)
- ⬜ 37 modality framework pages (Phase 3)
- ⬜ Site integration - nav/footer updates (Phase 4)
- ✅ Navigation UX overhaul (Phase 5 COMPLETE)

### Phase 2 Progress: Text Frameworks (2/52)
```
Progress: [█░░░░░░░░░░░░░░░░░░░] 4%
```

**Completed Pages:**
1. ✅ zero-shot.html
2. ✅ zero-shot-cot.html

**Remaining HIGH Priority (10 pages):**
3. one-shot.html
4. example-selection.html
5. least-to-most.html
6. plan-and-solve.html
7. tree-of-thought.html
8. self-refine.html
9. self-verification.html
10. code-prompting.html
11. self-debugging.html
12. structured-output.html

---

## PAGE REQUIREMENTS (For New Framework Pages)

### Content Requirements
- **Mix of engagement, information, and interactivity**
- **No duplicate content** from other pages unless relevant
- **Original content** - not copy-paste designs
- **Verifiable academic sources** (.edu, .gov, peer-reviewed) with working URLs

### Interactive Components Available
| Component | CSS Class | Use For |
|-----------|-----------|---------|
| Tabbed comparisons | `.comparison-tabs` | Before/after demos |
| Accordions | `.accordion` | Expandable examples |
| Feature lists | `.feature-list` | Benefits with checkmarks |
| Stat cards | `.stat-card` | Key statistics |
| Highlight boxes | `.highlight-box` | Important callouts |
| Pillar cards | `.pillar-card--interactive` | Hover effects |

### Page Structure Template
1. Hero section with breadcrumb & badge
2. Content badges row
3. Main content sections (unique per framework)
4. Related frameworks section
5. Sources section with citation links
6. CTA section

---

## CRITICAL RULES - MUST FOLLOW

### 1. Security & CSP Compliance (A+ Rating)

**NEVER violate these rules:**
- **NO inline styles** - Never use `style=""` attributes
- **NO inline scripts** - Never use `onclick=""`, `onload=""`, or inline `<script>`
- **NO external resources** - No CDNs, Google Fonts, external APIs
- **All styles → styles.css** (single file)
- **All scripts → app.js** (single file with `defer`)

### 2. Citation Standards (STRICT)

- .EDU and .GOV domains only
- Publication date: 2022-2026
- **MANDATORY LINKS** - Every citation MUST include a direct URL
- **NO LINK = NO FACT** - Cannot find a verifiable source? Don't add the claim.

### 3. Code Notation
```
HTML:  <!-- === SECTION === --> ... <!-- /SECTION -->
CSS:   /* === SECTION === */ ... /* Component ---- */
JS:    // === SECTION === ... /** JSDoc comments */
```

---

## FILE STRUCTURE

```
_public_html/
├── index.html              # Home page
├── styles.css              # ALL styles (single file)
├── app.js                  # ALL JavaScript (single file)
├── learn/                  # Framework pages
│   ├── zero-shot.html      # NEW (Session 24)
│   ├── zero-shot-cot.html  # NEW (Session 24)
│   └── modality/           # For code/image/audio/video/3d frameworks
├── data/
│   ├── glossary.json       # 33 prompting terms
│   └── search-index.json   # Site search data
└── .claude/
    ├── HANDOFF.md          # THIS FILE
    ├── COMPLETED.md        # Archived completed tasks
    └── plans/
        └── FrameworkOverhaul.md  # Master plan with session logs
```

---

## DEFERRED TASKS

| Task | Priority |
|------|----------|
| Navigation/footer updates | After ALL pages created |
| Search index updates | After ALL pages created |
| Badge lightbox popups | Low |

---

## REFERENCE

| Document | Purpose |
|----------|---------|
| `.claude/HANDOFF.md` | Current state (this file) |
| `.claude/plans/FrameworkOverhaul.md` | Master plan with full session logs |
| `learn/chain-of-thought.html` | Reference template for page structure |

---

*Always read this file first when resuming work. Update FrameworkOverhaul.md frequently.*
