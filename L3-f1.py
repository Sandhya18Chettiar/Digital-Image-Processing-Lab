# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:30:09 2020

@author: sandhya chettiar
"""
#Python code for Otsu’s thresholding
import matplotlib.pyplot as plt
from skimage import io
from skimage.filters import threshold_otsu
img = io.imread('C:/Users/sandhya chettiar/Desktop/Seattle_night_Rizal_Park.jpeg', as_gray=True)
print(img)
thresh = threshold_otsu(img)
print(thresh)
binary = img > thresh
#plt.gray()
#plt.imshow(img)
plt.show()
plt.imshow(binary)
plt.show()
