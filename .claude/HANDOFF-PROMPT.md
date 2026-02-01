# Praxis Project Handoff Prompt

## AUTOMATED LOADING

The `CLAUDE.md` file in the project root is **automatically read** at the start of every Claude Code session. No manual prompt needed.

The manual prompt below is a **backup** if automation isn't working.

---

## MANUAL PROMPT (Backup)

```
I'm continuing work on the Praxis website project. Before we begin, please read the following files to understand the project rules, standards, and current progress:

1. `.claude/HANDOFF.md` - Project rules, standards, and session continuity
2. `.claude/plans/praxis-enhancement-plan.md` - Master plan with all phases

## Critical Rules (Summary)

- **NO inline styles or scripts** - All CSS in styles.css, all JS in app.js
- **CSP A+ compliance** - No external resources, no CDNs, no eval
- **Performance 100%** - Efficient code, no unused code, defer scripts
- **Code notation required** - Clear section markers, JSDoc comments, documented regions
- **WCAG AA accessibility** - Keyboard nav, contrast, alt text, heading hierarchy

## Code Standards

All code must be well-notated with:
- `===` block borders for major sections
- `---` separators for sub-sections
- JSDoc comments for functions
- Opening/closing HTML region markers
- Inline "why" comments for complex logic

## Current State

Read the HANDOFF.md file to see:
- What tasks are completed
- What tasks are in progress
- What tasks are pending
- Key implementation details

## How to Proceed

1. Read both documentation files first
2. Confirm you understand the current state
3. Ask if anything is unclear
4. Continue with the next pending task

Do not make changes until you've reviewed the documentation and confirmed understanding.
```

---

## USAGE NOTES

- Paste this prompt at the start of every new session
- The AI will read the documentation files and pick up where you left off
- Update HANDOFF.md as you complete tasks to keep it current
- The prompt is intentionally generic so it works regardless of which phase you're in

---

## QUICK VERSION

If you need a shorter version:

```
Continuing Praxis project. Read `.claude/HANDOFF.md` and `.claude/plans/praxis-enhancement-plan.md` first. Follow all CSP/security rules (no inline code), notation standards (documented sections), and performance requirements. Confirm understanding before proceeding.
```
