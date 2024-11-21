import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

def rgb_to_pca_components(image):
    height, width, channels = image.shape
    x = image.reshape(-1, channels)
    x_mean = np.mean(x, axis=0)
    
    W = x - x_mean
    C = np.cov(W.T)
    lmbd, e = np.linalg.eigh(C)
    Ep = e[:, np.argsort(lmbd)[::-1]]
    E = W @ Ep
    ki = (E @ Ep.T) + x_mean

    return ki.reshape(height, width, channels).transpose(2, 0, 1)
    
image = cv2.imread('cv09/Cv09_obr.bmp')
if image is None:
    print("Error: Nelze načíst obrázek")
    sys.exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

components = rgb_to_pca_components(image_rgb)

standard_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure()

plt.subplot(221)
plt.imshow(standard_gray, cmap='gray')
plt.title('gray')
plt.axis('off')

plt.subplot(222)
plt.imshow(components[0], cmap='gray')
plt.title("k1")
plt.axis('off')

plt.subplot(223)
plt.imshow(components[1], cmap='gray')
plt.title("k2")
plt.axis('off')

plt.subplot(224)
plt.imshow(components[2], cmap='gray')
plt.title("k3")
plt.axis('off')

plt.tight_layout()
plt.show()