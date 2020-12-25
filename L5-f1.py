# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:17:55 2020

@author: sandhya chettiar
"""

#LAB5
#bit slicing 


from skimage import img_as_ubyte
import numpy as np
from matplotlib import pyplot as plt
from skimage import io

img = io.imread('C:/Users/sandhya chettiar/Desktop/flower.jpg',as_gray=True)

plt.gray()
print(img)

a = img_as_ubyte(img)
y = np.zeros((len(a),len(a[0])))

for i in range(0,len(a),1):
    for j in range(0,len(a[0]),1):
        x=int(bin(a[i][j])[2:])
        y[i][j]=int((x/1000000)%10)*10000000  #For 7
        
       #x = int('0'+bin(a[i][j])[2:])
       #y[i][j] = int(x/1000000)*10000000     #For 7 and 8
plt.imshow(y)