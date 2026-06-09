# CLAUDE.md — Project Instructions for Claude Code

You are building a portfolio website for Luong Huynh.

## Goal

Create a premium, cinematic, responsive portfolio website using static HTML/CSS/JS, optimized for maintainability via AI Vibe Coding.

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

- Keep it static and easy to preview in `front-end/`.
- Use semantic HTML.
- Use one global CSS file: `front-end/assets/css/styles.css`.
- Use minimal vanilla JS in `front-end/assets/js/main.js`.
- No external dependencies unless explicitly requested.
- Avoid framework lock-in. Focus on lightweight, clean, semantic HTML/CSS structures.
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
- `front-end/index.html`
- `front-end/portfolio.html`
- `front-end/about.html`
- `front-end/project-detail.html`
- `front-end/assets/css/styles.css`
- `front-end/assets/js/main.js`
- `README.md`

## QA checklist

Before finalizing:
- All pages load locally under the `front-end` directory.
- Navigation works.
- Portfolio filters work.
- Mobile menu works.
- Text does not mention Fullstack Developer.
- Services are visual-art services, not eCommerce/web maintenance services.
- No broken local paths inside `front-end/`.
