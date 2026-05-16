# Claude Code Prompt — Build Full Reviewable Luong Huynh Portfolio Website

You are inside the `luong-portfolio-claude-code-fullsite` project folder.

Read these files first:
- `CLAUDE.md`
- `SKILL.md`
- `references/current-site-audit.md`
- `index.html`
- `portfolio.html`
- `about.html`
- `assets/css/styles.css`
- `assets/js/main.js`
- `elementor/section-map.md`

## Task

Turn this into a complete, premium, reviewable static portfolio website for Luong Huynh.

This is not only a design system. I need a full coded website that I can open locally, review in browser, approve visually, then rebuild into Elementor.

## Requirements

### Pages

Build/refine:

1. Homepage
   - Cinematic hero
   - Clear positioning: "Digital Artist specializing in 3D, AI-generated Art, and VFX"
   - Location/year: "Ho Chi Minh / 2026"
   - Featured works: Stride Beyond, Nexora, BT Studio – CGI Beverage Demo
   - Services preview
   - CTA: Available for Work / Get in Touch

2. Portfolio
   - Full card grid
   - Filters: All, 3D Model, AI Generated, Branding, CGI, Feature, Film, Key Visuals, TVC, Web Design
   - Use current project names from the audit
   - Use clean project cards and placeholders until real images are supplied

3. About
   - Replace "Fullstack Developer" with: "Digital Artist & Visual Technologist"
   - Keep the actual creative positioning around 3D, AI-generated images and VFX
   - Replace template services with visual-art services
   - Add concise process/approach section

### Technical

- Static HTML/CSS/JS only.
- No React.
- No build system required.
- Keep `python -m http.server 5173` preview working.
- Use only local assets.
- Keep the class prefix `lh-`.
- Make all sections easy to rebuild in Elementor Containers.
- CSS should live in `assets/css/styles.css`.
- JS should live in `assets/js/main.js`.
- Portfolio filter should work with vanilla JS.
- Mobile menu should work.
- Make it responsive.
- Avoid generic AI-looking design.

### Elementor handoff

After updating the static site, update:
- `elementor/global-css.css`
- `elementor/section-map.md`
- `elementor/html-widget-snippets.html`

The Elementor folder must explain:
- what Elementor widget/container to use per section
- which CSS class to assign
- which content/image to replace
- where optional HTML widget snippets are useful

## QA before finishing

Check:
- no broken local file references
- all pages link to each other
- mobile layout is usable
- no "Fullstack Developer" text remains
- services are aligned with 3D/AI/VFX
- portfolio filters work
- Elementor handoff matches actual classes used in HTML/CSS

At the end, summarize:
1. What files changed.
2. How to preview.
3. What images/content I need to replace before Elementor rebuild.
