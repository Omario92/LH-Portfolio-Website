# Claude Code Prompt — Convert Static Site to Elementor Build Plan

Read the current static website and produce an Elementor rebuild plan.

Files to read:
- `index.html`
- `portfolio.html`
- `about.html`
- `assets/css/styles.css`
- `elementor/section-map.md`

Task:
Update the Elementor handoff files so a non-developer can rebuild the website in Elementor.

Output/update:
- `elementor/README.md`
- `elementor/section-map.md`
- `elementor/global-css.css`
- `elementor/html-widget-snippets.html`

For each page and section, specify:
- Elementor Container structure
- Widgets to use
- Class names to assign under Advanced > CSS Classes
- Content to paste
- Image/video replacement notes
- Whether the section should be dynamic or static
- Which CSS rules are critical
- Which effects can be approximated with Elementor settings instead of CSS

Do not assume I will paste full page HTML into Elementor. The final Elementor implementation should use Containers and widgets, with global CSS for the custom look.
