# Praxis Project Instructions

**This file is automatically read at the start of every Claude Code session.**

---

## Required Reading

Before making ANY changes, read these files:
1. `.claude/HANDOFF.md` - Current state, rules, and progress
2. `.claude/plans/praxis-enhancement-plan.md` - Master plan with all phases

---

## Critical Rules (Always Follow)

### Security (A+ CSP Compliance)
- **NO inline styles** - Never use `style=""` in HTML
- **NO inline scripts** - Never use `onclick=""`, `onload=""`, or inline `<script>`
- **NO external resources** - No CDNs, Google Fonts, or external APIs
- **All styles in styles.css** - Single external stylesheet
- **All scripts in app.js** - Single external script with `defer`

### Performance (100% Score)
- Efficient, minimal code
- No render-blocking resources
- Remove all unused code

### Code Notation (Required)
```
HTML:  <!-- === SECTION === --> ... <!-- /SECTION -->
CSS:   /* === SECTION === */ ... /* Component ---- */
JS:    // === SECTION === ... /** JSDoc comments */
```

### Accessibility (WCAG AA)
- Meaningful alt text
- 4.5:1 color contrast
- Full keyboard navigation
- Proper heading hierarchy

---

## Prompt Management Rules

### Auto-Compact Policy
- **At 90% context capacity:** Automatically compact/summarize the conversation
- **Pre-warning required:** Alert user when approaching 90% total prompt capacity
- **Never reach "Prompt is full":** Proactively manage context before hitting limits
- **Preserve critical context:** When compacting, retain current task state and HANDOFF.md updates

### Context Preservation Priority
1. Current task status and progress
2. Uncommitted code changes
3. Active file modifications
4. Recent error/debugging context
5. Session-specific decisions

---

## Workflow

1. Read HANDOFF.md for current task status
2. Confirm understanding before proceeding
3. Follow notation standards in all code
4. Update HANDOFF.md when completing tasks
5. Monitor prompt capacity and compact proactively

---

## Quick Reference

| File | Purpose |
|------|---------|
| `.claude/HANDOFF.md` | Session continuity & rules |
| `.claude/plans/praxis-enhancement-plan.md` | Full phase details |
| `styles.css` | ALL CSS (single file) |
| `app.js` | ALL JavaScript (single file) |
