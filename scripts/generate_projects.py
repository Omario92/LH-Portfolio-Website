import os

# Define project database
projects = {
    'tvc-ovaltine-2015-adaptation': {
        'type': 'tvc',
        'title': 'TVC Ovaltine 2015 Adaptation',
        'tags': ['TVC'],
        'lead': 'Campaign adaptation with cinematic product treatment.',
        'cover': 'assets/img/placeholders/tvc-ovaltine-2015-adaptation.svg',
        'client': 'Ovaltine',
        'year': '2015',
        'scope': 'Post-production, Visual Adaptation',
        'output': 'TV Commercial, Broadcast',
        'content': [
            'A broadcast-scale visual adaptation project for Ovaltine, focusing on cinematic product shots, high-energy lighting, and precise color grading.',
            'The team enhanced the 3D assets and composited them with live-action footage, maintaining brand visual assets and high-end finish.',
            'The commercial aired across regional networks, showing outstanding visual appeal and campaign consistency.'
        ],
        'gallery': [
            'assets/img/placeholders/tvc-ovaltine-2015-adaptation.svg',
            'assets/img/placeholders/stride-beyond.svg',
            'assets/img/placeholders/nexora.svg',
            'assets/img/placeholders/cheers-to-victory.svg'
        ],
        'prev': 'bt-studio-cgi-beverage-demo',
        'next': 'bt-studio-cgi-huda-football'
    },
    'bt-studio-cgi-huda-football': {
        'type': 'cgi-hybrid',
        'title': 'BT Studio – CGI Huda Football',
        'tags': ['CGI', 'Feature'],
        'lead': 'CGI beer-football visual system for energetic campaign assets.',
        'cover': 'assets/img/placeholders/bt-studio-cgi-huda-football.svg',
        'client': 'Huda Beer',
        'year': '2024',
        'scope': 'CGI, Liquid Simulation, Key Visual',
        'output': 'Digital, Print, OOH',
        'content': [
            'An energetic CGI campaign concept combining Huda Beer\'s brand world with dynamic football graphics.',
            'Developed custom ice and liquid simulations, stadium lighting structures, and metallic textures to match the energetic summer-sports theme.',
            'The assets were deployed across social, digital channels, and large-format outdoor print billboards.'
        ],
        'gallery': [
            'assets/img/placeholders/bt-studio-cgi-huda-football.svg',
            'assets/img/placeholders/bt-studio-cgi-beverage-demo.svg',
            'assets/img/placeholders/cheers-to-victory.svg',
            'assets/img/placeholders/huda-beach-carnival-2023.svg'
        ],
        'prev': 'tvc-ovaltine-2015-adaptation',
        'next': 'stride-beyond'
    },
    'stride-beyond': {
        'type': 'album',
        'title': 'Stride Beyond',
        'tags': ['AI Generated', 'Branding'],
        'lead': 'AI-led identity exploration for a futuristic visual language.',
        'cover': 'assets/img/placeholders/stride-beyond.svg',
        'client': 'Stride Corp',
        'year': '2025',
        'scope': 'AI Generation, Branding, Visual Concept',
        'output': 'Key Visual, Digital Campaign',
        'content': [
            'Stride Beyond represents an AI-first conceptual exploration for a futuristic brand identity. The project was commissioned to test the boundaries of generative systems in establishing coherent brand worlds.',
            'The workflow combined high-density custom prompts and stable-diffusion model tuning to maintain visual consistency across all key assets, focusing on iridescent textures and high-contrast composition.',
            'The resulting key visual set was featured in Stride Corp\'s annual keynote and digital campaigns, defining their design direction for the next cycle.'
        ],
        'gallery': [
            'assets/img/placeholders/stride-beyond.svg',
            'assets/img/placeholders/astralis.svg',
            'assets/img/placeholders/circuit.svg',
            'assets/img/placeholders/spectral.svg'
        ],
        'prev': 'bt-studio-cgi-huda-football',
        'next': 'cheers-to-victory'
    },
    'cheers-to-victory': {
        'type': 'cgi-hybrid',
        'title': 'Cheers to Victory',
        'tags': ['3D Model', 'AI Generated'],
        'lead': 'Victory-themed 3D/AI visual with energetic beer celebration mood.',
        'cover': 'assets/img/placeholders/cheers-to-victory.svg',
        'client': 'Internal Concept',
        'year': '2024',
        'scope': '3D Modeling, AI Generation, Compositing',
        'output': 'Key Visual Portfolio',
        'content': [
            'Cheers to Victory combines 3D asset modeling and AI-generated concepts to create a high-impact celebration scene.',
            'Focused on golden lighting, dynamic splash physics, and high-energy motion design cues to establish PMF for sports campaigns.',
            'This exploration serves as an agency benchmark for fast key visual turnarounds.'
        ],
        'gallery': [
            'assets/img/placeholders/cheers-to-victory.svg',
            'assets/img/placeholders/bt-studio-cgi-beverage-demo.svg',
            'assets/img/placeholders/stride-beyond.svg',
            'assets/img/placeholders/huda-beach-carnival-2023.svg'
        ],
        'prev': 'stride-beyond',
        'next': 'afc-key-visual'
    },
    'afc-key-visual': {
        'type': 'cgi-hybrid',
        'title': 'AFC Key Visual',
        'tags': ['3D Model', 'Key Visuals'],
        'lead': 'High-impact sports key visual direction and product composition.',
        'cover': 'assets/img/placeholders/afc-key-visual.svg',
        'client': 'AFC Group',
        'year': '2023',
        'scope': '3D Modeling, Lighting, Key Visual Design',
        'output': 'Print, Digital Advertising',
        'content': [
            'Commissioned key visual design for AFC Group\'s seasonal campaign, highlighting corporate precision and athletic energy.',
            'Built geometric metallic elements and optimized custom shader materials to represent speed and premium engineering.',
            'The visuals were distributed across digital touchpoints and brand keynotes.'
        ],
        'gallery': [
            'assets/img/placeholders/afc-key-visual.svg',
            'assets/img/placeholders/stride-beyond.svg',
            'assets/img/placeholders/circuit.svg',
            'assets/img/placeholders/twister-pack-visual.svg'
        ],
        'prev': 'cheers-to-victory',
        'next': 'twister-pack-visual'
    },
    'twister-pack-visual': {
        'type': 'cgi-hybrid',
        'title': 'Twister Pack Visual',
        'tags': ['3D Model', 'Key Visuals'],
        'lead': 'Pack-focused 3D visual built for retail and campaign usage.',
        'cover': 'assets/img/placeholders/twister-pack-visual.svg',
        'client': 'Twister Brand',
        'year': '2023',
        'scope': '3D Packaging Render, Asset Creation',
        'output': 'Point of Sale, OOH',
        'content': [
            'Created high-definition pack visual assets for Twister, focusing on plastic/foil material accuracy and vibrant colors.',
            'The lighting setup emphasizes the product shape, giving it a premium shelf-ready feel in commercial environments.',
            'Assets were integrated into regional retail POS layouts and digital advertising.'
        ],
        'gallery': [
            'assets/img/placeholders/twister-pack-visual.svg',
            'assets/img/placeholders/afc-key-visual.svg',
            'assets/img/placeholders/stride-beyond.svg',
            'assets/img/placeholders/nexora.svg'
        ],
        'prev': 'afc-key-visual',
        'next': 'halida-tet-2022-key-visual'
    },
    'halida-tet-2022-key-visual': {
        'type': 'cgi-hybrid',
        'title': 'Halida Tet 2022 Key Visual',
        'tags': ['3D Model', 'Key Visuals'],
        'lead': 'Seasonal Tet composition combining beer product and festive energy.',
        'cover': 'assets/img/placeholders/halida-tet-2022-key-visual.svg',
        'client': 'Halida Beer',
        'year': '2022',
        'scope': '3D Packaging Render, Creative Direction',
        'output': 'OOH, Retail POS, Digital Packaging',
        'content': [
            'Developed the signature 3D visual assets for Halida Beer\'s Tet 2022 campaign, integrating cultural elements with corporate visuals.',
            'Rendered golden crest assets and liquid droplets, producing a crisp, festive premium feel.',
            'The campaign visuals saw wide distribution across retail, digital, and OOH billboards.'
        ],
        'gallery': [
            'assets/img/placeholders/halida-tet-2022-key-visual.svg',
            'assets/img/placeholders/bt-studio-cgi-beverage-demo.svg',
            'assets/img/placeholders/cheers-to-victory.svg',
            'assets/img/placeholders/huda-beach-carnival-2023.svg'
        ],
        'prev': 'twister-pack-visual',
        'next': 'huda-beach-carnival-2023'
    },
    'huda-beach-carnival-2023': {
        'type': 'cgi-hybrid',
        'title': 'Huda Beach Carnival 2023',
        'tags': ['3D Model', 'Key Visuals'],
        'lead': 'Event visual with beach, summer, and brand-world atmosphere.',
        'cover': 'assets/img/placeholders/huda-beach-carnival-2023.svg',
        'client': 'Huda Beer',
        'year': '2023',
        'scope': '3D Environment Modeling, Key Visual',
        'output': 'OOH, Event Branding',
        'content': [
            'An immersive 3D scene designed to establish Huda Beach Carnival 2023\'s key visual theme.',
            'Modeled the stylized stage, beach landscape, and sunset atmospheric glows to reflect energetic carnival moods.',
            'Deployed widely on OOH billboards, stage banners, and digital ticket passes.'
        ],
        'gallery': [
            'assets/img/placeholders/huda-beach-carnival-2023.svg',
            'assets/img/placeholders/bt-studio-cgi-huda-football.svg',
            'assets/img/placeholders/cheers-to-victory.svg',
            'assets/img/placeholders/halida-tet-2022-key-visual.svg'
        ],
        'prev': 'halida-tet-2022-key-visual',
        'next': 'circuit'
    },
    'circuit': {
        'type': 'ui-showcase',
        'title': 'Circuit',
        'tags': ['Web Design'],
        'lead': 'Visual interface direction for a modern digital product concept.',
        'cover': 'assets/img/placeholders/circuit.svg',
        'client': 'Circuit Tech',
        'year': '2023',
        'scope': 'UI/UX Visual Design, Concept Development',
        'output': 'Web Application Design',
        'content': [
            'A visual interface design showcasing complex data visualization in a sleek, glassmorphic layout.',
            'Created custom icons, interactive dashboards, and color systems designed for premium readability.',
            'The project serves as a showcase of visual UI direction for tech applications.'
        ],
        'gallery': [
            'assets/img/placeholders/circuit.svg',
            'assets/img/placeholders/astralis.svg',
            'assets/img/placeholders/stride-beyond.svg',
            'assets/img/placeholders/nexora.svg'
        ],
        'prev': 'huda-beach-carnival-2023',
        'next': 'spectral'
    },
    'spectral': {
        'type': 'album',
        'title': 'Spectral',
        'tags': ['Web Design'],
        'lead': 'Prismatic light dispersion and volumetric color studies.',
        'cover': 'assets/img/placeholders/spectral.svg',
        'client': 'Internal Concept',
        'year': '2024',
        'scope': 'AI Concept Generation, Color Study',
        'output': 'Fine Art Print',
        'content': [
            'Spectral is a visual concept series focusing on volumetric light, light diffraction, and high-saturation color theory.',
            'Used AI systems to generate complex prism refractions, enhanced by post-production sharpening and detail painting.',
            'Featured in visual arts blogs and printed for private collectors.'
        ],
        'gallery': [
            'assets/img/placeholders/spectral.svg',
            'assets/img/placeholders/astralis.svg',
            'assets/img/placeholders/stride-beyond.svg',
            'assets/img/placeholders/nexora.svg'
        ],
        'prev': 'circuit',
        'next': 'nexora'
    },
    'nexora': {
        'type': 'ui-showcase',
        'title': 'Nexora',
        'tags': ['Branding'],
        'lead': 'Brand system exploration with premium futuristic identity cues.',
        'cover': 'assets/img/placeholders/nexora.svg',
        'client': 'Nexora Labs',
        'year': '2025',
        'scope': '3D Modeling, Branding, Visual Design',
        'output': 'Visual Identity, Product Concept',
        'content': [
            'Nexora is a comprehensive brand system exploration built for a next-generation tech enterprise. The creative goal was to merge organic shapes with mechanical precision, producing a brand feel that is both human and advanced.',
            'We developed a set of 3D metallic structures that form the core brand patterns, utilizing complex lighting setups to highlight the chrome and frosted-glass surfaces.',
            'The project established Nexora\'s brand guidelines, visual assets, and high-impact concept boards for print and digital channels.'
        ],
        'gallery': [
            'assets/img/placeholders/nexora.svg',
            'assets/img/placeholders/circuit.svg',
            'assets/img/placeholders/astralis.svg',
            'assets/img/placeholders/spectral.svg'
        ],
        'prev': 'spectral',
        'next': 'astralis'
    },
    'astralis': {
        'type': 'album',
        'title': 'Astralis',
        'tags': ['Film'],
        'lead': 'Film-inspired visual direction with atmospheric narrative framing.',
        'cover': 'assets/img/placeholders/astralis.svg',
        'client': 'Internal Concept',
        'year': '2024',
        'scope': 'AI Prompt Engineering, Post-processing',
        'output': 'Digital Art Print',
        'content': [
            'Astralis explores generative techniques to render abstract cosmic phenomena, scale shifts, and nebulous light patterns.',
            'Processed high-resolution outputs with manual digital retouching to restore fine details and contrast depth.',
            'The series has been printed on metallic paper for display in visual showcases.'
        ],
        'gallery': [
            'assets/img/placeholders/astralis.svg',
            'assets/img/placeholders/spectral.svg',
            'assets/img/placeholders/stride-beyond.svg',
            'assets/img/placeholders/circuit.svg'
        ],
        'prev': 'nexora',
        'next': 'bt-studio-cgi-beverage-demo'
    },
    'bt-studio-cgi-beverage-demo': {
        'type': 'cgi-hybrid',
        'title': 'BT Studio – CGI Beverage Demo',
        'tags': ['Branding', 'CGI'],
        'lead': 'Product-led CGI beverage demo with polished advertising finish.',
        'cover': 'assets/img/placeholders/bt-studio-cgi-beverage-demo.svg',
        'client': 'BT Studio',
        'year': '2024',
        'scope': 'CGI, Product Render, Liquid Physics',
        'output': 'Digital Campaign, Print Ads',
        'content': [
            'This project serves as a showcase of high-end CGI product rendering and liquid simulation capabilities, designed for beverage advertisements.',
            'Using advanced particle physics and raytracing inside 3D suites, we captured the fresh condensation, realistic splashing, and premium refraction through glass and aluminum.',
            'The assets are optimized for print campaigns and high-definition digital display networks, demonstrating commercial production-grade finish.'
        ],
        'gallery': [
            'assets/img/placeholders/bt-studio-cgi-beverage-demo.svg',
            'assets/img/placeholders/bt-studio-cgi-huda-football.svg',
            'assets/img/placeholders/cheers-to-victory.svg',
            'assets/img/placeholders/huda-beach-carnival-2023.svg'
        ],
        'prev': 'astralis',
        'next': 'tvc-ovaltine-2015-adaptation'
    }
}

# Common HTML Head, Header, Footer templates
head_tpl = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Luong Huynh</title>
  <meta name="description" content="Case study for {title} by Luong Huynh — Digital Artist.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
<div class="lh-page">

<header class="lh-header">
  <div class="lh-container lh-nav">
    <a class="lh-brand" href="index.html" aria-label="Luong Huynh homepage">
      <span class="lh-brand-mark">LH</span>
      <span>Luong Huynh</span>
    </a>
    <button class="lh-mobile-toggle" type="button" data-menu-toggle aria-expanded="false">Menu</button>
    <nav class="lh-menu" data-menu aria-label="Main navigation">
      <a data-nav href="index.html">Homepage</a>
      <a data-nav href="portfolio.html">Portfolio</a>
      <a data-nav href="about.html">About</a>
      <a class="lh-nav-cta" href="#contact">Available for Work</a>
    </nav>
  </div>
</header>
"""

tvc_media_tpl = """
  <!-- ── VIDEO COVER (TVC) ────────────────────────────── -->
  <div class="lh-container">
    <div class="lh-reveal" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: var(--lh-radius-lg); background: var(--lh-panel); margin-block: clamp(32px, 5vw, 72px); border: 1px solid var(--lh-line);">
      <iframe src="https://player.vimeo.com/video/placeholder" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>
"""

album_media_tpl = """
  <!-- ── DYNAMIC ART SHOWCASE (ALBUM) ──────────────────── -->
  <div class="lh-container">
    <div class="lh-reveal" style="display: grid; grid-template-columns: 2fr 1fr; gap: clamp(12px, 2vw, 24px); margin-block: clamp(32px, 5vw, 72px);">
      <img src="{cover}" alt="Primary artwork" style="width: 100%; aspect-ratio: 4/3; object-fit: cover; border-radius: var(--lh-radius-lg); border: 1px solid var(--lh-line);">
      <div style="display: flex; flex-direction: column; gap: clamp(12px, 2vw, 24px);">
        <img src="{img1}" alt="Detail artwork 1" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: var(--lh-radius-md); border: 1px solid var(--lh-line);">
        <img src="{img2}" alt="Detail artwork 2" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: var(--lh-radius-md); border: 1px solid var(--lh-line);">
      </div>
    </div>
  </div>
"""

cgi_media_tpl = """
  <!-- ── COVER IMAGE ─────────────────────────────────── -->
  <div class="lh-container">
    <img class="lh-detail-cover lh-reveal" src="{cover}" alt="CGI main render">
  </div>
"""

ui_media_tpl = """
  <!-- ── DASHBOARD PREVIEW ───────────────────────────── -->
  <div class="lh-container">
    <img class="lh-detail-cover lh-reveal" src="{cover}" alt="Interface preview" style="border: 1px solid var(--lh-line);">
  </div>
"""

body_start_tpl = """
  <main>
    <!-- ── DETAIL HERO ─────────────────────────────────── -->
    <section class="lh-section lh-detail-hero">
      <div class="lh-container">
        <div class="lh-detail-meta lh-reveal">
          {chips}
        </div>
        <h1 class="lh-detail-title lh-reveal lh-reveal-d1">{title}</h1>
        <p class="lh-detail-lead lh-reveal lh-reveal-d2">{lead}</p>
      </div>
    </section>
"""

body_middle_tpl = """
    <!-- ── DETAIL BODY ─────────────────────────────────── -->
    <section class="lh-section">
      <div class="lh-container">
        <div class="lh-detail-body">
  
          <!-- Sidebar: project info -->
          <aside class="lh-detail-sidebar lh-reveal">
            <div class="lh-detail-info-row">
              <div class="lh-detail-info-label">Client</div>
              <div class="lh-detail-info-value">{client}</div>
            </div>
            <div class="lh-detail-info-row">
              <div class="lh-detail-info-label">Year</div>
              <div class="lh-detail-info-value">{year}</div>
            </div>
            <div class="lh-detail-info-row">
              <div class="lh-detail-info-label">Scope</div>
              <div class="lh-detail-info-value">{scope}</div>
            </div>
            <div class="lh-detail-info-row">
              <div class="lh-detail-info-label">Output</div>
              <div class="lh-detail-info-value">{output}</div>
            </div>
            <div style="margin-top: 32px;">
              <a class="lh-button lh-button-primary" href="portfolio.html">Back to Portfolio</a>
            </div>
          </aside>
  
          <!-- Main content -->
          <div class="lh-detail-content lh-reveal lh-reveal-d1">
            {paragraphs}
          </div>
  
        </div>
"""

ui_specs_tpl = """
        <!-- ── UI/UX SYSTEM SPEC SHEET ────────────────────── -->
        <div class="lh-reveal" style="margin-block: clamp(32px, 5vw, 64px); padding: clamp(24px, 4vw, 48px); background: var(--lh-bg-soft); border-radius: var(--lh-radius-lg); border: 1px solid var(--lh-line);">
          <h3 style="font-family: var(--font-display); font-size: 20px; margin-bottom: 24px; text-transform: uppercase; color: var(--lh-text);">Design System Tokens</h3>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px;">
            <div>
              <h4 style="font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; color: var(--lh-accent); margin-bottom: 8px;">Palette</h4>
              <div style="display: flex; gap: 8px;">
                <span style="width: 24px; height: 24px; background: #00f0ff; border-radius: 4px; display: inline-block;" title="Cyan Accent"></span>
                <span style="width: 24px; height: 24px; background: #f4f0e8; border-radius: 4px; display: inline-block; border: 1px solid #333;" title="Text Cream"></span>
                <span style="width: 24px; height: 24px; background: #151515; border-radius: 4px; display: inline-block;" title="Panel Dark"></span>
              </div>
            </div>
            <div>
              <h4 style="font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; color: var(--lh-accent); margin-bottom: 8px;">Typography</h4>
              <div style="font-size: 14px; font-family: var(--font-display-alt); font-weight: 700;">Inter Tight / Satoshi</div>
            </div>
            <div>
              <h4 style="font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; color: var(--lh-accent); margin-bottom: 8px;">Grid System</h4>
              <div style="font-size: 14px;">12-Column Responsive Layout</div>
            </div>
          </div>
        </div>
"""

hybrid_media_gallery_tpl = """
        <!-- ── GALLERY (MIXED STILLS + LOOPS) ────────────── -->
        <div class="lh-detail-gallery lh-reveal">
          <img class="lh-detail-gallery-item" src="{img1}" alt="Detail render 1">
          <div class="lh-detail-gallery-item" style="position: relative; overflow: hidden; background: var(--lh-panel); display: flex; align-items: center; justify-content: center; border: 1px solid var(--lh-line); border-radius: var(--lh-radius-md);">
            <div style="position: absolute; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px; color: var(--lh-muted); font-size: 11px; text-transform: uppercase; font-family: var(--font-mono); font-weight: bold; background: rgba(7, 7, 7, 0.7); inset: 0;">
              <span>Liquid loop render</span>
              <span style="color: var(--lh-accent);">Click to play preview</span>
            </div>
            <video autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover; opacity: 0.5;">
              <source src="" type="video/mp4">
            </video>
          </div>
          <img class="lh-detail-gallery-item" src="{img2}" alt="Detail render 2">
          <img class="lh-detail-gallery-item" src="{img3}" alt="Detail render 3">
        </div>
"""

standard_gallery_tpl = """
        <!-- ── GALLERY ────────────────────────────────────── -->
        <div class="lh-detail-gallery lh-reveal">
          <img class="lh-detail-gallery-item" src="{img0}" alt="Gallery image 1">
          <img class="lh-detail-gallery-item" src="{img1}" alt="Gallery image 2">
          <img class="lh-detail-gallery-item" src="{img2}" alt="Gallery image 3">
          <img class="lh-detail-gallery-item" src="{img3}" alt="Gallery image 4">
        </div>
"""

body_end_tpl = """
      </div>
    </section>
  
    <!-- ── PROJECT NAVIGATION ──────────────────────────── -->
    <div class="lh-container">
      <nav class="lh-project-nav" aria-label="Project navigation">
        <a class="lh-project-nav-item" href="{prev_link}">
          <div class="lh-project-nav-label">← Previous</div>
          <div class="lh-project-nav-title">{prev_title}</div>
        </a>
        <a class="lh-project-nav-item" href="{next_link}" style="text-align: right;">
          <div class="lh-project-nav-label">Next →</div>
          <div class="lh-project-nav-title">{next_title}</div>
        </a>
      </nav>
    </div>
  
    <!-- ── CTA ─────────────────────────────────────────── -->
    <section class="lh-section-tight" id="contact">
      <div class="lh-container">
        <div class="lh-cta">
          <p class="lh-section-kicker">Project Inquiry</p>
          <h2>Need campaign visuals, CGI or AI art direction?</h2>
          <div class="lh-hero-actions">
            <a class="lh-button lh-button-primary" href="mailto:hello@luonghuynh.com">Get in Touch</a>
            <a class="lh-button" href="portfolio.html">Explore Work</a>
          </div>
        </div>
      </div>
    </section>
  
  </main>
  
  <footer class="lh-footer">
    <div class="lh-container lh-footer-grid">
      <div>© 2026 Luong Huynh. All rights reserved.</div>
      <div class="lh-socials" aria-label="Social links">
        <a href="https://behance.com" target="_blank" rel="noreferrer">Behance</a>
        <a href="https://dribbble.com" target="_blank" rel="noreferrer">Dribbble</a>
        <a href="https://instagram.com" target="_blank" rel="noreferrer">Instagram</a>
        <a href="https://linkedin.com" target="_blank" rel="noreferrer">LinkedIn</a>
      </div>
    </div>
  </footer>
  
  </div>
  <script src="assets/js/main.js"></script>
  </body>
  </html>
"""

# Output directory
out_dir = "front-end"

for slug, p in projects.items():
    html_content = ""
    
    # 1. Header
    html_content += head_tpl.format(title=p['title'])
    
    # 2. Hero Section
    chips_html = "".join([f'<span class="lh-chip{"" if i > 0 else " lh-chip-strong"}">{tag}</span>\n' for i, tag in enumerate(p['tags'])])
    html_content += body_start_tpl.format(chips=chips_html, title=p['title'], lead=p['lead'])
    
    # 3. Media Header (covers, carousels, mockups, players)
    if p['type'] == 'tvc':
        html_content += tvc_media_tpl
    elif p['type'] == 'album':
        html_content += album_media_tpl.format(cover=p['cover'], img1=p['gallery'][1], img2=p['gallery'][2])
    elif p['type'] == 'ui-showcase':
        html_content += ui_media_tpl.format(cover=p['cover'])
    else: # cgi-hybrid
        html_content += cgi_media_tpl.format(cover=p['cover'])
        
    # 4. Info Sidebar & Paragraphs
    p_html = "".join([f"<p>{text}</p>\n" for text in p['content']])
    html_content += body_middle_tpl.format(
        client=p['client'],
        year=p['year'],
        scope=p['scope'],
        output=p['output'],
        paragraphs=p_html
    )
    
    # 5. UI Specs (for ui-showcase only)
    if p['type'] == 'ui-showcase':
        html_content += ui_specs_tpl
        
    # 6. Gallery
    if p['type'] == 'cgi-hybrid':
        html_content += hybrid_media_gallery_tpl.format(
            img1=p['gallery'][1],
            img2=p['gallery'][2],
            img3=p['gallery'][3]
        )
    else:
        html_content += standard_gallery_tpl.format(
            img0=p['gallery'][0],
            img1=p['gallery'][1],
            img2=p['gallery'][2],
            img3=p['gallery'][3]
        )
        
    # 7. Navigation & Footer
    prev_project = projects[p['prev']]
    next_project = projects[p['next']]
    html_content += body_end_tpl.format(
        prev_link=f"{p['prev']}.html",
        prev_title=prev_project['title'],
        next_link=f"{p['next']}.html",
        next_title=next_project['title']
    )
    
    # Write file
    file_path = os.path.join(out_dir, f"{slug}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated {file_path}")

print("Successfully generated all project files!")
