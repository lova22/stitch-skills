# Design system: "Free Library Marketplace" (final)

Source site: crochetpatternsco.com (theme `crochet-patterns-co`, v3.2.0, WordPress block theme).
Purpose of this file: rebuild the same structure for **another WordPress site** (another niche, another brand) without redesigning anything. Everything below is taken from the shipped code (`assets/site.css`, `assets/pattern-extra.css`, `inc/*.php`).

Status notes
- Section 1-10 describe what is built and live (v3.1) or in the draft theme (v3.2: pattern extras).
- Items marked **Recommended** are fixes found while writing this document and are not yet in the live CSS.
- Language: English only. Light mode only (`color-scheme: light`). No dark mode, no black backgrounds.

---

## 1. Principles

1. **Marketplace, not blog.** A clean, bright, product-card layout in the style of Noon / Teachers Pay Teachers: yellow header, white rounded cards on a warm grey canvas, one strong action colour.
2. **One action colour.** Olive green is the only "do something" colour (download, apply, submit). Yellow is brand and highlight. Berry/rose is a secondary accent.
3. **Answer first.** Every content page starts with a short quotable answer (Quick answer), then details. This serves readers, Google and AI answers.
4. **Mobile first, thumb first.** Phones get a bottom tab bar and a sticky download bar; desktop gets a sticky header and sticky gallery.
5. **Ads look like content, but are always labelled.** Every ad is wrapped in a labelled "Advertisement" card; never disguised as a download button.
6. **Empty means hidden.** A block whose data is empty renders nothing, so thin items never show empty boxes.
7. **Illustrated placeholders.** Items without a photo get a tinted tile with a vector motif, so the grid always looks finished.

---

## 2. Design tokens

### 2.1 CSS custom properties (copy as-is into `:root`)

```css
:root {
  /* spacing scale: 4 / 8 / 12 / 16 / 24 / 32 / 48 */
  --s1: 4px; --s2: 8px; --s3: 12px; --s4: 16px; --s5: 24px; --s6: 32px; --s7: 48px;

  /* brand */
  --cp-yellow: #FFD84A;   /* header, highlights, badges */
  --cp-hd:     #3B2A22;   /* cocoa: text on yellow, logo mark, tooltips */

  /* surfaces and text */
  --cp-page:  #F5F4F1;    /* canvas */
  --cp-card:  #FFFFFF;    /* cards, drawers, sheets */
  --cp-ink:   #2B2320;    /* body text */
  --cp-muted: #7B706A;    /* secondary text (see 2.3: Recommended #6E635D) */
  --cp-line:  #E9E5DF;    /* borders, dividers */
  --cp-chip:  #F1EEE9;    /* neutral chip, progress track */

  /* action and accents */
  --cp-cta:   #4C6B22;    /* primary button */
  --cp-cta-d: #3D571A;    /* primary button hover */
  --cp-link:  #A8456A;    /* text links, "see all" links */
  --cp-free:  #2F7A2E;    /* "FREE" price label */
  --cp-olive: #4C5B2A;    /* top strip, rank badge */
  --cp-berry: #B64E6C;    /* ribbons, hover on filter chips, newsletter focus */

  /* pastel tints (tiles, chips, promo cards) */
  --cp-moss:  #DDE5BE;    /* green tint, "Beginner" */
  --cp-blush: #F9DFE6;    /* pink tint, "Advanced", newsletter */
  --cp-sand:  #F1E2D0;    /* beige tint, "Intermediate" */

  --cp-ad: #EDEBE6;       /* ad placeholder background */

  /* layout */
  --cp-wrap: 1280px;      /* max content width */
  --cp-r: 18px;           /* default card radius */
  --cp-tab-h: 64px;       /* mobile bottom tab bar */
  --cp-dlbar-h: 72px;     /* mobile sticky download bar */
  --cp-admin: var(--wp-admin--admin-bar--height, 0px);
  --cp-f: 'Plus Jakarta Sans', system-ui, -apple-system, 'Segoe UI', sans-serif;
  color-scheme: light;
}
```

Also registered in `theme.json` as editor palette: `page, ink, muted, yellow, olive (#4C6B22), moss, berry, blush, sand`; content width 760px, wide width 1280px; body font size clamp(14px..15px).

### 2.2 Palette roles at a glance

| Role | Token | Hex | Used for |
|---|---|---|---|
| Brand | `--cp-yellow` | #FFD84A | Header bar, logo ring, highlights, "Instant PDF" tag, rank badge, step numbers |
| Brand ink | `--cp-hd` | #3B2A22 | Text on yellow, logo disc |
| Action | `--cp-cta` / `--cp-cta-d` | #4C6B22 / #3D571A | Primary buttons, checked radios, active tab, pagination current |
| Link | `--cp-link` | #A8456A | Inline links, "View all" links |
| Free | `--cp-free` | #2F7A2E | "FREE" label |
| Strip | `--cp-olive` | #4C5B2A | Top promo strip, rank icon |
| Accent | `--cp-berry` | #B64E6C | Ribbons, filter-chip hover, input focus on pink |
| Canvas | `--cp-page` | #F5F4F1 | Page background, inner rows (kv, faq items) |
| Card | `--cp-card` | #FFFFFF | Cards, boxes, drawers |
| Tint green/pink/beige | moss / blush / sand | #DDE5BE / #F9DFE6 / #F1E2D0 | Level chips, category tiles, promo cards |

Level colours (fixed mapping): Beginner = moss, Intermediate = sand, Advanced = blush (`.cp-chip--b/--i/--a`, `.cp-lvc--b/--i/--a`).

Hero slide gradients: `--1` olive `#5B6B32 → #3F4B22` (white text), `--2` rose `#C65F7D → #A23F5E` (white text), `--3` yellow `#FFE16B → #FFC93C` (cocoa text).

### 2.3 Contrast (computed WCAG ratios)

| Pair | Ratio | Verdict |
|---|---|---|
| White on CTA #4C6B22 | 6.12 | AA |
| White on CTA hover | 8.15 | AAA |
| Cocoa #3B2A22 on yellow #FFD84A | 9.85 | AAA |
| Ink on card / page | 15.4 / 14.0 | AAA |
| Prose #4A3F39 on card | 10.19 | AAA |
| FREE green on card | 5.32 | AA |
| Link #A8456A on card / page | 5.64 / 5.13 | AA |
| White on olive strip | 7.40 | AAA |
| White on berry | 4.89 | AA |
| Chip text: beginner / intermediate / advanced | 9.34 / 7.97 / 7.46 | AAA |
| **Muted #7B706A on card** | 4.81 | AA |
| **Muted #7B706A on page canvas** | **4.37** | **fails AA for small text** |

**Recommended:** change `--cp-muted` to `#6E635D` (5.82 on white, 5.30 on page canvas, 5.03 on chip). Do this in the new site from day one.

### 2.4 Typography

- Family: **Plus Jakarta Sans** (Google Fonts, weights 500, 700, 800, `display=swap`), fallback system stack.
- Headings: weight 800, line-height 1.2, letter-spacing -0.01em.
- Body: 15px / 1.55, antialiased.

| Element | Size |
|---|---|
| Page H1 (article) | `clamp(26px, 4vw, 38px)` |
| Page H1 (generic page) | `clamp(28px, 4vw, 40px)` |
| Results H1 (list) | `clamp(24px, 3.4vw, 32px)` |
| Home intro H1 | `clamp(20px, 3.2vw, 28px)` |
| Product H1 (in box) | 24px mobile, 28px desktop |
| Hero slide title | `clamp(26px, 5.6vw, 36px)`, max 13ch, `text-wrap: balance` |
| Section heading (`.cp-sh h2`) | 20px |
| Box heading (`.cp-box h2`) | 19px |
| Article H2 | 24px |
| Card title | 14px / 700, clamped to 2 lines |
| Lead paragraph | 16px / 1.6 |
| Meta, captions | 12-14px |
| Eyebrow label | 11-13px, 800, uppercase, letter-spacing .06-.08em |

### 2.5 Radius, borders, shadow, motion

- Radius: chips 8px, buttons 12px, inputs 12px, kv rows 14px, boxes 20px, default card `--cp-r` 18px, hero/promo/level cards 22px, newsletter 24px, bottom sheet 24px 24px 0 0, pills 999px.
- Borders: 1px `--cp-line` on cards; 2px on inputs/outline buttons.
- Shadows: card hover `0 10px 26px rgba(60,40,25,.12)`; button hover `0 8px 18px rgba(60,80,25,.2)`; open drawers `0 0 40px rgba(0,0,0,.3)`.
- Motion: 150-250ms ease on transform/box-shadow/background only. Hover lift `translateY(-2px)` (cards, tiles) or `-3px` (level cards). `prefers-reduced-motion` turns transitions off and smooth scroll to `auto`.

### 2.6 Breakpoints

| Name | Range | Key changes |
|---|---|---|
| Phone | < 768px | Bottom tab bar, sticky download bar, sticky ad bar, filter drawer from the right, 2-column grid, rows show 2.25 cards |
| Tablet | 768-1023px | No tab/download bar, header search inline, nav row visible, 3-column grid, hero shows 2 slides, rows 3.5 cards |
| Desktop | >= 1024px | Sticky yellow header, text links in header, filters become a sticky left sidebar (270px), 4-column grid, rows 5 cards, hero 3 slides, sticky 300x600 ad |
| Wide | >= 1200px | Rows show 6 cards |

Layers (z-index): tab bar 40, download bar 39, sticky ad 38, header 60, scrim 90, drawers 100, bottom sheet 110, interstitial 200.

---

## 3. Layout primitives

| Class | Role |
|---|---|
| `.cp-wrap` | Centered container, max 1280px, padding 16px (24px from tablet) |
| `.cp-sec` | Section with top margin 32px (48px from tablet) |
| `.cp-sh` | Section header: H2 left, "View all" link right |
| `.cp-box` | White rounded content box, padding 16px |
| `.cp-page` | Generic page column, max 820px |
| `.cp-artbox` | Article column, max 860px |
| `.cp-grid` | Product grid: 2 / 3 / 4 columns |
| `.cp-rw` | Horizontal snap row of cards (scroll on phone) |
| `.cp-shw` | Horizontal snap row of showcase tiles |

---

## 4. Components

All class names use the `cp-` prefix. Build in this order for a new site.

### 4.1 Buttons
`.cp-btn` (solid olive, white text, 12px radius, 800 weight). Modifiers: `--sm`, `--lg` (full width, 17px), `--y` (yellow, cocoa text), `--outline` (white with line border). Icon inside is 20px. `.cp-mbtn` / `.cp-iconbtn` = 44px round icon buttons (touch target). Focus: 3px `--cp-link` outline.

### 4.2 Top strip
`.cp-strip`: olive bar with yellow icon tile, 2-line message, small yellow button, close button (phones only). Content is set in Site settings.

### 4.3 Header
`.cp-hd` yellow bar: menu button (phone) + logo + search + links. Logo = cocoa disc with yellow ring (`.cp-logo i`) + wordmark 21px/800. Search: white pill-ish field, 12px radius, search icon button on the right. `.cp-nav` second row (tablet+): white, horizontally scrollable category links with a yellow underline on hover. Sticky from 1024px.

### 4.4 Menu drawer (phones)
`.cp-drawer`: slides from the left, width `min(86vw, 380px)`, scrim behind. Two-level list: main list rows (`.cp-list__row`) and category panels (`.cp-panel`, with `.cp-back`). Category rows show a 44px tinted icon tile (`.cp-list__ic`).

### 4.5 Bottom tab bar (phones)
`.cp-tabs`: 4 equal tabs, 11.5px labels: **Home**, **Categories** (opens the menu drawer on its categories panel), **Popular** (archive sorted by downloads), **Newsletter** (jumps to `/#newsletter`). The active tab has an olive label and a light-green pill behind the icon. Includes safe-area inset. Hidden from 768px.

### 4.6 Hero carousel
`.cp-car` snap scroller with `.cp-sl` slides (22px radius, gradient, art SVG top-right, ribbon `.cp-sl__rb`, title, short text, button). Phone shows 88% width, tablet 2, desktop 3. Controls `.cp-car__ctl` with `.cp-pz` pause/play.

### 4.6a Category tiles
`.cp-cats` row of `.cp-ct` tiles (aspect 1 / 1.12), pastel tint, motif SVG at 60% width, label at the bottom. Phone: horizontal scroll, 104px columns. Tablet: auto-fill grid. Desktop: 9 columns.

### 4.7 Product (pattern) card
`.cp-pc` (white, line border, 18px radius, hover lift):
- `.cp-pc__im` square image or motif; `.cp-tag` category (top-left, white); `.cp-rk` rank badge `#1` (top-right, yellow).
- `.cp-pc__bd`: title (2 lines), chips (level + download count), `.cp-fr` "FREE PDF" (green), `.cp-ex` yellow "Instant PDF" tag.
- Variants: `.cp-pc--demo` (opacity .8), `.cp-pc--ad` (dashed border, hosts an in-feed ad).

### 4.8 Chips
`.cp-chip` neutral; `--b` moss (beginner), `--i` sand (intermediate), `--a` blush (advanced), `--link` white with border. `.cp-fchip` = removable filter chip (pill). `.cp-ex` = yellow micro-tag.

### 4.9 Showcase, promo duo, level cards
- `.cp-sc` tile: 4/5 image on tint, 22px radius, title below.
- `.cp-duo` two promo cards `.cp-pr--1` (moss) and `--2` (blush), 22px radius, illustration top-right.
- `.cp-levels` three `.cp-lvc` cards (`--b/--i/--a`) with eyebrow, 26px title, one-line description.

### 4.10 Browse (lists and filters)
- Breadcrumb `.cp-crumbs`, heading + result count, toolbar `.cp-toolbar` (Filter button on phones, Sort select), active filter chips row with "Clear all".
- Filters `.cp-filters`: right drawer on phone/tablet (88vw, max 420px, sticky footer with full-width Apply), left sticky sidebar 270px on desktop. Sections are `<details class="cp-fsec">` with 19px/800 summaries; options `.cp-opt` are round radios (22px) with counts; "show more" toggle `.cp-morebtn`.
- Pager `.cp-pager`: 12px-radius number buttons, current = solid olive.
- Empty state `.cp-empty`: dashed border box with a message and a button.

### 4.11 Pattern (product) page

Order of blocks:
1. Breadcrumb.
2. `.cp-pg` two columns on tablet+: **gallery** (`.cp-gal`: main 1:1 image + thumbs; thumbs are a left column on desktop; Pin button over the image; sticky) and **buy box** (`.cp-rt`).
3. Buy box: chips (level + categories) -> H1 -> "Free pattern by Brand · N downloads" -> `.cp-price` (FREE, PDF size/pages, "Instant download") -> big download button (desktop) -> share row (Pinterest, Facebook, Copy link).
4. `.cp-best` rank card ("#3 most downloaded in Category") only if rank <= 10.
5. Ad slot below the download box.
6. "Download details" kv list (`.cp-kv`): printable PDF, no account needed.
7. **Jump bar** `.cp-jump` (pill links to sections + Print button). *[v3.2]*
8. Two columns `.cp-cols`: **Quick answer** (`.cp-lead`) + **Pattern at a glance** tiles (`.cp-specs--glance`: 2 columns phone, 3 tablet+, yarn spans full width) | **About this pattern** (`.cp-prose` editor content). *[glance tiles v3.2]*
9. **Materials and tools** (`.cp-mat`, `.cp-checks` with green check bubbles). *[v3.2]*
10. **Photo steps** (`.cp-steps`: numbered rows with yellow number disc, title, short text, photo; on tablet+ the photo sits right at 38% width). *[v3.2]*
11. In-content ad, then **Tips and common mistakes** (`.cp-tips`, yellow star bubbles), sidebar ad. *[v3.2]*
12. **FAQ** (`.cp-faq`, `<details>` rows on canvas colour, chevron rotates open).
13. **Technique guides** (`.cp-guides` link rows) and **Maker box** (`.cp-maker`: avatar disc, "Pattern designer", name, bio, "Tested by"). *[v3.2]*
14. Publisher box `.cp-pub` ("All patterns" button).
15. Related patterns row (`.cp-rw`) with an in-feed ad card at the end.
16. Phones only: sticky **download bar** `.cp-dlbar` (price tag + big button) above the tab bar; sticky ad bar above that.
17. **Download sheet** `.cp-sheet` (bottom sheet on phones, centered dialog on desktop): "Getting your file ready", 5-second countdown with progress bar `.cp-bar`, an ad slot, then a "Start download" button. Counter + redirect are server side (`?cpco_dl=ID`, noindex, bots not counted).

Photo steps rule: step line format is `Title | Short description | optional photo ID`. Without a photo a published page shows text only; drafts show a dashed "Your step photo goes here" tile.

### 4.12 Blog and article
Blog list = same card grid (`.cp-grid--blog`, 3 columns from tablet) with meta (`.cp-postmeta`) and 3-line excerpt. Article = `.cp-artbox`, 860px column, rounded 16px images, H2 24px, blockquote with a yellow left border, ordered/unordered lists.

### 4.13 Newsletter
`.cp-news`: blush card, 24px radius, H2 24px, email input (white, 12px radius) + olive button; success text olive, error text `#9B3E58`. Honeypot field `website`, nonce, stored as private CPT `cpco_subscriber` (optional, no registration).

### 4.14 Footer
`.cp-ft`: white, top border. Brand block (logo, one sentence, social links with yellow underline) + 3 link columns (pages are listed automatically; Home, Blog and Privacy are excluded from the auto list) + base row (copyright, legal links). Phone: 2 columns; tablet+: `1.4fr 1fr 1fr 1fr`.

### 4.15 Ads
See section 7.

### 4.16 Print
`@media print` hides header, footer, jump bar, download bar, sheet, share row, ads, related row and publisher box; boxes avoid page breaks.

---

## 5. Illustrated placeholder system

Every product without a photo gets a tinted tile + vector motif so grids never look empty.

`cpco_cat_style( $slug )` returns `[ tint, motif, colourA, colourB, colourC ]`:

| Category slug | Tint | Motif | A / B / C |
|---|---|---|---|
| trends | #F9DFE6 | flower | #E58AA3 / #FFFFFF / #F2C94C |
| new | #DDE5BE | ball | #7E8F4E / #FFFFFF / #F2C94C |
| baby-kids | #F9DFE6 | bunny | #F4B8C6 / #FFFFFF / #E58AA3 |
| clothing | #F1E2D0 | stripes | #C9A98A / #8C5B3E / #F4EBDD |
| seasonal-decor | #FFF1B8 | heart | #D9783C / #8C5B3E / #F2C94C |
| home-living | #DDE5BE | hex | #7E8F4E / #4C5B2A / #DDE5BE |
| accessories | #F9DFE6 | hex | #C47A8C / #FFFFFF / #E58AA3 |
| toys-plushies | #F1E2D0 | bunny | #C9E0A8 / #FFFFFF / #7E8F4E |
| granny-squares | #FFF1B8 | granny | #F2C94C / #8C5B3E / #4C5B2A |

Motifs available (`cpco_motif`, 100x100 viewBox): `granny`, `flower`, `heart`, `hex`, `stripes`, `ball`, `bunny` (default). Tile background: `linear-gradient(165deg, #fff 25%, tint)`. **For a new niche:** keep the function, replace the slug map and draw 5-8 motifs that fit the niche (keep dashed "stitch" strokes only for crochet).

Icon set (`cpco_icon`, 24x24, 2px round stroke, `currentColor`): menu, close, search, chev, back, down, plus, minus, filter, dl, check, yarn, home, grid, mail, share, file, star. Add niche icons in the same style.

---

## 6. Imagery and social formats

| Name | Size | Use |
|---|---|---|
| `cpco_card` | 520 x 520 | Card thumbnails |
| `cpco_og` | 1200 x 630 | Open Graph / Twitter large card |
| `cpco_pin` | 1000 x 1500 | Pinterest vertical pin and main product image |

Rules: use the featured image as the main photo (min 1000 x 1500); extra photos attached to the post appear as thumbnails (max 6); alt text always describes the object and step; images use `loading="lazy"` except the first (`fetchpriority="high"`). Brand look for generated thumbnails: cream background, cocoa text, yellow + olive + rose accents, Plus Jakarta Sans 800 headline, small logo bottom-left. Use own photos only.

---

## 7. Ad system

14 named slots (`cpco_ad_slots()`; label, size, shape class):

| Slot | Where | Size | Shape |
|---|---|---|---|
| home_top | Home, under hero | 728x90 | lb |
| home_mid | Home, between rows | 728x90 | lb |
| home_bottom | Home, before newsletter | 728x90 | lb |
| list_top | Lists, above grid | 728x90 | lb |
| sidebar | Lists, under filters | 300x250 | rect |
| in_grid | Lists, card after 5th item | in-feed | card |
| list_bottom | Lists, below grid | 728x90 | lb |
| pat_after_dl | Pattern, below download box | 728x90 | lb |
| pat_wait | Pattern, inside 5s wait | 300x250 | rect |
| pat_content | Pattern, in content | 336x280 | rect |
| pat_sidebar | Pattern, sticky sidebar (desktop) | 300x600 | tall |
| pat_related | Pattern, in-feed in related row | in-feed | card |
| sticky_mobile | Phones, bar above tab bar | 320x50 | bar |
| interstitial | Full screen between pages (off by default) | full | full |

Behaviour
- Output: `<aside class="cp-ad cp-ad--{shape} cp-ad--{slot}" aria-label="Advertisement"><span class="cp-ad__lbl">Advertisement</span>...</aside>`.
- Empty slot shows a grey "Ad space + size" placeholder when "Show placeholders" is on (always for editors); with it off, empty slots output nothing.
- Paste the AdSense/other code per slot in **Patterns -> Ad slots**; the shortcode `[cpco_ad slot="home_top"]` also works in content.
- Min heights prevent layout shift: lb 100px, rect 270px, tall 300px (620px sticky on desktop), bar 58px, card 240px.
- Sticky phone bar is dismissible and only on pattern pages.
- Interstitial needs both code and the toggle (default off). Rules in `site.js`: never on the first two page views of a session (from the 3rd), once per session, never on product pages, appears after 1.2 s, close button after 3 s, closes itself after 20 s.
- The carousel auto-advances every 5 s (off when the visitor prefers reduced motion or presses pause); the download wait is 5 s (`data-wait`).
- Keep the first screen on a pattern page free of ads above the Quick answer; lazy-load ad scripts.

---

## 8. WordPress architecture (to rebuild)

### 8.1 File map

```
theme-root/
  style.css            theme header only
  theme.json           v3: palette, font, content widths, element styles
  functions.php        defines VER, requires inc/*
  inc/core.php         setup, image sizes, CPT + taxonomies + meta, metabox, ad slots, download counter,
                       newsletter handler, icons, motifs, card helpers, stats
  inc/settings.php     admin pages: Ad slots, Site settings
  inc/layout.php       dynamic blocks + shortcodes: header, footer, hero, categories, row, showcase,
                       duo, levels, newsletter, faq, browse, pattern, blog, article, searchbox, ad
  inc/browse.php       lists, filters, sort, pagination
  inc/pattern.php      single product page
  inc/pattern-extra.php  jump bar, materials, steps, tips, guides, maker box (empty = hidden)
  inc/seo.php          titles/meta/OG/JSON-LD/llms.txt/robots/feed/sitemap (defers to Rank Math)
  inc/blog.php         blog list + article
  inc/perf.php         performance tweaks
  assets/site.css      all component CSS (this document)
  assets/pattern-extra.css  v3.2 pattern blocks + print
  assets/site.js       drawers, carousel, filters, gallery, download wait, interstitial
  parts/header.html, parts/footer.html   one dynamic block each
  templates/           index, front-page, home, page, single, single-pattern, archive, archive-pattern,
                       taxonomy-pattern_category, taxonomy-skill_level, search, 404
```

Design pattern: **templates are tiny.** Each template is the header part, one dynamic block (`cpco/...`) or `post-content`, and the footer part. All HTML is produced in PHP (shortcode functions wrapped by dynamic blocks) with newlines collapsed, so `wpautop` never injects stray `<p>`/`<br>`.

### 8.2 Content model

- CPT `pattern` (public, single URL `/pattern/{slug}/`, archive `/patterns/`, supports title, editor, thumbnail, excerpt, custom-fields, author; REST on).
- Taxonomies (all REST-enabled): `pattern_category` (hierarchical, URL `/category/{slug}/`; seeded: Trends, New, Baby & Kids, Clothing, Seasonal Decor, Home & Living, Accessories, Toys & Plushies, Granny Squares), `skill_level` (hierarchical, `/level/{slug}/`; Beginner, Intermediate, Advanced), `pattern_tag` (flat, `/tag/{slug}/`).
- Private CPT `cpco_subscriber` (newsletter emails).
- Meta fields (all `show_in_rest`; editable in the "Pattern details and search summary" metabox):

| Key | Type | Meaning |
|---|---|---|
| cpco_pdf_url | url | File on object storage (Cloudflare R2) |
| cpco_file_size | text | e.g. "2.4 MB" |
| cpco_pages | number | PDF pages |
| cpco_hook | text | Hook size |
| cpco_yarn | text | Yarn and amount |
| cpco_finished | text | Finished size |
| cpco_time | text | Approx. time (leave empty if unknown) |
| cpco_terms | text | US or UK terms |
| cpco_summary | textarea | Quick answer, 1-2 sentences (used by SEO and AI answers) |
| cpco_faq | textarea | One per line: `Question \| Answer` |
| cpco_materials | textarea | One per line *(v3.2)* |
| cpco_steps | textarea | One per line: `Title \| Description \| photo ID` *(v3.2)* |
| cpco_tips | textarea | One per line, real experience only *(v3.2)* |
| cpco_guides | textarea | One per line: `Title \| URL` *(v3.2)* |
| cpco_maker | text | Designer name *(v3.2, also schema author)* |
| cpco_maker_bio | textarea | Real bio *(v3.2)* |
| cpco_tested | text | Real testers only *(v3.2)* |
| cpco_pin_title / cpco_pin_desc | text / textarea | Pinterest copy |
| cpco_downloads | number | Counter (drives "most downloaded" and rank) |

### 8.3 SEO layer (built in `inc/seo.php`)

- Defers to Rank Math when active (titles, meta, OG, sitemap); the theme adds what it lacks.
- JSON-LD: CreativeWork (free, PDF, level, material, interaction count, author = designer if set), FAQPage, BreadcrumbList, BlogPosting, WebPage, CollectionPage. **Never** Recipe or Product schema.
- Twitter card large image, Pinterest rich pin meta, hreflang, noindex on search, filter combinations and author archives.
- `llms.txt`; robots.txt blocks the download counter (`/*?cpco_dl=`) and internal search (`?s=`) for everyone, and allows these AI crawlers (toggle in Site settings): GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, Claude-User, anthropic-ai, PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended.
- RSS carries images and the Quick answer so Pinterest RSS, Metricool, Buffer, Zapier, Make or IFTTT can auto-post. Rank Math sitemap filter at `/sitemap_index.xml`.
- Rank Math description fallback comes from the Quick answer.

### 8.4 Settings pages
Patterns -> **Ad slots** (14 code boxes) and **Site settings** (social URLs, default OG image, AI crawlers toggle, top-strip text/button/link, 3 home banners, interstitial toggle, show placeholders).

---

## 9. Voice and content rules

- English only, plain and friendly. Short sentences. US spelling.
- Every product page opens with a Quick answer (1-2 sentences: what it is, level, size, what you need, that it is free).
- Titles: primary keyword first, benefit and format last, under 60 characters (e.g. "Free ... Pattern (PDF + Photos)").
- Meta descriptions 135-160 characters; never claim a level the page does not support (be consistent between description, Quick answer, FAQ and schema).
- FAQ: 4-6 questions, answers built from real facts of that item; no identical template answers across pages.
- Never invent designers, testers, reviews, times or prices. Leave a field empty instead.
- Publish only files you own or that clearly allow redistribution. Check the PDF itself for "do not share/post" clauses.

---

## 10. Quality checklist (per page type)

- [ ] Light theme only, no black blocks, yellow header, olive CTA.
- [ ] 2 / 3 / 4 column grid at phone / tablet / desktop; no horizontal scroll at 360px width.
- [ ] Touch targets at least 44px (icon buttons, tabs).
- [ ] One H1 per page; headings in order; images have alt text.
- [ ] Ads labelled, placeholders styled, no layout shift (min heights).
- [ ] Empty fields hide their blocks.
- [ ] Contrast checked (use `--cp-muted: #6E635D`).
- [ ] Core Web Vitals: only Plus Jakarta Sans loaded (3 weights), first image eager, rest lazy.
- [ ] Rank Math title/description/focus keyword set; JSON-LD valid; sitemap submitted after real items exist.

---

## 11. Rebuild recipe for a new niche

1. **Rename.** Pick a 4-letter prefix (this site: `cpco`, CSS `cp-`). Search/replace `cpco_` and `cp-` (functions, options, meta keys, classes, block names `cpco/*`) in one pass. Rename the CPT `pattern` and taxonomies (`pattern_category`, `skill_level`, `pattern_tag`) to the new niche words (e.g. `recipe`, `meal_type`, `difficulty`). Keep slugs short.
2. **Brand tokens.** Change only section 2.1 values (yellow/cocoa/olive/rose) and the font if wanted. Keep the spacing scale, radii and breakpoints. Keep `--cp-muted: #6E635D`.
3. **Taxonomy seed.** Replace the category and level seeds in `core.php` and the slug map in `cpco_cat_style`; draw matching motifs.
4. **Meta fields.** Replace `cpco_meta_fields()` with the niche's facts (keep `pdf_url`/file fields if it is also a download library, keep `summary`, `faq`, `steps`, `tips`, `maker`, `downloads`). Update the At-a-glance rows in `pattern.php`.
5. **Schema.** Choose the right type: `CreativeWork` for downloads; for recipes use `Recipe` (and only then); for other content use `Article`. Keep FAQPage and BreadcrumbList.
6. **Copy.** Rewrite header tagline, hero slides, category names, footer sentence, legal pages (not legal advice: have them reviewed).
7. **Build order.** Core + CPT -> CSS tokens -> header/footer/tab bar -> cards + browse -> product page -> blog/article -> ads -> SEO -> perf -> content import.
8. **Workflow with WPVibe.** Create a draft theme, edit, preview, then publish only after a backup and explicit approval. New meta keys are only registered once the theme is live, so set them with WP-CLI `post meta update <id> <key> <value>` or publish first.

---

## 12. Lessons learned (do not repeat)

- **CDN/WAF:** Hostinger's CDN blocked large `functions.php` writes (403). Split code into `inc/` files and keep edits small.
- **Rate limits:** Hostinger 429s on bursts. Space writes out; avoid parallel bulk calls. The WPVibe free plan allows about 300 calls per 24 hours.
- **wpautop:** collapse newlines in shortcode output and use dynamic blocks in templates.
- **Draft posts:** drafts are not fetchable by tools; the owner must open the preview while logged in. Always confirm a post's status (a "draft" demo was actually published once).
- **Meta in REST:** keys that are registered only by an unpublished draft theme are silently ignored by REST writes.
- **Rank Math meta** are protected keys: write with WP-CLI `post meta update ... --force`.
- **JSON-LD:** decode HTML entities (`html_entity_decode`) before output; truncated meta descriptions need a safe word-boundary cut.
- **z-index:** sticky footers inside drawers need `z-index: 5` above ads.
- **Third-party PDFs:** check for redistribution bans before importing; never upload someone else's photos.
