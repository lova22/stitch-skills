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
