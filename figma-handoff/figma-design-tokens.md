# Figma Design Tokens
# Luong Huynh Portfolio — UiChemy → Elementor v4 Atomic Elements

Source of truth: `Design Files/colors_and_type.css` + `assets/css/styles.css`

---

## Color Styles

Create all colors as named **Color Styles** in Figma under `Colors/` groups.

### Base

| Token name | Figma style name | Value |
|------------|-----------------|-------|
| `--lh-bg` | `Colors/Base/Black Room` | `#070707` |
| `--lh-bg-soft` | `Colors/Base/Soft` | `#101010` |
| `--lh-panel` | `Colors/Panel/Default` | `#151515` |
| `--lh-panel-2` | `Colors/Panel/Hover` | `#1c1c1c` |

### Foreground

| Token name | Figma style name | Value |
|------------|-----------------|-------|
| `--lh-text` | `Colors/Text/Primary` | `#f4f0e8` |
| `--lh-muted` | `Colors/Text/Muted` | `#9b978f` |
| `--lh-soft` | `Colors/Text/Soft` | `#6b6760` |

### Borders

| Token name | Figma style name | Value |
|------------|-----------------|-------|
| `--lh-line` | `Colors/Border/Default` | `rgba(244,240,232,0.14)` |
| `--lh-line-strong` | `Colors/Border/Strong` | `rgba(244,240,232,0.28)` |

### Accents

| Token name | Figma style name | Value |
|------------|-----------------|-------|
| `--lh-accent` | `Colors/Accent/Cyan` | `#00f0ff` |
| `--lh-accent-warm` | `Colors/Accent/Indigo` | `#6366f1` |
| `--lh-on-accent` | `Colors/Accent/On Cyan` | `#070707` |

---

## Text Styles

Create all type styles as named **Text Styles** in Figma under `Type/` groups.

### Display (Newake font — uppercase only)

> Note: Newake Demo is uppercase-only. Apply `text-transform: uppercase` to all Newake styles. If Newake is not installed in Figma, substitute Inter Tight weight 900 as a placeholder.

| Style name | Font | Size | Weight | Line Height | Tracking |
|------------|------|------|--------|-------------|---------|
| `Type/Hero` | Newake | 200px | 400 | 92% | 10% |
| `Type/H1` | Newake | 140px | 400 | 94% | 12% |
| `Type/H2 Section` | Newake | 80px | 400 | 96% | 10% |
| `Type/H2` | Newake | 64px | 400 | 100% | 15% |
| `Type/H3` | Newake | 44px | 400 | 102% | 11% |
| `Type/Detail Title` | Newake | 140px | 400 | 94% | 12% |

### Body (Inter font — mixed case)

| Style name | Font | Size | Weight | Line Height | Tracking |
|------------|------|------|--------|-------------|---------|
| `Type/Lead` | Inter | 30px | 400 | 122% | -3% |
| `Type/Body` | Inter | 16px | 400 | 155% | -0.5% |
| `Type/Body Large` | Inter | 20px | 400 | 165% | -0.5% |
| `Type/Small` | Inter | 14px | 400 | 150% | 0 |

### Display Alt (Inter Tight — card titles, mixed case)

| Style name | Font | Size | Weight | Line Height | Tracking |
|------------|------|------|--------|-------------|---------|
| `Type/Card Title` | Inter Tight | 28px | 700 | 98% | -5% |
| `Type/Service Title` | Inter Tight | 28px | 700 | 105% | -4% |
| `Type/Nav Label` | Inter | 11px | 700 | 100% | 14% |

### Micro (Inter — uppercase labels)

| Style name | Font | Size | Weight | Line Height | Tracking |
|------------|------|------|--------|-------------|---------|
| `Type/Eyebrow` | Inter | 13px | 700 | 100% | 16% |
| `Type/Meta` | Inter | 12px | 600 | 110% | 14% |
| `Type/Tag` | Inter | 10px | 700 | 100% | 12% |
| `Type/Mono` | JetBrains Mono | 10px | 400 | 100% | 0 |

---

## Figma Variables

Create a **Variables** collection named `Spacing` with number values:

| Variable name | Value |
|---------------|-------|
| `spacing/1` | 4 |
| `spacing/2` | 8 |
| `spacing/3` | 12 |
| `spacing/4` | 16 |
| `spacing/5` | 24 |
| `spacing/6` | 32 |
| `spacing/7` | 48 |
| `spacing/8` | 72 |
| `spacing/9` | 120 |

Create a **Variables** collection named `Layout`:

| Variable name | Value |
|---------------|-------|
| `layout/max-width` | 1440 |
| `layout/gutter-desktop` | 72 |
| `layout/gutter-mobile` | 20 |
| `layout/section-y-desktop` | 160 |
| `layout/section-y-mobile` | 72 |
| `layout/radius-sm` | 12 |
| `layout/radius-md` | 20 |
| `layout/radius-lg` | 32 |
| `layout/radius-pill` | 999 |

---

## Gradient Fills

### Hero background
- Radial gradient, Cyan `#00f0ff` 10% opacity, origin top-right 78% 28%, fade to transparent at 24vw
- Radial gradient, Indigo `#6366f1` 14% opacity, origin bottom-left 20% 85%, fade to transparent at 26vw
- Base fill: `Colors/Base/Black Room`

### Section muted background
- Radial gradient, Cyan `#00f0ff` 5% opacity, origin top-left, fade to transparent at 34vw
- Base fill: `Colors/Base/Soft`

### CTA panel
- Linear gradient 135°, Cyan `#00f0ff` 8% opacity, fade to transparent at 40%
- Base fill: `Colors/Panel/Default`

---

## Border Radius Reference

| Token | Value | Figma variable |
|-------|-------|----------------|
| `--lh-radius-sm` | 12px | `layout/radius-sm` |
| `--lh-radius-md` | 20px | `layout/radius-md` |
| `--lh-radius-lg` | 32px | `layout/radius-lg` |
| `--lh-pill` | 999px | `layout/radius-pill` |

Work card image top corners: `radius-lg`. Bottom corners: `radius-md`.

---

## Elementor v4 Global Classes (post-UiChemy)

After UiChemy export, apply these as Elementor Global Classes in Site Settings:

### Spacing classes
```
.lh-section        { padding-block: 160px; }   /* desktop */
.lh-section-tight  { padding-block: 96px; }
.lh-container      { max-width: 1440px; margin-inline: auto; padding-inline: 72px; }
.lh-gutter         { padding-inline: 72px; }
```

### Typography classes
```
.lh-eyebrow   { font: 700 13px/1 Inter; letter-spacing: 0.16em; text-transform: uppercase; color: #00f0ff; }
.lh-meta      { font: 600 12px/1.1 Inter; letter-spacing: 0.14em; text-transform: uppercase; color: #9b978f; }
.lh-lead      { font: 400 30px/1.22 Inter; letter-spacing: -0.03em; }
```

### Color classes
```
.lh-text-accent  { color: #00f0ff; }
.lh-text-muted   { color: #9b978f; }
.lh-bg-soft      { background: #101010; }
.lh-bg-panel     { background: #151515; }
```
