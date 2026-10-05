import math, random, struct, wave, sys
SR = 44100
T_TITLE, N = 6.0, 6
DURS = [5.7, 6.4, 7.2, 5.9, 8.1, 10.3]
STARTS = [T_TITLE + sum(DURS[:i]) for i in range(N)]
T_OUT = T_TITLE + sum(DURS)
END = T_OUT + 4.6
L = [0.0] * int(END * SR)
R = [0.0] * int(END * SR)
random.seed(5)

def add(t0, samples, gain=1.0, pan=0.0):
    i0 = int(t0 * SR)
    gl = gain * (1 - max(0, pan)); gr = gain * (1 + min(0, pan))
    for k, v in enumerate(samples):
        i = i0 + k
        if 0 <= i < len(L):
            L[i] += v * gl; R[i] += v * gr

def env(n, a, d):  # attack/decay exponential
    return [min(1, k / (a * SR + 1)) * math.exp(-k / (d * SR)) for k in range(n)]

def tone(freq, dur, a=0.005, d=0.3, harm=(1.0, 0.4, 0.2), gain=1.0):
    n = int(dur * SR); e = env(n, a, d)
    return [gain * e[k] * sum(h * math.sin(2 * math.pi * freq * (j + 1) * k / SR) for j, h in enumerate(harm)) for k in range(n)]

def noise_sweep(dur, f0, f1, q=0.08, gain=1.0, shape="bell"):
    n = int(dur * SR); lp = bp = 0.0; out = []
    for k in range(n):
        x = k / n
        f = f0 + (f1 - f0) * x
        c = 2 * math.sin(math.pi * f / SR)
        w = random.uniform(-1, 1)
        hp = w - lp - q * 10 * bp
        bp += c * hp; lp += c * bp
        e = math.sin(math.pi * x) ** 2 if shape == "bell" else (1 - x) ** 2
        out.append(bp * e * gain)
    return out

def thump(dur=0.35, f0=140, f1=48, gain=1.0):
    n = int(dur * SR); ph = 0.0; out = []
    for k in range(n):
        x = k / n; f = f0 * (f1 / f0) ** x; ph += 2 * math.pi * f / SR
        out.append(math.sin(ph) * math.exp(-x * 6) * gain)
    return out

def click(gain=0.3):
    n = int(0.012 * SR)
    return [random.uniform(-1, 1) * math.exp(-k / (0.002 * SR)) * gain for k in range(n)]

def bell(freq, dur=1.6, gain=0.5):
    n = int(dur * SR); out = []
    for k in range(n):
        t = k / SR
        v = sum(a * math.sin(2 * math.pi * freq * m * t) * math.exp(-t * dcy) for m, a, dcy in ((1, 1, 2.2), (2.76, .5, 3.4), (5.4, .25, 5), (8.9, .12, 7)))
        out.append(v * gain)
    return out

def ease(x): x = min(1, max(0, x)); return x * x * (3 - 2 * x)

# ---------- music bed: D hijaz (D Eb F# G A Bb C), 96 bpm ----------
bpm = 96; beat = 60 / bpm
scale = [293.66, 311.13, 369.99, 392.0, 440.0, 466.16, 523.25, 587.33]
pattern = [0, 2, 3, 2, 4, 3, 2, 1, 0, 2, 3, 5, 4, 3, 2, 3]
t = 0.0; step = 0
while t < END - 0.5:
    idx = pattern[step % len(pattern)]
    f = scale[idx] * (0.5 if step % 8 < 4 else 1.0)
    pan = ((step % 4) - 1.5) * 0.12
    add(t, tone(f, 0.55, a=0.004, d=0.28, harm=(1, .35, .15)), 0.05, pan)
    if step % 2 == 0:
        add(t, thump(0.22, 110, 60, 0.35), 0.10)      # soft frame-drum on the beat
    else:
        add(t, click(1.0), 0.05)
    t += beat / 2; step += 1
# drone pad
for t0 in range(0, int(END), 4):
    for f, g in ((73.42, .05), (110.0, .035), (146.83, .02)):
        n = int(4.4 * SR)
        add(t0, [g * math.sin(2 * math.pi * f * k / SR) * min(1, k / (1.2 * SR)) * max(0, 1 - max(0, (k / SR - 3.2)) / 1.2) for k in range(n)], 1.0)

# ---------- title ----------
add(0.55, noise_sweep(1.2, 500, 3000, gain=1.2), 0.20)
add(1.55, noise_sweep(0.7, 900, 5200, gain=1.0), 0.14)
add(1.5, thump(0.4, 180, 55, 1.0), 0.28)

# ---------- wipes + scenes ----------
for i, tb in enumerate(STARTS + [T_OUT]):
    add(tb - 0.5, noise_sweep(1.0, 3800, 380, gain=1.6), 0.40, 0.0)      # whoosh
    add(tb - 0.04, thump(0.45, 130, 40, 1.0), 0.30)                       # impact under the cover
for i in range(N):
    s0 = STARTS[i]; e0 = 0.12
    add(s0 + e0 + 0.02, thump(0.3, 220, 70, 1.0), 0.20)                   # circle pop
    add(s0 + e0 + 0.22, noise_sweep(0.5, 600, 2400, gain=1.0), 0.12)      # image rises
    add(s0 + e0 + 0.45, tone(880 * 1.0, .18, a=.002, d=.06, harm=(1, .3)), 0.07)   # cloud ping
    add(s0 + e0 + 0.55, noise_sweep(0.5, 2500, 800, gain=1.0), 0.12)      # flag whip
    add(s0 + e0 + 0.72, thump(0.25, 160, 80, 1.0), 0.20)                  # label slap
    add(s0 + e0 + 0.72, noise_sweep(0.35, 4000, 1500, gain=1.0, shape="x"), 0.12)  # paper
    # count ticks
    t_ = s0 + e0 + 1.0; k = 0
    while t_ < s0 + e0 + 2.5:
        x = (t_ - (s0 + e0 + 1.0)) / 1.5
        add(t_, tone(1200 + 900 * x, 0.03, a=.0005, d=.01, harm=(1,)), 0.07 + 0.05 * x)
        t_ += 0.05 + 0.07 * ease(x) ; k += 1
    add(s0 + e0 + 2.5, bell(1318.5 if i % 2 == 0 else 1174.7, 1.4, 0.55), 0.16)   # ding at final number
    add(s0 + e0 + 2.45, thump(0.3, 150, 60, 1.0), 0.18)
    add(s0 + e0 + 2.4, noise_sweep(0.4, 1000, 3500, gain=1.0), 0.10)               # unit text

# ---------- outro ----------
add(T_OUT + 0.15, noise_sweep(0.9, 500, 3000, gain=1.2), 0.2)
add(T_OUT + 0.2, thump(0.4, 170, 50, 1.0), 0.30)
for j, f in enumerate((587.33, 739.99, 880.0, 1174.66)):
    add(T_OUT + 0.9 + j * 0.12, bell(f, 2.2, 0.5), 0.12)
add(T_OUT + 1.2, click(1.0), 0.12)

# ---------- master: fade out, normalise, write ----------
fade = 1.8
for i in range(len(L)):
    tt = i / SR
    g = 1.0
    if tt < 0.05: g = tt / 0.05
    if tt > END - fade: g = max(0, (END - tt) / fade)
    L[i] *= g; R[i] *= g
peak = max(max(abs(v) for v in L), max(abs(v) for v in R)) or 1
sc = 0.89 / peak
w = wave.open("sfx.wav", "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes(b"".join(struct.pack("<hh", int(max(-1, min(1, a * sc)) * 32767), int(max(-1, min(1, b * sc)) * 32767)) for a, b in zip(L, R)))
w.close()
print("ok", END)
