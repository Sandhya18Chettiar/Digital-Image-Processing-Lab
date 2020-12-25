# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 00:38:37 2020

@author: sandhya chettiar
"""

#LAB2 - Color to Gray scale conversion

#Direct code using library function

from matplotlib import pyplot as plt
from skimage import io
img = io.imread('C:/Users/sandhya chettiar/Desktop/Seattle_night_Rizal_Park.jpeg', as_gray=True)
plt.gray()        #Gives gray coloured image
plt.imshow(img)
