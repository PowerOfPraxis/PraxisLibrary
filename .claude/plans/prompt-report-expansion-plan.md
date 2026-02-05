# Prompt Report Expansion Plan

## Overview

Expand the Praxis site to comprehensively cover all 58 text prompting frameworks and 40 modality frameworks from "The Prompt Report" (arXiv:2406.06608v6), plus add 33 vocabulary terms to the glossary.

**Source:** The Prompt Report - A Systematic Survey of Prompting Techniques (2024)

---

## Current State

### Existing Frameworks (11 total in learn/)
1. CRISP Framework (crisp.html) - Practitioner framework
2. CRISPE Framework (crispe.html) - Practitioner framework
3. COSTAR Framework (costar.html) - Practitioner framework
4. ReAct Framework (react.html) - ✓ Covered
5. Flipped Interaction (flipped-interaction.html) - Practitioner framework
6. Chain-of-Thought (chain-of-thought.html) - ✓ Covered
7. Few-Shot Learning (few-shot-learning.html) - ✓ Covered
8. Role Prompting (role-prompting.html) - ✓ Covered
9. Constrained Output (constrained-output.html)
10. Self-Consistency (self-consistency.html) - ✓ Covered
11. Prompt Chaining (prompt-chaining.html) - ✓ Covered

**Already Covered from Prompt Report:** 6 (CoT, Self-Consistency, Few-Shot, Role Prompting, ReAct, Prompt Chaining)

---

## Phase 1: Glossary Expansion (33 Terms)

### New Vocabulary Terms to Add

Add to `pages/glossary.html` under appropriate letters with category tag "Prompting":

| Term | Letter | Description |
|------|--------|-------------|
| Prefix Prompt | P | Text placed before the main task instruction |
| Cloze Prompt | C | Fill-in-the-blank style prompts |
| Discrete Prompt | D | Hard prompts using actual tokens from vocabulary |
| Continuous Prompt | C | Soft prompts using continuous embeddings |
| Prompt Template | P | Reusable structure with placeholders for task-specific content |
| Answer Engineering | A | Designing the output space and format for model responses |
| Prompt Mining | P | Automated discovery of effective prompt patterns |
| Prompt Paraphrasing | P | Generating variations of prompts to improve robustness |
| Gradient-based Search | G | Using gradients to optimize prompt tokens |
| Prompt Generation | P | Automatic creation of prompts by LLMs |
| Prompt Scoring | P | Evaluating prompt effectiveness through metrics |
| In-Context Learning | I | Learning from examples provided within the prompt |
| Demonstration | D | Example input-output pairs shown to guide the model |
| Exemplar | E | A single example used in few-shot prompting |
| Verbalizer | V | Mapping between output tokens and task labels |
| Label Space | L | The set of possible output categories or classes |
| Reasoning Chain | R | Sequential steps of logical inference in CoT |
| Rationale | R | Explanation or justification for a model's answer |
| Decomposition | D | Breaking complex tasks into simpler sub-tasks |
| Ensemble | E | Combining multiple model outputs for better accuracy |
| Self-Critique | S | Model evaluating and improving its own outputs |
| Refinement | R | Iteratively improving outputs through feedback |
| Tool Use | T | LLM invoking external tools (calculators, APIs, etc.) |
| Retrieval-Augmented | R | Enhancing prompts with retrieved external knowledge |
| Context Window | C | Maximum input length a model can process |
| Token Budget | T | Limit on tokens available for prompt and response |
| Temperature | T | Parameter controlling output randomness/creativity |
| Top-k Sampling | T | Selecting from k most likely next tokens |
| Top-p Sampling | T | Nucleus sampling from cumulative probability threshold |
| Greedy Decoding | G | Always selecting the most probable next token |
| Beam Search | B | Exploring multiple candidate sequences in parallel |
| Prompt Injection | P | Adversarial input attempting to override instructions |
| Jailbreak | J | Techniques to bypass model safety restrictions |

---

## Phase 2: Text Framework Pages (52 New Pages)

### Category 1: Zero-Shot Frameworks (8 pages)

| Framework | File | Description | Priority |
|-----------|------|-------------|----------|
| Zero-Shot | zero-shot.html | Basic prompting without examples | High |
| Emotion Prompting | emotion-prompting.html | Adding emotional context to improve responses | Medium |
| Role Prompting (extended) | (exists) | Expand existing page with paper techniques | - |
| Style Prompting | style-prompting.html | Controlling output style and tone | Medium |
| S2A (System 2 Attention) | s2a.html | Focusing model attention on relevant context | Low |
| SimToM | simtom.html | Simulating Theory of Mind reasoning | Low |
| RaR (Rephrase and Respond) | rar.html | Self-rephrasing for clarity | Medium |
| RE2 (Re-Reading) | re2.html | Multiple passes over input for comprehension | Low |

### Category 2: In-Context Learning Frameworks (10 pages)

| Framework | File | Description | Priority |
|-----------|------|-------------|----------|
| Few-Shot Learning (extended) | (exists) | Expand with k-shot variants | - |
| One-Shot | one-shot.html | Single example prompting | High |
| Many-Shot | many-shot.html | Large number of demonstrations | Medium |
| Example Selection | example-selection.html | Choosing optimal demonstrations | High |
| Example Ordering | example-ordering.html | Sequencing demonstrations for best results | Medium |
| KNN Prompting | knn-prompting.html | Nearest-neighbor example selection | Low |
| Vote-k | vote-k.html | Ensemble voting over example subsets | Low |
| Self-Generated ICL | self-generated-icl.html | Model creates its own examples | Medium |
| Demonstration Ensembling | demo-ensembling.html | Combining multiple demo sets | Low |
| Active Example Selection | active-example.html | Dynamic example choice during inference | Low |

### Category 3: Thought Generation Frameworks (12 pages)

| Framework | File | Description | Priority |
|-----------|------|-------------|----------|
| Chain-of-Thought (extended) | (exists) | Already comprehensive | - |
| Zero-Shot CoT | zero-shot-cot.html | "Let's think step by step" | High |
| Analogical Reasoning | analogical-reasoning.html | Using analogies to solve problems | Medium |
| Step-Back Prompting | step-back.html | Abstracting before solving | Medium |
| Thread of Thought | thread-of-thought.html | Managing complex reasoning threads | Low |
| Tab-CoT | tab-cot.html | Tabular chain of thought | Low |
| Contrastive CoT | contrastive-cot.html | Showing correct vs incorrect reasoning | Medium |
| Uncertainty-Routed CoT | uncertainty-cot.html | Adaptive depth based on confidence | Low |
| Complexity-Based Prompting | complexity-prompting.html | Scaling reasoning to task difficulty | Low |
| Active Prompting | active-prompting.html | Interactive reasoning refinement | Low |
| Memory-of-Thought | memory-of-thought.html | Persistent reasoning context | Low |
| Automatic CoT (Auto-CoT) | auto-cot.html | Automated reasoning chain generation | Medium |

### Category 4: Decomposition Frameworks (8 pages)

| Framework | File | Description | Priority |
|-----------|------|-------------|----------|
| Least-to-Most | least-to-most.html | Solving simple to complex | High |
| DECOMP | decomp.html | Systematic task decomposition | Medium |
| Plan-and-Solve | plan-and-solve.html | Planning before execution | High |
| Tree of Thought (ToT) | tree-of-thought.html | Branching reasoning paths | High |
| Graph of Thought (GoT) | graph-of-thought.html | Network-based reasoning | Medium |
| Recursion of Thought | recursion-of-thought.html | Recursive problem solving | Low |
| Program of Thought | program-of-thought.html | Code-based reasoning | Medium |
| Faithful CoT | faithful-cot.html | Verified reasoning chains | Low |

### Category 5: Ensembling Frameworks (6 pages)

| Framework | File | Description | Priority |
|-----------|------|-------------|----------|
| Self-Consistency (extended) | (exists) | Expand existing page | - |
| COSP (Consistency Self-Prompting) | cosp.html | Self-consistent prompting | Low |
| DENSE (Diverse Ensembles) | dense.html | Diverse reasoning paths | Low |
| Max Mutual Information | max-mutual-info.html | Information-theoretic ensemble | Low |
| Meta-Reasoning over Paths | meta-reasoning.html | Aggregating reasoning strategies | Low |
| Universal Self-Consistency | universal-self-consistency.html | Cross-domain consistency | Low |

### Category 6: Self-Criticism Frameworks (8 pages)

| Framework | File | Description | Priority |
|-----------|------|-------------|----------|
| Self-Refine | self-refine.html | Iterative self-improvement | High |
| Self-Verification | self-verification.html | Checking own outputs | High |
| Chain-of-Verification | chain-of-verification.html | Multi-step verification | Medium |
| CRITIC | critic.html | Structured self-critique | Medium |
| Cumulative Reasoning | cumulative-reasoning.html | Building on previous answers | Low |
| Reversing CoT | reversing-cot.html | Backward verification | Low |
| Self-Calibration | self-calibration.html | Confidence calibration | Low |
| Reflexion | reflexion.html | Learning from mistakes | Medium |

---

## Phase 3: Modality Frameworks Section

### New Directory Structure

```
learn/
├── index.html (Update with new categories)
├── modality/
│   ├── index.html (Modality hub page)
│   ├── image/
│   │   ├── image-prompting.html
│   │   ├── multimodal-cot.html
│   │   └── ... (10 pages)
│   ├── audio/
│   │   ├── audio-prompting.html
│   │   └── ... (5 pages)
│   ├── video/
│   │   ├── video-prompting.html
│   │   └── ... (5 pages)
│   ├── code/
│   │   ├── code-prompting.html
│   │   └── ... (8 pages)
│   └── 3d/
│       ├── 3d-prompting.html
│       └── ... (5 pages)
```

### Image Prompting Frameworks (12 pages)

| Framework | File | Description |
|-----------|------|-------------|
| Image Prompting Basics | image-prompting.html | Fundamentals of image input |
| Multimodal CoT | multimodal-cot.html | Reasoning with images |
| Visual Chain of Thought | visual-cot.html | Step-by-step visual reasoning |
| Image-as-Text | image-as-text.html | Converting images to descriptions |
| Visual Question Answering | vqa.html | Asking questions about images |
| Image Generation Prompting | image-gen-prompting.html | Text-to-image techniques |
| Negative Prompting | negative-prompting.html | What NOT to generate |
| ControlNet Prompting | controlnet-prompting.html | Structural guidance |
| Inpainting Prompting | inpainting-prompting.html | Selective image editing |
| Style Transfer Prompting | style-transfer.html | Applying artistic styles |
| Image-to-Image | image-to-image.html | Image transformation |
| Composition Prompting | composition-prompting.html | Layout and arrangement |

### Audio/Speech Frameworks (6 pages)

| Framework | File | Description |
|-----------|------|-------------|
| Audio Prompting Basics | audio-prompting.html | Voice/audio input fundamentals |
| Speech-to-Text Prompting | stt-prompting.html | Transcription guidance |
| Text-to-Speech Prompting | tts-prompting.html | Voice synthesis control |
| Audio Classification | audio-classification.html | Sound categorization |
| Music Generation Prompting | music-gen.html | Creating music with AI |
| Voice Cloning Prompting | voice-cloning.html | Voice replication techniques |

### Video Frameworks (6 pages)

| Framework | File | Description |
|-----------|------|-------------|
| Video Prompting Basics | video-prompting.html | Video understanding fundamentals |
| Video Generation Prompting | video-gen.html | Text-to-video techniques |
| Temporal Reasoning | temporal-reasoning.html | Understanding time in video |
| Video QA | video-qa.html | Asking questions about videos |
| Video Captioning | video-captioning.html | Describing video content |
| Video Editing Prompting | video-editing.html | AI-assisted video editing |

### Code/Structured Frameworks (8 pages)

| Framework | File | Description |
|-----------|------|-------------|
| Code Prompting Basics | code-prompting.html | Programming with LLMs |
| Program Synthesis | program-synthesis.html | Generating code from specs |
| Self-Debugging | self-debugging.html | Auto code repair |
| Code Explanation | code-explanation.html | Understanding code |
| Code Review Prompting | code-review.html | AI code review |
| Test Generation | test-generation.html | Auto test creation |
| Structured Output | structured-output.html | JSON/XML generation |
| SQL Generation | sql-generation.html | Database query creation |

### 3D/Spatial Frameworks (5 pages)

| Framework | File | Description |
|-----------|------|-------------|
| 3D Prompting Basics | 3d-prompting.html | Spatial AI fundamentals |
| 3D Model Generation | 3d-model-gen.html | Text-to-3D |
| Scene Understanding | scene-understanding.html | 3D scene analysis |
| Pose Estimation Prompting | pose-estimation.html | Human pose guidance |
| Point Cloud Prompting | point-cloud.html | 3D point data |

---

## Phase 4: Site Structure Updates

### Navigation Changes

Update mega-menu structure in all 48 HTML files:

```html
<div class="mega-menu-section">
    <h4>Text Frameworks</h4>
    <a href="zero-shot.html">Zero-Shot</a>
    <a href="few-shot-learning.html">Few-Shot</a>
    <a href="chain-of-thought.html">Chain-of-Thought</a>
    <!-- + grouped submenu for 52 frameworks -->
</div>
<div class="mega-menu-section">
    <h4>Modality Frameworks</h4>
    <a href="modality/index.html">All Modalities</a>
    <a href="modality/image/index.html">Image</a>
    <a href="modality/code/index.html">Code</a>
    <a href="modality/audio/index.html">Audio/Video</a>
</div>
```

### Learn Hub Redesign (learn/index.html)

1. Add category filter tabs (Zero-Shot, ICL, Thought Gen, Decomposition, Ensemble, Self-Critic, Modality)
2. Create framework grid with all 98 frameworks
3. Add difficulty indicators (Beginner, Intermediate, Advanced)
4. Add "Modality Frameworks" section with visual icons

### Search Index Updates (data/search-index.json)

Add entries for all 52 new text framework pages and 40 modality pages.

---

## Implementation Phases

### Phase A: Foundation (Do First)
1. Add 33 glossary terms to pages/glossary.html
2. Create template for new framework pages
3. Create 8 HIGH priority text framework pages:
   - zero-shot.html
   - zero-shot-cot.html
   - one-shot.html
   - least-to-most.html
   - plan-and-solve.html
   - tree-of-thought.html
   - self-refine.html
   - self-verification.html

### Phase B: Core Expansion
1. Create 15 MEDIUM priority text framework pages
2. Create modality/index.html hub page
3. Create modality/image/ directory with 5 core pages
4. Create modality/code/ directory with 4 core pages

### Phase C: Comprehensive Coverage
1. Create remaining 29 LOW priority text framework pages
2. Complete modality/image/ (7 more pages)
3. Create modality/audio/ (6 pages)
4. Create modality/video/ (6 pages)
5. Complete modality/code/ (4 more pages)
6. Create modality/3d/ (5 pages)

### Phase D: Integration
1. Update all 48 navigation menus
2. Update learn/index.html with new hub design
3. Update data/search-index.json
4. Update Framework Matcher tool
5. Cross-link related frameworks
6. Extend existing framework pages with Prompt Report content

---

## Page Template Structure

Each new framework page should include:

```
1. Hero section with framework name and one-line description
2. Content badges (AI for Everybody, UD/UDL, etc.)
3. "What Is [Framework]?" section
4. "How It Works" with visual diagram
5. "When to Use" with use cases
6. "Example Prompts" with practical examples
7. "Best Practices" bullet list
8. "Common Mistakes" to avoid
9. "Related Frameworks" navigation
10. Citations/References from Prompt Report
```

---

## File Counts Summary

| Category | Count |
|----------|-------|
| Glossary terms to add | 33 |
| New text framework pages | 52 |
| New modality framework pages | 37 |
| Navigation updates | 48 files |
| **Total new pages** | **89** |

---

## Quality Standards

All new pages must meet:
- CSP A+ compliance (no inline styles/scripts)
- WCAG AA accessibility
- Consistent BEM notation
- Mobile responsive design
- Cross-linked to related frameworks
- Citations to Prompt Report where applicable

---

## Awaiting Approval

This plan covers:
1. ✅ Add 33 vocabulary terms to glossary
2. ✅ Create pages for ALL 52 missing text frameworks
3. ✅ Create Modality Section with 37 framework pages
4. ✅ Site structure/navigation updates

**Total scope: 89 new pages + 33 glossary terms + navigation updates**

Confirm to proceed with implementation.
