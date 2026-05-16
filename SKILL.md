# SKILL.md — Luong Portfolio Website Builder

## Purpose

Use this skill when building, reviewing, or converting the Luong Huynh portfolio website.

The output should be a complete static website that can be reviewed in-browser, then rebuilt in Elementor using mapped sections, classes and global CSS.

## Inputs

- Current website audit in `references/current-site-audit.md`
- Existing project names from the current portfolio
- User preference: Claude Design can be used for visual exploration, but Claude Code must code the full site for review
- Final implementation target: Elementor

## Required output

1. Full static review website:
   - `index.html`
   - `portfolio.html`
   - `about.html`
   - `assets/css/styles.css`
   - `assets/js/main.js`

2. Elementor handoff:
   - `elementor/global-css.css`
   - `elementor/section-map.md`
   - `elementor/html-widget-snippets.html`

3. Clear README:
   - local preview command
   - Claude Code workflow
   - Elementor rebuild workflow
   - content replacement notes

## Design rules

- Make the website look like a premium digital artist / VFX portfolio.
- Do not make it look like a generic developer portfolio, SaaS landing page, or Elementor template.
- Use large media-first sections.
- Use a dark cinematic background.
- Keep copy short, confident and portfolio-oriented.
- Use `lh-` prefix for all project-specific classes.

## Elementor rules

- Every major section must map to an Elementor Container.
- Avoid styling native tags globally unless necessary.
- Prefer reusable classes over inline styles.
- Avoid JS-dependent functionality that Elementor cannot reproduce.
- Portfolio filtering can be rebuilt using Elementor Loop Grid, taxonomy filters, or a filterable gallery plugin.

## Quality bar

The website should feel:
- polished
- cinematic
- editorial
- brand-campaign oriented
- easy to translate into Elementor
