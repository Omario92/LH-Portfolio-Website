# Responsive Frame Specification
# Luong Huynh Portfolio — Figma Breakpoints for UiChemy

## Breakpoint Overview

| Frame Name | Width | Elementor Breakpoint | Notes |
|------------|-------|---------------------|-------|
| `Desktop` | 1440px | Desktop (≥ 1025px) | Primary design frame |
| `Laptop` | 1366px | Desktop narrow variant | Same layout as desktop |
| `Tablet` | 1024px | Tablet (768–1024px) | 2-column collapse begins |
| `Mobile` | 390px | Mobile (≤ 767px) | Single column, large type |

---

## Desktop (1440px)

### Layout rules
- Content max-width: 1440px, centered
- Horizontal padding (gutter): 72px each side
- Section vertical padding: 160px

### Typography
- Hero title: 200px (Newake, tracking 0.10em)
- H1: 140px
- H2 (section): 80px
- H3 (card): 44px
- Lead: 30px
- Body: 16px
- Eyebrow: 13px

### Grid columns
- Work grid: 3 columns, gap 28px
- Service grid: 4 columns, gap 1px
- About: 2 columns (0.78fr + 1.1fr)
- Detail body: 2 columns (sidebar + content)

### Navigation
- Full horizontal menu visible
- "Available for Work" CTA badge visible
- Mobile toggle hidden

---

## Laptop (1366px)

### Layout rules
- Same as Desktop
- Content max-width: 1366px (frame width)
- Gutter: 64px

### Typography
- Same as Desktop (clamp values handle this automatically)

### Grid columns
- Same as Desktop

### Navigation
- Same as Desktop

---

## Tablet (1024px)

### Layout rules
- Horizontal padding (gutter): 32px each side
- Section vertical padding: 120px

### Typography (Figma: use 1024px frame, override type sizes)
- Hero title: ~120px (clamp mid-point)
- H2 section: ~52px
- Lead: ~24px
- Body: 16px (unchanged)

### Grid columns
- Work grid: **2 columns**, gap 16px
- Service grid: **2 columns**, gap 1px
- Section head: **1 column** (stacked, copy below title)
- About: **1 column** (portrait panel unsticky, stacked above text)
- Detail body: **1 column**
- Filter bar: wraps across 2 rows

### Navigation
- Full horizontal menu may compress — reduce gap
- CTA badge still visible

### Figma notes
- Use Auto Layout wrap for grids
- Set portrait panel to `position: relative` (no longer sticky)
- CTA panel padding reduces to 64px

---

## Mobile (390px)

### Layout rules
- Horizontal padding (gutter): 20px each side
- Section vertical padding: 72px
- Nav height: 64px

### Typography (Figma: use 390px frame, set explicit sizes)
- Hero title: 86px (Newake, tracking 0.04em — tighter on mobile)
- H1: 72px
- H2: 48px
- H3: 28px
- Lead: 18px
- Body: 16px (unchanged)
- Eyebrow: 11px

### Grid columns
- Work grid: **1 column**
- Work card image: aspect-ratio 16/11 (wider on mobile)
- Service grid: **1 column**
- Service card: min-height 180px (reduced)
- Filter bar: wraps freely

### Navigation
- Full menu hidden
- Mobile toggle button visible (pill border)
- Menu dropdown: absolute positioned, full width, dark panel, 20px padding
- "Available for Work" CTA badge hidden

### Specific mobile overrides
- Hero min-height: 80vh
- CTA panel padding: 32px
- About portrait: max-width 480px, centered
- Info list: label stacks above value (1 column)
- Detail body: content first, sidebar second
- Gallery: 1 column
- Project nav: 1 column (stacked)

---

## Figma Responsive Frame Setup Steps

1. Create 4 frames per page: Desktop (1440), Laptop (1366), Tablet (1024), Mobile (390).
2. Set all frames to Auto Layout: Vertical, gap 0.
3. Fill with `Colors/Base/Black Room`.
4. Build Desktop frame first (primary design).
5. Duplicate Desktop → rename → adjust for Laptop (minimal changes).
6. Duplicate Desktop → rename → adjust for Tablet (collapse grids, adjust type).
7. Duplicate Tablet → rename → adjust for Mobile (single col, mobile nav, adjust type).
8. Use component instances everywhere — override only what changes per breakpoint.

---

## Elementor v4 Responsive Mapping

| Figma Frame | Elementor Breakpoint Setting |
|-------------|------------------------------|
| Desktop (1440) | Desktop (default) |
| Laptop (1366) | Desktop — no separate breakpoint needed; same layout |
| Tablet (1024) | Tablet (set breakpoint ≤ 1024px) |
| Mobile (390) | Mobile (set breakpoint ≤ 767px) |

In Elementor v4, set responsive overrides on each Atomic Flexbox's padding, gap, and column count using the device-mode toggles in the Elementor editor. Do not create separate sections — use one section with responsive property overrides.

---

## Clamp Reference (CSS to Figma)

These CSS clamp values map to the following Figma sizes per breakpoint:

| CSS Clamp | Mobile (390) | Tablet (1024) | Desktop (1440) |
|-----------|-------------|---------------|----------------|
| `clamp(64px, 14vw, 200px)` | 64px | 143px | 200px |
| `clamp(48px, 9vw, 140px)` | 48px | 92px | 140px |
| `clamp(36px, 5vw, 80px)` | 36px | 51px | 80px |
| `clamp(18px, 2vw, 30px)` | 18px | 20px | 30px |
| `clamp(72px, 10vw, 160px)` | 72px | 102px | 160px |
| `clamp(20px, 5vw, 72px)` | 20px | 51px | 72px |

Use the desktop value in your Desktop frame, mobile value in your Mobile frame.
