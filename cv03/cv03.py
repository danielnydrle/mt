import cv2
import numpy as np
import matplotlib.pyplot as plt

# 2

def imread(filename):
    with open(filename, "rb") as f:
        data = f.read()
    image = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_UNCHANGED)
    if image is not None and len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

img = imread("cv03/cv03_objekty1.bmp")
plt.imshow(img)
plt.show()

# 3

img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv)
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(ycrcb)

# 3.1: gray
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("RGB")
plt.subplot(1,2,2)
plt.imshow(gray, cmap="gray")
plt.title("Gray")
plt.show()

# 3.2: HSV
plt.subplot(2,2,1)
plt.imshow(img)
plt.title("RGB")

plt.subplot(2,2,2)
plt.imshow(h, cmap="turbo")
plt.colorbar()
plt.title("H")

plt.subplot(2,2,3)
plt.imshow(s, cmap="turbo")
plt.colorbar()
plt.title("S")

plt.subplot(2,2,4)
plt.imshow(v, cmap="turbo")
plt.colorbar()
plt.title("V")

plt.show()

# 3.3: YCrCb
plt.subplot(2,2,1)
plt.imshow(img)
plt.title("RGB")

plt.subplot(2,2,2)
plt.imshow(y, cmap="gray")
plt.title("Y")
plt.colorbar()

plt.subplot(2,2,3)
plt.imshow(cr, cmap="turbo")
plt.title("Cr")
plt.colorbar()

plt.subplot(2,2,4)
plt.imshow(cb, cmap="turbo")
plt.title("Cb")
plt.colorbar()

plt.show()

# 4

img = imread("cv03/cv03_red_object.jpg")
img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
r = img_bgr[:,:,2] / (img_bgr.sum(axis=2) + 1e-6)
mask = r < 0.5
img[mask] = 255
plt.imshow(img)
plt.show()

