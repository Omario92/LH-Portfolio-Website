# Elementor Section Map — Luong Huynh Portfolio

Use this map when rebuilding the static site inside Elementor.
Each static section maps to an Elementor Container + widget set.
Add CSS classes via **Advanced → CSS Classes** (no leading dot).

---

## Global setup

| Step | Action |
|---|---|
| 1 | Paste `elementor/global-css.css` into **Elementor Pro → Site Settings → Custom CSS** |
| 2 | Set body font to **Inter** in **Site Settings → Typography** |
| 3 | Add `@font-face` for Newake into the Custom CSS block (already included in global-css.css) |
| 4 | Set page background color to `#070707` in **Site Settings → Layout** |

---

## Homepage (index.html)

### Section 1 — Header (Global)
- **Type:** Elementor Header template (Sticky)
- **CSS class on section:** `lh-header`
- **Inner container:** `lh-nav`
- **Widgets:**
  - Logo text widget → class `lh-brand` + inner mark span → `lh-brand-mark`
  - Nav menu widget → class `lh-menu`
  - Button widget → class `lh-nav-cta` (text: "Available for Work")

### Section 2 — Hero
- **Type:** Elementor Container (full-width, min-height 92vh)
- **CSS class:** `lh-hero`
- **Alignment:** content aligned to bottom (flex align-items: end)
- **Inner container:** no extra class needed
- **Widgets (top to bottom):**
  1. Text widget → class `lh-eyebrow` (text: "Ho Chi Minh City · 2026")
  2. Heading widget → class `lh-hero-title` (H1: "CINEMATIC DIGITAL ART")
  3. Text widget → class `lh-hero-copy`
  4. Button group container → class `lh-hero-actions`
     - Button → `lh-button lh-button-primary` (View Portfolio)
     - Button → `lh-button` (About Luong)

### Section 3 — Featured Work
- **Type:** Container
- **CSS class:** `lh-section`
- **Inner widgets:**
  1. Section header container → `lh-section-head`
     - Text → `lh-section-kicker`
     - Heading → `lh-section-title`
     - Text → `lh-section-copy`
  2. Work grid container → `lh-work-grid`
     - For each card: Container → `lh-work-card`
       - Image widget → inside `lh-work-media`
       - Inner container → `lh-work-info`
         - Tag row → `lh-tag-row` with span → `lh-tag`
         - Heading → `lh-work-title`
         - Text → (body copy)

### Section 4 — Services / Capabilities
- **Type:** Container
- **CSS class:** `lh-section lh-section-muted`
- **Inner:**
  - Section header → `lh-section-head`
  - Grid container → `lh-service-grid` (or `lh-capabilities`)
    - Each cell: Container → `lh-service-card` (or `lh-capability-card`)
      - Text → `lh-service-number`
      - Heading → `lh-service-title`
      - Text → `lh-service-copy`

### Section 5 — Contact CTA
- **Type:** Container
- **CSS class:** `lh-section`
- **Inner container:** `lh-cta` (or `lh-footer-cta`)
- **Widgets:**
  - Text → `lh-section-kicker`
  - Heading → (H2, Newake display)
  - Text → body copy
  - Button group → `lh-hero-actions`

### Section 6 — Footer (Global)
- **Type:** Elementor Footer template
- **CSS class:** `lh-footer`
- **Inner container:** `lh-footer-grid`
- **Widgets:**
  - Text (copyright) → left
  - Nav or text links → `lh-socials`

---

## Portfolio page (portfolio.html)

### Section 1 — Header (Global, same as homepage)

### Section 2 — Portfolio Header + Filter
- **Type:** Container
- **CSS class:** `lh-section`
- **Widgets:**
  - Section head → `lh-section-head`
  - Filter bar → `lh-filter-bar` (or `lh-filter-row`)
    - Each button → `lh-filter-btn` (or `lh-filter-pill`) with `data-filter` attribute
  - Work grid → `lh-work-grid`
    - 13 project cards, same structure as homepage work cards
- **Note:** Portfolio filter JS must be embedded or added via Elementor HTML widget

### Section 3 — Inquiry CTA
- **CSS class:** `lh-section-tight`
- **Inner:** `lh-cta`

---

## About page (about.html)

### Section 1 — Header (Global)

### Section 2 — About Grid
- **Type:** Container (two-column on desktop)
- **CSS class:** `lh-section`
- **Left column:** `lh-portrait-panel` (sticky top: 90px)
  - Image → `lh-portrait`
  - Caption container → `lh-hero-card-caption`
    - Tags → `lh-meta-row` with `lh-chip` / `lh-chip-strong`
- **Right column:** `lh-rich-text`
  - Text → `lh-eyebrow`
  - Heading → H1 (Newake display)
  - Paragraphs → body copy
  - List container → `lh-list`
    - Each row: two-column inner (label + content)

### Section 3 — Services (same structure as homepage services)

### Section 4 — Contact CTA + Footer

---

## Notes for Elementor implementation

- **Never use Elementor-generated IDs** in custom CSS — they change on every edit.
- **Newake is uppercase-only** in the demo OTF. All `h1/h2` text set in Newake will render in caps automatically — write in any case, CSS applies `text-transform: uppercase`.
- **Card titles** (`lh-work-title`, `lh-service-title`) use Inter Tight — set `text-transform: none` to override Elementor's heading defaults.
- **Portfolio filter** requires JavaScript — use the Elementor HTML Widget to embed the filter bar and the `main.js` script, or use a custom JS plugin.
- **Work cards** need `data-categories` attributes for JS filtering — use an HTML Widget per card if using the filter script.
