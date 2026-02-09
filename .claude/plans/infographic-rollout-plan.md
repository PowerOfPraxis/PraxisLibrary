# Phase 6: Prompt Infographic Rollout Plan

**Created:** Session 61 (2026-02-08)
**Scope:** 108 framework pages across all categories
**Goal:** Add a professional prompt infographic to every framework page showing what a complete prompt using that technique looks like.

---

## OVERVIEW

Every framework page on the site has a "The Concept" section (section 3 of the 13-section template) with a split layout: explanatory text on the left, a highlight-box on the right. We are adding a **prompt infographic** component above the existing highlight-box in the right column — identical in format to the prototype on `learn/costar.html`.

The infographic acts as an **information radiator** — a quick-glance visual that shows users exactly what a professional prompt looks like when using that framework. Each row represents a component/step of the technique with a badge, a label, and example text.

---

## PROTOTYPE REFERENCE: learn/costar.html

The approved prototype has:
- White background, red gradient top accent bar (3px)
- **Header:** Badge row (letter/number squares) + "Professional Prompt Template" subtitle
- **Rows:** Each row has a colored badge (28px square), a label (uppercase, 0.68rem), and example text (0.74rem)
- **Footer:** Summary line (e.g., "6 dimensions — one precision-calibrated prompt")
- **Layout:** Top of `split-section__visual`, above the existing highlight-box
- **Alignment:** `split-section--align-start` (top-aligned, not center)
- **Colors:** Brand palette only — `--primary` (red), `--text-primary` (near-black), `--text-muted` (gray), `--primary-dark` (dark red)

---

## SCOPE

### Included (108 pages)
All framework pages with the 13-section template:

| Category | Count | Pages |
|----------|-------|-------|
| Getting Started | 2 | prompt-basics, facts-fictions |
| Structured Frameworks | 5 | crisp, crispe, costar (DONE), constrained-output, context-structure |
| Reasoning & CoT | 15 | chain-of-thought, zero-shot-cot, auto-cot, contrastive-cot, faithful-cot, reversing-cot, structured-cot, tab-cot, uncertainty-cot, complexity-prompting, step-back, graph-of-thought, tree-of-thought, cumulative-reasoning, flipped-interaction |
| Decomposition | 8 | plan-and-solve, least-to-most, decomp, program-of-thought, recursion-of-thought, skeleton-of-thought, prompt-chaining, dense-prompting |
| Self-Correction | 7 | self-refine, self-verification, self-calibration, chain-of-verification, reflexion, critic, self-ask |
| Ensemble Methods | 7 | self-consistency, universal-self-consistency, demo-ensembling, diverse-prompting, vote-k, max-mutual-info, active-prompting |
| In-Context Learning | 13 | few-shot-learning, zero-shot, one-shot, shot-prompting, role-prompting, example-selection, knn-prompting, many-shot, example-ordering, self-generated-icl, active-example, prompt-mining, memory-of-thought |
| Prompting Strategies | 14 | emotion-prompting, style-prompting, s2a, re2, cosp, rar, meta-reasoning, simtom, thread-of-thought, analogical-reasoning, system-prompting, rag, agentic-prompting, react |
| Code | 8 | code-prompting, self-debugging, structured-output, program-synthesis, code-explanation, code-review, test-generation, sql-generation |
| Image | 12 | image-prompting, multimodal-cot, visual-cot, image-as-text, vqa, image-gen-prompting, negative-prompting, controlnet-prompting, inpainting-prompting, style-transfer, image-to-image, composition-prompting |
| Audio | 6 | audio-prompting, stt-prompting, tts-prompting, audio-classification, music-gen, voice-cloning |
| Video | 6 | video-prompting, video-gen, temporal-reasoning, video-qa, video-captioning, video-editing |
| 3D | 5 | 3d-prompting, 3d-model-gen, scene-understanding, pose-estimation, point-cloud |

### Excluded (9 pages — no concept section)
- 7 category pages: structured-frameworks.html, reasoning-cot.html, decomposition.html, self-correction.html, in-context-learning.html, ensemble-methods.html, prompting-strategies.html
- 2 hub pages: learn/index.html (Discover), learn/modality/index.html (Modality)

### Already Done (1 page)
- costar.html — Prototype completed Session 61. SKIP in batch.

### Remaining Work
- **107 pages** need infographic injection (108 - 1 done)

---

## TWO BADGE TYPES

### Letter Badges (3 pages)
For acronym frameworks where EACH LETTER maps to a distinct prompt component the user fills in:

| Page | Acronym | Letters → Labels |
|------|---------|------------------|
| costar.html | CO-STAR | C→Context, O→Objective, S→Style, T→Tone, A→Audience, R→Response |
| crisp.html | CRISP | C→Context, R→Role, I→Instructions, S→Scope, P→Parameters |
| crispe.html | CRISPE | C→Context, R→Role, I→Instructions, S→Scope, P→Parameters, E→Evaluation |

### Number Badges (105 pages)
Everything else uses numbered step badges (1, 2, 3...) from their "How It Works" section.

Each page's "How It Works" already has numbered steps with titles and examples in the `element-timeline`. The infographic condenses these into a compact visual template showing what a complete prompt looks like.

**Row count varies by page:**
- 2 rows: zero-shot-cot (rare)
- 3 rows: chain-of-thought, react, self-consistency, etc.
- 4 rows: self-ask, tree-of-thought, image-prompting, code-prompting, etc.
- 5 rows: critic, chain-of-verification, etc.
- 6 rows: reflexion, etc.

---

## IMPLEMENTATION STEPS

### Step 1: CSS Generalization
**Time estimate:** ~20 minutes
**File:** `styles.css` (~line 25394)

**Current problem:** Colors are hardcoded for exactly 6 rows (nth-child 1-6).
**Fix:** Replace with cycling 4-color pattern that works for any row count.

**Changes:**
```css
/* REPLACE hardcoded nth-child(1-6) with cycling pattern */
/* Header letter badges */
.prompt-infographic__letters span:nth-child(4n+1) { background: var(--primary); }
.prompt-infographic__letters span:nth-child(4n+2) { background: var(--text-primary); }
.prompt-infographic__letters span:nth-child(4n+3) { background: var(--text-muted); }
.prompt-infographic__letters span:nth-child(4n) { background: var(--primary-dark); }

/* Row letter badges — same pattern */
.prompt-infographic__row:nth-child(4n+1) .prompt-infographic__letter { background: var(--primary); }
.prompt-infographic__row:nth-child(4n+2) .prompt-infographic__letter { background: var(--text-primary); }
.prompt-infographic__row:nth-child(4n+3) .prompt-infographic__letter { background: var(--text-muted); }
.prompt-infographic__row:nth-child(4n) .prompt-infographic__letter { background: var(--primary-dark); }

/* Row field borders — same pattern */
.prompt-infographic__row:nth-child(4n+1) .prompt-infographic__field { border-left-color: var(--primary); }
.prompt-infographic__row:nth-child(4n+2) .prompt-infographic__field { border-left-color: var(--text-primary); }
.prompt-infographic__row:nth-child(4n+3) .prompt-infographic__field { border-left-color: var(--text-muted); }
.prompt-infographic__row:nth-child(4n) .prompt-infographic__field { border-left-color: var(--primary-dark); }
```

Also update:
- Remove `margin-top: var(--space-md)` from `.prompt-infographic` (infographic is now first element)
- Add `margin-bottom: var(--space-sm)` for spacing before highlight-box below

### Step 2: Content Extraction Script
**Time estimate:** ~30 minutes to write, ~5 minutes to run
**File:** `extract_infographic_data.py` (temporary, delete after use)

**Purpose:** Automatically extract infographic content from each page's "How It Works" section.

**Algorithm:**
1. For each of the 108 HTML files:
   a. Read the file
   b. Find `<!-- === HOW IT WORKS === -->` section
   c. Count `element-timeline__item` elements = number of rows
   d. Extract each `element-timeline__title` text = row labels
   e. Extract each `element-timeline__example` first `<p>` text = row example text
   f. Determine badge type: check if filename is in ACRONYM_PAGES list
   g. For letter-badge pages: use acronym letters as badges, component names as labels
   h. For number-badge pages: use step numbers as badges, step titles as labels
2. Write results to `data/infographic-content.json`

**JSON schema:**
```json
[
  {
    "file": "learn/chain-of-thought.html",
    "depth": 1,
    "badge_type": "number",
    "title": "Professional Prompt Template",
    "rows": [
      {
        "badge": "1",
        "label": "Reasoning Demo",
        "text": "Q: Roger has 5 tennis balls. He buys 2 more cans of 3. How many? A: Started with 5. 2 cans × 3 = 6 new. 5 + 6 = 11."
      },
      {
        "badge": "2",
        "label": "Target Problem",
        "text": "Q: The cafeteria had 23 apples. Used 20 for lunch, bought 6 more. How many now?"
      },
      {
        "badge": "3",
        "label": "Answer Extraction",
        "text": "Show reasoning step by step, then state the final answer."
      }
    ],
    "footer_count": "3 steps",
    "footer_desc": "one transparent reasoning chain"
  }
]
```

**Special handling:**
- ACRONYM_PAGES = {"costar.html": "COSTAR", "crisp.html": "CRISP", "crispe.html": "CRISPE"}
- Step title trimming: Extract just the key phrase (e.g., "Context — Set the Scene" → "Context")
- Example text trimming: Max ~120 characters, one sentence
- Footer auto-generation: "{N} steps — one [technique-specific summary]"

### Step 3: Content Review & Refinement
**Time estimate:** ~45-60 minutes (manual review)

After the extraction script generates the JSON:
1. Review every entry for quality and accuracy
2. Trim any overly long text (max ~120 chars per row)
3. Verify badge assignments are correct
4. Ensure labels are clear, concise, and unique within each page
5. Write custom footer descriptions (the extraction script can't auto-generate these well)
6. Handle special cases:
   - `facts-fictions.html` — Infographic shows "How to Evaluate AI Claims" steps
   - `prompt-basics.html` — Infographic shows "The Four Elements of a Prompt"
   - Pages with very short "How It Works" (2 steps) — ensure infographic still looks good

### Step 4: HTML Injection Script
**Time estimate:** ~30 minutes to write
**File:** `inject_infographic.py` (temporary, delete after use)

**Purpose:** Read the JSON data file and inject infographic HTML into each page.

**Algorithm:**
1. Read `data/infographic-content.json`
2. For each entry:
   a. Read the HTML file
   b. Check if infographic already exists (skip if so)
   c. Find `split-section--center` in the concept section → change to `split-section--align-start`
   d. Find `<div class="split-section__visual">` inside the concept section
   e. Inject infographic HTML immediately after the opening tag
   f. Write the modified file

**HTML template to inject:**
```html
                        <!-- === PROMPT INFOGRAPHIC === -->
                        <div class="prompt-infographic">
                            <div class="prompt-infographic__header">
                                <div class="prompt-infographic__letters">
                                    {badge_spans}
                                </div>
                                <span class="prompt-infographic__title">Professional Prompt Template</span>
                            </div>
                            <div class="prompt-infographic__rows">
                                {rows_html}
                            </div>
                            <div class="prompt-infographic__footer">
                                <span class="prompt-infographic__footer-text"><strong>{footer_count}</strong> &mdash; {footer_desc}</span>
                            </div>
                        </div>
                        <!-- /PROMPT INFOGRAPHIC -->
```

**Per-row template:**
```html
                                <div class="prompt-infographic__row">
                                    <div class="prompt-infographic__letter">{badge}</div>
                                    <div class="prompt-infographic__field">
                                        <span class="prompt-infographic__label">{label}</span>
                                        <p class="prompt-infographic__text">{text}</p>
                                    </div>
                                </div>
```

**Depth handling:**
- Depth 1 (learn/*.html): Standard indentation
- Depth 3 (learn/modality/code/*.html, etc.): Same indentation, different file path

### Step 5: Batch Execution
**Time estimate:** ~5 minutes per wave + QA time

Run the injection script in waves for easier debugging:

| Wave | Category | Pages | Notes |
|------|----------|-------|-------|
| 1 | Structured Frameworks | 4 | crisp, crispe, constrained-output, context-structure (costar already done) |
| 2 | Getting Started | 2 | prompt-basics, facts-fictions |
| 3 | Reasoning & CoT | 15 | chain-of-thought, zero-shot-cot, auto-cot, etc. |
| 4 | Decomposition | 8 | plan-and-solve, least-to-most, etc. |
| 5 | Self-Correction | 7 | self-refine, self-verification, critic, etc. |
| 6 | Ensemble Methods | 7 | self-consistency, vote-k, etc. |
| 7 | In-Context Learning | 13 | few-shot, zero-shot, one-shot, etc. |
| 8 | Prompting Strategies | 14 | emotion-prompting, react, rag, etc. |
| 9 | Code | 8 | code-prompting, self-debugging, etc. |
| 10 | Image | 12 | image-prompting, multimodal-cot, etc. |
| 11 | Audio | 6 | audio-prompting, stt-prompting, etc. |
| 12 | Video | 6 | video-prompting, video-gen, etc. |
| 13 | 3D | 5 | 3d-prompting, 3d-model-gen, etc. |

**Note:** Waves can be combined. The Python script processes all pages in the JSON in one run. Waves are for QA spot-checking.

### Step 6: QA & Verification
**Time estimate:** ~20 minutes

Post-injection checks:
1. **Count verification:** 108 pages should have infographic (107 new + 1 existing costar)
2. **CSP compliance:** `grep -r "style=" learn/` — zero inline styles
3. **No duplicates:** No page should have two infographics
4. **Layout check:** All concept sections should use `split-section--align-start`
5. **Visual spot-check:** Open 5-6 representative pages in browser
6. **Responsive check:** Verify infographic looks good at mobile widths

---

## ESTIMATED EFFORT

| Step | Task | Estimate |
|------|------|----------|
| 1 | CSS generalization | 20 min |
| 2 | Extraction script | 35 min |
| 3 | Content review | 45-60 min |
| 4 | Injection script | 30 min |
| 5 | Batch execution | 15 min |
| 6 | QA & verification | 20 min |
| **Total** | | **~3 hours** |

Can be done across 1-2 chat sessions.

---

## COMMIT STRATEGY

Single commit after all 107 pages are done + CSS updated:
```
feat: Add prompt infographic to all 108 framework pages

- Professional prompt template visual on every framework page
- Shows technique-specific example in the "Concept" section
- CSS generalized for variable row counts (3-7)
- 3 letter-badge pages (CRISP, CRISPE, CO-STAR)
- 105 number-badge pages (process frameworks)
- Consistent brand palette: red, black, gray, dark-red cycle
```

---

## FILES MODIFIED

| File | Changes |
|------|---------|
| `styles.css` | Generalize nth-child colors to cycling pattern |
| 107 HTML files | Add infographic HTML + change split-section alignment |
| `data/infographic-content.json` | NEW — content data for all 108 infographics |

**Temporary files (delete after):**
- `extract_infographic_data.py`
- `inject_infographic.py`

---

## CRITICAL RULES COMPLIANCE

- [ ] Zero inline styles
- [ ] Zero inline scripts
- [ ] Zero external resources
- [ ] All styles in styles.css
- [ ] All HTML follows BEM notation
- [ ] Section comments: `<!-- === PROMPT INFOGRAPHIC === -->` / `<!-- /PROMPT INFOGRAPHIC -->`
- [ ] Brand colors only (--primary, --text-primary, --text-muted, --primary-dark)
- [ ] Accessible: proper contrast, readable at all sizes
- [ ] Responsive: works on mobile

---

*This plan was created in Session 61. Implementation begins in Session 62.*
