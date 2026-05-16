"""
Generate valid Elementor Container (flexbox) JSON templates for all three pages.
Run: python scripts/gen_elementor_json.py
Output: elementor/homepage-template.json
        elementor/portfolio-template.json
        elementor/about-template.json
"""

import json, random, string, os

# ──────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────

def uid():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=8))

def container(settings, elements, is_inner=False):
    return {
        "id": uid(),
        "elType": "container",
        "isInner": is_inner,
        "settings": settings,
        "elements": elements,
    }

def widget(widget_type, settings):
    return {
        "id": uid(),
        "elType": "widget",
        "widgetType": widget_type,
        "isInner": False,
        "settings": settings,
        "elements": [],
    }

def heading(text, tag, css=""):
    s = {"title": text, "header_size": tag}
    if css:
        s["css_classes"] = css
    return widget("heading", s)

def richtext(html, css=""):
    s = {"editor": html}
    if css:
        s["css_classes"] = css
    return widget("text-editor", s)

def html_widget(html):
    return widget("html", {"html": html})

def btn(text, url, css):
    return widget("button", {
        "text": text,
        "link": {"url": url, "is_external": False, "nofollow": False},
        "css_classes": css,
    })

# ──────────────────────────────────────────────────────────
# Reusable section wrappers
# ──────────────────────────────────────────────────────────

def lh_section(css_classes, inner_elements):
    """Full-width outer section -> boxed inner container (lh-container)."""
    return container(
        {
            "css_classes": css_classes,
            "flex_direction": "column",
            "content_width": "full",
        },
        [
            container(
                {
                    "css_classes": "lh-container",
                    "flex_direction": "column",
                    "content_width": "boxed",
                    "boxed_width": {"unit": "px", "size": 1440, "sizes": {}},
                    "gap": {"unit": "px", "size": 0, "isLinked": True},
                },
                inner_elements,
                is_inner=True,
            )
        ],
    )

def section_head(kicker_text, title_text, copy_text, h_tag="h2"):
    """Two-column section header: left = kicker+title, right = copy."""
    return container(
        {
            "css_classes": "lh-section-head",
            "flex_direction": "row",
            "flex_align_items": "flex-end",
            "gap": {"unit": "px", "size": 32, "isLinked": True},
        },
        [
            container(
                {"flex_direction": "column", "gap": {"unit": "px", "size": 14, "isLinked": True}},
                [
                    heading(kicker_text, "h6", "lh-section-kicker"),
                    heading(title_text, h_tag, "lh-section-title"),
                ],
                is_inner=True,
            ),
            richtext(f"<p>{copy_text}</p>", "lh-section-copy"),
        ],
        is_inner=True,
    )

# ──────────────────────────────────────────────────────────
# Work card + grid HTML helpers
# ──────────────────────────────────────────────────────────

def card_html(img, title, desc, cats, tags, link="#"):
    tag_spans = "".join(f'<span class="lh-tag">{t}</span>' for t in tags)
    return (
        f'<article class="lh-work-card" data-categories="{cats}">'
        f'<a href="{link}">'
        f'<div class="lh-work-media">'
        f'<img src="/wp-content/uploads/{img}" alt="{title}" loading="lazy">'
        f"</div>"
        f'<div class="lh-work-info">'
        f'<div class="lh-tag-row">{tag_spans}</div>'
        f'<h3 class="lh-work-title">{title}</h3>'
        f"<p>{desc}</p>"
        f"</div></a></article>"
    )

def work_grid_html(cards, link="#"):
    inner = "\n  ".join(card_html(*c, link=link) for c in cards)
    return f'<div class="lh-work-grid">\n  {inner}\n</div>'

# ──────────────────────────────────────────────────────────
# Capability / service grid HTML helper
# ──────────────────────────────────────────────────────────

def caps_html(items):
    cells = "".join(
        f'<article class="lh-service-card">'
        f'<span class="lh-service-number">{n}</span>'
        f'<div><h3 class="lh-service-title">{title}</h3>'
        f'<p class="lh-service-copy">{blurb}</p></div>'
        f"</article>\n"
        for n, title, blurb in items
    )
    return f'<div class="lh-service-grid">\n{cells}</div>'

# ──────────────────────────────────────────────────────────
# CTA block HTML helper
# ──────────────────────────────────────────────────────────

def cta_html(kicker, title, body, btn1_text, btn1_url, btn2_text=None, btn2_url=None):
    body_p = f"<p>{body}</p>" if body else ""
    btn2 = (
        f'<a class="lh-button" href="{btn2_url}">{btn2_text}</a>'
        if btn2_text else ""
    )
    return (
        f'<div class="lh-cta">'
        f'<p class="lh-section-kicker">{kicker}</p>'
        f"<h2>{title}</h2>"
        f"{body_p}"
        f'<div class="lh-hero-actions">'
        f'<a class="lh-button lh-button-primary" href="{btn1_url}">{btn1_text}</a>'
        f"{btn2}"
        f"</div></div>"
    )

# ──────────────────────────────────────────────────────────
# Content data
# ──────────────────────────────────────────────────────────

CAPS_HOME = [
    ("01", "3D Product & CGI Visuals",            "Premium product compositions, pack shots and campaign-ready CGI scenes."),
    ("02", "AI Campaign Imagery",                  "AI-assisted visual exploration, concept boards and stylized brand imagery."),
    ("03", "VFX & Post-production",                "Compositing, retouching, enhancement and cinematic finishing for moving or still assets."),
    ("04", "Visual Direction",                     "Campaign look development, key visual systems and production-ready visual storytelling."),
]

CAPS_ABOUT = [
    ("01", "3D Modeling & Scene Design",  "Product-centric 3D scenes and stylized campaign worlds."),
    ("02", "Generative Art Direction",    "AI image workflows refined into premium, brand-safe visual directions."),
    ("03", "VFX & Compositing",           "Cinematic polish, retouching and post-production integration."),
    ("04", "Campaign Key Visuals",        "Hero images, visual systems and adaptations for brand campaigns."),
]

CARDS_HOME = [
    ("stride-beyond.jpg",      "Stride Beyond",                 "AI-led identity exploration for a futuristic visual language.",     "ai branding",  ["AI Generated", "Branding"]),
    ("nexora.jpg",             "Nexora",                        "Brand system exploration with premium futuristic identity cues.",   "branding",     ["Branding"]),
    ("bt-studio-beverage.jpg", "BT Studio – CGI Beverage Demo", "Product-led CGI beverage demo with polished advertising finish.", "branding cgi", ["Branding", "CGI"]),
]

CARDS_ALL = [
    ("tvc-ovaltine.jpg",       "TVC Ovaltine 2015 Adaptation",         "Campaign adaptation with cinematic product treatment.",              "tvc",         ["TVC"]),
    ("bt-studio-huda.jpg",     "BT Studio – CGI Huda Football",   "CGI beer-football visual system for energetic campaign assets.",     "cgi feature", ["CGI", "Feature"]),
    ("stride-beyond.jpg",      "Stride Beyond",                        "AI-led identity exploration for a futuristic visual language.",     "ai branding", ["AI Generated", "Branding"]),
    ("cheers-to-victory.jpg",  "Cheers to Victory",                    "Victory-themed 3D/AI visual with energetic beer celebration mood.", "3d ai",       ["3D Model", "AI Generated"]),
    ("afc-key-visual.jpg",     "AFC Key Visual",                        "High-impact sports key visual direction and product composition.",  "3d keyvisual",["3D Model", "Key Visuals"]),
    ("twister-pack-visual.jpg","Twister Pack Visual",                   "Pack-focused 3D visual built for retail and campaign usage.",       "3d keyvisual",["3D Model", "Key Visuals"]),
    ("halida-tet-2022.jpg",    "Halida Tet 2022 Key Visual",           "Seasonal Tet composition combining beer product and festive energy.","3d keyvisual",["3D Model", "Key Visuals"]),
    ("huda-beach-carnival.jpg","Huda Beach Carnival 2023",              "Event visual with beach, summer, and brand-world atmosphere.",      "3d keyvisual",["3D Model", "Key Visuals"]),
    ("circuit.jpg",            "Circuit",                               "Visual interface direction for a modern digital product concept.",  "web",         ["Web Design"]),
    ("spectral.jpg",           "Spectral",                              "Editorial web concept with atmospheric motion and dark UI styling.","web",         ["Web Design"]),
    ("nexora.jpg",             "Nexora",                                "Brand system exploration with premium futuristic identity cues.",   "branding",    ["Branding"]),
    ("astralis.jpg",           "Astralis",                              "Film-inspired visual direction with atmospheric narrative framing.","film",        ["Film"]),
    ("bt-studio-beverage.jpg", "BT Studio – CGI Beverage Demo",   "Product-led CGI beverage demo with polished advertising finish.",   "branding cgi",["Branding", "CGI"]),
]

FILTER_BTNS = [
    ("all","All"), ("3d","3D Model"), ("ai","AI Generated"), ("branding","Branding"),
    ("cgi","CGI"), ("feature","Feature"), ("film","Film"), ("keyvisual","Key Visuals"),
    ("tvc","TVC"), ("web","Web Design"),
]

def portfolio_block_html():
    pills = "".join(
        f'<button class="lh-filter-btn{"  is-active" if slug == "all" else ""}" data-filter="{slug}">{label}</button>'
        for slug, label in FILTER_BTNS
    )
    grid = work_grid_html(CARDS_ALL)
    js = (
        "<script>(function(){"
        "var btns=document.querySelectorAll('[data-filter]');"
        "var cards=document.querySelectorAll('[data-categories]');"
        "btns.forEach(function(b){b.addEventListener('click',function(){"
        "var f=b.dataset.filter;"
        "btns.forEach(function(x){x.classList.remove('is-active')});"
        "b.classList.add('is-active');"
        "cards.forEach(function(c){"
        "c.hidden=!(f==='all'||c.dataset.categories.includes(f));"
        "});});});"
        "})();</script>"
    )
    return (
        f'<div class="lh-filter-bar" aria-label="Portfolio filters">{pills}</div>\n'
        + grid
        + "\n"
        + js
    )

ABOUT_BIO_HTML = (
    '<div class="lh-rich-text">'
    '<span class="lh-eyebrow">About</span>'
    "<h1>Digital Artist &amp; Visual Technologist.</h1>"
    "<p>I’m a digital artist focused on 3D visuals, AI-generated images and VFX."
    " I collaborate with brands, agencies and production teams to create campaign-ready visuals,"
    " cinematic key visuals and experimental AI-assisted imagery.</p>"
    "<p>Based in Ho Chi Minh City, I work across the full visual pipeline —"
    " from concept and art direction through to production-finished assets"
    " ready for print, digital and broadcast.</p>"
    '<ul class="lh-list">'
    "<li><strong>Focus</strong><span>3D product visuals, AI-generated art, CGI key visuals,"
    " campaign image systems and VFX finishing.</span></li>"
    "<li><strong>Clients</strong><span>Brands, agencies, production teams and campaign creators"
    " needing high-impact visuals.</span></li>"
    "<li><strong>Approach</strong><span>Blend art direction, generative workflows, compositing"
    " and production sensibility into finished assets.</span></li>"
    "<li><strong>Output</strong><span>Key visuals, product renders, pitch frames, social campaign"
    " assets, launch imagery and moving-image look development.</span></li>"
    "</ul>"
    "</div>"
)

ABOUT_PORTRAIT_HTML = (
    '<div class="lh-portrait-panel">'
    '<img class="lh-portrait"'
    ' src="/wp-content/uploads/luong-huynh-portrait.jpg"'
    ' alt="Luong Huynh portrait" loading="eager">'
    '<div class="lh-hero-card-caption">'
    '<div class="lh-meta-row">'
    '<span class="lh-chip lh-chip-strong">Digital Artist</span>'
    '<span class="lh-chip">Ho Chi Minh City</span>'
    "</div></div></div>"
)

# ──────────────────────────────────────────────────────────
# HOMEPAGE template
# ──────────────────────────────────────────────────────────

hero = container(
    {
        "css_classes": "lh-hero",
        "flex_direction": "column",
        "content_width": "full",
        "flex_justify_content": "flex-end",
        "min_height": {"unit": "vh", "size": 92, "sizes": {}},
        "background_background": "classic",
        "background_color": "#070707",
    },
    [
        container(
            {
                "css_classes": "lh-hero-body lh-container",
                "flex_direction": "column",
                "content_width": "boxed",
                "boxed_width": {"unit": "px", "size": 1440, "sizes": {}},
                "flex_align_items": "flex-start",
                "gap": {"unit": "px", "size": 0, "isLinked": True},
                "padding": {
                    "unit": "px",
                    "top": "0", "right": "0",
                    "bottom": "96", "left": "0",
                    "isLinked": False,
                },
            },
            [
                richtext('<p class="lh-eyebrow">Ho Chi Minh City · 2026</p>'),
                heading("Cinematic digital art", "h1", "lh-hero-title"),
                richtext(
                    "<p>Digital Artist crafting 3D visuals, AI-generated imagery"
                    " and VFX for brands, campaigns and cinematic stories.</p>",
                    "lh-hero-copy",
                ),
                container(
                    {
                        "flex_direction": "row",
                        "flex_wrap": "wrap",
                        "gap": {"unit": "px", "size": 14, "isLinked": True},
                        "css_classes": "lh-hero-actions",
                    },
                    [
                        btn("View Portfolio", "/portfolio/", "lh-button lh-button-primary"),
                        btn("About Luong", "/about/", "lh-button"),
                    ],
                    is_inner=True,
                ),
            ],
            is_inner=True,
        )
    ],
)

featured_work = lh_section("lh-section", [
    section_head(
        "Featured work",
        "Selected visuals with campaign-grade finish.",
        "A focused selection of recent campaign imagery, CGI and AI-generated visuals"
        " — spanning brand identity, product worlds and key visual systems.",
    ),
    html_widget(work_grid_html(CARDS_HOME, link="/portfolio/")),
])

services_home = lh_section("lh-section lh-section-muted", [
    section_head(
        "Services",
        "Built for visual campaigns.",
        "Focused on campaign-grade output for brands, agencies and production teams"
        " who need premium visual assets.",
    ),
    html_widget(caps_html(CAPS_HOME)),
])

cta_home = lh_section("lh-section", [
    html_widget(cta_html(
        "Available for Work",
        "Let’s build the next cinematic brand visual.",
        "Send over the brief, references and target deliverables."
        " I can help shape the visual direction from concept to finished campaign asset.",
        "Get in Touch", "mailto:hello@luonghuynh.com",
        "Explore Work", "/portfolio/",
    )),
])

homepage = {
    "version": "0.4",
    "title": "Luong Huynh — Homepage",
    "type": "page",
    "content": [hero, featured_work, services_home, cta_home],
    "page_settings": {
        "background_background": "classic",
        "background_color": "#070707",
        "hide_title": "yes",
    },
}

# ──────────────────────────────────────────────────────────
# PORTFOLIO PAGE template
# ──────────────────────────────────────────────────────────

portfolio_section = lh_section("lh-section", [
    section_head(
        "Portfolio",
        "A curated archive of 3D, AI, CGI, TVC and brand visuals.",
        "An archive of campaign visuals, product renders, AI-generated imagery"
        " and visual direction work — across CGI, key visuals, branding and film.",
        h_tag="h1",
    ),
    html_widget(portfolio_block_html()),
])

cta_portfolio = lh_section("lh-section-tight", [
    html_widget(cta_html(
        "Project Inquiry",
        "Need campaign visuals, CGI or AI art direction?",
        "",
        "Get in Touch", "mailto:hello@luonghuynh.com",
        "About Luong", "/about/",
    )),
])

portfolio_page = {
    "version": "0.4",
    "title": "Luong Huynh — Portfolio",
    "type": "page",
    "content": [portfolio_section, cta_portfolio],
    "page_settings": {
        "background_background": "classic",
        "background_color": "#070707",
        "hide_title": "yes",
    },
}

# ──────────────────────────────────────────────────────────
# ABOUT PAGE template
# ──────────────────────────────────────────────────────────

about_grid = lh_section("lh-section", [
    container(
        {
            "css_classes": "lh-about-grid",
            "flex_direction": "row",
            "flex_align_items": "flex-start",
            "gap": {"unit": "px", "size": 86, "isLinked": True},
        },
        [
            html_widget(ABOUT_PORTRAIT_HTML),
            html_widget(ABOUT_BIO_HTML),
        ],
        is_inner=True,
    )
])

services_about = lh_section("lh-section lh-section-muted", [
    section_head(
        "Services",
        "Creative services shaped around campaign delivery.",
        "Each project is approached from concept through to production-ready delivery"
        " — visual-first, always.",
    ),
    html_widget(caps_html(CAPS_ABOUT)),
])

cta_about = lh_section("lh-section-tight", [
    html_widget(cta_html(
        "Contact",
        "Available for selected visual campaigns.",
        "For project inquiries, include objective, timeline, references,"
        " deliverables and usage channel.",
        "hello@luonghuynh.com", "mailto:hello@luonghuynh.com",
        "View Work", "/portfolio/",
    )),
])

about_page = {
    "version": "0.4",
    "title": "Luong Huynh — About",
    "type": "page",
    "content": [about_grid, services_about, cta_about],
    "page_settings": {
        "background_background": "classic",
        "background_color": "#070707",
        "hide_title": "yes",
    },
}

# ──────────────────────────────────────────────────────────
# Write files
# ──────────────────────────────────────────────────────────

BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "elementor",
)

FILES = {
    "homepage-template.json":  homepage,
    "portfolio-template.json": portfolio_page,
    "about-template.json":     about_page,
}

for fname, data in FILES.items():
    path = os.path.join(BASE, fname)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    kb = os.path.getsize(path) / 1024
    # count top-level containers and total elements
    def count_elements(node):
        total = 1
        for child in node.get("elements", []):
            total += count_elements(child)
        return total
    total = sum(count_elements(c) for c in data["content"])
    print(f"{fname}  |  {kb:.1f} KB  |  {total} nodes")

print("\nAll templates written to elementor/")
