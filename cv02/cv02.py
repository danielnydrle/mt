import struct
import numpy as np
import matplotlib.pyplot as plt


FILES = [
    "cv02/cv02_wav_01.wav",
    "cv02/cv02_wav_02.wav",
    "cv02/cv02_wav_03.wav",
    "cv02/cv02_wav_04.wav",
    "cv02/cv02_wav_05.wav",
    "cv02/cv02_wav_06.wav",
    "cv02/cv02_wav_07.wav"
]

def read_wav(file):
    print(f"Reading file: {file}")
    with open(file, "rb") as f:
        head = f.read(44)
        print(head)
        if head[:4] != b"RIFF" or head[8:12] != b"WAVE":
            return "Nekompletní soubor"
        a1 = struct.unpack("i", head[4:8])[0]
        wave = struct.unpack("i", head[12:16])[0]
        fmt = struct.unpack("i", head[16:20])[0]
        af = struct.unpack("i", head[20:24])[0]
        k = struct.unpack("h", head[22:24])[0]
        c = struct.unpack("h", head[24:26])[0]
        vf = struct.unpack("i", head[24:28])[0]
        pb = struct.unpack("i", head[28:32])[0]
        vb = struct.unpack("h", head[32:34])[0]
        vv = struct.unpack("h", head[34:36])[0]
        data = head[36:40]
        a2 = struct.unpack("i", head[40:44])[0]

        print(f"a1: {a1}, wave: {wave}, fmt: {fmt}, af: {af}, k: {k}, c: {c}, vf: {vf}, pb: {pb}, vb: {vb}, vv: {vv}, data: {data}, a2: {a2}")

        raw_data = f.read(a2)
        print(f"Raw data length: {len(raw_data)}")

        if len(raw_data) != a2:
            print(f"Error: Data chunk size mismatch for {file}")
            return

        # Determine format for unpacking based on bit depth
        num_samples = a2 // (k * vv // 8)
        fmt = f"<{num_samples * k}h" if vv == 16 else f"<{num_samples * k}B"
        
        try:
            data = struct.unpack(fmt, raw_data)
        except struct.error as e:
            print(f"Error unpacking data for {file}: {e}")
            return

        # Reshape the data into channels
        channels = np.reshape(data, (num_samples, k)).T  # Transpose for channel separation

        # Time axis
        time = np.linspace(0, num_samples / vf, num=num_samples)

        # Plot each channel
        fig, axes = plt.subplots(k, 1, figsize=(10, 6), sharex=True)
        if k == 1:
            axes = [axes]  # Ensure axes is iterable for single channel
        
        for i, channel in enumerate(channels):
            axes[i].plot(time, channel, label=f"Channel {i + 1}")
            axes[i].set_title(f"Kanál {i + 1}")
            axes[i].set_xlabel('Čas [s]')
            axes[i].set_ylabel('Amplituda')
            axes[i].legend(loc="upper right")

        plt.tight_layout()
        plt.suptitle(f"Signal from {file}", y=1.02)
        plt.show()
   
for file in FILES:
    read_wav(file)
