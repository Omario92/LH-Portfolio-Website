# Elementor Handoff — Luong Huynh Portfolio

This folder converts the static website into an Elementor rebuild plan.

## Recommended Elementor approach

Do not paste the entire HTML page into one Elementor HTML widget.

Use:
- Elementor Containers for section layout
- Heading widgets for titles
- Text Editor widgets for copy
- Image or Video widgets for visual media
- Button widgets for CTAs
- Loop Grid / Posts / Portfolio widget for project cards if the projects will be dynamic
- HTML widget only for small custom snippets if needed

## Global CSS

Copy:

```txt
elementor/global-css.css
```

Into:

```txt
Elementor → Site Settings → Custom CSS
```

Then assign class names from `section-map.md` to each Elementor Container or widget.

## Important

When entering CSS classes in Elementor:

```txt
lh-section lh-hero
```

Do not type:

```txt
.lh-section .lh-hero
```

## Build order

1. Site Header
2. Homepage Hero
3. Homepage Featured Work
4. Homepage Services
5. CTA/Footer
6. Portfolio Page Grid
7. About Page
8. Mobile QA
9. Replace placeholder imagery with real work
10. SEO title/meta cleanup

## Dynamic portfolio option

If using WordPress custom posts:
- Create Portfolio CPT or use Elementor Portfolio widget.
- Add taxonomy terms matching the current portfolio filters.
- Use Loop Grid for cards.
- Apply `lh-work-card`, `lh-work-media`, `lh-work-body`, `lh-tag`, `lh-work-title`.
