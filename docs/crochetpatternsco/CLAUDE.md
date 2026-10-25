# crochetpatternsco.com: project memory (read this first)

Last updated: 2026-10-25. Keep this file short. Put dated progress in `PROJECT-NOTES.md` and read only its last 40 lines.

## Goal and owner
- Goal: TRAFFIC. A fast, SEO/GEO/AI-ready library of free crochet PDF patterns (about 1,000 planned). Nothing is sold. PDFs live on Cloudflare R2 at `https://files.crochetpatternsco.com/`.
- The owner works mostly from a phone and writes short English. Be brief, give exact taps and URLs, do not ask the same question twice.
- The owner states that all PDFs and photos are the team's own. Do NOT ask again about ownership or whether a photo is real. Exceptions already handled: the sheep pattern (designer @anastasiya_budaeva, credit kept on page and PDF, written permission still to be kept by the owner) and the Easy Winter Beanie (third party, not published).
- Never invent hook sizes, times, stats or designers. Do not call AI images the finished toy.

## Stack and tools
- WordPress block theme `crochet-patterns-co` (live version in `functions.php`, `CPCO_VER`; 3.5.3 on 2026-10-25). Custom post type `pattern`; taxonomies `pattern_category`, `skill_level`, `pattern_tag`. Rank Math SEO is active.
- WPVibe MCP controls the site. Quota: 100 calls per rolling 24 hours (about 95 used on 25 Oct). Save calls: batch, use `/wpvibe/v1/content/search` and `/content/edit` (literal match, `replace_all` works) instead of reading or rewriting whole posts, use `_fields=`, use `get_page_html` with `selector` or `offset`. On a Hostinger 429, wait 60 to 90 s with `python3 time.sleep`.
- Theme work is draft first: `create_draft_theme`, `edit_file` (single-line anchors; multi-line often fails), preview with `get_preview_url`, then publish ONLY after the owner says "publish" and confirms a recent backup. The previous theme is kept as `crochet-patterns-co-wpvibe-backup`.
- Preview-only PHP helper trick (used for PDF photo extraction, WebP regeneration): add a temporary file to the draft theme that runs only with a secret query argument on the preview URL, read its output with `get_page_html`, then delete it before publishing. SAFETY RULE: any helper that deletes files must be dry-run first and the posts that link those files must be checked (a cleanup once broke three sheep images).
- Search Console MCP (`mcp__google_search_console__*`) is read-only: inspect URLs, sitemaps, redirects, TLS, robots, PageSpeed, search analytics. Free quota 15 pulls per day. Requesting indexing is manual in the Search Console website (no API).
- Sandbox cannot reach crochetpatternsco.com, Semrush, Canva preview hosts or most upload hosts; it can read the site only through WPVibe. Do not try to bypass this.
- Cloudflare: AI bot policy set to Search = Allow, Agent = Allow, Training = Disallow; AI Labyrinth off; Bot fight mode on. `robots.txt` rules come from the theme (`inc/seo.php`) after Cloudflare's managed block.
- Hosting: Hostinger Premium, 25 GB disk and 400,000 inodes shared; about 4.4 GB and 175k inodes used on 25 Oct. Uploads: the theme shrinks images wider than 1600 px, makes WebP copies and deletes the leftover original. Revisit an R2 offload plugin at about 15 GB or 300k files.

## New pattern workflow (the owner sends a PDF URL and a thumbnail)
1. Read the PDF: `get_page_html` on the PDF URL returns its text. If the PDF has third-party credits or a no-distribution notice, stop and ask once.
2. Build the article content with a script (blocks, Rank Math TOC block with matching heading anchors, 6+ internal links, CPSC small-parts link, keyword in first sentence, an H2, SEO title, description and image alt; about 1,000 to 1,700 words; keyword density at least 0.5%; paragraphs under 120 words). Recipe: `RANKMATH-90-RECIPE.md`. Full permalink 75 characters or fewer.
3. Create the post as a draft: `POST /wp/v2/pattern` with `title`, `slug`, `content`, `excerpt`, `pattern_category`, `skill_level` and `meta`.
   Meta keys: `cpco_pdf_url`, `cpco_file_size` (for example "3.7 MB"), `cpco_pages`, `cpco_hook`, `cpco_yarn`, `cpco_finished`, `cpco_time` (leave blank if unknown), `cpco_terms` (US or UK), `cpco_summary`, `cpco_faq` (lines "Question | Answer"), `cpco_pin_title`, `cpco_pin_desc`, `cpco_materials` (one per line), `cpco_steps` (lines "Title | text"), `cpco_tips` (one per line), `cpco_maker`, `cpco_maker_bio`.
   IDs: categories 2 Trends, 3 New, 4 Baby & Kids, 5 Clothing, 6 Seasonal Decor, 7 Home & Living, 8 Accessories, 9 Toys & Plushies, 10 Granny Squares; levels 11 Beginner, 12 Intermediate, 13 Advanced.
4. Rank Math fields, one WP-CLI call each: `post meta update <id> rank_math_title '...' --force` (60 characters or fewer, keyword first, a number, Free), `rank_math_description` (135 to 160 characters), `rank_math_focus_keyword 'a,b,c'`.
5. Thumbnail: `request_upload` (give the owner the link), `check_upload`, then `upload_media` with `post_id` (sets the featured image) and keyword alt text; add an image block under the intro with `content/edit`.
6. Publish with `PUT /wp/v2/pattern/<id>` `{"status":"publish"}`. Verify the live head with `get_page_html` (title, description, canonical, og:image), run `page_speed`, and tell the owner which URLs to request for indexing.
7. Append a short dated entry to `PROJECT-NOTES.md`, commit and push to the session branch. Never create a pull request unless asked.

## Pinterest plan
Details in `PINTEREST-PIPELINE.md` (5 different pins per pattern, 1000 x 1500, title 100 characters or fewer, board per keyword, Canva brand kit `kAHJGFJ36OE`, Canva MCP, CSV or scheduler for posting). Still to do: vertical pins for the van, sheep and elf; Pinterest account claim; boards.

## Published patterns (post IDs)
41 bunny, 42 koala, 69 sheep, 80 Christmas van, 83 Elf Chris. Tools page 63 (hook converter and stitch calculator). Guides 23 to 26 and 31 to 40. Drafts: 20 Teddy bear, 22 Elara doll. Media 82 is an unused duplicate. Pattern PDFs: bunny and koala names in the notes; sheep `sheep.pdf`; van `Christmas_Van_Pattern.pdf`; elf `Elf_Chris_Crochet_Pattern.pdf`.

## Open items (as of 2026-10-25)
- Owner: request indexing in Search Console for the elf, van, bunny, koala, hat size chart and /blog/; press Update once in the editor for each new post and send red Rank Math tests; keep the sheep designer's written permission; check Cloudflare Security events for blocked Googlebot (the redirect checker got 403).
- Ask the sheep designer: romper row 9 (original x 6 gives 70, edition uses x 5) and the meaning of "P" (assumed puff stitch).
- Van PDF has no roof instructions (page says so); the owner may add a roof page.
- Pins for van, sheep, elf; Pinterest setup; weekly Search Console report (Make scenario into a Google Sheet, needs the owner to authorise Google in Make once).
- More internal links to the hat size chart and the Christmas ornaments guide; Trends and New hub texts; optional Google Fonts self-hosting.

## Cheap sessions
A long session re-reads its whole history on every message. Start a new session per task, read this file and the tail of `PROJECT-NOTES.md`, do not paste whole pages or PDFs into the conversation, and keep answers short.
