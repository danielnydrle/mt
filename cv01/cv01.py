import struct
import numpy as np
import matplotlib.pyplot as plt

with open("cv01/cv01_dobryden.wav", "rb") as a:
    riff = a.read(4)
    print(f"Riff: {riff}")

    a1 = struct.unpack("i", a.read(4))[0]
    print(f"B do konce souboru: {a1}") # počet bytů do konce souboru

    wave = struct.unpack("i", a.read(4))[0]
    print(f"Wave: {wave}")

    fmt = struct.unpack("i", a.read(4))[0]
    print(f"FMT: {fmt}")

    af = struct.unpack("i", a.read(4))[0]
    print(f"AF: {af}") # počet bytů do konce části FMT

    k = struct.unpack("h", a.read(2))[0]
    print(f"K: {k}")  # kompresní kód, zde 1 = PCM

    c = struct.unpack("h", a.read(2))[0]
    print(f"Počet kanálů: {c}") # počet kanálů

    vf = struct.unpack("i", a.read(4))[0]
    print(f"Vz. frekvence: {vf}") # vzorkovací frekvence

    pb = struct.unpack("i", a.read(4))[0]
    print(f"Byte rate: {pb}") # počet bytů za sekundu

    vb = struct.unpack("h", a.read(2))[0]
    print(f"B na blok vzorků: {vb}") # počet bytů na vzorek

    vv = struct.unpack("h", a.read(2))[0]
    print(f"b na vzorek: {vv}") # počet bitů na vzorek

    data = a.read(4)
    print(f"Data: {data}") # data

    a2 = struct.unpack("i", a.read(4))[0]
    print(f"B do konce souboru: {a2}")

    sig = np.zeros(a2)
    for i in range(0, a2):
        sig[i] = struct.unpack("B", a.read(1))[0]

t = np.arange(a2).astype(float) / vf

plt.plot(t, sig)
plt.xlabel('t [s]')
plt.ylabel('A')
plt.show()