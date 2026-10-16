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
