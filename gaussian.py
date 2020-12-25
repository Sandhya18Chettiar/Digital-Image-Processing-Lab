# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:59:17 2020

@author: sandhya chettiar
"""

from skimage import data
import numpy as np
from matplotlib import pyplot as plt

#Image reading

img = data.text()
plt.gray()


m, n = img.shape

mask = [[1,2,1],
        [2,4,2],
        [1,2,2]]
mask = np.array(mask)

mask = mask/16


img_new = np.zeros([m, n])

for i in range(1,m-1):
    for j in range(1,n-1):
        temp = img[i-1,j-1]*mask[2-0,2-0] + img[i-1,j]*mask[2-0,2-1] + img[i-1,j+1]*mask[2-0,2-2] + img[i,j-1]*mask[2-1,2-0] + img[i,j]*mask[2-1,2-1] + img[i,j+1]*mask[2-1,2-2] + img[i+1,j-1]*mask[2-2,2-0] + img[i+1,j]*mask[2-2,2-1] +img[i+1,j+1]*mask[2-2,2-2]

        img_new[i,j] = temp
        


img_new = img_new.astype(np.uint8)
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(img_new)

plt.show()
