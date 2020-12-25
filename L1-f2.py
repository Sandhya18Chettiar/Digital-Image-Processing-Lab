# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 08:28:28 2020

@author: sandhya chettiar
"""
#LAB1
#Program to read an image and display it
from skimage import io
from matplotlib import pyplot as plt
my_image=io.imread("C:/Users/sandhya chettiar/Desktop/Seattle_night_Rizal_Park.jpeg")
print(my_image)
plt.imshow(my_image)
