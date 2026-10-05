import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR=44100; rng=np.random.default_rng(7)
T_INTRO=6.0; DURS=[5.7,6.4,7.2,5.9,8.1,10.3]
STARTS=[T_INTRO+sum(DURS[:i]) for i in range(6)]; T_OUT=T_INTRO+sum(DURS); END=T_OUT+4.6
BOUNDS=STARTS+[T_OUT]
N=int(END*SR); L=np.zeros(N); R=np.zeros(N)
def add(t0,x,g=1.0,pan=0.0):
    i=int(t0*SR)
    if i<0: x=x[-i:]; i=0
    if i>=N: return
    x=x[:N-i]
    L[i:i+len(x)]+=x*g*(1-max(0,pan)); R[i:i+len(x)]+=x*g*(1+min(0,pan))
def tt(d): return np.arange(int(d*SR))/SR
def bp(x,lo,hi): return sosfilt(butter(2,[lo,hi],btype='band',fs=SR,output='sos'),x)
def hp(x,f): return sosfilt(butter(2,f,btype='high',fs=SR,output='sos'),x)
def lp(x,f): return sosfilt(butter(2,f,btype='low',fs=SR,output='sos'),x)
def noise(d): return rng.uniform(-1,1,int(d*SR))
def kick(g=1): t=tt(.35); f=45+120*np.exp(-t*30); ph=2*np.pi*np.cumsum(f)/SR; return np.sin(ph)*np.exp(-t*11)*g
def snare(): t=tt(.22); return (hp(noise(.22),1200)*np.exp(-t*20)*.7+np.sin(2*np.pi*190*t)*np.exp(-t*25)*.5)
def hat(op=False): d=.16 if op else .05; t=tt(d); return hp(noise(d),7500)*np.exp(-t*(18 if op else 70))*.5
def boom(): t=tt(1.8); f=38+70*np.exp(-t*6); ph=2*np.pi*np.cumsum(f)/SR; return np.sin(ph)*np.exp(-t*2.4)
def crash(d=1.6): t=tt(d); return hp(noise(d),2500)*np.exp(-t*2.6)*.6
def riser(d): 
    t=tt(d); n=noise(d); out=np.zeros_like(n); ch=40; cs=len(n)//ch
    for k in range(ch):
        f=300*(30**(k/ch)); seg=n[k*cs:(k+1)*cs]; out[k*cs:(k+1)*cs]=bp(seg,f,min(f*1.6,18000))
    return out*(t/d)**2.2
def whoosh(d,down=False):
    n=noise(d); out=np.zeros_like(n); ch=30; cs=len(n)//ch
    for k in range(ch):
        x=k/ch; f=(6000*(1-x)+300*x) if down else (400*(1-x)+6000*x); out[k*cs:(k+1)*cs]=bp(n[k*cs:(k+1)*cs],f,f*1.8)
    t=tt(d); return out*np.sin(np.pi*t/d)**1.5
def bell(f,d=1.8): t=tt(d); return sum(a*np.sin(2*np.pi*f*m*t)*np.exp(-t*dc) for m,a,dc in ((1,1,2.0),(2.76,.45,3.2),(5.4,.2,5),(8.9,.1,7)))*.5
def tick(f,d=.04): t=tt(d); return np.sin(2*np.pi*f*t)*np.exp(-t*90)
def pad(freqs,d,g=.05):
    t=tt(d); x=np.zeros_like(t)
    for f in freqs:
        for det in (-0.4,0,0.4):
            ff=f*(1+det*0.004)
            x+=sum(np.sin(2*np.pi*ff*k*t)/k for k in (1,2,3,4))
    x=lp(x,1700); env=np.minimum(1,t/0.6)*np.minimum(1,(d-t)/0.5); return x*env*g/len(freqs)
# ---------------- music bed: 100 BPM, Am F C G ----------------
bpm=100; beat=60/bpm; chords=[[110,164.8,220,261.6],[87.3,130.8,174.6,220],[130.8,196,261.6,329.6],[98,146.8,196,246.9]]
t0=0.0; bar=0
while t0<END-0.5:
    ch=chords[bar%4]
    add(t0,pad([f*2 for f in ch],4*beat+0.3,.09),1.0,0.15)
    for b in range(4):
        tb=t0+b*beat
        add(tb,kick(.55*(0.65 if t0<T_INTRO-0.5 else 1)),1)
        if b in (1,3): add(tb,snare(),.28)
        add(tb+beat/2,hat(),.16,.2); add(tb,hat(),.10,-.2)
        if b==3: add(tb+beat/2,hat(True),.14,.3)
        # bass note
        tbn=tt(beat*.9); add(tb,np.sin(2*np.pi*ch[0]/2*tbn)*np.exp(-tbn*3)*.35,1)
        # plucked arp
        for s in range(2):
            ta=tb+s*beat/2; f=ch[(b*2+s)%4]*2; tp=tt(.3); add(ta,np.sin(2*np.pi*f*tp)*np.exp(-tp*9)*.06+np.sin(2*np.pi*f*2*tp)*np.exp(-tp*14)*.03,1,(-.3 if s else .3))
    t0+=4*beat; bar+=1
# ---------------- intro ----------------
add(0.0,riser(0.7),.30); add(0.7,boom(),.95); add(0.7,crash(1.4),.5); add(1.05,boom(),.8); add(1.05,crash(1.3),.45)
for k in range(6): add(3.2+k*0.17,tick(900+k*130),.6); add(3.2+k*0.17,bell(1318*(1+k*.05),0.4),.12)
add(2.1,whoosh(.4),.35); add(5.25,riser(0.75),.45)
# ---------------- boundaries / scenes ----------------
for i,B in enumerate(BOUNDS):
    add(B-1.0,riser(.9),.35 if i else .55); add(B-0.45,whoosh(.85,False),.55); add(B-0.02,boom(),1.0); add(B,crash(1.5),.65); add(B+0.05,whoosh(.7,True),.3)
for i,B in enumerate(STARTS):
    add(B+0.45,boom(),.55); add(B+0.45,bell(784,1.2),.18); add(B+0.7,tick(1800),.5)
    n=18
    for k in range(n):
        x=k/(n-1); tk=B+1.9+ (1.5)*(1-(1-x)**2.2); add(tk,tick(700+900*x),.55)
    add(B+3.4,boom(),.8); add(B+3.4,crash(1.2),.5)
    for m,f in enumerate((1568,2093,2637,3136)): add(B+3.4+m*0.06,bell(f,1.6),.22)
    add(B+3.75,tick(2400),.4)
# ---------------- outro ----------------
add(T_OUT+0.5,boom(),1.0); add(T_OUT+0.5,crash(1.8),.55)
for m,f in enumerate((784,988,1175,1568)): add(T_OUT+0.9+m*0.1,bell(f,2.2),.3)
add(T_OUT+1.9,boom(),.7); add(T_OUT+1.95,bell(2093,2.4),.35)
for k in range(6): add(T_OUT+2.3+k*0.1,tick(1200+k*180),.5)
# fades
t=np.arange(N)/SR; g=np.minimum(1,t/0.05)*np.minimum(1,(END-t)/2.0)
L*=g;R*=g
pk=max(np.abs(L).max(),np.abs(R).max()); sc=0.9/pk
st=np.stack([L,R],1)*sc
wavfile.write("music3.wav",SR,(st*32767).astype(np.int16)); print("ok",END)
