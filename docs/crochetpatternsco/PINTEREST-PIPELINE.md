# Pinterest pipeline for crochetpatternsco.com (approved 2026-10-16)

Decisions: real photos plus AI pictures allowed; posting with the Pinterest scheduler and bulk upload (free, Metricool for stats only); design in Canva.
Guardrails: pin text must be true (no "step by step with photos" unless the PDF has them); an AI picture never stands in for the finished toy of a pattern; alt text on every pin.

## Specs (check Pinterest help before large batches)
Pin image 2:3, 1000 x 1500 px. Title up to 100 characters (first ~40 show). Description about 500 characters. About 1 to 5 fresh pins a day; avoid near-duplicate pins; save a pin to at most about 10 relevant boards. Pinterest labels detected AI images.

## Steps per pattern
1. Owner sends PDF and real photos (angles, close-up, size shot, one vertical), hook, yarn, size.
2. Canva: redesigned PDF with photos -> compress -> upload to Cloudflare R2 -> update pattern page fields (PDF link, pages, file size).
3. Canva: master thumbnail -> 5 pins (hero, free PDF, facts, gift or season angle, collage) -> export PNG 1000 x 1500, plus 1200 x 630 and square card.
4. Pin text per pin (title, description, alt text, board, link) in `pins/pins-<pattern>.csv`.
5. Owner uploads pins (scheduler or bulk upload), a few per day.
6. Weekly: owner sends Pinterest Analytics CSV; keep winners, retire weak layouts.

## Boards (keyword names)
Free Crochet Patterns; Amigurumi and Toys; Baby and Kids Crochet; Crochet for Beginners; Crochet Blankets and Home; Crochet Hats and Accessories; Crochet Clothing; Granny Squares and Flowers; Crochet Christmas and Seasonal; Crochet Tips, Charts and Guides.

## Pilot: baby bunny (post 41)
Canva assets: bunny photo wood table `MAHYMXwOtLA`, bunny photo white fabric `MAHYMVdTv_0`. Four candidates were generated per pin; the owner picks in Canva. Pin text: `pins/pins-bunny.csv`.

## Order of work for every new pattern (updated 2026-10-16)
1. Owner sends the pattern PDF and real photos.
2. I read the PDF and write the full pattern post as a draft (written pattern, materials, FAQ, schema fields, Rank Math title, description, focus keywords, TOC, links; recipe in `RANKMATH-90-RECIPE.md`).
3. Redesigned PDF and thumbnail (Canva), upload PDF to R2, set the download link.
4. Five pins from the thumbnail (Canva), exported 1000 x 1500, uploaded to the media library; pin text from `pins/pins-<pattern>.csv`.
5. Publish the post, then the owner posts the pins (a few per day).
Bunny (41) and koala (42) already have their posts; the pins and redesigned PDFs are the new part.

## Connection test, 2026-10-16
| Link | Result |
|---|---|
| WPVibe to site (read) | works, administrator; publishing and uploads tested separately |
| WPVibe upload from a Canva export URL | works: attachment 68, 1000 x 1500 PNG |
| Canva: upload photo, generate pins, save design, read, export PNG | works; pin size is 1000 x 1500 |
| Cloudflare R2 | bucket `crochet-patterns` found; the connector cannot upload files, so the PDF upload stays a manual step in the Cloudflare dashboard |
| Google Drive | works (read) |
| GitHub repo push | works |
| Metricool | account connected but no social network is connected (Pinterest is not linked) |
| Magnific, Higgsfield | balance checks were declined by the owner, not tested |
| Adobe tools | not tested yet |
| This environment viewing Canva previews | blocked by the network proxy, so the owner approves designs visually in Canva |
Finding: the pin generator dropped the subtitle ("Baby amigurumi bunny, 18 cm tall") and the "Free PDF" chip on pin 1 (design text read only: "Free Crochet Bunny Pattern", "Beginner", "crochetpatternsco.com"). Fix by editing the design, or choose another candidate.
