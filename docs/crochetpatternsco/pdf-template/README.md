# PDF template (HTML to PDF)
`build_bunny.py` builds `bunny.html` (A4, site colours, Inter font, cover, materials, rounds tables, back page with QR); `pdf.js` prints it to PDF with Playwright Chromium (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`). Photos (`hero.jpg`, `dup1.jpg`, `dup2.jpg`, `back.jpg`) and `qr.svg` (reportlab QR of the pattern page) sit next to the script. Render pages with `pdftoppm -r 60 -png` and look at them before sending. For a new pattern change the text blocks in `build_bunny.py` and the photos.
Result for the bunny: 6 pages, 0.7 MB (original 4.8 MB).
