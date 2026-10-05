const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async()=>{
  const [a,b]=[+process.argv[2],+process.argv[3]], FPS=30;
  const br=await chromium.launch();
  const p=await br.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+process.cwd()+'/video2.html'); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(600);
  // warm-up so every scene's images are decoded before the first captured frame
  const warm=await p.evaluate(()=>STARTS.map(s=>s+2.6).concat([T_OUT+1]));
  for(const t of warm){await p.evaluate(t=>renderFrame(t),t);await p.waitForTimeout(250);}
  for(let f=a;f<b;f++){
    await p.evaluate(t=>renderFrame(t),f/FPS);
    await p.screenshot({path:`frames/f_${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});
  }
  await br.close();
})();
