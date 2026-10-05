const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async()=>{
  const [a,b]=[+process.argv[2],+process.argv[3]], FPS=30;
  const br=await chromium.launch();
  const p=await br.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+process.cwd()+'/video.html'); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(600);
  for(let f=a;f<b;f++){
    await p.evaluate(t=>renderFrame(t),f/FPS);
    await p.screenshot({path:`frames/f_${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});
  }
  await br.close();
})();
