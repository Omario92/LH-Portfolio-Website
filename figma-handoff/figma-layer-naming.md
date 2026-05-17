# Figma Layer Naming Convention
# Luong Huynh Portfolio — UiChemy → Elementor v4 Atomic Elements

## Purpose

UiChemy reads Figma layer names to determine Elementor element type and class assignment. Follow these naming rules exactly so UiChemy can map correctly.

---

## Naming Format

```
[ElementType]/[VariantOrRole]
```

Examples:
- `Heading/Hero Title`
- `Paragraph/Body Copy`
- `Image/Work Card Thumbnail`
- `Button/Primary`
- `Flexbox/Section Row`

---

## Global Naming Rules

1. Use Title Case for all layer names.
2. Separate element type from role with `/`.
3. No spaces inside the element type prefix (`Heading` not `Heading Text`).
4. Components use PascalCase: `WorkCard`, `ServiceCard`, `FilterPill`.
5. Frames that become Flexbox containers start with `Flexbox/`.
6. Frames that become sections start with `Section/`.
7. Wrapper containers start with `Container/`.
8. Never use Figma default names (`Frame 1`, `Group 2`, etc.) in the final handoff.

---

## Page & Frame Names

| Frame | Naming |
|-------|--------|
| Desktop homepage | `Homepage/Desktop` |
| Laptop homepage | `Homepage/Laptop` |
| Tablet homepage | `Homepage/Tablet` |
| Mobile homepage | `Homepage/Mobile` |
| Desktop portfolio | `Portfolio/Desktop` |
| Desktop about | `About/Desktop` |
| Desktop detail | `ProjectDetail/Desktop` |

---

## Section Layer Names

| Section | Layer Name |
|---------|------------|
| Sticky header | `Section/Header` |
| Hero | `Section/Hero` |
| Featured work | `Section/FeaturedWork` |
| Services | `Section/Services` |
| CTA / contact | `Section/CTA` |
| Footer | `Section/Footer` |
| Portfolio archive | `Section/PortfolioArchive` |
| About grid | `Section/AboutGrid` |
| Detail hero | `Section/DetailHero` |
| Detail body | `Section/DetailBody` |
| Gallery | `Section/Gallery` |
| Project nav | `Section/ProjectNav` |

---

## Component Layer Names

### Header
```
Component/Header
  Flexbox/Nav
    Flexbox/Brand
      SVG/Brand Mark (or Image/Brand Mark)
      Heading/Brand Name
    Flexbox/Menu
      Paragraph/Nav Link → Homepage
      Paragraph/Nav Link → Portfolio
      Paragraph/Nav Link → About
      Button/Nav CTA → Available for Work
    Button/Mobile Toggle (visible on mobile only)
```

### Work Card
```
Component/WorkCard
  Flexbox/WorkCard Inner
    Image/Work Thumbnail
    Flexbox/Work Info
      Flexbox/Tag Row
        Component/Tag ×N
      Heading/Work Title
      Paragraph/Work Description
```

### Service Card
```
Component/ServiceCard
  Flexbox/ServiceCard Inner
    Paragraph/Service Number [mono, muted]
    Flexbox/Service Text
      Heading/Service Title
      Paragraph/Service Copy
```

### Button
```
Component/Button
  Variant: Primary / Secondary / Nav CTA
  Paragraph/Button Label
```

### Tag / Chip
```
Component/Tag
  Variant: Default / Strong
  Paragraph/Tag Label
```

### Filter Pill
```
Component/FilterPill
  Variant: Default / Active
  Paragraph/Filter Label
```

### Footer
```
Component/Footer
  Flexbox/Footer Row
    Paragraph/Copyright
    Flexbox/Socials
      Paragraph/Social Link → Behance
      Paragraph/Social Link → Dribbble
      Paragraph/Social Link → Instagram
      Paragraph/Social Link → LinkedIn
```

---

## Text Layer Naming

Always name text layers by their semantic role, not their content:

| Semantic Role | Layer Name |
|---------------|------------|
| Large display hero | `Heading/Hero Title` |
| Section h2 | `Heading/Section Title` |
| Card title h3 | `Heading/Work Title` or `Heading/Service Title` |
| Eyebrow label | `Paragraph/Eyebrow` |
| Lead copy | `Paragraph/Lead` |
| Body copy | `Paragraph/Body` |
| Muted meta info | `Paragraph/Meta` |
| Tag text | `Paragraph/Tag Label` |
| Button text | `Paragraph/Button Label` |
| Footer copyright | `Paragraph/Copyright` |

---

## Image Layer Naming

| Role | Layer Name |
|------|------------|
| Work card thumbnail | `Image/Work Thumbnail` |
| About portrait | `Image/Portrait` |
| Project cover | `Image/Cover` |
| Gallery item | `Image/Gallery Item` |
| Logo / SVG icon | `SVG/Icon Name` |

---

## Flexbox / Layout Layer Naming

| Role | Layer Name |
|------|------------|
| Max-width page wrapper | `Container/Page` |
| Section row layout | `Flexbox/Section Row` |
| Section column layout | `Flexbox/Section Col` |
| Card grid | `Flexbox/Work Grid` |
| Service grid | `Flexbox/Service Grid` |
| Filter bar | `Flexbox/Filter Bar` |
| Hero actions row | `Flexbox/Hero Actions` |
| Two-column body | `Flexbox/Two Col` |
| Detail sidebar | `Flexbox/Sidebar` |
| Gallery grid | `Flexbox/Gallery Grid` |
| Project nav row | `Flexbox/Project Nav` |

---

## Class Name Conventions for UiChemy

When UiChemy exports a layer, it uses the layer name to assign a CSS class. Follow the pattern `lh-[role]` to match the existing global stylesheet.

| Layer Name | → CSS class |
|------------|-------------|
| `Section/Hero` | `lh-hero` |
| `Flexbox/Work Grid` | `lh-work-grid` |
| `Component/WorkCard` | `lh-work-card` |
| `Image/Work Thumbnail` | `lh-work-media` |
| `Flexbox/Work Info` | `lh-work-body` |
| `Heading/Work Title` | `lh-work-title` |
| `Paragraph/Work Description` | `lh-work-desc` |
| `Flexbox/Service Grid` | `lh-service-grid` |
| `Component/ServiceCard` | `lh-service-card` |
| `Flexbox/Filter Bar` | `lh-filter-bar` |
| `Component/FilterPill` | `lh-filter-btn` |
| `Component/Tag` | `lh-tag` |
| `Container/Page` | `lh-container` |
| `Component/Button Primary` | `lh-button lh-button-primary` |
| `Component/Button Secondary` | `lh-button` |
| `Section/CTA` | `lh-cta` |
| `Component/Footer` | `lh-footer` |
| `Flexbox/Socials` | `lh-socials` |
