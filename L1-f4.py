# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 08:30:24 2020

@author: sandhya chettiar
"""
#LAB1
#Creating a dark image 
from skimage import io
from skimage import img_as_float
from matplotlib import pyplot as plt
my_image=io.imread("C:/Users/sandhya chettiar/Desktop/pic.jpeg")
dark_im=(img_as_float(my_image))*0.25
plt.imshow(dark_im)
