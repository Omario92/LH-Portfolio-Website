# Luong Huynh Portfolio — Claude Code Full-Site Build Kit

This package is not just a design system. It is a reviewable static website scaffold plus a Claude Code workflow for turning the current luonghuynh.com portfolio into a stronger Elementor-ready site.

## What is included

```txt
.
├── index.html
├── portfolio.html
├── about.html
├── assets/
│   ├── css/styles.css
│   ├── js/main.js
│   └── img/placeholders/*.svg
├── .claude/
│   ├── commands/build-luong-portfolio.md
│   └── skills/luong-portfolio-frontend/SKILL.md
├── CLAUDE.md
├── SKILL.md
├── elementor/
│   ├── README.md
│   ├── global-css.css
│   ├── section-map.md
│   └── html-widget-snippets.html
├── prompts/
│   ├── claude-code-full-build.md
│   ├── claude-code-review-fix.md
│   └── elementor-conversion.md
└── references/
    └── current-site-audit.md
```

## How to preview locally

```bash
cd luong-portfolio-claude-code-fullsite
python -m http.server 5173
```

Open:

```txt
http://localhost:5173
```

Optional Node command:

```bash
npm run preview
```

## Recommended workflow

1. Put this folder into a local project.
2. Open Claude Code in this folder.
3. Paste `prompts/claude-code-full-build.md`.
4. Let Claude Code refine the full website.
5. Preview locally.
6. Paste `prompts/claude-code-review-fix.md` for QA and polish.
7. Use `elementor/section-map.md` and `elementor/global-css.css` to rebuild the final direction inside Elementor.

## Elementor migration principle

Do not paste the entire static HTML into Elementor as one block. Instead:

- Rebuild layout with Elementor Containers.
- Use the class names in `elementor/section-map.md`.
- Copy `elementor/global-css.css` into Site Settings > Custom CSS.
- Replace placeholder SVGs with real project images/video thumbnails from Media Library.
- Use Elementor Loop Grid or Posts widget for portfolio cards if project data will be dynamic.
