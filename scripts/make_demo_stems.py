import os, numpy as np, soundfile as sf

def sine(sr, dur, f, a):
    t = np.linspace(0, dur, int(sr*dur), endpoint=False)
    return (a*np.sin(2*np.pi*f*t)).astype(np.float32)

if __name__ == "__main__":
    sr = 16000; dur = 1.5
    outdir = "data/samples/stems"
    os.makedirs(outdir, exist_ok=True)

    s1 = sine(sr, dur, 220, 0.2)
    s2 = sine(sr, dur, 440, 0.15)
    s3 = sine(sr, dur, 880, 0.1)

    master = 0.8*s1 + 0.6*s2 + 0.4*s3

    sf.write(os.path.join(outdir, "s1.wav"), s1, sr)
    sf.write(os.path.join(outdir, "s2.wav"), s2, sr)
    sf.write(os.path.join(outdir, "s3.wav"), s3, sr)
    sf.write("data/samples/master.wav", master, sr)

    print(f"wrote demo stems + master to data/samples/")
