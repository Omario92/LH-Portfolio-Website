# CLAUDE.md — Project Instructions for Claude Code

You are building a portfolio website for Luong Huynh.

## Goal

Create a premium, cinematic, responsive portfolio website that can be reviewed as static HTML/CSS/JS first, then rebuilt inside Elementor.

## Brand positioning

Luong Huynh is a Digital Artist specializing in:
- 3D visuals
- AI-generated art
- VFX
- CGI product visuals
- Campaign key visuals
- Visual direction for brands and agencies

Avoid positioning him as a fullstack developer or generic website agency.

## Current website audit

Use `references/current-site-audit.md` as source material.

Core current-site content:
- Homepage nav: Homepage / Portfolio / About
- Homepage hero: Luong Huynh
- Positioning: Digital Artist specializing in 3D, AI-generated Art, and VFX
- Location/year: Ho Chi Minh / 2026
- Featured works: Stride Beyond, Nexora, BT Studio – CGI Beverage Demo
- Portfolio filters: 3D Model, AI Generated, Branding, CGI, Feature, Film, Key Visuals, TVC, Web Design
- Footer/socials: Behance, Dribbble, Instagram, LinkedIn
- About page mismatch: currently says Fullstack Developer and web-agency services; fix this.

## Technical constraints

- Keep it static and easy to preview.
- Use semantic HTML.
- Use one global CSS file: `assets/css/styles.css`.
- Use minimal vanilla JS in `assets/js/main.js`.
- No external dependencies unless explicitly requested.
- Avoid framework lock-in. The final output must be easy to translate into Elementor Containers.
- Maintain a consistent `lh-` CSS class prefix.
- Include responsive behavior for mobile, tablet, desktop.
- Do not use placeholder lorem ipsum. Use real portfolio-oriented copy.

## Visual direction

Premium cinematic dark interface:
- Black / charcoal base
- Soft grid or glow atmosphere
- Large editorial typography
- High-impact visual cards
- Round, glass-like panels
- Subtle motion only, no gimmicky animation
- Make project images dominant

## Deliverables

Maintain or produce:
- `index.html`
- `portfolio.html`
- `about.html`
- `assets/css/styles.css`
- `assets/js/main.js`
- `elementor/global-css.css`
- `elementor/section-map.md`
- `elementor/html-widget-snippets.html`
- `README.md`

## QA checklist

Before finalizing:
- All pages load locally.
- Navigation works.
- Portfolio filters work.
- Mobile menu works.
- Text does not mention Fullstack Developer.
- Services are visual-art services, not eCommerce/web maintenance services.
- CSS class names are suitable for Elementor Advanced > CSS Classes.
- No broken local paths.
