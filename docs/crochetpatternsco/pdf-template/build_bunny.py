import re, html
qr=open('qr.svg').read()
def rows(block):
    out=[]
    for ln in block.strip().split('\n'):
        ln=ln.strip()
        if not ln: continue
        m=re.match(r'^(\d+(?:[–-]\d+)?)\)\s*(.*?)(?:\s*\((\d+)\))?$',ln)
        if m: out.append(('r',m.group(1).replace('-','–'),m.group(2),m.group(3) or ''))
        else: out.append(('n',ln))
    return out
def table(block):
    h='<table class="rounds"><thead><tr><th>Round</th><th>Instructions</th><th>Stitches</th></tr></thead><tbody>'
    for r in rows(block):
        if r[0]=='r': h+=f'<tr><td class="rn">{r[1]}</td><td>{html.escape(r[2])}</td><td class="st">{r[3]}</td></tr>'
        else: h+=f'<tr class="note"><td colspan="3">{html.escape(r[1])}</td></tr>'
    return h+'</tbody></table>'
arms=table("""1) 8 sc in MR (8)
2–12) 8 sc (8)
Fold the arm in half and crochet 4 sc through both layers to close the opening.""")
ears=table("""1) 6 sc in MR (6)
2) inc × 6 (12)
3) (1 sc, inc) × 6 (18)
4–11) 18 sc (18)
12) (1 sc, dec) × 6 (12)
13–16) 12 sc (12)
Fold the ear in half and crochet 6 sc through both layers to close the opening.""")
head=table("""1) 6 sc in MR (6)
2) inc × 6 (12)
3) (1 sc, inc) × 6 (18)
4) (2 sc, inc) × 6 (24)
5) (3 sc, inc) × 6 (30)
6) (4 sc, inc) × 6 (36)
7) (5 sc, inc) × 6 (42)
8) (6 sc, inc) × 6 (48)
9–18) 48 sc (48)
19) (6 sc, dec) × 6 (42)
20) (5 sc, dec) × 6 (36)
21) (4 sc, dec) × 6 (30)
Stuff the head lightly.
22) (1 sc, dec) × 10 (20)
23) work 2 decreases on the sides (18)
Stuff the head firmly. Embroider the eyes (on the 7th round from the bottom) and the nose.""")
legs=table("""1) 6 sc in MR (6)
2) inc × 6 (12)
3–9) 12 sc (12)
Stuff lightly. Fold in half and crochet 6 sc through both layers to close the opening.
Fasten off the first leg. Do not fasten off the second leg: chain 3 and continue with the body.""")
body=table("""1) 12 sc around the first leg, 3 sc along the chain, 12 sc around the second leg, 3 sc along the chain (30)
2–10) 30 sc (30)
11) 2 decreases on the sides (28)
12) 2 decreases on the sides (26)
13) 2 decreases on the sides (24)
14) 2 decreases on the sides (22)
15) 2 decreases on the sides (20)
16) crochet the arms into this round (20)
17) 2 decreases on the sides (18)
Stuff the body. Sew the head to the body and sew the ears to the top of the head.""")
collar=table("""Chain 24.
1) Starting in the 2nd chain from the hook, 23 sc (23)
2) Ruffle edge: (dc, ch 2, dc, ch 2, dc) all in the same stitch, skip 1 stitch, sl st in the next stitch. Repeat to the end of the row.
Sew the collar around the bunny's neck.""")
css="""
@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:'Inter',sans-serif;color:#2B2320;font-size:10.5pt;line-height:1.45}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.page:last-child{page-break-after:auto}
.cover{background:#FFF7E0;padding:16mm 16mm 12mm}
.brand{display:flex;justify-content:space-between;align-items:center;font-weight:600;color:#4C5B2A;font-size:10pt;letter-spacing:.02em}
.brand b{background:#F2C94C;color:#2B2320;padding:3px 10px;border-radius:99px;font-size:9pt}
h1.title{font-size:46pt;line-height:1.02;margin:12mm 0 2mm;color:#4C5B2A;letter-spacing:-.02em;font-weight:800}
.sub{font-size:15pt;color:#8C5B3E;font-weight:600;margin:0 0 8mm}
.hero{width:100%;height:160mm;object-fit:cover;border-radius:8mm;display:block;box-shadow:0 4mm 10mm rgba(76,91,42,.18)}
.chips{display:flex;gap:3mm;flex-wrap:wrap;margin:8mm 0 0}
.chip{background:#fff;border:1.5px solid #F2C94C;color:#4C5B2A;padding:2.5mm 5mm;border-radius:99px;font-weight:700;font-size:10.5pt}
.cover .foot{position:absolute;left:16mm;right:16mm;bottom:12mm;display:flex;justify-content:space-between;align-items:center;color:#4C5B2A;font-size:10pt}
.cover .free{font-size:13pt;font-weight:800}
.inner{padding:16mm 16mm 20mm}
.runhead{position:absolute;left:16mm;right:16mm;top:8mm;display:flex;justify-content:space-between;font-size:8.5pt;color:#8C5B3E;border-bottom:1px solid #F2C94C;padding-bottom:2mm}
.pgfoot{position:absolute;left:16mm;right:16mm;bottom:8mm;display:flex;justify-content:space-between;font-size:8.5pt;color:#8C5B3E}
h2{font-size:17pt;color:#4C5B2A;margin:7mm 0 3mm;font-weight:800;display:flex;align-items:baseline;gap:3mm}
h2 small{font-size:10pt;color:#8C5B3E;font-weight:600}
.inner h2:first-of-type{margin-top:6mm}
ul.checks{list-style:none;padding:0;margin:0}
ul.checks li{padding:2mm 0 2mm 9mm;position:relative;border-bottom:1px dotted #e4d9c4}
ul.checks li:before{content:'';position:absolute;left:0;top:3.2mm;width:4.5mm;height:4.5mm;border:1.5px solid #4C5B2A;border-radius:1.2mm}
.glance{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin:4mm 0}
.glance div{background:#FFF7E0;border-radius:3mm;padding:3mm 4mm}
.glance span{display:block;font-size:8pt;color:#8C5B3E;text-transform:uppercase;letter-spacing:.06em;font-weight:700}
.glance b{font-size:12pt;color:#4C5B2A}
table.abbr{width:100%;border-collapse:collapse}
table.abbr td{padding:1.6mm 2mm;border-bottom:1px solid #eee3cf}
table.abbr td:first-child{font-weight:800;color:#4C5B2A;width:28mm}
.photos{display:flex;gap:5mm;margin-top:6mm}
.photos img{height:84mm;width:auto;border-radius:4mm;flex:1;object-fit:cover;min-width:0}
.photos img{width:calc(50% - 2.5mm)}
table.rounds{width:100%;border-collapse:collapse;margin-bottom:2mm}
table.rounds th{text-align:left;font-size:8pt;text-transform:uppercase;letter-spacing:.06em;color:#8C5B3E;padding:1.5mm 2mm;border-bottom:2px solid #F2C94C}
table.rounds td{padding:1.5mm 2mm;border-bottom:1px solid #eee3cf;vertical-align:top}
table.rounds td.rn{width:20mm;font-weight:800;color:#4C5B2A;white-space:nowrap}
table.rounds td.st{width:20mm;text-align:right;font-weight:700;color:#8C5B3E}
table.rounds th:last-child{text-align:right}
table.rounds tr.note td{background:#FFF7E0;font-style:italic;color:#5b4a3b;border-bottom:none;padding:2mm 3mm;border-radius:2mm}
.callout{background:#FFF7E0;border-left:1.5mm solid #F2C94C;padding:3mm 4mm;border-radius:2mm;margin:3mm 0}
.back{background:#FFF7E0;text-align:center;padding:20mm 16mm}
.back img.ph{height:120mm;border-radius:8mm;box-shadow:0 4mm 10mm rgba(76,91,42,.18)}
.back h3{font-size:22pt;color:#4C5B2A;margin:8mm 0 2mm}
.back p{margin:1mm 0;color:#5b4a3b}
.qrrow{display:flex;gap:6mm;align-items:center;justify-content:center;margin-top:8mm;text-align:left}
.qrrow svg{width:30mm;height:30mm;background:#fff;padding:2mm;border-radius:3mm}
.qrrow div{max-width:80mm;font-size:10pt}
.qrrow b{color:#4C5B2A}
"""
def run(n,title): 
    return f'<div class="runhead"><span>crochetpatternsco.com</span><span>{title}</span></div><div class="pgfoot"><span>Baby Bunny Amigurumi Crochet Pattern</span><span>{n}</span></div>'
H=f"""<!doctype html><html><head><meta charset="utf-8"><title>Baby Bunny Amigurumi Crochet Pattern</title><style>{css}</style></head><body>
<section class="page cover">
 <div class="brand"><span>crochetpatternsco.com</span><b>FREE PDF PATTERN</b></div>
 <h1 class="title">Baby Bunny</h1>
 <p class="sub">Amigurumi crochet pattern</p>
 <img class="hero" src="hero.jpg" alt="Six crocheted baby bunnies">
 <div class="chips"><span class="chip">Beginner</span><span class="chip">2 mm hook</span><span class="chip">About 18 cm (7 in) tall</span><span class="chip">US terms</span></div>
 <div class="foot"><span class="free">Free pattern by Crochet Patterns Co</span><span>6 pages</span></div>
</section>
<section class="page inner">{run(2,'Materials and abbreviations')}
 <h2>What you need</h2>
 <ul class="checks">
  <li><b>Semi-cotton yarn</b> such as YarnArt Jeans: one main colour for the body and a contrast colour for the collar</li>
  <li><b>Crochet hook</b> 2 mm</li>
  <li><b>Black and brown cotton thread</b> for embroidering the eyes and nose</li>
  <li>Tapestry needle with a large eye</li>
  <li>Scissors</li>
  <li>Polyester fiberfill stuffing</li>
 </ul>
 <div class="glance"><div><span>Level</span><b>Beginner</b></div><div><span>Hook</span><b>2 mm</b></div><div><span>Size</span><b>18 cm / 7 in</b></div><div><span>Terms</span><b>US</b></div></div>
 <h2>Abbreviations</h2>
 <table class="abbr">
  <tr><td>ch</td><td>chain</td></tr><tr><td>sc</td><td>single crochet</td></tr><tr><td>dc</td><td>double crochet</td></tr>
  <tr><td>inc</td><td>increase: work 2 sc in the same stitch</td></tr><tr><td>dec</td><td>decrease</td></tr>
  <tr><td>sl st</td><td>slip stitch</td></tr><tr><td>MR</td><td>magic ring</td></tr><tr><td>(…) × N</td><td>repeat the instructions in brackets N times</td></tr>
 </table>
 <h2>Before you start</h2>
 <div class="callout">The number in <b>(parentheses)</b> is the total stitch count you should have when the round is complete. The toy is worked in <b>continuous rounds (spiral)</b>: do not join the rounds and do not work turning chains. Mark the beginning of each round with a stitch marker or a short piece of contrasting thread.</div>

 
</section>
<section class="page inner">{run(3,'Pattern: arms, ears, legs')}

 <h2>Arms <small>make 2</small></h2>{arms}
 <h2>Ears <small>make 2</small></h2>{ears}
 <h2>Legs <small>make 2</small></h2>{legs}
</section>
<section class="page inner">{run(4,'Pattern: head')}
 <h2>Head</h2>{head}
 <div class="photos"><img src="dup1.jpg" alt="Crocheted baby bunny"><img src="dup2.jpg" alt="Crocheted baby bunnies"></div>
</section>
<section class="page inner">{run(5,'Pattern: body and collar')}
 <h2>Body</h2>{body}
 <h2>Collar</h2>{collar}
 <h2>Finishing checklist</h2>
 <ul class="checks"><li>Stuff the head firmly and the body, and embroider the eyes (7th round from the bottom of the head) and the nose</li><li>Sew the head to the body</li><li>Sew the ears to the top of the head</li><li>Crochet the arms into round 16 of the body</li><li>Sew the collar around the neck and weave in all ends</li></ul>
</section>
<section class="page back">
 <img class="ph" src="back.jpg" alt="Finished crocheted baby bunny">
 <h3>Your baby bunny is ready!</h3>
 <p>Happy crocheting. Wishing you cute toys and even stitches.</p>
 <div class="qrrow">{qr}<div><b>Pattern prepared by Crochet Patterns Co</b><br>Scan for the pattern page and more free crochet patterns at crochetpatternsco.com<br><small>For personal use. Please credit crochetpatternsco.com when you share a finished piece.</small></div></div>
</section>
</body></html>"""
open('bunny.html','w').write(H); print('ok',len(H))
