# Copilot Instructions - Basiliso Rosario Portfolio Site

## Project Overview
A static, security-hardened portfolio website showcasing prompt engineering expertise and education. No frameworks, backend, or external dependencies—vanilla HTML/CSS/JavaScript only.

**Purpose:** Professional branding + educational library of AI prompt engineering methodologies (CRISP, CRISPE, COSTAR frameworks for 7 different professional roles).

---

## Architecture & File Roles

| File | Purpose | Key Responsibility |
|------|---------|-------------------|
| `library.html` | Core educational content | 2000+ lines: CRISP/CRISPE/COSTAR methodologies for Entry/Intermediate/Advanced levels across 7 roles (EAs, Engineers, Managers, etc.) |
| `app.js` | Client-side interactivity | Tab navigation (library), clipboard copy with feedback, simple event delegation |
| `styles.css` | Design system | Responsive grid layouts, color scheme (#D71920 red accent), typography, mobile breakpoint @768px |
| `index.html` | Landing page | Hero section, profile, navigation hub |
| `security.html` | Security documentation | CSP, HSTS, headers philosophy, site hardening rationale |

---

## Code Conventions & Patterns

### CSS & Naming
- **Classes:** kebab-case (`.nav-item`, `.sec-card`, `.framework-grid`, `.text-red`)
- **Layout system:** Sidebar navigation with `.main-wrapper`, `.container`, `.sidebar` pattern
- **Grid layouts:** Responsive using flexbox/grid (`.framework-grid`, `.sec-grid`)
- **Utilities:** `.text-red`, `.text-green`, `.text-white`, `.active`, `.hidden`
- **Responsive breakpoint:** `@media (max-width: 768px)` — all responsive changes use this threshold
- **Brand color:** `#D71920` (red accent throughout)

### HTML Data Attributes & State
- **Tab system:** `data-tab="foundation"` — matches sidebar nav items to tab-content divs in library.html
- **Semantic structure:** `.section-divider`, `.sec-section`, `.sec-card` for repeating content blocks
- **Icons:** Local SVG files in `Icons/SVG/` directory, referenced as `<img src="Icons/SVG/[name].svg" />`

### JavaScript Patterns
- **Event delegation:** Single event listener on parent container (see `app.js`)
- **Null checks:** Defensive programming (`if (!targetTab) return;`)
- **DOM manipulation:** `querySelector()`, `classList` for interactivity
- **No frameworks:** Pure DOM APIs only
- **Clipboard API:** `navigator.clipboard.writeText()` for copy-to-clipboard functionality with visual feedback

---

## Library Structure (Core Content)

The library is organized by **methodology → role → level → prompts**:

```
CRISP Methodology
├── Role 1: EAs
│   ├── Entry Level (basic guidelines + 3 prompts)
│   ├── Intermediate (enhanced techniques + 3 prompts)
│   └── Advanced (expert patterns + 3 prompts)
├── Role 2: Engineers
│   └── [same structure...]
└── ... 7 roles total

CRISPE & COSTAR (similar structure)
```

**Adding new library content:**
1. Insert new `<div class="tab-content" id="[role-abbreviation]">` in library.html
2. Add corresponding `<div class="nav-item" data-tab="[role-abbreviation]">` in sidebar
3. Follow existing structure: methodology header → role intro → three level sections with prompt examples
4. Use `.sec-section` divs for each level (Entry/Intermediate/Advanced)
5. Maintain consistent date format in headers: `Month DD, YYYY`

---

## Security & Non-Functional Requirements

**This is a security-first site.** All design decisions reflect defense-in-depth:
- **No external CDNs, trackers, or scripts** — everything is self-hosted
- **Strict Content-Security-Policy:** Inline script `nonce` attributes required in production
- **No eval() or dynamic code execution** — app.js defers-loaded and linted
- **HTTPS/HSTS enforced** — security headers in all pages
- **No external APIs** — LinkedIn links are navigation only, no data collection

When adding features:
- **Never add external dependencies** without explicit consideration of security implications
- **Never inline script content** without nonce (CSP violation)
- **Test responsive design** at 768px breakpoint minimum

---

## Common Development Tasks

### Adding a New Prompt/Entry to Library
1. Navigate to relevant role in library.html
2. Find target level section (Entry/Intermediate/Advanced)
3. Add new `<div class="prompt-item">` following existing format:
   ```html
   <div class="prompt-item">
     <h4>Prompt Title</h4>
     <p class="prompt-text">Your prompt content...</p>
   </div>
   ```

### Updating Security Page
- Edit `<section id="security">` in security.html
- Update date stamps and explanations
- Ensure CSP headers are documented accurately

### Styling Changes
- Modify styles.css using existing color variables and breakpoints
- Test at `@media (max-width: 768px)` for mobile responsiveness
- Keep `.text-red` (#D71920), `.text-green`, `.text-white` utilities consistent

### Adding Icons
- Place SVG in `Icons/SVG/[descriptive-name].svg`
- Reference: `<img src="Icons/SVG/[descriptive-name].svg" alt="description" />`
- Ensure SVGs follow security-first principles (no embedded scripts)

---

## Known Issues & Fixes (January 22, 2026)

### Critical Issue Fixed
**styles.css was incomplete** — Only contained security page styles (48 lines). Complete stylesheet rebuilt with:
- ✓ Full sidebar navigation styling
- ✓ Hero section layout for index.html
- ✓ All library page components (tabs, grids, example blocks)
- ✓ Mobile responsive design (@media 768px)
- ✓ All utility classes and color system
- ✓ Framework grid layouts (cols-5, cols-6)
- ✓ Level headers and prompts styling
- ✓ Security page styles (preserved)

### Responsive Design Implementation
- Mobile breakpoint: `@media (max-width: 768px)`
- Sidebar converts to horizontal on mobile with dropdown nav
- Hero section stacks vertically on mobile
- Framework grids convert to single-column on mobile
- All text sizes reduce appropriately for small screens
- Edge navigation repositions to bottom on mobile

---

## Debugging Tips

**Tab navigation not working?**
- Check `data-tab` attribute matches tab-content `id` exactly
- Ensure corresponding nav-item exists in sidebar
- Verify `app.js` event listener is attached to sidebar container

**Styling not applying?**
- Check class names use kebab-case
- Verify media query breakpoint: `@media (max-width: 768px)`
- Clear browser cache and reload
- Ensure styles.css is fully loaded (should be ~600+ lines)

**Copy-to-clipboard not working?**
- Confirm `navigator.clipboard` is available (requires HTTPS in production)
- Check console for CSP violations
- Ensure text node exists in DOM when copy triggered

**Mobile display issues?**
- Test at 768px viewport width (primary breakpoint)
- Sidebar should reflow to horizontal row on mobile
- Navigation becomes hidden until toggled on small screens
- Hero section should stack vertically, not side-by-side
