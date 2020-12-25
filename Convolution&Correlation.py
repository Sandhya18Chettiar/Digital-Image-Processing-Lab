# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:57:49 2020

@author: sandhya chettiar
"""


# Convolution & Correlation

from numpy.core.defchararray import array
from skimage import data
import numpy as np
from matplotlib import pyplot as plt


# Read the image
img = data.text()
plt.gray()

# Obtain number of rows and columns of the image
m, n = img.shape
mask = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
mask = mask/9

# reversing the mask
temp = []
for i in mask:
    temp1 = [ele for ele in reversed(i)]
    temp.append(temp1)
temp = [ele for ele in reversed(mask)]
mask1 = np.array(temp)

# image Padding
image_padded = np.zeros((img.shape[0] + 2, img.shape[1] + 2))
image_padded[1:-1, 1:-1] = img
img = image_padded

# Correlatiom the 3X3 mask over the image
img_cor = np.zeros([m, n])
for i in range(1, m-1):
    for j in range(1, n-1):
        temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0] + img[i, j] * \
            mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2,
                                                                     0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2]

        img_cor[i, j] = temp

# Convolve the 3X3 mask over the image
img_con = np.zeros([m+2, n+2])
for i in range(1, m+1):
    for j in range(1, n+1):
        temp = img[i-1, j-1]*mask1[0, 0]+img[i-1, j]*mask1[0, 1]+img[i-1, j + 1]*mask1[0, 2]+img[i, j-1]*mask1[1, 0] + img[i, j] * \
            mask1[1, 1]+img[i, j + 1]*mask1[1, 2]+img[i + 1, j-1]*mask1[2,
                                                                        0]+img[i + 1, j]*mask1[2, 1]+img[i + 1, j + 1]*mask1[2, 2]
        img_con[i, j] = temp

img_cor = img_cor.astype(np.uint8)
img_con = img_con.astype(np.uint8)

# cropping
img_con = img_con[1:-1, 1:-1]

plt.figure(1)
plt.subplot(2, 2, 1)
plt.title("Orignal")
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.title("Correlation")
plt.imshow(img_cor)
plt.subplot(2, 2, 3)
plt.imshow(img_con)
plt.title("Convolution")