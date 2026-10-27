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

### 2026-10-13: Rank Math 90+ pass on the two published patterns (41, 42)
- Rank Math only analyses `post_content` (not the theme's meta blocks such as FAQ/materials), and the score is calculated in the editor, so it cannot be read or set from outside. Fixes follow Rank Math's checklist: primary focus keyword = exact phrase in title/slug/intro ("baby bunny amigurumi crochet pattern", "baby koala amigurumi crochet pattern"), SEO title starts with the keyword and has a number and power words, description contains the keyword, keyword in the first paragraph and in an H2, content over 600 words, an image with keyword alt text, a Rank Math TOC block, internal links plus one external link (CPSC small parts), short paragraphs (pattern rows split into blocks under 120 words), keyword used about 7 times.
- Secondary keywords added. Slugs unchanged (full URL is 75 characters).
- TODO: owner opens each post in the editor to read the score and sends a screenshot of failing tests; apply the same method to the 14 guides, the Elara draft (22) and key pages.

### 2026-10-13: Rank Math 90+ pass on the guides (23-26, 31-40)
- Recipe saved as WPVibe skill `rankmath-90-recipe` and as `RANKMATH-90-RECIPE.md`. Applied to every guide: exact-phrase focus keyword in SEO title (under 60 characters, number + power word), slug, first sentence and one H2; Rank Math TOC block with matching heading anchors; at least one external dofollow link (Craft Yarn Council / CPSC); keyword about 1% density.
- Post 37 slug changed to `crochet-gauge-swatch-guide` (title "Crochet Gauge Swatch: Easy Guide to Yarn and Fit (2026)"). Posts 38, 39, 40 rewritten with TOC, anchors and external link; titles: "Beginner Crochet Stitches: 8 Easy Ones to Learn (2026)", "How to Read Crochet Charts: Easy Symbol Guide (2026)", "How to Find Good Free Crochet Patterns: 9 Checks (2026)".
- Not done: guides have no in-content image with keyword alt (needs the owner's real photos or chosen Canva images), so the "image alt" test will still fail on them. Scores can only be read in the editor: owner opens a post, presses Update, and sends the failing-test list.

### 2026-10-13: outside audit of the koala page (7/10), checked against the live HTML
- FIXED: Rank Math Local SEO had default opening hours (Mo-Su 09:00-17:00) and type HobbyShop in the Organization JSON-LD. Cleared `opening_hours` and set `local_business_type` to Organization in option `rank-math-options-titles`; verified the schema graph no longer has openingHours.
- Audit points that were wrong: "Free" is already in the SEO title/OG title; the Rank Math TOC has 6 links in the HTML; the Download button exists (JS button, plus a sticky mobile bar); a quick-facts box ("Pattern at a glance") exists; CreativeWork, FAQPage, Organization, WebSite and WebPage schema exist; related patterns, byline and Pinterest buttons exist. HowTo schema is not worth adding (Google dropped HowTo rich results).
- Audit points that were right (theme v3.4.0 list): in-content download button after the intro and at the end; BreadcrumbList schema; main image alt shows "Baby Koala Amigurumi Crochet Pattern crochet pattern"; "Photo steps" label with no photos; Pinterest icon looks like an upload arrow; byline not linked to /about/; "1 downloads" grammar and the "#1 most downloaded" badge shown with a single download (misleading, show only after a threshold); more photos needed from the owner; hook size and time must come from the owner, never invented.

### 2026-10-13: theme v3.4.0 PUBLISHED (owner approved; previous theme kept as `crochet-patterns-co-wpvibe-backup`)
- Pattern pages: main image uses the media library alt text (fallback "<title> crochet pattern"); "1 download" singular; byline links to /about/; Pinterest button shows "Pin it"; jump link says "Steps" unless a step has a photo ID; two in-content "Download free PDF" call-to-action boxes (after the quick answer and after the pattern text), hidden in print; BreadcrumbList JSON-LD is now printed even when Rank Math is active (Rank Math does not print it for this theme).
- Verified: draft preview and live bunny page show the new alt text and Pin it; koala preview shows breadcrumb schema and CTA. Owner confirmed the "1 download" and the "#1 most downloaded" badge are real (own test download), so the badge stays.
- Not changed: dedicated pin-image field (the button uses the 1000x1500 crop of the featured image); gallery order (core already sorts attached media by menu_order).
- Open: owner photos for both patterns (angles, size shot, vertical pin); hook size and time for the koala; Cloudflare AI-bot setting; Search Console indexing requests; Rank Math editor screenshots.

### 2026-10-15: SEO research plan approved
- Plan saved in `SEO-RESEARCH-PLAN.md`: claude-seo on the owner's laptop for the technical/schema/GEO audit, Semrush CSV exports (US, CA, AU, UK, DE, FR, ES) for keywords and competitors, Search Console CSVs for tracking. Skipped rankme.fast (Docker plus paid DataForSEO), SEO-Image-Toolkit (Etsy tool, proprietary licence) and AnswerThePublic (Semrush covers it).
- This cloud session cannot reach crochetpatternsco.com, Semrush or AnswerThePublic; it reads the site through WPVibe only.
- Waiting for: Semrush exports and claude-seo audit reports from the owner.

### 2026-10-15: US Semrush data analysed
- Two exports (16,963 keywords, volume 50+; and KD 49 or lower, 16,701 keywords). Result in `SEO-KEYWORD-PLAN.md`: clusters, quick fixes, publishing order for the PDF library, 12-week plan.
- Finding: "baby bunny amigurumi crochet pattern" and "baby koala ..." have no measurable volume; real searches are "crochet bunny pattern" (2,400, KD 12), "bunny crochet pattern" 2,900, "koala crochet pattern" 320. Proposed retarget of focus keywords/titles for posts 41, 42 and 26 (not applied yet, waiting for owner OK).
- Biggest keyword: "crochet patterns for beginners" 135,000 (KD 29) for `/level/beginner/`.

### 2026-10-15: theme v3.5.0 PUBLISHED (hub text + free tools), page 63
- New `inc/hub.php`: category and skill-level hubs show an intro above the pattern list and a longer guide below it (page 1 of the plain hub only). Text lives in term meta `cpco_intro` and `cpco_body` (registered for REST; `wp term meta` is not allowed in WPVibe WP-CLI, so write them with `PUT /wp/v2/<taxonomy>/<id>` and `{"meta":{...}}`). The archive uses options `cpco_archive_intro` and `cpco_archive_body` (not filled yet).
- Hub texts written: Beginner (skill_level 11), Baby & Kids (4), Home & Living (7), Accessories (8), Toys & Plushies (9). Not yet: Clothing (5), Seasonal Decor (6), Granny Squares (10), Trends (2), New (3), `/patterns/` archive.
- New `inc/tools.php` + `assets/tools.js`: shortcode `[cpco_calculators]` (hook size converter mm/US/UK with matching yarn weight, and stitch count calculator with swatch gauge, multiple and extra stitches). Page 63 `/crochet-hook-size-converter/` (published; Rank Math title, description, focus keywords set). Tested the script in headless Chromium with the real markup: conversions and counts correct, no errors.
- Observed: all 10 scheduled guides are now published (dates 14 Oct 20:42), most likely because the owner pressed Update on each in the editor. The 3-week drip no longer applies.
- Open: link to `/crochet-hook-size-converter/` from the hook size chart guide; check hub page titles/descriptions; hub texts for the other categories; Semrush check of volume for "crochet hook size converter" (not verified); retarget keywords on posts 41, 42, 26 (waiting for owner OK).

### 2026-10-15: keyword retarget applied, remaining hub texts
- Posts retargeted from the Semrush data (slugs unchanged): 41 bunny: title "Crochet Bunny Pattern: Baby Amigurumi Bunny", Rank Math title "Crochet Bunny Pattern: Free Baby Amigurumi, 18 cm (PDF)", focus "crochet bunny pattern, free crochet bunny pattern, bunny crochet pattern", first sentence, H2, image alt and quick-answer summary changed. 42 koala: title "Koala Crochet Pattern: Baby Amigurumi Koala", Rank Math title "Koala Crochet Pattern: Free Baby Amigurumi Koala (PDF)", focus "koala crochet pattern, crochet koala pattern free, koala bear crochet pattern". 26: Rank Math title "How to Read Crochet Patterns: Easy Beginner Guide (2026)", focus "how to read crochet patterns, ...", first sentence and first H2 changed.
- Hub texts added for Clothing (5), Seasonal Decor (6), Granny Squares (10) and the `/patterns/` archive (options `cpco_archive_intro`, `cpco_archive_body`). Hook size chart guide (24) now links to the converter. Verified `/patterns/` shows the new card titles.
- WPVibe quota: 100 calls per rolling 24 hours; about 75 used after this batch. Plan large jobs with fewer calls (batch edits, avoid repeated reads).
- Still open: Trends and New hub texts; owner photos for patterns; Semrush volume for "crochet hook size converter"; Search Console indexing requests; link plan; Cloudflare AI-bot setting; first 30 targets list (patterns need the owner's PDFs).

### 2026-10-16: PDF redesign and rights decisions
- Baby bunny PDF redesigned (6 pages, 0.7 MB; stitch counts re-checked; text unchanged). Template saved in `pdf-template/`. Owner has not yet approved or uploaded it to R2 (target name `baby-bunny-amigurumi-crochet-pattern.pdf`; then update `cpco_pdf_url`, `cpco_pages` = 6, `cpco_file_size`).
- Owner sent two third-party PDFs: Easy Winter Beanie (by Sarah Thompson / Rich Textures Crochet; its last page says personal use only and no reproduction or distribution) and "Mini Пухля Овечка" (by @anastasiya_budaeva; carries red advert stamps of a pattern resale library, pages 3, 12, 16, one mentioning "leaked" masterclasses). Decision: not redesigned or published without the designers' written permission; drafts of permission messages (English, Russian) given. A third file `yes.pdf` is the same sheep PDF with the author line, links and stamps removed, and is not a permission; not used.
- Options given to the owner: written permission, link roundups to the designers' own pages, original patterns written by us, own-team patterns (bunny, koala, others).

### 2026-10-16: Mini Fluffy Sheep PUBLISHED (pattern 69)
- Owner reported the designer (@anastasiya_budaeva) said yes; written terms are not yet on file (keep her message). Credit stays on the page, in the PDF and in the maker box ("Pattern and photos by ... English edition presented by Crochet Patterns Co").
- English, US-terms, redesigned PDF (21 pages, 3.3 MB) uploaded by the owner to R2: `https://files.crochetpatternsco.com/sheep.pdf` (`cpco_pdf_url`, `cpco_pages` 21, `cpco_file_size` 3.3 MB).
- Page: `/pattern/crochet-sheep-pattern-amigurumi/` (70 characters). Focus keyword "crochet sheep pattern" (+ amigurumi sheep pattern, crochet lamb pattern); search volume NOT checked in Semrush. Rank Math title "Crochet Sheep Pattern: Free Mini Amigurumi, 17 cm (PDF)", description 149 characters, TOC block, 6 internal links, CPSC link, designer Instagram link, about 1,700 words, keyword about 10 times. Category Toys & Plushies, level Intermediate (our judgement), time left blank.
- Photos: the sandbox cannot reach any upload host, so a one-off helper in a DRAFT theme (deleted afterwards, never published) downloaded the PDF on the server, cut out the 6 embedded JPEGs byte for byte (objects 28, 163, 185, 126, 73, 142) and saved them as media 70-75 (70 = featured and first image). Alt text carries the keyword. Technique reusable for any PDF whose photos are plain DCT JPEG streams.
- Content fixes recorded on the page: romper row 9 uses x 5 (original x 6 gives 70, not the stated 60); "P" is described as a puff (bobble) stitch from the romper photos. Still to confirm with the designer.
- Verified live: title, description, canonical, OG image (1128 x 1128), WebPage schema, download sheet, related patterns, maker box.
- Open: owner presses Update in the editor to read the Rank Math score; Search Console indexing request; 5 pins + board plan for the sheep; check the designer's written permission; Semrush volume for the sheep keywords.

### 2026-10-24: Search Console review and AI-bot access fixed
- Search Console is linked to Rank Math (`sc-domain:crochetpatternsco.com`) but no performance data is stored (no GSC data table, no analytics cron). Only 4 URL inspections exist: sheep pattern, crochet charts guide and yarn weight chart "Submitted and indexed"; `/blog/` "URL is unknown to Google". No Search Console connector exists in this session; options: re-save the Google connection in Rank Math Analytics, CSV exports, or a Make scenario into a Google Sheet.
- Internal links (Rank Math link counter, content links only): sheep (69), koala (42), Christmas ornaments guide (31) and "find good free patterns" guide (40) have 0 incoming content links; to add contextual links (bunny/koala/sheep cross links and guides to patterns).
- Cloudflare (owner changed in dashboard): Search = Allow, Agent = Allow (was "Block on pages with ads"), Training = Disallow, Bot Preference Sync on, AI Labyrinth off, Bot fight mode on.
- Theme `inc/seo.php` robots.txt rules: only AI search and assistant bots get "Allow" (OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User). Training bots (GPTBot, ClaudeBot, anthropic-ai, Google-Extended, Applebot-Extended) are left to the Cloudflare Disallow block, so no contradiction. Published (backup theme `crochet-patterns-co-wpvibe-backup`); live robots.txt verified.

### 2026-10-25: health check, speed work, upload limits, Christmas Van published
- Health check (Search Console + Rank Math): 14 of 25 inspected URLs indexed; bunny, koala, /blog/ and 7 legal pages "unknown to Google"; /crochet-hat-size-chart/ "crawled, currently not indexed". Redirects clean (http->https, www->apex, trailing slash: single 301). TLS valid to 2027-01-06. Mobile PageSpeed: home 94, sheep 91 (LCP 2.6 s). Search traffic still negligible (2 clicks, about 22 impressions in 28 days).
- Internal links added (bunny/koala/sheep cross links; guides 32, 34, 40 link to the patterns; 32 also to the ornaments guide).
- Theme 3.5.1: WebP copies for new JPEG/PNG uploads; publisher @id now follows Rank Math's Person/Company type (#person vs #organization). Theme 3.5.2: uploads wider than 1600 px or taller than 2400 px are shrunk in place; 1536/2048 copies no longer made. Existing media unchanged. Hosting: Premium plan 25 GB, about 4.4 GB and 175k of 400k inodes used (shared across sites); decision: keep photos in WordPress with the caps, revisit R2 offload at about 15 GB or 300k files.
- Christmas Year-Round Van (pattern 80) PUBLISHED: `/pattern/crochet-christmas-van-pattern/`. PDF `https://files.crochetpatternsco.com/Christmas_Van_Pattern.pdf` (8 pages, 0.6 MB). Featured image media 81 (owner's real photo, 1200x800); media 82 is a duplicate upload, unused. Owner states the PDF and photo are the team's own. The PDF has no instructions for the snowy bobble roof and gives some counts in short form; the page says so and does not claim a roof. Focus keyword "crochet christmas van pattern" (volume not checked). Mobile PageSpeed 93, LCP 2.6 s, CLS 0.
- Open: Search Console indexing requests for the new and unknown URLs (manual button); the redirect-check tool returned 403 for any page of the site on 25 Oct (sheep page too, which returned 200 earlier) while PageSpeed and WPVibe load the pages fine: check Cloudflare Security events for blocks on Googlebot; vertical 1000x1500 pins for the van and sheep.

### 2026-10-25: Elf Chris published, theme 3.5.3
- Elf Chris crochet doll (pattern 83) PUBLISHED: `/pattern/crochet-elf-doll-pattern/`. PDF `https://files.crochetpatternsco.com/Elf_Chris_Crochet_Pattern.pdf` (27 pages, 3.7 MB). Focus keyword "crochet elf doll pattern" (volume not checked); Rank Math title "Crochet Elf Doll Pattern: Free Elf Chris, 11 in (PDF)"; level Advanced; categories Toys & Plushies and Seasonal Decor. Featured media 84 (owner's image, 1254x1254). The page summarises how each part is built and leaves the row-by-row text to the PDF. Owner states the pattern is the team's own.
- Theme 3.5.3: when WordPress converts an upload to WebP the leftover original PNG/JPEG is deleted automatically. A one-off cleanup deleted the leftover originals of media 70-75 (sheep), 81, 82 (van) and 84 (elf), freeing 5.2 MB. MISTAKE: it also removed three sheep JPEGs still linked in the sheep article; the links were repointed to the WebP files within minutes and the page has no `.jpg` references left. Lesson: dry-run any file-deleting helper and check which posts link the files before running it.
- Known minor issue: og:image:type still says image/jpeg or image/png while the files are WebP (attachment mime type not updated); scrapers read the real header.
- WPVibe quota nearly used (95 of 100 per rolling 24 h).

### 2026-10-27: 4 new blog guides published (category Guides, ID 15)
- Method: competitor tutorials for each topic were read through public search (moss stitch, how to crochet a blanket, join yarn / magic knot, borders), then original articles were written (own wording, own structure, no copied text). Built with a script that checks words, keyword count, paragraph length and link count before posting. Topics chosen from Semrush (moss stitch crochet 12,100; how to crochet a blanket 6,600; join yarn 2,400; borders = a top page of makeanddocrew) and from the Search Console queries (crochet charts, crochet gauge, US terms; all 0 clicks so far).
- Posts: 91 `/moss-stitch-crochet-tutorial/` (focus "moss stitch crochet"), 92 `/how-to-crochet-a-blanket-for-beginners/` ("how to crochet a blanket"), 93 `/how-to-join-yarn-in-crochet/` ("how to join yarn in crochet"), 94 `/crochet-borders-for-blankets/` ("crochet borders"). Each about 1,200 to 1,500 words, Rank Math TOC block, 6 to 14 internal links, one external link (Craft Yarn Council or HealthyChildren), FAQ. Rank Math title, description and 3 focus keywords set with WP-CLI. Live head of 93 verified (title, description, canonical, index).
- Not done: no images in the posts (the "image alt" Rank Math test will fail until the owner sends real photos); stitch rows were written from general technique, so the owner should crochet one swatch of the moss stitch and the shell/picot borders to confirm the wording; the Rank Math score is read only in the editor (press Update once per post).
- Open: owner requests indexing for 91 to 94 in Search Console; add links from older guides (38 beginner stitches, 35 best yarn, 33 granny squares) to the new posts; next topics: waffle stitch (5,400), magic ring, crochet stitches library (18,100), crochet washcloth.

### 2026-10-27 (later): 4 more general blog guides published (category Guides, ID 15)
- Posts: 99 `/front-post-double-crochet-tutorial/` ("front post double crochet"), 100 `/how-to-hold-a-crochet-hook/` ("how to hold a crochet hook"), 101 `/magic-ring-crochet-tutorial/` ("magic ring crochet"), 102 `/crochet-washcloth-for-beginners/` ("crochet washcloth"). Same format as 91 to 94 (original wording, TOC block, internal links, one external link, FAQ, Rank Math title, description and 3 focus keywords via WP-CLI). Slugs and volumes not checked in Semrush for the last three (washcloth 2,400 comes from the competitor report).
- Waffle stitch was NOT written: the public tutorials disagree on the row structure and it could not be swatch-tested. Write it only after the owner confirms a tested row sequence. "Crochet stitches library" was skipped because guide 38 already covers it (would compete with it).
- Found drafts 86 to 90 (`crochet-gauge`, `crochet-gauge-too-big-or-too-small`, `crochet-stitch-symbols-chart`, `how-to-read-circular-crochet-diagrams`, `us-vs-uk-crochet-terms`) created outside this session; left untouched.
- Open: request indexing for 91 to 94 and 99 to 102; press Update once per new post and send red Rank Math tests; no images in these posts yet (image-alt test will fail); add links from older guides to the new ones.
