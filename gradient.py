# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:01:42 2020

@author: sandhya chettiar
"""
#Gradient Filter -prewitt,Sobel, Roberts filters

from skimage import filters
from skimage import data
import math
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = data.text()
img=filters.gaussian(img, 1)
#plt.imshow(img)
pad= np.pad(img, [1, 1], mode='constant')
#plt.imshow(pad)
plt.gray()
# Obtain number of rows and columns
# of the image
m, n = img.shape
# Develop Averaging filter(3, 3) mask
maskx = [[-1,0,1],[-2,0,2],[-1,0,1]]
masky= [[1,2,1],[0,0,0],[-1,-2,-1]]
# Convolve the 3X3 mask over the image
img_new = np.zeros([m, n])
for i in range(1, m-1):
    for j in range(1, n-1):
        gx = maskx[0][0]*pad[i-1][j-1]+maskx[0][1]*pad[i-1][j]+maskx[0][2]*pad[i-1][j+1]+maskx[1][0]*pad[i][j-1]+maskx[1][1]*pad[i][j]+maskx[1][2]*pad[i][j+1]+maskx[2][0]*pad[i+1][j-1]+maskx[2][1]*pad[i+1][j]+maskx[2][2]*pad[i+1][j+1]
        gy = masky[0][0]*pad[i-1][j-1]+masky[0][1]*pad[i-1][j]+masky[0][2]*pad[i-1][j+1]+masky[1][0]*pad[i][j-1]+masky[1][1]*pad[i][j]+masky[1][2]*pad[i][j+1]+masky[2][0]*pad[i+1][j-1]+masky[2][1]*pad[i+1][j]+masky[2][2]*pad[i+1][j+1]
img_new[i, j]= math.sqrt(gx**2+gy**2)
img_new=img_new[1:-1,1:-1]
img_new = img_new.astype(np.uint8)

plt.figure(1)
plt.subplot(3,1,1)
plt.imshow(img)
plt.subplot(3,1,2)
plt.imshow(img_new)
sob=filters.sobel(img,mask=None)
plt.subplot(3,1,3)
plt.imshow(sob)