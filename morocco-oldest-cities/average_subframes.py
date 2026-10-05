import json,glob,numpy as np
from PIL import Image
from concurrent.futures import ProcessPoolExecutor
meta=[]
for m in glob.glob("sub/meta_*.json"): meta+=json.load(open(m))
meta.sort()
def work(a):
    f,k=a
    ims=[np.asarray(Image.open(f"sub/f_{f:05d}_{j}.jpg").convert("RGB"),dtype=np.float32) for j in range(k)]
    out=(sum(ims)/k).clip(0,255).astype(np.uint8)
    Image.fromarray(out).save(f"fb/f_{f:05d}.png",compress_level=1)
    return f
with ProcessPoolExecutor(4) as ex: n=len(list(ex.map(work,meta,chunksize=20)))
print(n)
