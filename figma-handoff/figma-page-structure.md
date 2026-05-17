# Figma Page Structure
# Section-by-section breakdown for Luong Huynh Portfolio

Each section below defines:
1. Figma frame name
2. Layer hierarchy
3. Auto Layout direction
4. Gap / Padding
5. Width / Height behavior
6. Suggested Figma styles/variables
7. UiChemy Atomic element mapping
8. Responsive notes

---

## HOMEPAGE

### Section: Header

**Figma frame name:** `Header/Desktop`

**Layer hierarchy:**
```
Header [Frame, sticky]
  └─ Nav Container [Frame, H: Auto Layout Row]
       ├─ Brand [Group]
       │    ├─ Brand Mark [Ellipse, 30×30, fill Cyan]
       │    └─ Brand Name [Text, Type/Nav Label]
       ├─ Menu [Frame, Auto Layout Row]
       │    ├─ Link: Homepage [Text]
       │    ├─ Link: Portfolio [Text]
       │    ├─ Link: About [Text]
       │    └─ CTA Badge [Frame, pill border]
       └─ [spacer]
```

**Auto Layout:** Horizontal, Align Center, Space Between  
**Height:** 72px fixed  
**Width:** Fill container (max 1440px centered)  
**Padding:** 0 72px (desktop), 0 20px (mobile)  
**Background:** `#070707` at 90% opacity  
**Border:** Bottom 1px `Colors/Line/Default`  
**UiChemy mapping:** Atomic Flexbox (row) → Atomic Heading (brand name) → Atomic Button (CTA badge)  
**Responsive:** On mobile (390), hide Menu links, show hamburger icon button. CTA badge hides at 767px.

---

### Section: Hero

**Figma frame name:** `Hero/Desktop`

**Layer hierarchy:**
```
Hero [Frame, min-height 860px]
  ├─ Gradient Wash [Rectangle, fills]
  │    └─ Fill 1: radial cyan at top-right 10% opacity
  │    └─ Fill 2: radial indigo at bottom-left 14% opacity
  ├─ Dot Grid [Rectangle, image fill or noise pattern, 4% opacity]
  └─ Hero Body [Frame, Auto Layout Column, max-width 1100px]
       ├─ Eyebrow [Text, Type/Eyebrow, color Cyan]
       ├─ Hero Title [Text, Type/Hero, ivory]
       ├─ Hero Copy [Text, Type/Lead, ivory 82% opacity]
       └─ Actions [Frame, Auto Layout Row, gap 14px]
            ├─ Button/Primary: View Portfolio
            └─ Button/Secondary: About Luong
```

**Auto Layout:** Vertical, Align Start, justify End (bottom-aligned content)  
**Padding:** 180px top, 96px bottom (desktop); 96px top, 48px bottom (mobile)  
**Width:** Full bleed  
**UiChemy mapping:** Atomic Flexbox (col) → Atomic Heading (hero title) → Atomic Paragraph (copy) → Atomic Button ×2  
**Responsive:** Hero title scales via clamp. On mobile, letter-spacing tightens from 0.10em to 0.04em. Copy font-size drops to 18px.

---

### Section: Featured Work

**Figma frame name:** `Featured Work/Desktop`

**Layer hierarchy:**
```
Section [Frame, padding 120px top/bottom]
  └─ Container [Frame, max-width 1440px]
       ├─ Section Head [Frame, Auto Layout Row, space-between]
       │    ├─ Left [Frame, Auto Layout Col]
       │    │    ├─ Kicker [Text, Type/Eyebrow, Cyan]
       │    │    └─ Title [Text, Type/H2, ivory]
       │    └─ Copy [Text, Type/Body, muted, max-width 420px]
       └─ Work Grid [Frame, Auto Layout Row, gap 24px, wrap]
            ├─ Work Card 1: Stride Beyond
            ├─ Work Card 2: Nexora
            └─ Work Card 3: BT Studio CGI
```

**Auto Layout:** Vertical → inner grid is Horizontal with Wrap  
**Grid:** 3 equal columns desktop; 2 columns tablet; 1 column mobile  
**Gap:** 24px (desktop), 16px (mobile)  
**UiChemy mapping:** Atomic Flexbox (col) → Atomic Heading → Atomic Paragraph → Atomic Flexbox (row, wrap) → Work Card component instances  
**Responsive:** Section head stacks vertically at 1024px. Grid drops to 2 col at 1024, 1 col at 767.

---

### Section: Services

**Figma frame name:** `Services/Desktop`

**Layer hierarchy:**
```
Section [Frame, bg Soft #101010, padding 120px]
  └─ Container [max-width 1440px]
       ├─ Section Head [Row, space-between]
       └─ Service Grid [Frame, Auto Layout Row, gap 1px, bg Line color]
            ├─ Service Card 01
            ├─ Service Card 02
            ├─ Service Card 03
            └─ Service Card 04
```

**Auto Layout:** The grid container background is `Colors/Line/Default` — cards sit on `bg-soft` with 1px gaps between.  
**Card height:** 260px minimum  
**Columns:** 4 desktop; 2 tablet; 1 mobile  
**UiChemy mapping:** Atomic Flexbox (row) → Service Card (Atomic Flexbox col) → Atomic Paragraph (number) → Atomic Heading (title) → Atomic Paragraph (copy)

---

### Section: CTA / Contact

**Figma frame name:** `CTA/Desktop`

**Layer hierarchy:**
```
Section [padding 120px]
  └─ Container
       └─ CTA Panel [Frame, Auto Layout Col, border-radius 32px, bg Panel]
            ├─ Fill: Linear gradient cyan 8% top-left
            ├─ Border: 1px Line/Default
            ├─ Kicker [Type/Eyebrow, Cyan]
            ├─ Headline [Type/H1, ivory, max-width 980px]
            ├─ Body [Type/Body, muted]
            └─ Actions [Auto Layout Row, gap 14px]
                 ├─ Button/Primary: Get in Touch
                 └─ Button/Secondary: Explore Work
```

**Padding:** 120px (desktop); 32px (mobile)  
**UiChemy mapping:** Atomic Flexbox (col) → Atomic Heading → Atomic Paragraph → Atomic Button ×2

---

### Section: Footer

**Figma frame name:** `Footer/Desktop`

**Layer hierarchy:**
```
Footer [Frame, Auto Layout Row, space-between, border-top 1px]
  ├─ Copyright [Text, Type/Meta, muted]
  └─ Socials [Frame, Auto Layout Row, gap 20px]
       └─ Social Link ×4 [Text, Type/Meta, muted]
```

**Padding:** 32px vertical, gutter horizontal  
**UiChemy mapping:** Atomic Flexbox (row) → Atomic Paragraph → Atomic Flexbox (row) → Atomic Paragraph ×4

---

## PORTFOLIO PAGE

### Section: Portfolio Header

Same header component as homepage.

### Section: Portfolio Hero / Archive Intro

**Figma frame name:** `Portfolio Hero/Desktop`

```
Section [padding 120px]
  └─ Container
       ├─ Section Head [Row, space-between]
       │    ├─ Left: Kicker + H1 title
       │    └─ Right: Body copy
       ├─ Filter Bar [Frame, Auto Layout Row, wrap, gap 10px]
       │    └─ Filter Pill ×10 (All, 3D Model, AI Generated…)
       └─ Work Grid [3 col → 2 → 1, gap 24px]
            └─ Work Card ×13
```

**UiChemy mapping:** Atomic Flexbox (col) → Atomic Heading → Atomic Paragraph → Atomic Flexbox (row, wrap, filter pills) → Atomic Flexbox (grid) → Work Card instances  
**Note:** Filter functionality is JS-driven. UiChemy exports the visual structure; filtering requires custom JS or an Elementor filter widget post-export.

---

## ABOUT PAGE

### Section: About Grid

**Figma frame name:** `About Grid/Desktop`

```
Section [padding 120px]
  └─ Container [Auto Layout Row, gap 86px]
       ├─ Portrait Panel [Frame, 0.78fr, sticky top 90px]
       │    ├─ Portrait Image [Atomic Image, aspect-ratio 0.86, border-radius 26px]
       │    └─ Caption [Frame, col]
       │         └─ Chips [Row: "Digital Artist" (cyan) + "Ho Chi Minh City"]
       └─ Rich Text [Frame, 1.1fr, Auto Layout Col]
            ├─ Eyebrow [Type/Eyebrow, Cyan]
            ├─ H1 [Type/H1, ivory]
            ├─ Body paragraphs [Type/Body]
            └─ Info List [Frame, Auto Layout Col, border-top/bottom 1px]
                 └─ List Item ×4 [Row: label col + value col]
```

**Columns:** 2-col desktop (0.78fr + 1.1fr); 1-col tablet/mobile  
**Portrait sticky:** Implement as sticky-positioned Atomic Flexbox in Elementor  
**UiChemy mapping:** Atomic Flexbox (row) → Atomic Image → Atomic Flexbox (col) → Atomic Heading → Atomic Paragraph → Atomic Flexbox (col, list)

---

## PROJECT DETAIL PAGE

### Section: Detail Hero

**Figma frame name:** `Detail Hero/Desktop`

```
Section [padding 140px top, 72px bottom]
  └─ Container
       ├─ Meta Row [Auto Layout Row, gap 24px]
       │    └─ Tag/Chip ×N
       ├─ Project Title [Type/H1, ivory]
       └─ Lead Copy [Type/Lead, ivory 82%]
```

### Section: Cover Image

```
Container
  └─ Cover [Atomic Image, 16:9 aspect ratio, border-radius 32px, full width]
```

### Section: Detail Body

**Figma frame name:** `Detail Body/Desktop`

```
Section [padding 120px]
  └─ Container [Auto Layout Row, gap 96px]
       ├─ Sidebar [Frame, col, sticky top 90px]
       │    ├─ Info Row ×4 [col: label + value]
       │    └─ Button/Primary: Back to Portfolio
       └─ Content [Frame, col, 680px max]
            └─ Body paragraphs [Type/Body]
```

**Columns:** 2-col desktop (sidebar + content); 1-col mobile (content first, sidebar second)

### Section: Gallery

```
Gallery [Auto Layout Row, wrap, gap 24px]
  └─ Gallery Item ×4 [Atomic Image, 4:3 aspect ratio, border-radius 20px]
```

### Section: Project Nav

```
Project Nav [Auto Layout Row, gap 1px, bg Line]
  ├─ Prev [Frame, col, bg Black Room]
  │    ├─ Label [Type/Meta, Cyan] "← Previous"
  │    └─ Title [Type/H3, ivory]
  └─ Next [Frame, col, bg Black Room, text-align right]
       ├─ Label [Type/Meta, Cyan] "Next →"
       └─ Title [Type/H3, ivory]
```
