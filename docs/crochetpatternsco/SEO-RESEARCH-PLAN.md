# SEO research plan for crochetpatternsco.com (approved 2026-10-15)

Markets: USA, Canada, Australia, UK, Europe, then rest of the world. Language: English first.
Budget: $0 extra. Tools: Semrush (owned), claude-seo (free, on the laptop), Search Console (free).
Skipped on purpose: rankme.fast (needs Docker plus a paid data vendor, duplicates Semrush), SEO-Image-Toolkit (Etsy tool, proprietary licence, EXIF keywords do not help Google), AnswerThePublic (Semrush Topic Research covers it).

## Why a laptop is needed
This cloud session cannot reach crochetpatternsco.com, Semrush or AnswerThePublic (network proxy), and has no Docker. Crawling audits run on the laptop. Keyword data comes from Semrush CSV exports. I analyse the files and apply fixes through WPVibe.

## Step 1: seed keywords (paste these into Semrush Keyword Magic Tool, one at a time)
1. free crochet patterns
2. amigurumi pattern
3. crochet pattern pdf
4. baby crochet patterns
5. crochet bunny pattern
6. crochet koala pattern
7. crochet animal patterns
8. granny square pattern
9. crochet blanket pattern
10. crochet hat pattern
11. crochet christmas ornaments
12. crochet for beginners
13. beginner crochet stitches
14. crochet hook size chart
15. crochet yarn weight chart
16. crochet abbreviations

Why these: they match the live pages (2 patterns, hook/yarn/abbreviation guides, beginner guides, category hubs). Add any pattern idea you plan to publish next.

## Step 2: competitors to check (candidates only; confirm by keyword overlap in Semrush)
Large pattern sites, small pattern blogs and PDF sellers that appeared in searches or are well known in the niche: favecrafts.com, sweetsofties.com, sarahmaker.com, amigurumitoday.com, yarnspirations.com, allfreecrochet.com, ravelry.com, etsy.com (PDF sellers). In Semrush Organic Research, also look at the domains that rank for "baby bunny amigurumi crochet pattern" and "free amigurumi pattern" with low authority: those are the realistic targets. Remove any site that shows no keyword overlap. Never copy their text or patterns.

## Step 3: Semrush exports (about 30 minutes)
For each database US, CA, AU, UK, DE, FR, ES (and Global if available):
- Keyword Magic Tool for each seed: export CSV (keyword, volume, KD, intent, SERP features). Also export the Questions filter.
- Organic Research for 5 confirmed competitors: export Top pages and Keywords.
- Keyword Gap: crochetpatternsco.com against 3 competitors: export Missing and Weak.
- Topic Research for "amigurumi" and "crochet for beginners": export questions.
Upload the CSVs to the chat. Keep file names like `kmt-US-amigurumi-pattern.csv`.

## Step 4: claude-seo audit on the laptop (about 20 minutes)
1. Install Claude Code CLI, Python 3.10+ and git.
2. In Claude Code:
   - `/plugin marketplace add AgriciDaniel/claude-seo`
   - `/plugin install claude-seo@agricidaniel-claude-seo`
   - `/seo setup`, then `/seo doctor`
3. Run on https://crochetpatternsco.com: `/seo audit`, `/seo schema`, `/seo geo`, `/seo images`, `/seo sitemap`, and `/seo page` on the koala and bunny pages.
4. No API keys needed. Optional later: free Google PageSpeed key; Search Console login on the laptop only. Never paste keys into chat.
5. Send me the report files.

## Step 5: image SEO (no extra tool)
Send the real photos (several angles, a size photo with a hand or ruler, one vertical pin image). I resize to about 1200 px, convert to WebP, name files by subject, upload with keyword alt text and captions. No AI images presented as finished toys.

## Step 6: Search Console (weekly)
Export Performance (queries, pages, countries) as CSV. Request indexing for each new URL.

## What I deliver after Steps 3 and 4
`docs/crochetpatternsco/SEO-KEYWORD-PLAN.md`: keyword clusters with volume and difficulty per country, page mapping (pattern, hub, guide, roundup), a 12-week content calendar, the first 10 keywords to win, UK-term and translation notes (hreflang only when real translations exist), and the fix list from the audit.

## Permissions and installs
- Website: nothing to install. Rank Math and WPVibe are enough.
- Laptop: Claude Code CLI, Python 3.10+, git (Playwright is installed by `/seo setup`).
- Me: no new permission. Theme changes still need your explicit go and a backup.
