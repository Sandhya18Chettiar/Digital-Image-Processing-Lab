# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:00:36 2020

@author: sandhya chettiar
"""

from skimage import data
import numpy as np
from matplotlib import pyplot as plt

img = data.text()
plt.gray()


m, n = img.shape

img_new = np.zeros([m, n])

for i in range(1,m-1):
    for j in range(1,n-1):
        #Median
        median = [img[i,j],img[i,j-1],img[i,j+1],img[i-1,j],img[i-1,j-1],img[i-1,j+1],img[i+1,j],img[i+1,j-1],img[i+1,j+1]]
        median.sort()
        temp = median[4]
        
        img_new[i,j] = temp
        


img_new = img_new.astype(np.uint8)
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(img_new)

plt.show()
