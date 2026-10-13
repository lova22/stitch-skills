# crochetpatternsco.com: project notes and SEO playbook

Saved from the working session so the plan can be recapped later. Last updated: 2026-10-08.

## 1. Project in one paragraph

A professional, fast, ad-monetized WordPress site at https://crochetpatternsco.com offering about 1000 free crochet-pattern PDFs. No registration is needed and the newsletter is optional. PDFs are hosted on Cloudflare R2 (`files.crochetpatternsco.com`). The design is a Noon / Teachers-Pay-Teachers-style marketplace: yellow header, cocoa / olive / rose palette, light mode only, English only. Goals: strong SEO (Google, Gemini, ChatGPT, Claude answers), Rank Math compatibility, social/Pinterest readiness, ad slots with placeholders, AdSense-ready legal pages, and Claude-driven publishing. Later: auto-posting to Pinterest/Facebook (Metricool) and branded thumbnails (Canva/Adobe).

## 2. What exists today

- Live theme `crochet-patterns-co` (v3.1.0), a block theme with dynamic `cpco/*` blocks:
  - `functions.php` and `inc/` (core, settings, layout, browse, pattern, seo, blog, perf)
  - `assets/site.css`, `assets/site.js`, `templates/`, `parts/`, `theme.json`
- CPT `pattern` with taxonomies and meta: PDF URL, file size, pages, hook, yarn, finished size, time, terms, summary, faq, pin title, pin description, downloads.
- 14 ad slots, an optional interstitial, and a download counter.
- SEO layer: titles, meta, OG/Twitter/Pinterest, JSON-LD (CreativeWork, FAQPage, BreadcrumbList, BlogPosting, WebPage, CollectionPage), llms.txt, robots.txt with AI-bot rules, sitemap filter, RSS with images, noindex for search/filter/author. It defers to Rank Math (1.0.280). Sitemap: `/sitemap_index.xml`.
- Pages: Home(11), Blog(12), About(13), Contact(14), Privacy(3), Terms(16), Cookie(17), Disclaimer(18), Copyright(19).
- Sample patterns IDs 6, 7, 8 (to delete). Demo draft pattern ID 20 (teddy bear; to delete before launch).
- Cloudflare R2 bucket `crochet-patterns`. Hostinger hosting with Cache Manager on.
- Prototype artifact: https://claude.ai/artifact/1Rrguj789TyotmjtTShRvT

### Operating rules
- Theme edits: create a draft theme, edit, preview, and publish only after explicit approval and a confirmed backup.
- WPVibe Free plan has a 300 calls per 24h limit, and Hostinger rate-limits (429). Batch carefully.
- Rank Math meta must be written with `wp post meta update ... --force`.
- Contact email in use: contact@crochetpatternsco.com (confirm). Privacy and terms are generic templates, not legal advice.

## 3. SEO analysis of the demo post (ID 20): summary

Scores: technical 9/10, intent match 7, content depth 4, E-E-A-T 3, images 3, internal linking 2, GEO/AI 7, off-page 0.

Top weaknesses:
1. The page is thin: it is a PDF landing page, not a resource.
2. No original photos, so weak for Google Images and Pinterest.
3. No experience signals (designer, tester, real materials, mistakes and tips).
4. The primary keyword is too narrow. Use "teddy bear amigurumi crochet pattern".
5. "-demo" in the slug and title.
6. The post is isolated: no clusters or related links.
7. No tutorial layer (photo steps, magic ring, troubleshooting).
8. Scaled-content risk with 1000 templated pages (the biggest site-level threat).
9. Too many ads high on the page hurt Core Web Vitals.
10. The demo PDF is third-party and must be deleted before launch.

Ignore: Recipe/Product schema, keyword-density targets.

## 4. Page template: blocks every pattern needs

1. Pattern at a Glance box: skill, finished size (cm/in), yarn weight and amount, hook, time, stuffing, PDF pages, US/UK terms.
2. Quick answer, 40–60 words, quotable by AI.
3. Download button above the fold, with the ad below the first answer.
4. Maker box: real designer name, bio, "tested by" (never fabricated).
5. Photo steps, 6–10 original photos with descriptive alt text.
6. Tips and common mistakes from real making.
7. FAQ, unique per pattern, built from real stitch counts and sizing.
8. Jump links (materials / FAQ), print button, share and Pin buttons.
9. Related patterns (4), "next in series", last-updated date.

SEO fields for the teddy bear:
- Focus keyword: teddy bear amigurumi crochet pattern
- Secondary: free crochet teddy bear pattern, amigurumi bear with sweater, crochet teddy bear PDF
- Title (<60 chars): Free Teddy Bear Amigurumi Crochet Pattern (PDF + Photos)
- Slug: /patterns/teddy-bear-amigurumi-crochet-pattern/
- Meta (150–160 chars): A free beginner-friendly teddy bear amigurumi pattern with sweater and snood, including a printable PDF, materials list and step photos.

## 5. Decision: one page or two (tutorial vs download page)

**Recommendation: one main page per pattern, plus shared technique tutorials. Do not split every pattern into a tutorial post and a download post.**

- Each pattern gets ONE canonical URL that holds the download, the at-a-glance details, the photo steps, tips and FAQ. It owns the keyword "[x] crochet pattern". One keyword gets one URL.
- Separate tutorial articles are for reusable techniques that serve many patterns: magic ring, invisible decrease, stuffing and shaping, joining amigurumi parts, reading a pattern, sizing clothes. Each links to every pattern that uses the technique, and each pattern links back. This is the cluster that builds authority and earns backlinks.
- Optional, only for the top ~50 flagship patterns: a long "how to crochet a [x]" article for the how-to intent. It uses a different keyword and does not repeat the pattern page's text. It links both ways, and the pattern page stays the main page.
- On the pattern page, show photo milestones and key stitch counts. Keep the full row-by-row text in the PDF so the download keeps its value.
- Why: two near-identical pages per pattern would double the work for 1000 patterns, split ranking signals, risk cannibalization and thin pages, and make the scaled-content risk worse.

## 6. Topical clusters (launch order)

1. Amigurumi animals (teddy bear is the pillar), then bunny, cat, fox, etc.
2. Beginner crochet: stitch guides, magic ring, how to read patterns, best yarn for amigurumi.
3. Baby and gifts, then seasonal (Christmas, Easter, Halloween).

Each cluster has one pillar page and 8–15 children, all linked both ways, plus 5–8 supporting how-to articles.

## 7. Scaling to 1000 safely

- Publish 5–10 a day, starting with the best 50 licensed patterns.
- Every page needs unique value: own photos, unique intro and tips, unique FAQ. Do not clone template FAQ wording.
- Pages without photos stay noindex until improved.
- Only publish files you own or that clearly allow redistribution. Screen the Drive folder before any bulk import.
- Bulk CSV importer with a per-pattern unique-content checklist.

## 8. GEO / AI answers

- Keep Quick answer, At a Glance table and FAQ.
- Keep facts consistent across text, schema and PDF.
- Keep llms.txt and the sitemap current; keep AI crawlers allowed.
- Use the brand name "Crochet Patterns Co" consistently.
- An "About these patterns / how we test" page.

## 9. Off-page and traffic plan

1. Pinterest first: 3–5 vertical pins per pattern from own photos, scheduled in Metricool.
2. Google Search Console and Bing Webmaster Tools: submit the sitemap after the first real patterns are live.
3. Short video (Reels / Shorts / TikTok): timelapse of the finished toy.
4. Communities (Reddit r/crochet, r/amigurumi, Facebook groups): share finished photos, no link spam.
5. Outreach for roundups and features.
6. Weekly newsletter.

## 10. Open task list

- [ ] Build in a draft theme: At a Glance, maker box, jump/print buttons, related patterns, last-updated, pillar and tutorial templates.
- [ ] Apply all steps to the demo post (ID 20) so the full result can be reviewed.
- [ ] Delete the demo (ID 20) and the samples (IDs 6–8) before launch.
- [ ] Test one real licensed PDF through R2 (upload to `patterns/` on files.crochetpatternsco.com).
- [ ] Build the bulk CSV importer.
- [ ] Canva branded thumbnail template (Brand Kit id kAHJGFJ36OE exists; use own photos).
- [ ] Screen PDF licences via Google Drive.
- [ ] Cookie consent plugin (CookieYes or Complianz), backups (UpdraftPlus), newsletter provider.
- [ ] `ads.txt` after AdSense approval.
- [ ] Search Console sitemap submission: `https://crochetpatternsco.com/sitemap_index.xml`.
- [ ] Metricool scheduling to Pinterest/Facebook.
- [ ] Confirm the contact email.

## 11. Progress log

### 2026-10-08: draft theme `crochet-patterns-co-wpvibe-draft` (NOT published yet)
- New files: `inc/pattern-extra.php`, `assets/pattern-extra.css`. Edited: `functions.php` (v3.2.0), `inc/core.php` (new meta fields), `inc/pattern.php`, `inc/seo.php` (author = designer Person).
- New pattern fields: `cpco_materials`, `cpco_steps` (Title | text | photo ID), `cpco_tips`, `cpco_guides` (Title | URL), `cpco_maker`, `cpco_maker_bio`, `cpco_tested`.
- New page blocks: jump links + print button, "Pattern at a glance" tiles, materials, photo steps, tips, technique guides, maker box. Empty fields render nothing.
- Demo post ID 20: renamed to "Teddy Bear Amigurumi Crochet Pattern with Sweater and Snood", slug `teddy-bear-amigurumi-crochet-pattern`, Rank Math title/description/focus keywords set, new fields filled. It was found PUBLISHED and was set back to DRAFT.
- Not yet verified visually: materials, steps, tips and maker blocks (draft posts cannot be fetched by Claude; the owner must open the preview link while logged in).
- Gotcha: new meta keys are only registered by the draft theme, so REST writes to them are ignored until the theme is published. Use WP-CLI `post meta update <id> <key> <value>` before publishing.
- Gotcha: the demo PDF (Teddy Bear by Pupyreva Ksenia) states "Mailing, posting or sharing this pattern on the Internet is strictly prohibited". The designer's photos were NOT uploaded; steps use placeholder tiles. This pattern cannot be offered for download. Screen every real PDF for such clauses before import.
- WPVibe quota is nearly used up (about 300 calls per 24h). Hostinger returns 429 on bursts: space writes out.

- Reusable design system for cloning this structure to another site: `docs/crochetpatternsco/DESIGN-SYSTEM.md`.

### 2026-10-11: pattern post ID 22 (draft): Elara Doll and Chip the Soldier
- Slug `elara-doll-and-chip-soldier-crochet-pattern`; category Toys & Plushies; level Advanced (editorial judgement, change if needed); US terms.
- Rank Math: title "Crochet Doll Pattern: Elara and Chip the Soldier (Free)"; description 146 chars; focus keywords: crochet doll pattern, elara doll crochet pattern, crochet soldier doll pattern.
- Full written pattern kept word for word in the post body (H2 per doll, H3 per part). Materials, parts overview and tips are in the structured fields. No PDF yet (`cpco_pdf_url` empty), no photo (motif placeholder), no designer (`cpco_maker` empty), no time estimate.
- Open: confirm rights to the text, add real photos, upload PDF to R2, name the designer, check stitch counts (Chip hat row 15 adds up to 36, not the stated 40), create tags if wanted.

### 2026-10-11: always-visible download button and growth backlog
- Draft theme: the free download button and sheet now always show. With a PDF: normal flow (5 s wait, ad, `?cpco_dl`). Without a PDF: the last button reads "Save as PDF" and opens the print dialog (print CSS hides header, ads, footer). The no-PDF branch is not yet visually verified.
- Monetization backlog (priority order): (1) affiliate disclosure page + "Shop the supplies" box built automatically from the materials field (Amazon search links with tag, LoveCrafts / Hobbii links), `rel="sponsored nofollow"`, disclosure above the links; (2) real email provider (MailerLite/Brevo/ConvertKit) with a starter-pack lead magnet; (3) premium ad network when traffic allows (Raptive reported 25k monthly pageviews; verify); (4) paid extras (ad-free bundles, large-print or chart versions).
- Rules to verify before launch: Amazon Associates policy (updated Apr 2026) on links in downloadable files and emails; each network's current terms. Do not put affiliate links inside the PDFs until checked.
- Traffic ideas: seasonal Christmas patterns now (Pinterest lead time), technique tutorials, yarn/hook/size calculators, US/UK terms converter, stitch glossary, "I made this" photo uploads, video embeds, QR code and URL in every PDF footer.

### 2026-10-11: traffic-first audit and fixes
- FOUND: category archives `/category/{slug}/` return 404 on the live site (taxonomy base clashes with core post categories). FIXED IN DRAFT THEME v3.3.0: pattern_category base is now `/free-crochet-patterns/{slug}/` and pattern_tag is `/pattern-tag/{slug}/`. Rewrite rules flush on publish (version bump). Verified under draft preview: `/free-crochet-patterns/toys-plushies/` renders.
- FOUND: Cloudflare "managed robots.txt" adds `Disallow: /` for many AI agents (ClaudeBot, GPTBot, ChatGPT-User, Claude-User, Perplexity-User, Google-Extended, Applebot-Extended and more) BEFORE the theme's Allow rules for the same agents, so AI assistants may be blocked from citing the site. Owner must change the Cloudflare setting (Security / Bots, AI crawler or managed robots.txt option). Googlebot is allowed.
- DONE (live): trashed the three fake sample patterns (IDs 6-8; they had invented download counts); created post category Guides (ID 15); wrote descriptions for all 9 pattern categories.
- DONE (drafts, publish with theme): 4 guides, all in Guides category with Rank Math title, description and focus keywords: 23 crochet-abbreviations-us-uk-terms, 24 crochet-hook-size-chart, 25 crochet-yarn-weight-chart, 26 how-to-read-a-crochet-pattern.
- DRAFT THEME v3.3.0 also adds: table styling for guides, automatic "Helpful crochet guides" block on every pattern page (latest 4 Guides), "Free crochet patterns to try" row on guide pages, always-visible download button.
- NEXT: owner approves publish (after backup) -> publish theme, publish 4 guides, verify, submit sitemap in Search Console and Bing, fix Cloudflare AI setting, add real patterns with own photos, Pinterest.

### 2026-10-11 (later): PUBLISHED
- Theme v3.3.0 is LIVE (backup of the previous theme: `crochet-patterns-co-wpvibe-backup`; owner confirmed a site backup). Category pages now at `/free-crochet-patterns/{slug}/` (verified live).
- 4 guides published: /crochet-abbreviations-us-uk-terms/, /crochet-hook-size-chart/, /crochet-yarn-weight-chart/, /how-to-read-a-crochet-pattern/ (category Guides, ID 15).
- Fixed: the admin user display name was the owner's email address and showed publicly in post bylines; changed to "Crochet Patterns Co" (slug `crochet-patterns-co`).
- Sitemap index now lists post, page and category sitemaps (pattern sitemaps return when real patterns are published). Owner submitted the sitemap to Search Console.
- Open: Cloudflare AI-bot blocking (owner), domain-name similarity question (`crochetpatternco.com` reported by owner; check niche, activity and trademarks before deciding to rename), real patterns with photos and PDFs, Elara post still draft (ID 22), demo post ID 20 still draft (to delete).

### 2026-10-11: 10 scheduled guides (category Guides, ID 15), each with Rank Math title, description, focus keywords
| ID | Go-live (09:00) | Slug | Supports |
|---|---|---|---|
| 31 | 13 Oct | /crochet-christmas-ornaments-guide/ | seasonal-decor |
| 32 | 15 Oct | /amigurumi-for-beginners/ | toys-plushies |
| 33 | 17 Oct | /how-to-join-granny-squares/ | granny-squares |
| 34 | 20 Oct | /crochet-baby-toys-safety-guide/ | baby-kids |
| 35 | 22 Oct | /best-yarn-for-crochet-blankets-cushions/ | home-living |
| 36 | 24 Oct | /crochet-hat-size-chart/ | accessories |
| 37 | 27 Oct | /yarn-and-gauge-for-crochet-clothing/ | clothing |
| 38 | 29 Oct | /beginner-crochet-stitches/ | level/beginner |
| 39 | 31 Oct | /how-to-read-crochet-charts/ | trends |
| 40 | 3 Nov | /how-to-find-good-free-crochet-patterns/ | new |
- Internal links only go backward to guides that are already live on the publish date (plus the 4 existing guides, category hubs, /patterns/ and level pages). The "Keep reading" row adds forward links automatically. TODO after 3 Nov: add forward links from the older guides.
- Facts checked by web search: CPSC small-parts rule (baby safety), stiffening mixes (ornaments), CYC symbols (charts). Head sizes and blanket sizes are NOT from an official table (sources disagree), so the text calls them typical ranges.
- TODO after each goes live: open the URL, check one H1, table styling, links, sitemap entry; owner requests indexing in Search Console. Make a Pinterest chart pin from the hook, yarn and hat charts.

### 2026-10-13: first two real patterns (drafts, waiting for images and PDFs)
- Post 41 `baby-bunny-amigurumi-crochet-pattern` (Toys & Plushies + Baby & Kids, Beginner, 2 mm hook, 18 cm, 5 pages) and post 42 `baby-koala-amigurumi-crochet-pattern` (Toys & Plushies, Intermediate, no hook size or height in the PDF so those fields are empty, 6 pages). Full written pattern word for word, structured fields, FAQ, Rank Math title/description/keywords all set.
- PDF URLs set to `https://files.crochetpatternsco.com/patterns/baby-bunny-amigurumi-crochet-pattern.pdf` and `.../baby-koala-amigurumi-crochet-pattern.pdf`; owner must upload the renamed PDFs to R2 (bucket crochet-patterns, folder patterns). File sizes stored in decimal MB (4.8, 6.7).
- Images (owner's real photos): bunny featured = wide photo on wood; gallery = flowers photo + "Cute Baby Bunny" pin; koala featured = koala pin. Do not use the bunny pin that says "STEP BY STEP WITH PHOTOS" (the PDFs have no step photos). Some bunnies in the photos have a horn that the pattern does not include (the post says so).
- Next: owner uploads PDFs to R2 and images via the WPVibe upload link; then upload_media, attach gallery, verify, publish, Search Console indexing request. After 15 Oct add a link to "Amigurumi for beginners" in both posts.

### 2026-10-13: bunny (41) and koala (42) PUBLISHED
- URLs: /pattern/baby-bunny-amigurumi-crochet-pattern/ and /pattern/baby-koala-amigurumi-crochet-pattern/. PDFs on R2: `https://files.crochetpatternsco.com/Baby%20Bunny%20Pattern%20EN%20(1).pdf` and `.../Baby%20Koala%20PDF.pdf` (verified readable).
- Media IDs: 43 koala pin (featured of 42), 46 bunny wood photo (featured of 41), 47 bunny flowers photo, 45 "Cute Baby Bunny" pin (both attached to 41), 44 bunny pin "STEP BY STEP WITH PHOTOS" (unused, unattached, should not be used because the PDFs have no step photos). Owner says the images are test images; they can be replaced later.
- Verified live: title/description/canonical/robots index, OG image + alt, CreativeWork + FAQPage JSON-LD, sitemap lists both, content and blocks render, related row shows the koala on the bunny page.
- Gaps found, fix in theme v3.4.0 (needs draft, approval, backup): (1) main image alt is forced to "<title> crochet pattern" instead of the media alt text; (2) "Photo steps" jump link and heading appear even when there are no photos; (3) Pinterest button uses a crop of the featured image, add a dedicated pin-image field (use the vertical pin); (4) JSON-LD has no BreadcrumbList/WebPage/Organization on pattern pages (CreativeWork publisher points to a missing #organization node); (5) gallery order ignores menu_order.
- Not tested (would add a fake download): the `?cpco_dl=ID` redirect. Owner should click Download once on each page.
- After 15 Oct add a link to "Amigurumi for beginners" inside both posts.
