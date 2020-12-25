# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:57:20 2020

@author: sandhya chettiar
"""

##Intensity range adjustment

#Contrast Stretching

from skimage import exposure
import numpy as np
from matplotlib import pyplot as plt
from skimage import io
img = io.imread('C:/Users/sandhya chettiar/Desktop/la.jpg', as_gray=True)
plt.gray()
x=img.ravel()

plt.hist(img.ravel(), bins=256, range=(0.0, 1.0))
v_min, v_max = np.percentile(img, (0.2, 99.8))
better_contrast = exposure.rescale_intensity(img, in_range=(v_min, v_max))
plt.hist(better_contrast.ravel(),bins=256,range=(0.0, 1.0))

plt.figure(1)
plt.subplot(121)
#no of rows=1,no of cols=3,position=1
plt.imshow(img)
plt.subplot(122)
plt.imshow(better_contrast)
plt.show()

