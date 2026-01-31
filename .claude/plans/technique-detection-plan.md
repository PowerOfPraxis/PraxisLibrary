# Implementation Plan: Flipped Interaction & Full Technique Detection

## Overview
Add "The Flipped Interaction" technique as a new learning page and implement comprehensive technique detection in the Prompt Analyzer.

---

## Phase 1: Create Flipped Interaction Page

### Task 1.1: Create learn/flipped-interaction.html
- [ ] Page structure with header, hero, breadcrumb
- [ ] What is Flipped Interaction section
- [ ] Why it works (prevents generic advice)
- [ ] How to use it (trigger phrases)
- [ ] Progressive build examples with department tabs (5 examples)
- [ ] When to use / When not to use
- [ ] Common variations
- [ ] Footer

### Task 1.2: Update Navigation
- [ ] Add to learn/index.html card grid
- [ ] Add to header nav dropdown if applicable
- [ ] Update all footer links across site
- [ ] Add to patterns/index.html as a pattern card

### Task 1.3: Update Prompt Builder (tools/guidance.html)
- [ ] Consider adding Flipped Interaction as a methodology option

---

## Phase 2: Full Technique Detection Library

### Task 2.1: Define Technique Patterns in app.js

```javascript
const TECHNIQUE_PATTERNS = {
    flippedInteraction: {
        name: "Flipped Interaction",
        description: "Asking AI to interview you first",
        signals: [
            { pattern: /\b(ask me|interview me|question me)\b/i, weight: 1.0 },
            { pattern: /\b(before (you )?(answer|respond|help)|first ask)\b/i, weight: 0.9 },
            { pattern: /\b(what (do you|else do you) need to know)\b/i, weight: 0.8 },
            { pattern: /\b(gather (more )?information|clarify(ing)? questions)\b/i, weight: 0.7 }
        ]
    },
    chainOfThought: {
        name: "Chain of Thought",
        description: "Step-by-step reasoning",
        signals: [
            { pattern: /\b(step by step|think through|walk me through)\b/i, weight: 1.0 },
            { pattern: /\b(show (your )?reasoning|explain (your )?thinking)\b/i, weight: 0.9 },
            { pattern: /\b(let'?s think|reason through|work through)\b/i, weight: 0.8 }
        ]
    },
    fewShot: {
        name: "Few-Shot Learning",
        description: "Providing examples before request",
        signals: [
            { pattern: /\bexample\s*\d*\s*:/i, weight: 1.0 },
            { pattern: /\binput\s*:.*output\s*:/i, weight: 1.0 },
            { pattern: /→|->/, weight: 0.7 },
            { pattern: /\blike this:/i, weight: 0.6 },
            { pattern: /\bfor instance:/i, weight: 0.5 }
        ]
    },
    rolePrompting: {
        name: "Role Prompting",
        description: "Assigning AI a persona",
        signals: [
            { pattern: /\b(act as|you are|pretend to be|imagine you('re| are))\b/i, weight: 1.0 },
            { pattern: /\b(as (a|an) (expert|specialist|professional))\b/i, weight: 0.9 },
            { pattern: /\b(approach this (like|as))\b/i, weight: 0.8 },
            { pattern: /\b(from the perspective of)\b/i, weight: 0.7 }
        ]
    },
    constraintsFirst: {
        name: "Constraints First",
        description: "Leading with limitations",
        signals: [
            { pattern: /^(constraints?|requirements?|rules?):/im, weight: 1.0 },
            { pattern: /\b(must be (under|less than|no more than))\b/i, weight: 0.8 },
            { pattern: /\b(don'?t|do not|never|avoid|exclude)\b/i, weight: 0.6 },
            { pattern: /\b(only use|limit(ed)? to|maximum|minimum)\b/i, weight: 0.7 }
        ]
    },
    selfVerification: {
        name: "Self-Verification",
        description: "Asking AI to check its work",
        signals: [
            { pattern: /\b(verify|double[- ]?check|review for (errors|accuracy))\b/i, weight: 1.0 },
            { pattern: /\b(are you sure|check (your|the) (answer|work|response))\b/i, weight: 0.9 },
            { pattern: /\b(confirm (this is|that)|validate)\b/i, weight: 0.8 }
        ]
    },
    audienceSpec: {
        name: "Audience Specification",
        description: "Defining who output is for",
        signals: [
            { pattern: /\b(for (beginners|experts|executives|children|professionals))\b/i, weight: 1.0 },
            { pattern: /\b(target(ing|ed)? (audience|readers|users))\b/i, weight: 0.9 },
            { pattern: /\b(written for|aimed at|intended for)\b/i, weight: 0.8 },
            { pattern: /\b(audience is|readers are)\b/i, weight: 0.9 }
        ]
    },
    formatSpec: {
        name: "Format Specification",
        description: "Defining output structure",
        signals: [
            { pattern: /\b(as a (table|list|json|csv|markdown))\b/i, weight: 1.0 },
            { pattern: /\b(in (json|xml|yaml|csv) format)\b/i, weight: 1.0 },
            { pattern: /\b(bullet(ed)? (points|list)|numbered list)\b/i, weight: 0.9 },
            { pattern: /\b(format(ted)? (as|like|with))\b/i, weight: 0.7 },
            { pattern: /\{.*:.*\}/s, weight: 0.6 }
        ]
    },
    metaPrompting: {
        name: "Meta-Prompting",
        description: "Instructions about how to respond",
        signals: [
            { pattern: /\b(respond only with|just (give|provide|show) me)\b/i, weight: 1.0 },
            { pattern: /\b(don'?t explain|no (explanation|preamble|introduction))\b/i, weight: 0.9 },
            { pattern: /\b(skip (the|any) (intro|introduction|preamble))\b/i, weight: 0.8 },
            { pattern: /\b(output only|return only)\b/i, weight: 0.8 }
        ]
    },
    devilsAdvocate: {
        name: "Devil's Advocate",
        description: "Challenging or critiquing",
        signals: [
            { pattern: /\b(devil'?s advocate|argue against|critique|challenge)\b/i, weight: 1.0 },
            { pattern: /\b(what could go wrong|find (the )?(flaws|weaknesses|problems))\b/i, weight: 0.9 },
            { pattern: /\b(poke holes|stress[- ]?test)\b/i, weight: 0.8 }
        ]
    }
};
```

### Task 2.2: Create detectTechniques() Function
- [ ] Iterate through all technique patterns
- [ ] Score each technique based on signal matches
- [ ] Return array of detected techniques with confidence levels
- [ ] Handle multiple techniques in single prompt

### Task 2.3: Update Analyzer Display
- [ ] Add "Techniques Detected" section to results
- [ ] Show technique badges with confidence (high/medium/low)
- [ ] Provide tips for techniques that could enhance the prompt
- [ ] Link to relevant learn pages for each technique

### Task 2.4: Add Technique-Specific Scoring
- [ ] Flipped Interaction: Check for clear scope of questions
- [ ] Chain of Thought: Verify task is reasoning-appropriate
- [ ] Few-Shot: Count examples, check consistency
- [ ] Role: Evaluate specificity of role assignment

---

## Phase 3: UI/UX Updates

### Task 3.1: Analyzer Results Redesign
- [ ] Add technique detection badges
- [ ] Show "Techniques Used" vs "Techniques to Consider"
- [ ] Expandable sections for technique details

### Task 3.2: CSS for Technique Badges
- [ ] Color-coded by technique category
- [ ] Hover states with descriptions
- [ ] Responsive layout

---

## Phase 4: Testing & Validation

### Task 4.1: Test Prompts
- [ ] Create test prompts for each technique
- [ ] Verify detection accuracy
- [ ] Check for false positives/negatives
- [ ] Test mixed-technique prompts

### Task 4.2: Cross-Browser Testing
- [ ] Chrome, Firefox, Safari, Edge
- [ ] Mobile responsiveness

---

## Phase 5: Post-Implementation Audit (ReAct Framework)

### Security Analysis
- [ ] CSP headers check
- [ ] Input sanitization
- [ ] XSS prevention
- [ ] No external dependencies

### Code Quality
- [ ] Consistent patterns
- [ ] No dead code
- [ ] Performance optimization
- [ ] Error handling

### Continuity Check
- [ ] All navigation links work
- [ ] Footer consistency
- [ ] Breadcrumb accuracy
- [ ] Cross-page references

### Active Link Verification
- [ ] Internal links (all .html files)
- [ ] Anchor links (#sections)
- [ ] External links (LinkedIn, mailto)

---

## File Changes Summary

| File | Action | Description |
|------|--------|-------------|
| learn/flipped-interaction.html | CREATE | New technique page |
| learn/index.html | MODIFY | Add card for new technique |
| patterns/index.html | MODIFY | Add pattern card |
| app.js | MODIFY | Add technique detection logic |
| styles.css | MODIFY | Add technique badge styles |
| All footer files | MODIFY | Add Flipped Interaction link |
| tools/analyzer.html | MODIFY | Update UI for technique display |

---

## Execution Order

1. Create flipped-interaction.html (foundation)
2. Add technique detection to app.js (core logic)
3. Update analyzer display (user-facing)
4. Update navigation/footers (discoverability)
5. Test and validate
6. Full site audit with ReAct

