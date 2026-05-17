'use strict';

const fs   = require('fs');
const path = require('path');

const OUT = __dirname;

// ── CSS (embedded from _reference/global-css.css) ──────────────────────────
const CSS = fs.readFileSync(
  path.join(__dirname, '..', '..', '..', '..', 'elementor_v4', '_reference', 'global-css.css'),
  'utf8'
);

// ── GLOBAL CLASS REGISTRY ──────────────────────────────────────────────────
// IDs match the reference exactly so they can be shared across pages in Elementor
const GC = {
  'lh-hero':           'g-9366cf5',
  'lh-container':      'g-f50942b',
  'lh-hero-body':      'g-0a08ffe',
  'lh-section':        'g-2d400a9',
  'lh-section-muted':  'g-ee5b286',
  'lh-section-head':   'g-22e82fe',
  'lh-cta':            'g-4d79e46',
  'lh-eyebrow':        'g-0273a12',
  'lh-hero-title':     'g-88eb855',
  'lh-hero-copy':      'g-b7b8c19',
  'lh-hero-actions':   'g-df2027f',
  'lh-section-kicker': 'g-ed136ec',
  'lh-section-title':  'g-bf0a5fa',
  'lh-section-copy':   'g-36a1a7e',
  'lh-button':         'g-6c0963d',
  'lh-button-primary': 'g-98193da',
  'lh-service-number': 'g-6ef0cf6',
  'lh-service-title':  'g-49ff9d6',
  'lh-service-copy':   'g-1bf9772',
  'lh-service-card':   'g-035f52a',
  'lh-service-grid':   'g-7cad70c',
  'lh-reveal':         'g-50ee568',
  'is-visible':        'g-dd93f91',
  'lh-reveal-d1':      'g-aca3875',
  'lh-reveal-d2':      'g-96b0e68',
  'lh-reveal-d3':      'g-e333d13',
  'lh-work-grid':      'g-a1b2c3d',
  'lh-work-card':      'g-b2c3d4e',
  'lh-work-body':      'g-c3d4e5f',
  'lh-work-title':     'g-d4e5f6a',
  'lh-meta-row':       'g-e5f6a7b',
  'lh-tag':            'g-f6a7b8c',
  'lh-filter-bar':     'g-a7b8c9d',
  'lh-filter-btn':     'g-b8c9d0e',
  'lh-about-grid':     'g-c9d0e1f',
  'lh-portrait-panel': 'g-d0e1f2a',
  'lh-rich-text':      'g-e1f2a3b',
  'lh-list':           'g-f2a3b4c',
  'lh-detail-hero':    'g-a3b4c5d',
  'lh-detail-title':   'g-b4c5d6e',
  'lh-detail-lead':    'g-c5d6e7f',
  'lh-detail-meta':    'g-d6e7f8a',
  'lh-detail-body':    'g-e7f8a9b',
  'lh-detail-sidebar': 'g-f8a9b0c',
  'lh-detail-content': 'g-a9b0c1d',
  'lh-detail-gallery': 'g-b0c1d2e',
  'lh-project-nav':    'g-c1d2e3f',
};

const GC_META = {
  'g-9366cf5':  { label:'lh-hero', variants:[] },
  'g-f50942b':  { label:'lh-container', variants:[{meta:{breakpoint:'desktop',state:null},props:{display:{'$$type':'string',value:'flex'},'flex-direction':{'$$type':'string',value:'column'}},custom_css:null}] },
  'g-0a08ffe':  { label:'lh-hero-body', variants:[] },
  'g-2d400a9':  { label:'lh-section', variants:[] },
  'g-ee5b286':  { label:'lh-section-muted', variants:[] },
  'g-22e82fe':  { label:'lh-section-head', variants:[{meta:{breakpoint:'desktop',state:null},props:{display:{'$$type':'string',value:'flex'},'flex-direction':{'$$type':'string',value:'row'},'align-items':{'$$type':'string',value:'end'}},custom_css:null}] },
  'g-4d79e46':  { label:'lh-cta', variants:[] },
  'g-0273a12':  { label:'lh-eyebrow', variants:[] },
  'g-88eb855':  { label:'lh-hero-title', variants:[{meta:{breakpoint:'desktop',state:null},props:{'font-family':{'$$type':'string',value:'Newake'},'font-weight':{'$$type':'string',value:'500'}},custom_css:null}] },
  'g-b7b8c19':  { label:'lh-hero-copy', variants:[] },
  'g-df2027f':  { label:'lh-hero-actions', variants:[] },
  'g-ed136ec':  { label:'lh-section-kicker', variants:[] },
  'g-bf0a5fa':  { label:'lh-section-title', variants:[{meta:{breakpoint:'desktop',state:null},props:{'font-family':{'$$type':'string',value:'Newake'}},custom_css:null}] },
  'g-36a1a7e':  { label:'lh-section-copy', variants:[] },
  'g-6c0963d':  { label:'lh-button', variants:[] },
  'g-98193da':  { label:'lh-button-primary', variants:[] },
  'g-6ef0cf6':  { label:'lh-service-number', variants:[] },
  'g-49ff9d6':  { label:'lh-service-title', variants:[] },
  'g-1bf9772':  { label:'lh-service-copy', variants:[] },
  'g-035f52a':  { label:'lh-service-card', variants:[{meta:{breakpoint:'desktop',state:null},props:{display:{'$$type':'string',value:'flex'}},custom_css:null}] },
  'g-7cad70c':  { label:'lh-service-grid', variants:[{meta:{breakpoint:'desktop',state:null},props:{display:{'$$type':'string',value:'flex'}},custom_css:null}] },
  'g-50ee568':  { label:'lh-reveal', variants:[] },
  'g-dd93f91':  { label:'is-visible', variants:[] },
  'g-aca3875':  { label:'lh-reveal-d1', variants:[] },
  'g-96b0e68':  { label:'lh-reveal-d2', variants:[] },
  'g-e333d13':  { label:'lh-reveal-d3', variants:[] },
  'g-a1b2c3d':  { label:'lh-work-grid', variants:[] },
  'g-b2c3d4e':  { label:'lh-work-card', variants:[] },
  'g-c3d4e5f':  { label:'lh-work-body', variants:[] },
  'g-d4e5f6a':  { label:'lh-work-title', variants:[] },
  'g-e5f6a7b':  { label:'lh-meta-row', variants:[] },
  'g-f6a7b8c':  { label:'lh-tag', variants:[] },
  'g-a7b8c9d':  { label:'lh-filter-bar', variants:[] },
  'g-b8c9d0e':  { label:'lh-filter-btn', variants:[] },
  'g-c9d0e1f':  { label:'lh-about-grid', variants:[] },
  'g-d0e1f2a':  { label:'lh-portrait-panel', variants:[] },
  'g-e1f2a3b':  { label:'lh-rich-text', variants:[] },
  'g-f2a3b4c':  { label:'lh-list', variants:[] },
  'g-a3b4c5d':  { label:'lh-detail-hero', variants:[] },
  'g-b4c5d6e':  { label:'lh-detail-title', variants:[] },
  'g-c5d6e7f':  { label:'lh-detail-lead', variants:[] },
  'g-d6e7f8a':  { label:'lh-detail-meta', variants:[] },
  'g-e7f8a9b':  { label:'lh-detail-body', variants:[] },
  'g-f8a9b0c':  { label:'lh-detail-sidebar', variants:[] },
  'g-a9b0c1d':  { label:'lh-detail-content', variants:[] },
  'g-b0c1d2e':  { label:'lh-detail-gallery', variants:[] },
  'g-c1d2e3f':  { label:'lh-project-nav', variants:[] },
};

// ── HELPERS ────────────────────────────────────────────────────────────────

const usedIds = new Set();

function uid(id) {
  if (usedIds.has(id)) throw new Error(`Duplicate element ID: ${id}`);
  usedIds.add(id);
  return id;
}

function resetIds() { usedIds.clear(); }

const usedGC = new Set();

function cls(...labels) {
  return {
    '$$type': 'classes',
    value: labels.map(l => {
      if (!GC[l]) throw new Error(`Unknown class: ${l}`);
      usedGC.add(GC[l]);
      return GC[l];
    })
  };
}

function htmlV3(text) {
  return { '$$type':'html-v3', value:{ content:{'$$type':'string',value:text}, children:[] } };
}

function lnk(url) {
  if (!url) return { '$$type':'link', value:[] };
  return { '$$type':'link', value:{ destination:{'$$type':'url',value:url} } };
}

// e-flexbox: top-level section
function section(id, classLabels, elements, tag, cssid, title) {
  const s = {};
  if (classLabels && classLabels.length) s.classes = cls(...classLabels);
  s.tag = { '$$type':'string', value: tag || 'section' };
  s.link = lnk(null);
  if (cssid) s._cssid = { '$$type':'string', value: cssid };
  return { id:uid(id), settings:s, elements, isInner:false, elType:'e-flexbox', styles:[], interactions:[], editor_settings: title ? {title} : [], version:'0.0' };
}

// e-div-block with classes
function div(id, classLabels, elements, localStyles, title, tag) {
  const s = {};
  if (classLabels && classLabels.length) s.classes = cls(...classLabels);
  if (tag) s.tag = { '$$type':'string', value:tag };
  s.link = lnk(null);
  return { id:uid(id), settings:s, elements, isInner:false, elType:'e-div-block', styles: localStyles || [], interactions:[], editor_settings: title ? {title} : [], version:'0.0' };
}

// e-div-block with no settings (empty array per reference)
function divEmpty(id, elements, localStyles, title) {
  return { id:uid(id), settings:[], elements, isInner:false, elType:'e-div-block', styles: localStyles || [], interactions:[], editor_settings: title ? {title} : [], version:'0.0' };
}

function para(id, classLabels, text, tag, title) {
  const s = {};
  if (classLabels && classLabels.length) s.classes = cls(...classLabels);
  s.paragraph = htmlV3(text);
  if (tag) s.tag = { '$$type':'string', value:tag };
  s.link = lnk(null);
  return { id:uid(id), settings:s, elements:[], isInner:false, widgetType:'e-paragraph', elType:'widget', styles:[], interactions:[], editor_settings: title ? {title} : [], version:'0.0' };
}

function head(id, classLabels, text, tag, title) {
  const s = {};
  if (classLabels && classLabels.length) s.classes = cls(...classLabels);
  s.title = htmlV3(text);
  if (tag) s.tag = { '$$type':'string', value:tag };
  s.link = lnk(null);
  return { id:uid(id), settings:s, elements:[], isInner:false, widgetType:'e-heading', elType:'widget', styles:[], interactions:[], editor_settings: title ? {title} : [], version:'0.0' };
}

function btn(id, classLabels, text, url) {
  const s = {};
  if (classLabels && classLabels.length) s.classes = cls(...classLabels);
  s.text = htmlV3(text);
  s.link = lnk(url);
  return { id:uid(id), settings:s, elements:[], isInner:false, widgetType:'e-button', elType:'widget', styles:[], interactions:[], editor_settings:[], version:'0.0' };
}

function htmlWidget(id, html) {
  return { id:uid(id), settings:{html}, elements:[], isInner:false, widgetType:'html', elType:'widget', styles:[], interactions:[], editor_settings:[], version:'0.0' };
}

function localStyle(elemId, localId, props) {
  const key = `e-${elemId}-${localId}`;
  return { [key]:{ id:key, label:'local', type:'class', variants:[{meta:{breakpoint:'desktop',state:null},props,custom_css:null}] } };
}

// Build global_classes from only the IDs actually used in this page
function buildGlobalClasses() {
  const items = {};
  const order = [];
  for (const id of usedGC) {
    if (!GC_META[id]) throw new Error(`Missing GC_META for ${id}`);
    items[id] = { id, type:'class', label: GC_META[id].label, variants: GC_META[id].variants };
    order.push(id);
  }
  usedGC.clear();
  return { items, order };
}

function buildPage(title, type, content) {
  const global_classes = buildGlobalClasses();
  return {
    content,
    page_settings: { custom_css: CSS },
    version: '0.4',
    title,
    type,
    global_classes
  };
}

// ── SERVICE CARDS (reusable factory, IDs must be unique per call) ──────────

function serviceCards(prefix, cards) {
  return cards.map(([num, title, copy], i) => {
    const cid = `${prefix}sc${i}`;
    return div(`${cid}-wrap`, ['lh-service-card'], [
      para(`${cid}-num`, ['lh-service-number'], num, null, 'lh-service-number'),
      divEmpty(`${cid}-text`, [
        head(`${cid}-h`, ['lh-service-title'], title, 'h3'),
        para(`${cid}-p`, ['lh-service-copy'], copy),
      ]),
    ], [], 'lh-service-card', 'article');
  });
}

// ── CTA SECTION (reusable) ────────────────────────────────────────────────

function ctaSection(prefix, kicker, headline, body, btn1Text, btn1Url, btn2Text, btn2Url) {
  const localKey = `${prefix}-ctn-local`;
  return section(`${prefix}-cta-sec`, ['lh-section'], [
    div(`${prefix}-cta-ctn`, ['lh-container'], [
      div(`${prefix}-cta-box`, ['lh-cta'], [
        para(`${prefix}-cta-kick`, ['lh-section-kicker'], kicker, null),
        head(`${prefix}-cta-h`, null, headline, null),
        ...(body ? [para(`${prefix}-cta-p`, null, body)] : []),
        div(`${prefix}-cta-act`, ['lh-hero-actions'], [
          btn(`${prefix}-cta-b1`, ['lh-button','lh-button-primary'], btn1Text, btn1Url),
          btn(`${prefix}-cta-b2`, ['lh-button'], btn2Text, btn2Url),
        ], [], 'lh-hero-actions'),
      ], [], 'lh-cta'),
    ], [], 'lh-container'),
  ], 'section', null, 'lh-section');
}

// ── SECTION HEAD (reusable) ───────────────────────────────────────────────

function sectionHead(prefix, kicker, title, copy, headTag) {
  return div(`${prefix}-sh`, ['lh-section-head'], [
    divEmpty(`${prefix}-sh-left`, [
      para(`${prefix}-sh-kick`, ['lh-section-kicker'], kicker),
      head(`${prefix}-sh-title`, ['lh-section-title'], title, headTag || 'h2'),
    ]),
    para(`${prefix}-sh-copy`, ['lh-section-copy'], copy, null, 'lh-section-copy'),
  ], [], 'lh-section-head');
}

// ── WORK GRID HTML ────────────────────────────────────────────────────────

const WORK_GRID_3 = `<div class="lh-work-grid">

  <article class="lh-work-card" data-categories="ai branding">
    <a href="/portfolio/" aria-label="View Stride Beyond">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/stride-beyond.jpg" alt="Stride Beyond"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">AI Generated</span><span class="lh-tag">Branding</span></div>
        <h3 class="lh-work-title">Stride Beyond</h3>
        <p class="lh-work-desc">AI-led identity exploration for a futuristic visual language.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="branding">
    <a href="/portfolio/" aria-label="View Nexora">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/nexora.jpg" alt="Nexora"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">Branding</span></div>
        <h3 class="lh-work-title">Nexora</h3>
        <p class="lh-work-desc">Brand system exploration with premium futuristic identity cues.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="branding cgi">
    <a href="/portfolio/" aria-label="View BT Studio CGI Beverage Demo">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/bt-studio-cgi-beverage-demo.jpg" alt="BT Studio CGI Beverage Demo"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">Branding</span><span class="lh-tag">CGI</span></div>
        <h3 class="lh-work-title">BT Studio – CGI Beverage Demo</h3>
        <p class="lh-work-desc">Product-led CGI beverage demo with polished advertising finish.</p>
      </div>
    </a>
  </article>

</div>`;

const PORTFOLIO_FILTER_GRID = `<div class="lh-filter-bar" id="lh-filters" aria-label="Portfolio filters">
  <button class="lh-filter-btn is-active" data-filter="all">All</button>
  <button class="lh-filter-btn" data-filter="3d">3D Model</button>
  <button class="lh-filter-btn" data-filter="ai">AI Generated</button>
  <button class="lh-filter-btn" data-filter="branding">Branding</button>
  <button class="lh-filter-btn" data-filter="cgi">CGI</button>
  <button class="lh-filter-btn" data-filter="feature">Feature</button>
  <button class="lh-filter-btn" data-filter="film">Film</button>
  <button class="lh-filter-btn" data-filter="keyvisual">Key Visuals</button>
  <button class="lh-filter-btn" data-filter="tvc">TVC</button>
  <button class="lh-filter-btn" data-filter="web">Web Design</button>
</div>

<div class="lh-work-grid">

  <article class="lh-work-card" data-categories="tvc">
    <a href="#" aria-label="TVC Ovaltine 2015 Adaptation">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/tvc-ovaltine-2015-adaptation.jpg" alt="TVC Ovaltine 2015 Adaptation"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">TVC</span></div>
        <h3 class="lh-work-title">TVC Ovaltine 2015 Adaptation</h3>
        <p class="lh-work-desc">Campaign adaptation with cinematic product treatment.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="cgi feature">
    <a href="#" aria-label="BT Studio CGI Huda Football">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/bt-studio-cgi-huda-football.jpg" alt="BT Studio CGI Huda Football"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">CGI</span><span class="lh-tag">Feature</span></div>
        <h3 class="lh-work-title">BT Studio – CGI Huda Football</h3>
        <p class="lh-work-desc">CGI beer-football visual system for energetic campaign assets.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="ai branding">
    <a href="#" aria-label="Stride Beyond">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/stride-beyond.jpg" alt="Stride Beyond"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">AI Generated</span><span class="lh-tag">Branding</span></div>
        <h3 class="lh-work-title">Stride Beyond</h3>
        <p class="lh-work-desc">AI-led identity exploration for a futuristic visual language.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="3d ai">
    <a href="#" aria-label="Cheers to Victory">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/cheers-to-victory.jpg" alt="Cheers to Victory"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">3D Model</span><span class="lh-tag">AI Generated</span></div>
        <h3 class="lh-work-title">Cheers to Victory</h3>
        <p class="lh-work-desc">Victory-themed 3D/AI visual with energetic beer celebration mood.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="3d keyvisual">
    <a href="#" aria-label="AFC Key Visual">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/afc-key-visual.jpg" alt="AFC Key Visual"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">3D Model</span><span class="lh-tag">Key Visuals</span></div>
        <h3 class="lh-work-title">AFC Key Visual</h3>
        <p class="lh-work-desc">High-impact sports key visual direction and product composition.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="3d keyvisual">
    <a href="#" aria-label="Twister Pack Visual">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/twister-pack-visual.jpg" alt="Twister Pack Visual"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">3D Model</span><span class="lh-tag">Key Visuals</span></div>
        <h3 class="lh-work-title">Twister Pack Visual</h3>
        <p class="lh-work-desc">Pack-focused 3D visual built for retail and campaign usage.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="3d keyvisual">
    <a href="#" aria-label="Halida Tet 2022 Key Visual">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/halida-tet-2022-key-visual.jpg" alt="Halida Tet 2022 Key Visual"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">3D Model</span><span class="lh-tag">Key Visuals</span></div>
        <h3 class="lh-work-title">Halida Tet 2022 Key Visual</h3>
        <p class="lh-work-desc">Seasonal Tet composition combining beer product and festive energy.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="3d keyvisual">
    <a href="#" aria-label="Huda Beach Carnival 2023">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/huda-beach-carnival-2023.jpg" alt="Huda Beach Carnival 2023"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">3D Model</span><span class="lh-tag">Key Visuals</span></div>
        <h3 class="lh-work-title">Huda Beach Carnival 2023</h3>
        <p class="lh-work-desc">Event visual with beach, summer, and brand-world atmosphere.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="web">
    <a href="#" aria-label="Circuit">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/circuit.jpg" alt="Circuit"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">Web Design</span></div>
        <h3 class="lh-work-title">Circuit</h3>
        <p class="lh-work-desc">Visual interface direction for a modern digital product concept.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="web">
    <a href="#" aria-label="Spectral">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/spectral.jpg" alt="Spectral"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">Web Design</span></div>
        <h3 class="lh-work-title">Spectral</h3>
        <p class="lh-work-desc">Editorial web concept with atmospheric motion and dark UI styling.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="branding">
    <a href="#" aria-label="Nexora">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/nexora.jpg" alt="Nexora"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">Branding</span></div>
        <h3 class="lh-work-title">Nexora</h3>
        <p class="lh-work-desc">Brand system exploration with premium futuristic identity cues.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="film">
    <a href="#" aria-label="Astralis">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/astralis.jpg" alt="Astralis"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">Film</span></div>
        <h3 class="lh-work-title">Astralis</h3>
        <p class="lh-work-desc">Film-inspired visual direction with atmospheric narrative framing.</p>
      </div>
    </a>
  </article>

  <article class="lh-work-card" data-categories="branding cgi">
    <a href="#" aria-label="BT Studio CGI Beverage Demo">
      <div class="lh-work-media"><img src="/wp-content/uploads/lh/bt-studio-cgi-beverage-demo.jpg" alt="BT Studio CGI Beverage Demo"></div>
      <div class="lh-work-body">
        <div class="lh-meta-row"><span class="lh-tag">Branding</span><span class="lh-tag">CGI</span></div>
        <h3 class="lh-work-title">BT Studio – CGI Beverage Demo</h3>
        <p class="lh-work-desc">Product-led CGI beverage demo with polished advertising finish.</p>
      </div>
    </a>
  </article>

</div>

<script>
(function(){
  var btns = document.querySelectorAll('#lh-filters [data-filter]');
  var cards = document.querySelectorAll('.lh-work-grid [data-categories]');
  btns.forEach(function(b){
    b.addEventListener('click', function(){
      var f = b.dataset.filter;
      btns.forEach(function(x){ x.classList.remove('is-active'); });
      b.classList.add('is-active');
      cards.forEach(function(c){
        c.hidden = !(f === 'all' || c.dataset.categories.includes(f));
      });
    });
  });
})();
</script>`;

const ABOUT_PORTRAIT_HTML = `<div class="lh-portrait-panel">
  <img class="lh-portrait" src="/wp-content/uploads/lh/luong-huynh-portrait.jpg" alt="Luong Huynh — Digital Artist">
  <div class="lh-hero-card-caption">
    <div class="lh-meta-row">
      <span class="lh-chip lh-chip-strong">Digital Artist</span>
      <span class="lh-chip">Ho Chi Minh City</span>
    </div>
  </div>
</div>`;

const ABOUT_LIST_HTML = `<ul class="lh-list">
  <li><strong>Focus</strong><span>3D product visuals, AI-generated art, CGI key visuals, campaign image systems and VFX finishing.</span></li>
  <li><strong>Clients</strong><span>Brands, agencies, production teams and campaign creators needing high-impact visuals.</span></li>
  <li><strong>Approach</strong><span>Blend art direction, generative workflows, compositing and production sensibility into finished assets.</span></li>
  <li><strong>Output</strong><span>Key visuals, product renders, pitch frames, social campaign assets, launch imagery and moving-image look development.</span></li>
</ul>`;

const DETAIL_GALLERY_HTML = `<div class="lh-detail-gallery">
  <img class="lh-detail-gallery-item" src="/wp-content/uploads/lh/project-detail-1.jpg" alt="Project visual 1">
  <img class="lh-detail-gallery-item" src="/wp-content/uploads/lh/project-detail-2.jpg" alt="Project visual 2">
  <img class="lh-detail-gallery-item" src="/wp-content/uploads/lh/project-detail-3.jpg" alt="Project visual 3">
  <img class="lh-detail-gallery-item" src="/wp-content/uploads/lh/project-detail-4.jpg" alt="Project visual 4">
</div>`;

const DETAIL_NAV_HTML = `<nav class="lh-project-nav" aria-label="Project navigation">
  <a class="lh-project-nav-item" href="/portfolio/">
    <div class="lh-project-nav-label">← Previous</div>
    <div class="lh-project-nav-title">Stride Beyond</div>
  </a>
  <a class="lh-project-nav-item" href="/portfolio/" style="text-align:right">
    <div class="lh-project-nav-label">Next →</div>
    <div class="lh-project-nav-title">BT Studio CGI Beverage</div>
  </a>
</nav>`;

// ── PAGE 1: HOMEPAGE ───────────────────────────────────────────────────────

function buildHomepage() {
  resetIds();

  const content = [
    // ── Hero ──────────────────────────────────────────────────────────────
    section('6c465298', ['lh-hero'], [
      div('47d06898', ['lh-container'], [
        div('ab3145c', ['lh-hero-body'], [
          para('4014deb9', ['lh-eyebrow','lh-reveal'], 'Ho Chi Minh City · 2026', 'span'),
          head('7d2c5522', ['lh-hero-title','lh-reveal','lh-reveal-d1'], 'Cinematic digital art', null),
          para('279e9d62', ['lh-hero-copy','lh-reveal','lh-reveal-d2'], 'Digital Artist crafting 3D visuals, AI-generated imagery and VFX for brands, campaigns and cinematic stories.', 'span'),
          div('2b0bc4b8', ['lh-hero-actions','lh-reveal','lh-reveal-d3'], [
            btn('57593351', ['lh-button','lh-button-primary'], 'View Portfolio', '/portfolio/'),
            btn('41260296', ['lh-button'], 'About Luong', '/about/'),
          ], [], 'lh-hero-actions'),
        ], [], 'lh-hero-body'),
      ], localStyle('47d06898','0052c0b',{'flex-direction':{'$$type':'string',value:'column'}}), 'lh-container'),
    ], 'section', null, 'lh-hero'),

    // ── Featured Work ──────────────────────────────────────────────────────
    section('11158a15', ['lh-section'], [
      div('3f098498', ['lh-container'], [
        sectionHead('fw', 'Featured work', 'Selected visuals with campaign-grade finish.', 'A focused selection of recent campaign imagery, CGI and AI-generated visuals — spanning brand identity, product worlds and key visual systems.'),
        htmlWidget('505da262', WORK_GRID_3),
      ], [], 'lh-container'),
    ], 'section', null, 'lh-section'),

    // ── Services ───────────────────────────────────────────────────────────
    section('4f310e5e', ['lh-section','lh-section-muted'], [
      div('44905046', ['lh-container'], [
        sectionHead('svc', 'Services', 'Built for visual campaigns.', 'Focused on campaign-grade output for brands, agencies and production teams who need premium visual assets.'),
        div('1ea03e4d', ['lh-service-grid'],
          serviceCards('hm', [
            ['01','3D Product &amp; CGI Visuals','Premium product compositions, pack shots and campaign-ready CGI scenes.'],
            ['02','AI Campaign Imagery','AI-assisted visual exploration, concept boards and stylized brand imagery.'],
            ['03','VFX &amp; Post-production','Compositing, retouching, enhancement and cinematic finishing for moving or still assets.'],
            ['04','Visual Direction','Campaign look development, key visual systems and production-ready visual storytelling.'],
          ]),
          localStyle('1ea03e4d','47d6be0',{'flex-direction':{'$$type':'string',value:'row'}}),
          'lh-service-grid'),
      ], localStyle('44905046','1b5e0cd',{'flex-direction':{'$$type':'string',value:'column'}}), 'lh-container'),
    ], 'section', null, 'lh-section'),

    // ── CTA ────────────────────────────────────────────────────────────────
    section('64d0086e', ['lh-section'], [
      div('4c12e9e1', ['lh-container'], [
        div('52d42176', ['lh-cta'], [
          para('74561db4', ['lh-section-kicker'], 'Available for Work'),
          head('62add9', null, "Let’s build the next cinematic brand visual."),
          para('6fdf2680', null, 'Send over the brief, references and target deliverables. I can help shape the visual direction from concept to finished campaign asset.'),
          div('1d401ea6', ['lh-hero-actions'], [
            btn('b3ad7fd', ['lh-button','lh-button-primary'], 'Get in Touch', 'mailto:hello@luonghuynh.com'),
            btn('4cdef8a0', ['lh-button'], 'Explore Work', '/portfolio/'),
          ], [], 'lh-hero-actions'),
        ], [], 'lh-cta'),
      ], [], 'lh-container'),
    ], 'section', 'contact', 'lh-section'),
  ];

  return buildPage('Home Page', 'page', content);
}

// ── PAGE 2: PORTFOLIO ──────────────────────────────────────────────────────

function buildPortfolio() {
  resetIds();

  const content = [
    // ── Portfolio Archive ──────────────────────────────────────────────────
    section('p-arch-sec', ['lh-section'], [
      div('p-arch-ctn', ['lh-container'], [
        sectionHead('pf', 'Portfolio', 'A curated archive of 3D, AI, CGI, TVC and brand visuals.', 'An archive of campaign visuals, product renders, AI-generated imagery and visual direction work — across CGI, key visuals, branding and film.', 'h1'),
        htmlWidget('p-grid-html', PORTFOLIO_FILTER_GRID),
      ], [], 'lh-container'),
    ], 'section', null, 'lh-section'),

    // ── CTA ────────────────────────────────────────────────────────────────
    ctaSection('pf', 'Project Inquiry', 'Need campaign visuals, CGI or AI art direction?', null, 'Get in Touch', 'mailto:hello@luonghuynh.com', 'About Luong', '/about/'),
  ];

  return buildPage('Portfolio', 'page', content);
}

// ── PAGE 3: ABOUT ──────────────────────────────────────────────────────────

function buildAbout() {
  resetIds();

  const aboutGridStyle = localStyle('ab-grid','a1b2c',{
    'display':{'$$type':'string',value:'grid'},
    'grid-template-columns':{'$$type':'string',value:'0.78fr 1.1fr'},
    'gap':{'$$type':'string',value:'clamp(36px, 6vw, 86px)'},
    'align-items':{'$$type':'string',value:'start'},
  });

  const content = [
    // ── About Grid ────────────────────────────────────────────────────────
    section('ab-grid-sec', ['lh-section'], [
      div('ab-ctn', ['lh-container'], [
        div('ab-grid', ['lh-about-grid'], [
          // Left: portrait
          htmlWidget('ab-portrait-html', ABOUT_PORTRAIT_HTML),
          // Right: rich text
          div('ab-richtext', ['lh-rich-text'], [
            para('ab-eyebrow', ['lh-eyebrow'], 'About', 'span'),
            head('ab-h1', null, 'Digital Artist &amp; Visual Technologist.', 'h1'),
            para('ab-p1', null, "I’m a digital artist focused on 3D visuals, AI-generated images and VFX. I collaborate with brands, agencies and production teams to create campaign-ready visuals, cinematic key visuals and experimental AI-assisted imagery."),
            para('ab-p2', null, 'Based in Ho Chi Minh City, I work across the full visual pipeline — from concept and art direction through to production-finished assets ready for print, digital and broadcast.'),
            htmlWidget('ab-list-html', ABOUT_LIST_HTML),
          ], [], 'lh-rich-text'),
        ], aboutGridStyle, 'lh-about-grid'),
      ], [], 'lh-container'),
    ], 'section', null, 'lh-section'),

    // ── Services ───────────────────────────────────────────────────────────
    section('ab-svc-sec', ['lh-section','lh-section-muted'], [
      div('ab-svc-ctn', ['lh-container'], [
        sectionHead('ab-svc', 'Services', 'Creative services shaped around campaign delivery.', 'Each project is approached from concept through to production-ready delivery — visual-first, always.'),
        div('ab-svc-grid', ['lh-service-grid'],
          serviceCards('ab', [
            ['01','3D Modeling &amp; Scene Design','Product-centric 3D scenes and stylized campaign worlds.'],
            ['02','Generative Art Direction','AI image workflows refined into premium, brand-safe visual directions.'],
            ['03','VFX &amp; Compositing','Cinematic polish, retouching and post-production integration.'],
            ['04','Campaign Key Visuals','Hero images, visual systems and adaptations for brand campaigns.'],
          ]),
          localStyle('ab-svc-grid','flex-row',{'flex-direction':{'$$type':'string',value:'row'}}),
          'lh-service-grid'),
      ], localStyle('ab-svc-ctn','col',{'flex-direction':{'$$type':'string',value:'column'}}), 'lh-container'),
    ], 'section', null, 'lh-section'),

    // ── CTA ────────────────────────────────────────────────────────────────
    ctaSection('ab', 'Contact', 'Available for selected visual campaigns.', 'For project inquiries, include objective, timeline, references, deliverables and usage channel.', 'hello@luonghuynh.com', 'mailto:hello@luonghuynh.com', 'View Work', '/portfolio/'),
  ];

  return buildPage('About', 'page', content);
}

// ── PAGE 4: PROJECT TEMPLATE ────────────────────────────────────────────────

function buildProjectTemplate() {
  resetIds();

  const detailBodyStyle = localStyle('pr-body','grid',{
    'display':{'$$type':'string',value:'grid'},
    'grid-template-columns':{'$$type':'string',value:'1fr minmax(0, 680px)'},
    'gap':{'$$type':'string',value:'clamp(36px, 6vw, 96px)'},
    'align-items':{'$$type':'string',value:'start'},
  });

  const sidebarStyle = localStyle('pr-sidebar','sticky',{
    'position':{'$$type':'string',value:'sticky'},
    'top':{'$$type':'string',value:'90px'},
  });

  const content = [
    // ── Project Hero ───────────────────────────────────────────────────────
    section('pr-hero-sec', ['lh-section'], [
      div('pr-hero-ctn', ['lh-container'], [
        div('pr-hero-body', ['lh-detail-hero'], [
          div('pr-meta-row', ['lh-detail-meta'], [
            para('pr-tag1', ['lh-tag'], 'CGI', 'span'),
            para('pr-tag2', ['lh-tag'], '3D Model', 'span'),
            para('pr-tag3', ['lh-tag'], 'Key Visuals', 'span'),
          ], [], 'lh-detail-meta'),
          head('pr-title', ['lh-detail-title','lh-hero-title'], 'Project Title', 'h1'),
          para('pr-lead', ['lh-detail-lead','lh-hero-copy'], 'A short lead sentence describing the project — campaign type, client context, or visual approach. One to two sentences.', 'p'),
        ], [], 'lh-detail-hero'),
      ], [], 'lh-container'),
    ], 'section', null, 'lh-section'),

    // ── Cover Image ────────────────────────────────────────────────────────
    section('pr-cover-sec', ['lh-section'], [
      div('pr-cover-ctn', ['lh-container'], [
        htmlWidget('pr-cover-html', '<img class="lh-detail-cover" src="/wp-content/uploads/lh/project-cover.jpg" alt="Project cover">'),
      ], [], 'lh-container'),
    ], 'section', null, 'lh-section'),

    // ── Detail Body ────────────────────────────────────────────────────────
    section('pr-body-sec', ['lh-section'], [
      div('pr-body-ctn', ['lh-container'], [
        div('pr-body', ['lh-detail-body'], [
          // Sidebar
          div('pr-sidebar', ['lh-detail-sidebar'], [
            divEmpty('pr-info1', [
              para('pr-info1-lbl', ['lh-section-kicker'], 'Client'),
              para('pr-info1-val', null, 'Brand / Agency Name'),
            ]),
            divEmpty('pr-info2', [
              para('pr-info2-lbl', ['lh-section-kicker'], 'Year'),
              para('pr-info2-val', null, '2024'),
            ]),
            divEmpty('pr-info3', [
              para('pr-info3-lbl', ['lh-section-kicker'], 'Scope'),
              para('pr-info3-val', null, 'CGI, Key Visual, Product Render'),
            ]),
            divEmpty('pr-info4', [
              para('pr-info4-lbl', ['lh-section-kicker'], 'Output'),
              para('pr-info4-val', null, 'Print, Digital, Campaign'),
            ]),
            btn('pr-back-btn', ['lh-button','lh-button-primary'], 'Back to Portfolio', '/portfolio/'),
          ], sidebarStyle, 'lh-detail-sidebar'),
          // Content
          div('pr-content', ['lh-detail-content'], [
            para('pr-cp1', null, 'Describe the creative brief and visual problem here. What did the client need? What was the campaign context? Keep the tone confident and precise.'),
            para('pr-cp2', null, 'Explain the approach. What 3D or AI techniques were used? How did you develop the visual language? What references or constraints shaped the output?'),
            para('pr-cp3', null, 'Note the result: platform, reach, deliverables. What was produced and where was it used?'),
          ], [], 'lh-detail-content'),
        ], detailBodyStyle, 'lh-detail-body'),

        // Gallery
        htmlWidget('pr-gallery-html', DETAIL_GALLERY_HTML),
      ], [], 'lh-container'),
    ], 'section', null, 'lh-section'),

    // ── Project Nav ────────────────────────────────────────────────────────
    section('pr-nav-sec', ['lh-section'], [
      div('pr-nav-ctn', ['lh-container'], [
        htmlWidget('pr-nav-html', DETAIL_NAV_HTML),
      ], [], 'lh-container'),
    ], 'section', null, 'lh-section'),

    // ── CTA ────────────────────────────────────────────────────────────────
    ctaSection('pr', 'Project Inquiry', 'Need campaign visuals, CGI or AI art direction?', null, 'Get in Touch', 'mailto:hello@luonghuynh.com', 'Explore Work', '/portfolio/'),
  ];

  return buildPage('Project Template', 'page', content);
}

// ── WRITE FILES ────────────────────────────────────────────────────────────

const pages = [
  ['homepage_V4.json',        buildHomepage()],
  ['portfolio_V4.json',       buildPortfolio()],
  ['about_V4.json',           buildAbout()],
  ['project-template_V4.json',buildProjectTemplate()],
];

for (const [filename, data] of pages) {
  fs.writeFileSync(path.join(OUT, filename), JSON.stringify(data), 'utf8');
  console.log(`Wrote ${filename}`);
}

// Copy CSS
fs.writeFileSync(path.join(OUT, 'global-css.css'), CSS, 'utf8');
console.log('Wrote global-css.css');

console.log('Done.');
