# Elementor Class Map — Luong Huynh Portfolio

All classes use the `lh-` prefix. Add via **Advanced → CSS Classes** (no leading dot).
Copy `:root` tokens + all rules from `elementor/global-css.css` into Elementor Site Settings → Custom CSS.

---

## Layout classes

| Class | Apply to | Effect |
|---|---|---|
| `lh-site` | Body / page wrapper | Sets `background: #070707`, `color: #f4f0e8` |
| `lh-section` | Elementor Section container | `padding-block: clamp(72px, 10vw, 160px)` |
| `lh-section-tight` | Elementor Section container | `padding-block: clamp(48px, 7vw, 96px)` |
| `lh-section-muted` | Elementor Section container | Soft dark bg + faint cyan glow top-left |
| `lh-container` | Inner container | `width: min(100vw - gutter, 1440px); margin: auto` |

---

## Header & nav

| Class | Apply to | Effect |
|---|---|---|
| `lh-header` | Elementor Header section | Sticky, `rgba(7,7,7,0.90)` bg, hairline border |
| `lh-nav` | Inner container of header | Flex row, space-between, min-height 72px |
| `lh-brand` | Logo widget | Newake font, uppercase, flex row with mark |
| `lh-brand-mark` | Logo monogram span | Cyan circle, 30×30px |
| `lh-menu` | Nav menu widget | Flex row, uppercase Inter 11px, 0.14em tracking |
| `lh-nav-cta` | "Available for Work" button | Pill border, cyan dot `::before`, uppercase |
| `lh-mobile-toggle` | Mobile hamburger button | Hidden above 767px, pill border |

---

## Hero

| Class | Apply to | Effect |
|---|---|---|
| `lh-hero` | Hero section container | Min 92vh, bottom-aligned, radial cyan+indigo washes |
| `lh-hero-body` | Inner content wrapper | `max-width: 1100px` |
| `lh-hero-title` | H1 heading widget | Newake, `clamp(64px, 14vw, 200px)`, tracking 0.10em |
| `lh-hero-copy` | Subtitle text widget | `clamp(18px, 2vw, 26px)`, warm ivory 82% opacity |
| `lh-hero-actions` | Button row container | Flex, wrap, gap 14px |
| `lh-eyebrow` | Location/year text | Inter 11–13px, cyan, 0.16em tracking, uppercase |

---

## Buttons

| Class | Apply to | Effect |
|---|---|---|
| `lh-button` | Any button widget | Pill, transparent, ivory border, uppercase Inter 800 |
| `lh-button-primary` | Primary CTA button | Neon cyan fill → hover: warm ivory fill |
| `lh-button-secondary` | Secondary button | Transparent, ivory hairline border |

---

## Section typography

| Class | Apply to | Effect |
|---|---|---|
| `lh-section-kicker` | Eyebrow/label text | Cyan, uppercase, 11–13px, 0.16em tracking |
| `lh-section-title` | Section H2 heading | Newake, `clamp(36px, 5vw, 80px)`, tracking 0.10em |
| `lh-section-copy` | Section descriptor text | Muted ivory, 16px, 1.65 line-height |
| `lh-section-head` | Heading + copy wrapper | 2-col grid (title left, copy right), collapses 1-col tablet |

---

## Work cards

| Class | Apply to | Effect |
|---|---|---|
| `lh-work-grid` | Card grid container | 3-col → 2-col → 1-col responsive grid |
| `lh-work-card` | Each project card | Dark panel, 32px radius, lift + border alpha on hover |
| `lh-work-media` | Image wrapper inside card | 4:5 portrait ratio, top corners match card, bottom = 20px |
| `lh-work-info` | Text area inside card | `padding: clamp(16px, 2vw, 22px)` |
| `lh-work-title` | Project title heading | Inter Tight 700, mixed-case, `-0.05em` tracking |
| `lh-tag-row` | Tag container | Flex, wrap, gap 6px, margin-bottom 12px |
| `lh-tag` | Individual tag pill | 10px Inter 700, uppercase, 0.12em tracking, hairline border |

---

## Filter bar (Portfolio page)

| Class | Apply to | Effect |
|---|---|---|
| `lh-filter-bar` | Filter button row container | Flex, wrap, gap 10px |
| `lh-filter-btn` | Each filter button | Pill, muted text; `.is-active` → cyan fill |
| `lh-filter-pill` | Alias for `lh-filter-btn` | Same styles |

**Note:** Add `data-filter="all"` / `data-filter="cgi"` etc. attributes to each button, and `data-categories="cgi branding"` to each card. JS in `assets/js/main.js` handles the filtering.

---

## Service / capability grid

| Class | Apply to | Effect |
|---|---|---|
| `lh-service-grid` | Grid wrapper | 4-col, 1px-gap grid; wrapper bg = gap color |
| `lh-capabilities` | Alias for `lh-service-grid` | Same styles |
| `lh-service-card` | Each grid cell | Soft dark bg, flex column, space-between |
| `lh-capability-card` | Alias for `lh-service-card` | Same styles |
| `lh-service-number` | Catalog number (01, 02…) | JetBrains Mono, 10px, muted |
| `lh-service-title` | Service heading | Inter Tight 700, mixed-case, 20–28px |
| `lh-service-copy` | Service description | Muted ivory, 14px |

---

## Tags & chips

| Class | Apply to | Effect |
|---|---|---|
| `lh-tag` | Project category pill | 10px, uppercase, hairline border, muted |
| `lh-chip` | Alias for `lh-tag` | Same styles |
| `lh-chip-strong` | Highlighted chip | Cyan fill, dark text |
| `lh-meta-row` | Tag/chip row container | Flex, wrap, gap 6px |

---

## CTA block

| Class | Apply to | Effect |
|---|---|---|
| `lh-cta` | CTA section inner container | 32px radius panel, cyan gradient wash, hairline border |
| `lh-footer-cta` | Alias for `lh-cta` | Same styles |

---

## About page

| Class | Apply to | Effect |
|---|---|---|
| `lh-about-grid` | About section container | 2-col grid (portrait left, text right) |
| `lh-portrait-panel` | Portrait column | Sticky, dark panel, 32px radius |
| `lh-portrait` | Portrait image | `aspect-ratio: 0.86`, cover fit |
| `lh-hero-card-caption` | Caption below portrait | Soft bg, hairline border, 12px radius |
| `lh-rich-text` | About text column | Heading + body copy |
| `lh-list` | Spec list (Focus/Clients…) | Grid, hairline top border, rows = hairline bottom |

---

## Footer

| Class | Apply to | Effect |
|---|---|---|
| `lh-footer` | Footer section | Hairline top border, muted text |
| `lh-footer-grid` | Footer inner container | Flex, space-between, wrap |
| `lh-socials` | Social links row | Flex, gap 20px; hover → ivory |

---

## Elementor-specific notes

- Set **heading widgets** used as `lh-hero-title` to H1 tag in the widget settings.
- Set **heading widgets** used as `lh-section-title` to H2.
- Set **heading widgets** used as `lh-work-title` to H3 — and override font to Inter Tight in widget Advanced CSS or via `lh-work-title` class rule.
- When nesting containers inside `lh-work-card`, ensure **overflow: hidden** is set on the outer container so border-radius clips correctly.
- The `lh-service-grid` / `lh-capabilities` 1px gap effect requires the **container background = `rgba(244,240,232,0.14)`** and each child cell background = `#101010`. Set both in Elementor → Style → Background.
