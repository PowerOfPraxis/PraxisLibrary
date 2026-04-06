# BuiltByBas Quality Framework - Design Specification

**Date:** 2026-04-06
**Author:** Bas Rosario & Claude
**Status:** Draft - Awaiting Review
**Scope:** Universal (all BuiltByBas projects), implemented first in PraxisLibrary #ClaudeNBasWhereHere

---

## 1. Purpose

Every project that ships under the BuiltByBas name carries the Rosario family name. This framework defines the quality standard that protects it.

The BuiltByBas Quality Framework is a 13-pillar quality standard enforced by automated audit tooling across every project in the portfolio. It covers code quality, operational readiness, inclusive design, and disaster recovery. No project deploys without passing all 13 pillars with 0 errors.

**Core principle:** 0 errors = pass. No exceptions. No rationalizing.

---

## 2. The 13 Pillars

### 2.1 Security

**What it protects:** Users, data, and the business from vulnerabilities.

**Checks:**
- A+ CSP compliance: no inline styles, no inline scripts, no inline event handlers
- No external CDN or third-party resource loading
- No dangerous JS patterns: eval(), new Function(), document.write(), string setTimeout/setInterval
- External links have `rel="noopener noreferrer"` on `target="_blank"`
- No secrets, API keys, or credentials in source code
- No exposed internal error messages in user-facing content
- OWASP Top 10 awareness in all dynamic projects

**Standards:** CSP A+, OWASP Top 10

---

### 2.2 Performance

**What it protects:** User experience, SEO, bandwidth, device respect.

**Checks:**
- Single CSS file, single JS file (no render-blocking extras)
- Script tags use `defer` attribute
- Images under size threshold (warn >500KB per image, error >1MB)
- Total page weight monitoring (HTML + linked resources)
- No base64-encoded large assets inline in HTML
- Lazy loading on below-fold images (`loading="lazy"`)
- No unused external font loading

**Standards:** Lighthouse 100, Core Web Vitals targets

---

### 2.3 Readability

**What it protects:** Developer onboarding, code review speed, long-term comprehension.

**Checks (absorbs Template Compliance, Content Readiness, Source Verification):**
- Consistent page template structure across all HTML files
- Required meta tags present (description, viewport, charset, OG, Twitter)
- Favicon linked on every page
- Breadcrumb navigation on all interior pages
- SEO meta block present
- No placeholder content (TODO, TBD, FIXME, lorem ipsum, WIP)
- All citations verified and accessible
- Bot-blocked URLs have screenshot evidence in verified-items.json
- Code notation standards followed (HTML/CSS/JS section markers)

**Standards:** Google SEO, internal notation standards

---

### 2.4 Maintainability

**What it protects:** Future sessions, handoff quality, documentation accuracy.

**Checks (absorbs Content Consistency, Documentation):**
- Homepage counters match actual file/tool/term counts
- Glossary term counts consistent across all display locations
- HANDOFF.md exists and file counts match reality
- CLAUDE.md exists with project-specific instructions
- AUDIT.md exists with issue tracking
- ProjectHealth.md exists with health scores
- No stale session references in governance docs (gap > 5 sessions flagged)
- Comparison panels structurally complete
- No deprecated component classes in use
- Footer tool counts match discovered active tools

**Standards:** Internal governance protocol

---

### 2.5 Accessibility

**What it protects:** Every user regardless of ability, device, or context.

**Checks:**
- All images have alt text (descriptive or empty for decorative)
- Color contrast ratio 4.5:1 minimum for all text
- All interactive elements keyboard-accessible
- Visible focus indicators (no bare `outline: none`)
- Semantic HTML: proper heading hierarchy, no skipped levels
- ARIA attributes valid where used
- Touch targets 44x44px minimum on mobile
- `prefers-reduced-motion` respected in animations
- Anchor links use `scroll-margin-top` for sticky header clearance
- Skip-to-content link present
- Language attribute on `<html>` tag
- Form inputs have associated labels

**Standards:** WCAG 2.1 AA

---

### 2.6 Modularity

**What it protects:** Separation of concerns, independent changeability, cognitive load.

**Checks (absorbs and extends Site Architecture):**
- Clean directory structure: content pages, data files, assets, tools in proper directories
- No HTML files in root except index.html
- Data files organized by domain in data/ directory
- Learn pages follow consistent section structure (hero, concept, how-it-works, examples, when-to-use, CTA)
- Framework template completeness validated
- Navigation structure consistent (mega-menu, sidebar) across all pages
- ADL (Accessibility Dashboard) panel present on every page
- Badge lightbox component present on every page
- Back-to-top bar present on every page
- Ethics ticker present and functional

**Standards:** Single-responsibility principle, separation of concerns

---

### 2.7 Redundancy

**What it protects:** Business continuity, disaster recovery readiness.

**Checks:**
- Project is a git repository (.git/ exists)
- .gitignore exists and is non-empty
- Remote origin configured (code is not only local)
- All 4 governance files present (CLAUDE.md, HANDOFF.md, AUDIT.md, ProjectHealth.md)
- Deployment documentation exists (how to rebuild from scratch)
- VPS infrastructure documented (ports, services, configs)
- No single-source assets (everything reproducible from git)

**Standards:** 3-2-1 backup principle (3 copies, 2 media, 1 offsite)

---

### 2.8 Recovery

**What it protects:** Time-to-live after any failure scenario.

**Checks:**
- Git working tree is clean (no uncommitted changes in production)
- Git tags exist for known-good states
- PM2 ecosystem file exists (Node.js projects)
- Rollback procedure documented
- Last commit is not a work-in-progress
- No merge conflicts present
- Deploy script or documented deploy steps exist

**Recovery targets:**
| Scenario | Target |
|---|---|
| Bad deploy | < 2 minutes (git checkout tag, rebuild, restart) |
| VPS reboot | < 5 minutes (PM2 auto-restart) |
| VPS failure | < 1 hour (fresh VPS, deploy from git) |
| Full catastrophe | < 4 hours (new VPS, new DNS, full redeploy) |

**Standards:** RTO/RPO targets documented per project

---

### 2.9 Inclusive Design

**What it protects:** Every person's dignity, safety, and sense of belonging.

**Checks (absorbs Bias/Inclusivity):**
- Gender-neutral language by default (they/them, partner, humankind)
- No gendered assumptions in examples or templates
- No cultural or demographic assumptions
- No profanity or informal abbreviations
- Zero-tolerance slur detection (racial, homophobic, ableist)
- AI ethics disclosure where applicable
- Diverse representation in examples and personas
- Neurodivergent-friendly formatting (scannable, hierarchical, visual structure)
- LGBTQA+ inclusive language

**Standards:** Internal inclusive design policy, APA inclusive language guidelines

---

### 2.10 Cohesion

**What it protects:** Code organization, predictability, developer mental model.

**Checks:**
- Single CSS file pattern maintained (all styles in styles.css)
- Single JS file pattern maintained (all behavior in app.js)
- No scattered script or style files outside the main files
- Data files co-located by domain (glossary together, quiz together)
- Related HTML pages in proper subdirectories (learn/, pages/, tools/)
- Consistent footer across all pages (quote, links, badges)
- Consistent header/navigation across all pages
- No orphan pages (every page reachable from navigation)

**Standards:** High cohesion, low coupling principle

---

### 2.11 Efficiency

**What it protects:** Codebase health, build times, cognitive overhead.

**Checks:**
- No duplicate HTML `id` attributes within any file
- No empty content files (0-byte HTML)
- Search index valid (exists, non-empty, all entries have title + url)
- No duplicate entries in glossary data files
- No orphan data files (JSON files not referenced by any HTML/JS)
- CSS: no obviously duplicate selectors (basic pattern detection)
- No dead internal links (links to pages that don't exist)

**Standards:** DRY principle, zero dead code tolerance

---

### 2.12 Longevity

**What it protects:** The project from dying when a dependency or service dies.

**Checks:**
- No external CDN dependencies (already in Security, reinforced here)
- No external API calls required for core functionality
- No deprecated HTML elements or attributes (marquee, blink, font, center)
- No vendor-prefixed CSS without standard property fallback
- All assets self-hosted (fonts, icons, images)
- No reliance on third-party services for core content delivery
- Standard, semantic HTML5 elements used throughout
- No framework-specific markup that requires a build step to render
- Content readable without JavaScript (progressive enhancement)

**Standards:** Web standards (W3C), progressive enhancement, self-hosted everything

---

### 2.13 Reliability

**What it protects:** Consistent behavior under all conditions.

**Checks:**
- `<noscript>` fallback content present where JS drives critical UI
- No silent JS errors in core functionality (try/catch with proper handling)
- Error boundaries in dynamic applications (React/Next.js projects)
- Pino structured logging in all Node.js projects (required standard)
- Consistent HTTP status handling (404 page exists, error states handled)
- All interactive tools functional (quiz, analyzer, checklist load correctly)
- Form validation present on all input elements
- Graceful degradation: site usable on slow connections and old browsers

**Cross-project standards:**
- **Pino** for structured logging in all Node.js/server projects
- **Vitest** (or project-appropriate test runner) for automated testing
- **Error reporting:** every error surfaced, logged, and actionable, never swallowed
- **Testing throughout:** unit tests for business logic, integration tests for APIs, E2E for critical user flows

**Standards:** Pino logging, structured error handling, test coverage targets

---

## 3. Operational Readiness Plan

These plans are documented, costed, and ready to activate. No implementation cost until the business needs them.

### 3.1 Backup Strategy

| Layer | Strategy | Cost | Status |
|---|---|---|---|
| Code | Git + GitHub remote | Free | Active |
| VPS Config | Documented in vps-infrastructure.md | Free | Active |
| Database (future) | Automated daily dump to encrypted offsite (S3/Backblaze B2) | ~$1/mo | Script ready |
| Media/Assets | Git or rsync to secondary storage | Free-$5/mo | Documented |
| Secrets/Env | Never in git, encrypted backup procedure documented | Free | Documented |
| Full VPS Snapshot | Hostinger weekly + pre-deploy manual | Free (included) | Enable in panel |

### 3.2 Failover Tiers

| Tier | Strategy | Cost | Activation Trigger |
|---|---|---|---|
| Tier 0 (Now) | Known-good git tags, PM2 auto-restart, Hostinger snapshots | Free | Already available |
| Tier 1 (Revenue) | Health monitoring (UptimeRobot/Uptime Kuma), alerting | Free-$7/mo | Clients depend on uptime |
| Tier 2 (Critical) | Warm standby VPS, synced via git pull cron | ~$10/mo | Downtime costs money |
| Tier 3 (Enterprise) | Load balancer, 2 active instances, CDN edge, automated failover | ~$50-100/mo | Contractual SLA |

### 3.3 Recovery Checklist

```
1. Bad deploy?        -> git checkout <known-good-tag>, rebuild, restart  [< 2 min]
2. PM2 crashed?       -> pm2 resurrect or pm2 start ecosystem            [< 1 min]
3. VPS responsive?    -> SSH in, check disk/memory/processes             [< 5 min]
4. VPS dead?          -> Hostinger restore from snapshot                 [< 30 min]
5. Hostinger down?    -> Spin new VPS elsewhere, deploy from git         [< 1 hour]
6. DNS broken?        -> Cloudflare dashboard, verify A records          [< 10 min]
7. Everything gone?   -> Git has code, docs have config, rebuild         [< 4 hours]
```

---

## 4. Audit Implementation

### 4.1 Approach

Regroup the existing 11 audit categories in PraxisLibraryAudit.py into the 13 BuiltByBas pillars. Existing checks redistribute into their pillar. New checks fill gaps.

### 4.2 Category Mapping (Old to New)

| Old Category | New Pillar | Action |
|---|---|---|
| Security | Security | Keep, pillar 1 |
| Template Compliance | Readability | Merge into pillar 3 |
| Link Integrity | Readability | Merge into pillar 3 |
| Content Readiness | Readability | Merge into pillar 3 |
| Content Consistency | Maintainability | Merge into pillar 4 |
| Bias/Inclusivity | Inclusive Design | Rename, pillar 9 |
| Accessibility | Accessibility | Keep, pillar 5 |
| Source Verification | Readability | Merge into pillar 3 |
| Data Integrity | Efficiency | Merge into pillar 11 |
| Site Architecture | Modularity | Rename/extend, pillar 6 |
| Documentation | Maintainability | Merge into pillar 4 |

### 4.3 New Checkers to Build

| Pillar | Checker Class | Estimated Checks |
|---|---|---|
| Performance | PerformanceChecker | 7 checks |
| Redundancy | RedundancyChecker | 7 checks |
| Recovery | RecoveryChecker | 7 checks |
| Cohesion | CohesionChecker | 8 checks |
| Efficiency | EfficiencyChecker (extends DataAccuracyChecker) | 7 checks |
| Longevity | LongevityChecker | 9 checks |
| Reliability | ReliabilityChecker | 8 checks |

### 4.4 Merged Checkers to Refactor

| Pillar | New Class | Absorbs |
|---|---|---|
| Readability | ReadabilityChecker | ContinuityChecker + BrokenLinksChecker + RelevancyChecker + CitationChecker |
| Maintainability | MaintainabilityChecker | AccuracyChecker + DocumentationChecker |
| Modularity | ModularityChecker | StructuralChecker (extended) |
| Inclusive Design | InclusiveDesignChecker | BiasInclusivityChecker (renamed) |

### 4.5 Report Format

The audit report header will include:

```
============================================================
  BUILTBYBAS QUALITY FRAMEWORK AUDIT
  13 Pillars | 0 Errors = Pass | No Exceptions
============================================================
```

Each pillar reports: PASS/FAIL, error count, warning count, info count.

Overall score: 10.0 scale (current formula: -0.5 per unique error type, -0.1 per unique warning type).

### 4.6 Integrity Cascades

- If Security fails, Longevity and Reliability also fail (security is foundational)
- If Readability fails, Maintainability gets a warning (unreadable code is harder to maintain)
- If Recovery fails, Redundancy gets a warning (recovery depends on redundancy artifacts)

---

## 5. Global Knowledge Base Updates

### 5.1 New Global Files

| File | Content |
|---|---|
| `~/.claude/docs/builtbybas-quality-framework.md` | The 13 pillars, universal rules, pillar definitions |
| `~/.claude/docs/operational-readiness-plan.md` | Backup, failover, DR plans, recovery checklist |

### 5.2 Files to Update

| File | Change |
|---|---|
| `~/.claude/CLAUDE.md` | Add BuiltByBas Quality Framework reference under Eight Pillars |
| `~/.claude/docs/project-registry.md` | Add quality framework compliance status per project |
| `~/.claude/docs/working-patterns.md` | Add framework enforcement as session protocol |
| Each project's CLAUDE.md | Reference the framework, declare project-specific gates |
| Each project's AUDIT.md | Track framework compliance history |

---

## 6. Cross-Project Standards

These apply to ALL BuiltByBas projects regardless of stack:

| Standard | Applies To | Requirement |
|---|---|---|
| Pino structured logging | All Node.js projects | Required, no alternatives |
| Vitest/test runner | All projects with logic | Required, coverage targets per project |
| Error surfacing | All projects | Every error logged and actionable, never swallowed |
| Git governance | All projects | CLAUDE.md, HANDOFF.md, AUDIT.md, ProjectHealth.md |
| 0 errors = pass | All projects | No deploy without clean audit |
| Self-hosted assets | All projects | No CDN, no external fonts, no third-party core dependencies |
| Progressive enhancement | All web projects | Content accessible without JS |
| Inclusive language | All projects | Gender-neutral, bias-free, neurodivergent-friendly |

---

## 7. Success Criteria

The framework is complete when:

1. All 13 pillar checkers are implemented in the audit tool
2. PraxisLibrary passes all 13 pillars with 0 errors
3. Global framework doc exists at `~/.claude/docs/builtbybas-quality-framework.md`
4. Operational readiness plan exists at `~/.claude/docs/operational-readiness-plan.md`
5. Every project's CLAUDE.md references the framework
6. The audit report header says "BuiltByBas Quality Framework" not "Comprehensive Site Audit"
