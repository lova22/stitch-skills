const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs=require('fs');
(async()=>{
  const [a,b]=[+process.argv[2],+process.argv[3]], FPS=30, SHUT=0.5;
  const br=await chromium.launch();
  const p=await br.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+process.cwd()+'/broadcast.html'); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(2000);
  const info=await p.evaluate(()=>({B:BOUNDS,T_OUT}));
  const windows=[[0.6,1.7]];
  info.B.forEach((B,i)=>{windows.push([B-0.5,B+1.0]);if(i<6)windows.push([B+3.2,B+3.9])});
  windows.push([info.T_OUT+0.2,info.T_OUT+1.1]);
  const kOf=t=>windows.some(w=>t>=w[0]&&t<=w[1])?3:1;
  fs.mkdirSync('sub',{recursive:true});
  const meta=[];
  for(let f=a;f<b;f++){
    const t0=f/FPS, k=kOf(t0);
    for(let j=0;j<k;j++){
      const t=t0+(k===1?0:((j+0.5)/k-0.5)*SHUT/FPS);
      await p.evaluate(t=>renderFrame(t),Math.max(0,t));
      await p.screenshot({path:`sub/f_${String(f).padStart(5,'0')}_${j}.jpg`,type:'jpeg',quality:94});
    }
    meta.push([f,k]);
  }
  fs.writeFileSync(`sub/meta_${a}.json`,JSON.stringify(meta));
  await br.close();
})();
