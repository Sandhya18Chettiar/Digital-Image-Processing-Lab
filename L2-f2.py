# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 00:49:52 2020

@author: sandhya chettiar
"""
#LAB2 - Color to Gray scale conversion

#Code using conversion formula

from skimage import io
from matplotlib import pyplot as plt
rgb=io.imread("C:/Users/sandhya chettiar/Desktop/Seattle_night_Rizal_Park.jpeg")
r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
rgb = 0.2989 * r + 0.5870 * g + 0.1140 * b
plt.gray()
plt.imshow(rgb)
