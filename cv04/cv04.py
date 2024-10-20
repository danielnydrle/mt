from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import numpy as np
import cv2

# 1

img1 = imread("cv04/Cv04_porucha1.bmp")
img2 = imread("cv04/Cv04_porucha2.bmp")
etalon1 = imread("cv04/Cv04_porucha1_etalon.bmp")
etalon2 = imread("cv04/Cv04_porucha2_etalon.bmp")

img1_corrected = img1/etalon1
img2_corrected = img2/etalon2


plt.subplot(1,3,1)
plt.imshow(img1)
plt.title("f(y,x)")
plt.subplot(1,3,2)
plt.imshow(etalon1)
plt.title("e(y,x)")
plt.subplot(1,3,3)
plt.imshow(img1_corrected)
plt.title("g(y,x)")
plt.show()

plt.subplot(1,3,1)
plt.imshow(img2)
plt.title("f(y,x)")
plt.subplot(1,3,2)
plt.imshow(etalon2)
plt.title("e(y,x)")
plt.subplot(1,3,3)
plt.imshow(img2_corrected)
plt.title("g(y,x)")
plt.show()

# 2

img = imread("cv04/Cv04_rentgen.bmp", format="gray")
N, M = img.shape[0], img.shape[1]

img_corrected = np.zeros_like(img)

for channel in range(img.shape[2]):
    im_channel = img[:,:,channel]
    hist, bins = np.histogram(im_channel.flatten(), 256, [0, 256])
    P = hist/(N*M)
    cdf = np.cumsum(P)
    equalised_channel = np.floor(cdf[im_channel] * 255).astype(np.uint8)
    img_corrected[:,:,channel] = equalised_channel


plt.subplot(2,2,1)
plt.imshow(img, cmap="gray")
plt.title("f(y,x)")
plt.subplot(2,2,2)
plt.hist(img.flatten(), 256, [0, 256], color = 'r')
plt.title("Hf(y,x)")
plt.subplot(2,2,3)
plt.imshow(img_corrected, cmap="gray")
plt.title("g(y,x)")
plt.subplot(2,2,4)
plt.hist(img_corrected.flatten(), 256, [0, 256], color = 'r')
plt.title("Hg(y,x)")
plt.show()
