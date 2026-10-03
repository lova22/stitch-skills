# Maddar AI carousel: rebuilt with Stitch

These files rebuild slides 01–03 of the Maddar AI carousel ("بتستخدم الـAI... ولا بتطلب منه يكتب بوست وخلاص؟") from scratch with the Stitch MCP.

- Stitch project: `projects/8647666054446967972`
- Design system: `assets/6891842228623932837` ("Maddar AI Carousel"; primary `#1FC28C`, light mode, Rubik/Inter, ROUND_EIGHT, plus `DESIGN.md`)

| Slide | Prompt | Stitch screen ID |
|---|---|---|
| 01 — Cover / hook | `slide-01.prompt.md` | `e1189ef8a5cd4c419f6e8793bcb2ee34` |
| 02 — ١. افهم عميلك الأول | `slide-02.prompt.md` | `18294a7592b34d869afd69ee1a1514de` |
| 03 — ٢. بدل «هات أفكار» | `slide-03.prompt.md` | `5d336a532fb7493c81eebe1d6dc6250e` |

## Reproduce

Each slide was generated with `generate_screen_from_text`:

```json
{ "projectId": "8647666054446967972",
  "designSystem": "assets/6891842228623932837",
  "deviceType": "AGNOSTIC",
  "prompt": "<contents of slide-0N.prompt.md>" }
```

Follow the same prompt pattern for slides 04–08: change the page counter and the number of active progress dashes.
