import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("cv08/cv08_video.mp4")
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

sub_sum = []
sum_sub = []
hist = []
dct = []

segment_boundaries = [(209, 210), (269, 270)]

ret, prev_frame = cap.read()
gray_prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

def calc_sub_sum(frame, prev_frame):
    frame = frame.astype(int)
    prev_frame = prev_frame.astype(int)
    return abs(np.sum(frame) - np.sum(prev_frame))

def calc_sum_sub(frame, prev_frame):
    frame = frame.astype(int)
    prev_frame = prev_frame.astype(int)
    return np.sum(np.abs(frame - prev_frame))

def calc_hist(frame, prev_frame):
    hist_frame = cv2.calcHist([frame], [0], None, [256], [0, 256])
    hist_prev_frame = cv2.calcHist([prev_frame], [0], None, [256], [0, 256])
    return np.sum(np.abs(hist_frame - hist_prev_frame))

def calc_dct(frame, prev_frame):
    frame = frame.astype(float)
    prev_frame = prev_frame.astype(float)
    dct_frame = np.log(np.abs(cv2.dct(frame).flatten()))
    dct_frame_features = sorted(dct_frame, reverse=True)[:5]

    dct_prev_frame = np.log(np.abs(cv2.dct(prev_frame).flatten()))
    dct_prev_frame_features = sorted(dct_prev_frame, reverse=True)[:5]

    return np.sum(np.abs(np.array(dct_frame_features) - np.array(dct_prev_frame_features)))

for i in range(1, frame_count):
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    sub_sum.append(
        calc_sub_sum(gray_frame, gray_prev_frame)
    )

    sum_sub.append(
        calc_sum_sub(gray_frame, gray_prev_frame)
    )

    hist.append(
        calc_hist(gray_frame, gray_prev_frame)
    )

    dct.append(
        calc_dct(gray_frame, gray_prev_frame)
    )

    gray_prev_frame = gray_frame

cap.release()

def plot_boundaries():
    plt.axvline(x=segment_boundaries[0][0], color="r", linestyle="--", label="Segment boundaries")
    plt.axvline(x=segment_boundaries[1][0], color="r", linestyle="--")

plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.plot(sub_sum, label="SUB SUM")
plt.title("#1 SUB SUM")
plot_boundaries()
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(sum_sub, label="SUM SUB")
plt.title("#2 SUM SUB")
plot_boundaries()
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(hist, label="HIST")
plt.title("#3 HIST")
plot_boundaries()
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(dct, label="DCT")
plt.title("#4 DCT")
plot_boundaries()
plt.legend()

plt.show()

t = [x for x in range(1, frame_count)]

cap = cv2.VideoCapture('cv08/cv08_video.mp4')
for i in range(1, frame_count):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb, aspect="auto", extent=[min(t), max(t), min(sub_sum), max(sub_sum)])
    plot_boundaries()
    plt.plot(t, sub_sum, linewidth=2, color="b")
    plt.axvline(x=i, linewidth=2, color="g")
    plt.axis([min(t), max(t), min(sub_sum), max(sub_sum)])
    plt.pause(0.001)
    plt.clf()

cap.release()
plt.close()
