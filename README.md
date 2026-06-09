# Luong Huynh Portfolio — AI Vibe Coding Site Build Kit

This package is a cinematic static portfolio website for Luong Huynh, designed to be managed, extended, and polished entirely via AI Vibe Coding.

## What is included

```txt
.
├── front-end/               # Active frontend directory for AI Vibe Coding
│   ├── index.html           # Homepage
│   ├── portfolio.html       # Portfolio list page with filters
│   ├── about.html           # About page
│   ├── project-detail.html  # Project detail page
│   └── assets/              # CSS, JS, and image placeholders
├── .claude/
│   ├── commands/build-luong-portfolio.md
│   └── skills/luong-portfolio-frontend/SKILL.md
├── CLAUDE.md
├── SKILL.md
├── elementor/               # Legacy backup (not in active use)
│   ├── README.md
│   ├── global-css.css
│   ├── section-map.md
│   └── html-widget-snippets.html
├── prompts/
│   ├── claude-code-full-build.md
│   └── claude-code-review-fix.md
└── references/
    └── current-site-audit.md
```

## How to preview locally

Run the preview server from the root directory:

```bash
npm run preview
```

Or run Python's built-in HTTP server serving from the `front-end` directory:

```bash
python -m http.server 5173 -d front-end
```

Open:

```txt
http://localhost:5173
```

## Recommended workflow (AI Vibe Coding)

1. Open this folder in your AI editor (Cursor, Windsurf) or run your AI agent (Claude Code, Antigravity).
2. Prompt the AI assistant to add features, adjust designs, or update projects inside the `front-end/` folder.
3. Preview changes locally.
4. Run validation checks to ensure no broken paths:
   ```bash
   npm run check:paths
   ```

## AI Vibe Coding Guidelines

- Keep all active front-end files under the `front-end/` directory.
- Maintain global styles in `front-end/assets/css/styles.css` using the `lh-` namespace prefix.
- Keep vanilla JS interactions minimal in `front-end/assets/js/main.js`.
- Do not make updates to the `elementor/` directory, as it is now treated as a legacy backup.
