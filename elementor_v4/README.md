# Elementor v4 JSON Templates
# Luong Huynh Portfolio

Generated from: `elementor_v4/generate.js`
Schema source: `elementor_v4/_reference/homepage-template_V4.json`

---

## Files

| File | Page | Description |
|------|------|-------------|
| `homepage_V4.json` | Home (`/`) | Hero, Featured Work (3 cards), Services grid, CTA |
| `portfolio_V4.json` | Portfolio (`/portfolio/`) | Archive header, filter bar + 13-card grid, CTA |
| `about_V4.json` | About (`/about/`) | Portrait grid, rich text, Services grid, CTA |
| `project-template_V4.json` | Project detail | Hero, cover, body/sidebar, gallery, project nav, CTA |
| `global-css.css` | Site-wide | All design tokens and component styles |

---

## How to import each JSON into Elementor v4

### Step 1 — Import a single page template

1. In WordPress, go to **Elementor → My Templates → Import Templates**.
2. Click **Select File** and upload one of the JSON files (e.g. `homepage_V4.json`).
3. After import, open the target page in Elementor editor.
4. Click **+ Add Template** → **My Templates** → find the imported template → click **Insert**.
5. Elementor will insert the full page structure.

### Step 2 — Apply global CSS

Option A — Site Settings (recommended):
1. In Elementor editor, click the hamburger ≡ → **Site Settings → Custom CSS**.
2. Paste the entire contents of `global-css.css` into the Custom CSS field.
3. Click **Save Changes**.

Option B — WordPress Customizer:
1. Go to **Appearance → Customize → Additional CSS**.
2. Paste the contents of `global-css.css`.

Option C — Child theme:
Add `@import url('path/to/global-css.css');` to your child theme's `style.css`.

### Step 3 — Upload the Newake font

1. Go to **Elementor → Custom Fonts → Add New**.
2. Upload `Design Files/fonts/NewakeFont-Demo.otf`.
3. Set font family name to `Newake`.
4. Save.

### Step 4 — Set Global Colors

In **Elementor → Site Settings → Global Colors**, add:
- `lh-bg` → `#070707`
- `lh-text` → `#f4f0e8`
- `lh-accent` → `#00f0ff`
- `lh-muted` → `#9b978f`
- `lh-panel` → `#151515`

---

## Schema overview

Each JSON file follows the Elementor v4 Atomic schema:

```json
{
  "content": [ ...sections... ],
  "page_settings": { "custom_css": "..." },
  "version": "0.4",
  "title": "Page Name",
  "type": "page",
  "global_classes": {
    "items": { "g-xxxxxxx": { "id": "...", "type": "class", "label": "lh-xxx", "variants": [] } },
    "order": ["g-xxxxxxx", ...]
  }
}
```

### Element types used

| `elType` | `widgetType` | Purpose |
|----------|-------------|---------|
| `e-flexbox` | — | Top-level page sections |
| `e-div-block` | — | Containers, wrappers, grids, cards |
| `widget` | `e-heading` | All headings (h1–h3) |
| `widget` | `e-paragraph` | Body copy, eyebrows, meta, labels |
| `widget` | `e-button` | CTA buttons |
| `widget` | `html` | Work card grids, filter bar, portrait, gallery, project nav |

### Global class IDs (shared across all pages)

| CSS class | Global class ID |
|-----------|----------------|
| `lh-hero` | `g-9366cf5` |
| `lh-container` | `g-f50942b` |
| `lh-section` | `g-2d400a9` |
| `lh-section-muted` | `g-ee5b286` |
| `lh-section-head` | `g-22e82fe` |
| `lh-cta` | `g-4d79e46` |
| `lh-button` | `g-6c0963d` |
| `lh-button-primary` | `g-98193da` |
| `lh-section-kicker` | `g-ed136ec` |
| `lh-section-title` | `g-bf0a5fa` |
| `lh-service-grid` | `g-7cad70c` |
| `lh-service-card` | `g-035f52a` |
| `lh-work-grid` | `g-a1b2c3d` |
| `lh-filter-bar` | `g-a7b8c9d` |

---

## How to update images

The JSON files reference images at `/wp-content/uploads/lh/filename.jpg`. Upload your project images to WordPress Media Library with matching filenames, or update the `src` attributes in the `html` widget settings inside each JSON before importing.

Image slugs used:
- `stride-beyond.jpg`
- `nexora.jpg`
- `bt-studio-cgi-beverage-demo.jpg`
- `bt-studio-cgi-huda-football.jpg`
- `tvc-ovaltine-2015-adaptation.jpg`
- `cheers-to-victory.jpg`
- `afc-key-visual.jpg`
- `twister-pack-visual.jpg`
- `halida-tet-2022-key-visual.jpg`
- `huda-beach-carnival-2023.jpg`
- `circuit.jpg`
- `spectral.jpg`
- `astralis.jpg`
- `luong-huynh-portrait.jpg`

---

## Regenerating the JSON files

If you need to update content or structure, edit `generate.js` and re-run:

```bash
cd elementor_v4
node generate.js
```

Then validate:

```bash
node -e "JSON.parse(require('fs').readFileSync('elementor_v4/homepage_V4.json','utf8')); console.log('homepage ok')"
node -e "JSON.parse(require('fs').readFileSync('elementor_v4/portfolio_V4.json','utf8')); console.log('portfolio ok')"
node -e "JSON.parse(require('fs').readFileSync('elementor_v4/about_V4.json','utf8')); console.log('about ok')"
node -e "JSON.parse(require('fs').readFileSync('elementor_v4/project-template_V4.json','utf8')); console.log('project ok')"
```

---

## Known limitations

1. **Filter interactivity**: The portfolio filter bar is rendered as an `html` widget with an inline `<script>`. Elementor's built-in Content Security Policy may block inline scripts in some configurations. If filtering doesn't work, use an Elementor filter plugin (e.g. JetSmartFilters or Isotope via Elementor Custom Code).

2. **Newake font**: The Newake Demo font is uppercase-only. Any text set in Newake will be forced uppercase via CSS. Card titles use Inter Tight instead.

3. **Sticky portrait**: The About page portrait panel uses `position: sticky` via a local CSS style. Elementor may override this depending on theme settings — check the container overflow is not `hidden`.

4. **Project detail is a template**: `project-template_V4.json` is a static layout template. For a real project archive, connect it to a Custom Post Type (CPT) using Elementor Pro Loop Builder or a CPT plugin.

5. **Contact email**: The email `hello@luonghuynh.com` is a placeholder. Update `mailto:hello@luonghuynh.com` links to the real contact email after import.

6. **Image paths**: All image `src` values use `/wp-content/uploads/lh/` prefix. Upload images to that directory or update paths before importing.

7. **Version requirement**: These files require Elementor v4 with Atomic Elements support. They are not compatible with Elementor v3 Container/Flexbox templates.
