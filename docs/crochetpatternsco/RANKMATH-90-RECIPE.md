# Rank Math 90+ recipe for crochetpatternsco.com

Saved as a WPVibe skill named `rankmath-90-recipe` (load it with `load_skill`) and copied here.

Goal: every post and pattern scores 90+ in Rank Math. The score is calculated in the editor, so it cannot be read or set from outside. Build to this checklist, then open the post editor, press Update once, and check the panel.

## Key facts
- Rank Math analyses only `post_content`. The theme's meta blocks (FAQ, materials, steps, tips, summary) are not analysed, so the SEO elements must live in the content.
- The primary focus keyword must be the exact phrase used in the SEO title, slug, first sentence and one H2 (for example "baby bunny amigurumi crochet pattern"). Near matches fail most tests.
- Keep the full permalink at 75 characters or fewer.

## Checklist
1. SEO title under 60 characters, starts with the keyword, has a number (year, size) and a power word (Free, Easy).
2. Meta description 135-160 characters with the exact keyword and a number.
3. Keyword in the first sentence.
4. 600+ words (guides 1,000+).
5. Keyword in at least one H2/H3; about 1% density (6-10 times per 800-1,000 words).
6. At least one image in the content with the keyword in its alt text (owner's real photos only).
7. Rank Math TOC block with matching heading anchors.
8. Two or more internal links to live pages.
9. One or more external dofollow links to verified sources: https://www.cpsc.gov/FAQ/Small-Parts, https://www.craftyarncouncil.com/, https://www.healthychildren.org/.
10. Paragraphs under 120 words (split stitch rows into blocks of 8-12 rows).
11. Unique keyword.

## Block markup
```
<!-- wp:heading {"anchor":"x"} --><h2 class="wp-block-heading" id="x">Text</h2><!-- /wp:heading -->
<!-- wp:rank-math/toc-block {"title":"Table of Contents","headings":[{"key":"toc-1","content":"Text","level":2,"link":"#x","disable":false}]} --><div class="wp-block-rank-math-toc-block" id="rank-math-toc"><h2>Table of Contents</h2><nav><ul><li><a href="#x">Text</a></li></ul></nav></div><!-- /wp:rank-math/toc-block -->
```

## How to apply
1. `PUT /wp/v2/posts/<id>` (or `/wp/v2/pattern/<id>`) with `{"content": "..."}`.
2. WP-CLI, one call each: `post meta update <id> rank_math_title '...' --force`, then `rank_math_description`, then `rank_math_focus_keyword 'primary,secondary'`.
3. Small edits: `POST /wpvibe/v1/content/edit`; verify with `/wpvibe/v1/content/search`.
4. Verify live with `get_page_html` (add `?cb=N`).
5. Hostinger returns 429 on bursts: one write at a time, wait 60-90 s on a 429.

## Rules
Never invent hook sizes, times, designers or stats. Do not call AI or stock images the finished toy. A high Rank Math score is a checklist, not a ranking guarantee.
