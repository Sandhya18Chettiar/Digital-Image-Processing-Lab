# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 23:35:37 2020

@author: sandhya chettiar
"""

#Convolution

from skimage import data
import numpy as np
from matplotlib import pyplot as plt
   
      
# Read the image
img = data.text()
plt.gray()
# Obtain number of rows and columns  of the image

m, n = img.shape
# Develop Averaging filter(3, 3) mask
mask = np.ones([3, 3], dtype = int)
m_h=np.flip(mask,0)
m_v=np.flip(m_h,1)

mask = m_v / 9
mask_pad=np.pad(mask,(1,1),'mean')
print(mask_pad)
# Convolve the 3X3 mask over the image  
img_new = np.zeros([m, n])
for i in range(1, m-1):
    for j in range(1, n-1):
        temp = img[i-1, j-1]*mask_pad[0, 0]+img[i-1, j]*mask_pad[0, 1]+img[i-1, j + 1]*mask_pad[0, 2]+img[i, j-1]*mask_pad[1, 0]+ img[i, j]*mask_pad[1, 1]+img[i, j + 1]*mask_pad[1, 2]+img[i + 1, j-1]*mask_pad[2, 0]+img[i + 1, j]*mask_pad[2, 1]+img[i + 1, j + 1]*mask_pad[2, 2]
         
        img_new[i, j]= temp
img_new = img_new.astype(np.uint8)
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(img_new)


