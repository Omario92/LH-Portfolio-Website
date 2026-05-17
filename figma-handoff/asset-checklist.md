# Asset Checklist
# Luong Huynh Portfolio — All Assets Required for Figma Build & Elementor v4

---

## Fonts

| Font | Source | Format | Usage |
|------|--------|--------|-------|
| Newake Demo | `Design Files/fonts/NewakeFont-Demo.otf` | OTF | All display headings, hero, section titles |
| Inter | Google Fonts | WOFF2 via CDN | Body copy, meta, tags, nav |
| Inter Tight | Google Fonts | WOFF2 via CDN | Card titles, service titles |
| JetBrains Mono | Google Fonts | WOFF2 via CDN | Service numbers, code mono |

**Figma:** Install Newake via Figma's font uploader or use Inter Tight weight 900 as a placeholder. Install Inter and Inter Tight via Google Fonts plugin or system install.

**Elementor:** Upload `NewakeFont-Demo.otf` to Site Settings → Custom Fonts. Add Google Fonts via Site Settings → Google Fonts.

---

## Project Images

These are the production images that replace the SVG placeholder files. Collect from Luong's archive.

| Slug | HTML Placeholder | Description |
|------|-----------------|-------------|
| `stride-beyond` | `assets/img/placeholders/stride-beyond.svg` | AI identity visual — futuristic |
| `nexora` | `assets/img/placeholders/nexora.svg` | Brand system — premium futuristic |
| `bt-studio-cgi-beverage-demo` | `assets/img/placeholders/bt-studio-cgi-beverage-demo.svg` | CGI product shot — beverage |
| `tvc-ovaltine-2015-adaptation` | `assets/img/placeholders/tvc-ovaltine-2015-adaptation.svg` | TVC campaign still |
| `bt-studio-cgi-huda-football` | `assets/img/placeholders/bt-studio-cgi-huda-football.svg` | CGI beer football visual |
| `cheers-to-victory` | `assets/img/placeholders/cheers-to-victory.svg` | 3D/AI beer celebration |
| `afc-key-visual` | `assets/img/placeholders/afc-key-visual.svg` | Sports key visual |
| `twister-pack-visual` | `assets/img/placeholders/twister-pack-visual.svg` | Pack shot 3D render |
| `halida-tet-2022-key-visual` | `assets/img/placeholders/halida-tet-2022-key-visual.svg` | Tet seasonal visual |
| `huda-beach-carnival-2023` | `assets/img/placeholders/huda-beach-carnival-2023.svg` | Event visual — beach summer |
| `circuit` | `assets/img/placeholders/circuit.svg` | Web design concept |
| `spectral` | `assets/img/placeholders/spectral.svg` | Editorial dark web concept |
| `astralis` | `assets/img/placeholders/astralis.svg` | Film-inspired visual |

### Required specs for production images

| Spec | Value |
|------|-------|
| Work card (4:5) | Minimum 800×1000px, WEBP preferred |
| Work card (16:11 mobile crop) | Minimum 800×550px |
| About portrait (0.86 ratio) | Minimum 600×698px |
| Project cover (16:9) | Minimum 1440×810px, WEBP preferred |
| Gallery item (4:3) | Minimum 800×600px |

---

## About Portrait

- File: `assets/img/luong-huynh-portrait.jpg` (to be supplied)
- Aspect ratio: 0.86 (portrait, close to square)
- Subject: Luong Huynh
- Style: Dark, cinematic. Studio or dark background preferred.
- Currently using placeholder: `assets/img/placeholders/stride-beyond.svg`

---

## Brand Assets

| Asset | Status | Notes |
|-------|--------|-------|
| Brand mark (LH monogram) | Present — CSS generated | Currently an LH text in a cyan circle. Can be replaced with a custom SVG. |
| Brand wordmark | Present — CSS text | "Luong Huynh" in Newake |
| Favicon | Missing | Need 32×32 and 180×180 PNG or SVG |

### Favicon recommendation
Create `favicon.svg` and `apple-touch-icon.png` from the brand mark — cyan circle with `LH` monogram.

---

## Social Icons (Optional)

Currently socials are text-only links (Behance, Dribbble, Instagram, LinkedIn). If icon versions are needed:

| Platform | Icon source |
|----------|------------|
| Behance | SVG — download from Simple Icons |
| Dribbble | SVG — download from Simple Icons |
| Instagram | SVG — download from Simple Icons |
| LinkedIn | SVG — download from Simple Icons |

Place at `assets/img/icons/` if used.

---

## Figma Assets Required

| Asset | Usage in Figma |
|-------|---------------|
| All 13 project images | Work card thumbnails (4:5 crop) |
| Luong portrait | About page portrait panel |
| 1 project as cover | Project detail hero cover (16:9) |
| 4 project images | Project detail gallery items (4:3) |

---

## Elementor Production Asset Checklist

- [ ] Newake OTF uploaded to Elementor Custom Fonts
- [ ] Google Fonts (Inter, Inter Tight, JetBrains Mono) added via Site Settings
- [ ] All 13 project images uploaded to WordPress Media Library as WEBP
- [ ] About portrait uploaded to WordPress Media Library
- [ ] Favicon (32×32 SVG or PNG) set in Site Settings → Favicon
- [ ] Custom CSS from `assets/css/styles.css` pasted into Site Settings → Custom CSS
- [ ] Design tokens from `figma-design-tokens.md` entered as Elementor Global Colors and Global Fonts
- [ ] Social links updated with real URLs (not `https://behance.com` placeholder)
- [ ] Contact email updated from `hello@luonghuynh.com` to real address (`mr.luonghuynh@gmail.com`)
