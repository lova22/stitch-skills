const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 const p=await b.newPage(); await p.goto('file://'+process.cwd()+'/bunny.html'); await p.waitForTimeout(500);
 await p.pdf({path:'bunny-redesign.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});
 await b.close();
})();
