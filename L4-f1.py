# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:47:44 2020

@author: sandhya chettiar
"""
##Intensity range adjustment

#https://scikit-image.org/docs/dev/user_guide/transforming_image_data.html

#Image inversion

from skimage import util
from matplotlib import pyplot as plt
from skimage import io
col = io.imread('C:/Users/sandhya chettiar/Desktop/Seattle_night_Rizal_Park.jpeg')
img = io.imread('C:/Users/sandhya chettiar/Desktop/Seattle_night_Rizal_Park.jpeg', as_gray=True)
plt.gray()
#figure, axes = plt.subplots(nrows=1, ncols=2)
plt.figure(1)
plt.subplot(131)
#no of rows=1,no of cols=3,position=1
plt.imshow(col)
plt.subplot(132)
plt.imshow(img)
inverted_img = util.invert(img)
plt.subplot(133)
plt.imshow(inverted_img)
plt.show()
x=img.ravel()
plt.hist(img.ravel(), bins=256, range=(0.0, 1.0))

