# Maddar AI carousel: rebuilt with Stitch

These files rebuild slides 01–08 of the Maddar AI carousel ("بتستخدم الـAI... ولا بتطلب منه يكتب بوست وخلاص؟") from scratch with the Stitch MCP.

- Stitch project: `projects/8647666054446967972`
- Design system: `assets/6891842228623932837` ("Maddar AI Carousel"; primary `#1FC28C`, light mode, Rubik/Inter, ROUND_EIGHT, plus `DESIGN.md`)

| Slide | Prompt | Stitch screen ID |
|---|---|---|
| 01 — Cover / hook | `slide-01.prompt.md` | `e1189ef8a5cd4c419f6e8793bcb2ee34` |
| 02 — ١. افهم عميلك الأول | `slide-02.prompt.md` | `18294a7592b34d869afd69ee1a1514de` |
| 03 — ٢. بدل «هات أفكار» | `slide-03.prompt.md` | `5d336a532fb7493c81eebe1d6dc6250e` |
| 04 — ٣. فكرة واحدة، ٥ أشكال | `slide-04.prompt.md` | `8b7c1b656bc548cfbeec8b1ed6202fcb` |
| 05 — ٤. خليه ناقد، مش كاتب | `slide-05.prompt.md` | `4901e78f5c3d4a67a0a9fd161f1d6d67` |
| 06 — ٥. افهم أرقامك | `slide-06.prompt.md` | `2f1dbd92f7634fc390f77e9bb4dc8deb` |
| 07 — الخلاصة (recap) | `slide-07.prompt.md` | `31d2c9ad48d74ebba813ada95df358e8` |
| 08 — CTA | `slide-08.prompt.md` | `1dcbd230c1dd40c3997952b11711e1b7` |

Slides 01–03 are rebuilt from the original designs. The copy for slides 04–08 is a new draft written in the same voice; review it before publishing.

## Reproduce

Each slide was generated with `generate_screen_from_text`:

```json
{ "projectId": "8647666054446967972",
  "designSystem": "assets/6891842228623932837",
  "deviceType": "AGNOSTIC",
  "prompt": "<contents of slide-0N.prompt.md>" }
```
