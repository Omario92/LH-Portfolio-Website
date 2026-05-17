# Figma Build Guide
# Luong Huynh Portfolio — UiChemy → Elementor v4 Atomic Elements

## Purpose

This guide explains how to recreate the approved HTML review site inside Figma so it can be exported through UiChemy as Elementor v4 Atomic Elements. It does not produce Elementor JSON or Container v3 templates.

---

## Workflow Overview

```
HTML Review Site (approved design)
        ↓
Figma (4 frames: Desktop / Laptop / Tablet / Mobile)
        ↓
UiChemy Figma Plugin
        ↓
Elementor v4 Atomic Elements (WordPress)
```

---

## Step 1 — Figma File Setup

### File name
```
LH Portfolio — Figma Handoff v1
```

### Pages inside the Figma file

| Page | Purpose |
|------|---------|
| `🎨 Design Tokens` | Color Styles, Text Styles, Variables |
| `🏠 Homepage` | Desktop + Laptop + Tablet + Mobile frames |
| `🗂 Portfolio` | Desktop + Laptop + Tablet + Mobile frames |
| `👤 About` | Desktop + Laptop + Tablet + Mobile frames |
| `📄 Project Detail` | Desktop + Laptop + Tablet + Mobile frames |
| `🧩 Components` | All reusable components and variants |

---

## Step 2 — Set Up Design Tokens First

Before drawing any frames, set up all tokens. See `figma-design-tokens.md` for the full list.

**Color Styles** — Create under `Colors/` group:
- `Colors/Base/Black Room` → `#070707`
- `Colors/Base/Soft` → `#101010`
- `Colors/Panel/Default` → `#151515`
- `Colors/Panel/Hover` → `#1c1c1c`
- `Colors/Text/Primary` → `#f4f0e8`
- `Colors/Text/Muted` → `#9b978f`
- `Colors/Accent/Cyan` → `#00f0ff`
- `Colors/Accent/Indigo` → `#6366f1`
- `Colors/Line/Default` → `rgba(244,240,232,0.14)`
- `Colors/Line/Strong` → `rgba(244,240,232,0.28)`

**Text Styles** — Create under `Type/` group:
- `Type/Hero` — Newake, 200px, tracking 0.10em, uppercase
- `Type/H1` — Newake, 140px, tracking 0.12em, uppercase
- `Type/H2` — Newake, 64px, tracking 0.15em, uppercase
- `Type/H3` — Newake, 44px, tracking 0.11em, uppercase
- `Type/Lead` — Inter, 30px, tracking -0.03em
- `Type/Body` — Inter, 16px, tracking -0.005em
- `Type/Eyebrow` — Inter, 13px, weight 700, tracking 0.16em, uppercase
- `Type/Meta` — Inter, 12px, weight 600, tracking 0.14em, uppercase
- `Type/Tag` — Inter, 10px, weight 700, tracking 0.12em, uppercase

**Figma Variables** — Create a `Spacing` collection:
- `space/1` = 4
- `space/2` = 8
- `space/3` = 12
- `space/4` = 16
- `space/5` = 24
- `space/6` = 32
- `space/7` = 48
- `space/8` = 72
- `space/9` = 120

---

## Step 3 — Create Frames

For each page, create 4 frames:

| Frame Name | Width | Height |
|------------|-------|--------|
| `Desktop` | 1440 | Auto |
| `Laptop` | 1366 | Auto |
| `Tablet` | 1024 | Auto |
| `Mobile` | 390 | Auto |

Set all frames to:
- Background: `Colors/Base/Black Room` (`#070707`)
- Auto Layout: Vertical
- Clip content: Off (allow overflow for scroll)

---

## Step 4 — Build Components First

Before building page frames, build all reusable components on the `🧩 Components` page. See `figma-layer-naming.md` for naming and `uichemy-atomic-mapping.md` for UiChemy mappings.

Core components to build:
- `Header/Default`
- `Nav/Link`
- `Nav/CTA Badge`
- `Button/Primary`
- `Button/Secondary`
- `Tag/Default`
- `Tag/Strong`
- `Filter Pill/Default`
- `Filter Pill/Active`
- `Work Card/Default`
- `Work Card/Hover`
- `Service Card/Default`
- `Footer/Default`

---

## Step 5 — Build Pages

Assemble each page frame by placing component instances and unique section content. Use Auto Layout throughout. See `figma-page-structure.md` for section-by-section breakdown.

---

## Step 6 — UiChemy Export

1. Install the UiChemy plugin in Figma.
2. Select the Desktop frame for any page.
3. Run UiChemy → select **Atomic Elements** output mode.
4. Map each layer to the correct Elementor v4 Atomic Element (see `uichemy-atomic-mapping.md`).
5. Export and paste into Elementor on WordPress.
6. Apply global classes from `figma-design-tokens.md` for typography and color.
7. Repeat for each responsive breakpoint frame.

---

## Important Rules

- Do not use Elementor v3 Container/Flexbox language.
- Do not export Elementor JSON templates.
- All layout uses Elementor v4 Atomic Flexbox (not Container).
- All text is set via Atomic Heading or Atomic Paragraph elements.
- All images use Atomic Image element.
- All buttons use Atomic Button element.
- All SVG icons use Atomic SVG element.
- Spacing is applied via reusable global classes, not inline styles.
