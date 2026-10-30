# Therapy with Sazzy — therapywithsazzy.com

Static site (HTML/CSS/JS, no build step). Deploy the folder as-is to Netlify, Cloudflare Pages, or Vercel, then point therapywithsazzy.com at it.

Preview locally: `python3 -m http.server 8000`

## Before launch
- Add NJ LAC license number and supervisor details to the footer and privacy.html (NJ advertising rules).
- Confirm services, format (in-person/telehealth), fees/insurance wording with Sazzy.
- Contact form uses mailto; swap for a secure form/portal if clinical intake is wanted.
- Resources page toolkits are "coming soon" placeholders.

Logo files: assets/logo/ (mark, lockups, favicons). Brand: navy #0F2A4A, teal #2E9C95, cream #FBF6EE, coral #E8806A. Fonts: Fraunces + Plus Jakarta Sans.

## Resource center
- `resources/` holds the PDFs: one per resource, `complete-<toolkit>.pdf` bundles, the original 4-page Quick-Start Packs (`*-toolkit.pdf`), and `thumbs/` previews.
- Content lives in `tools/{kids,parents,teens,adults,trauma}.py`. Regenerate with `python3 tools/make_resources.py` (needs Google Chrome + PyMuPDF), then `python3 tools/build_resources_site.py` to rebuild `resources.html`, `toolkits/*.html`, and `js/catalog.js`.
- `tools/make_quickstart_packs.py` regenerates the original Quick-Start Pack PDFs.
