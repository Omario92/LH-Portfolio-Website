# UiChemy Atomic Element Mapping
# Luong Huynh Portfolio — Figma → Elementor v4 Atomic Elements

## Target: UiChemy → Elementor v4 Atomic Elements
Do NOT use Elementor v3 Container. Do NOT use Elementor Flexbox Container v3.

---

## UiChemy Atomic Element Types Reference

| UiChemy Atomic Element | Elementor v4 Widget | Purpose |
|------------------------|--------------------|---------| 
| Atomic Heading | Heading | All typographic headings (h1–h3) |
| Atomic Paragraph | Text Editor | Body copy, eyebrows, meta, captions |
| Atomic Image | Image | All photos, renders, placeholders |
| Atomic Button | Button | CTAs, nav CTA, "Get in Touch" |
| Atomic SVG | SVG Image | Icons, decorative SVG shapes |
| Atomic Flexbox | Flexbox Container | All layout wrappers, rows, columns, grids |

---

## Layer → Atomic Element Mapping

### Layout Containers

| Figma Layer | UiChemy Element | Settings |
|-------------|----------------|---------|
| `Section/Hero` | Atomic Flexbox | Direction: Column, Min-height: 860px, Align: End |
| `Section/FeaturedWork` | Atomic Flexbox | Direction: Column, Padding: 120px top/bottom |
| `Section/Services` | Atomic Flexbox | Direction: Column, BG: `#101010` |
| `Section/CTA` | Atomic Flexbox | Direction: Column, BG: `#151515` + gradient overlay |
| `Section/Footer` | Atomic Flexbox | Direction: Row, Border-top: 1px |
| `Container/Page` | Atomic Flexbox | Max-width: 1440px, margin auto, padding: 0 72px |
| `Flexbox/Work Grid` | Atomic Flexbox | Direction: Row, Wrap: Yes, Gap: 24px |
| `Flexbox/Service Grid` | Atomic Flexbox | Direction: Row, Wrap: Yes, Gap: 1px, BG: border color |
| `Flexbox/Filter Bar` | Atomic Flexbox | Direction: Row, Wrap: Yes, Gap: 10px |
| `Flexbox/Two Col` | Atomic Flexbox | Direction: Row, Gap: 86px |
| `Flexbox/Sidebar` | Atomic Flexbox | Direction: Column, Position: sticky top 90px |
| `Flexbox/Gallery Grid` | Atomic Flexbox | Direction: Row, Wrap: Yes, Gap: 24px |
| `Flexbox/Project Nav` | Atomic Flexbox | Direction: Row, Gap: 1px |
| `Flexbox/Hero Actions` | Atomic Flexbox | Direction: Row, Wrap: Yes, Gap: 14px |

### Typographic Elements

| Figma Layer | UiChemy Element | HTML Tag | CSS Class |
|-------------|----------------|----------|-----------|
| `Heading/Hero Title` | Atomic Heading | H1 | `lh-hero-title` |
| `Heading/Section Title` | Atomic Heading | H2 | `lh-section-title` |
| `Heading/Work Title` | Atomic Heading | H3 | `lh-work-title` |
| `Heading/Service Title` | Atomic Heading | H3 | `lh-service-title` |
| `Heading/Detail Title` | Atomic Heading | H1 | `lh-detail-title` |
| `Heading/Brand Name` | Atomic Heading | Span | `lh-brand` |
| `Paragraph/Eyebrow` | Atomic Paragraph | Span | `lh-eyebrow` |
| `Paragraph/Lead` | Atomic Paragraph | P | `lh-hero-copy` or `lh-detail-lead` |
| `Paragraph/Body` | Atomic Paragraph | P | (body default) |
| `Paragraph/Meta` | Atomic Paragraph | Span | `lh-meta` |
| `Paragraph/Tag Label` | Atomic Paragraph | Span | `lh-tag` |
| `Paragraph/Service Number` | Atomic Paragraph | Span | `lh-service-number` |
| `Paragraph/Copyright` | Atomic Paragraph | Span | (footer default) |
| `Paragraph/Nav Link` | Atomic Paragraph | A | `lh-menu a` |
| `Paragraph/Social Link` | Atomic Paragraph | A | `lh-socials a` |

### Image Elements

| Figma Layer | UiChemy Element | CSS Class | Notes |
|-------------|----------------|-----------|-------|
| `Image/Work Thumbnail` | Atomic Image | `lh-work-media` | Aspect ratio 4:5, object-fit cover |
| `Image/Portrait` | Atomic Image | `lh-portrait` | Aspect ratio 0.86, object-fit cover |
| `Image/Cover` | Atomic Image | `lh-detail-cover` | Aspect ratio 16:9, full width |
| `Image/Gallery Item` | Atomic Image | `lh-detail-gallery-item` | Aspect ratio 4:3 |

### Button Elements

| Figma Layer | UiChemy Element | CSS Class | Variant |
|-------------|----------------|-----------|---------|
| `Component/Button Primary` | Atomic Button | `lh-button lh-button-primary` | BG: Cyan, Color: Black |
| `Component/Button Secondary` | Atomic Button | `lh-button` | BG: transparent, Border: ivory |
| `Button/Nav CTA` | Atomic Button | `lh-nav-cta` | Pill border, pulse dot via CSS |

### SVG / Icon Elements

| Figma Layer | UiChemy Element | Notes |
|-------------|----------------|-------|
| `SVG/Brand Mark` | Atomic SVG | Circular, 30×30px, Cyan background |
| `SVG/Arrow Icon` | Atomic SVG | Used in project nav, CTA arrows |

---

## Work Card Component Mapping

```
Component/WorkCard → Atomic Flexbox (col) [class: lh-work-card]
  └─ Atomic Flexbox (col) [inner, flex: 1]
       ├─ Atomic Image [class: lh-work-media, aspect-ratio: 4/5]
       └─ Atomic Flexbox (col) [class: lh-work-body]
            ├─ Atomic Flexbox (row) [class: lh-meta-row]
            │    └─ Atomic Paragraph ×N [class: lh-tag]
            ├─ Atomic Heading H3 [class: lh-work-title]
            └─ Atomic Paragraph [class: lh-work-desc]
```

Border: 1px `Colors/Border/Default`, border-radius: `radius-lg`  
Hover state: handled via Elementor CSS custom class or motion effect

---

## Service Card Component Mapping

```
Component/ServiceCard → Atomic Flexbox (col, space-between) [class: lh-service-card]
  ├─ Atomic Paragraph [class: lh-service-number] — JetBrains Mono, muted
  └─ Atomic Flexbox (col)
       ├─ Atomic Heading H3 [class: lh-service-title]
       └─ Atomic Paragraph [class: lh-service-copy]
```

Min-height: 260px. Background: `Colors/Base/Soft`.

---

## Filter Pill Component Mapping

```
Component/FilterPill → Atomic Button [class: lh-filter-btn]
  Variant Default: border 1px Line, color Muted, BG transparent
  Variant Active: BG Cyan, border Cyan, color Black
```

Note: UiChemy exports the visual pill as an Atomic Button. The JS filter logic must be added manually in Elementor via Custom JavaScript or a filtering plugin.

---

## Header Component Mapping

```
Component/Header → Atomic Flexbox (row, space-between, sticky) [class: lh-header]
  └─ Container/Page
       ├─ Flexbox/Brand → Atomic Flexbox (row)
       │    ├─ Atomic SVG [brand mark circle]
       │    └─ Atomic Heading [brand name]
       ├─ Flexbox/Menu → Atomic Flexbox (row)
       │    ├─ Atomic Paragraph (nav link) ×3
       │    └─ Atomic Button (nav CTA)
       └─ [mobile: Atomic Button (hamburger toggle)]
```

Sticky: Set via Elementor Motion Effects → Sticky Top on the Header section.

---

## Post-UiChemy Checklist

After export to Elementor v4:

- [ ] Apply global class `lh-container` to all page-width wrappers
- [ ] Apply global class `lh-section` to all major sections
- [ ] Apply global class `lh-button-primary` to primary CTAs
- [ ] Set Elementor Global Colors matching the design tokens above
- [ ] Set Elementor Global Fonts: Newake (upload OTF), Inter, JetBrains Mono
- [ ] Enable sticky positioning on header section
- [ ] Add hover transition CSS via Additional CSS on work cards
- [ ] Add JS for filter pill interaction on portfolio page
- [ ] Test mobile breakpoints at 767px and 390px
- [ ] Set min-height on hero section (860px desktop, 80vh mobile)
