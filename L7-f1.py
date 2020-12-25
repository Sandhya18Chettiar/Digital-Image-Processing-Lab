# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 08:10:40 2020

@author: sandhya chettiar
"""

#LAB 7

#Exp07:Affine Transformation: Scaling, Shear horizontal, Shear vertical, Translation

import math
import numpy as np
from matplotlib import pyplot as plt
from skimage import data
from skimage import transform as tf

cat=data.chelsea()
plt.figure(1)
plt.subplot(131)
plt.subplot(131).set_title("Original image")
plt.imshow(cat,cmap=plt.cm.gray)

tform=tf.SimilarityTransform(scale=(1,1),rotation=math.pi/100,translation=(1,1))
rotated=tf.warp(cat,tform)

plt.subplot(132)
plt.subplot(132).set_title("Rotated")
plt.imshow(rotated,cmap=plt.cm.gray)

tform2=tf.SimilarityTransform(scale=(2,2),translation=(1,1))
scaled = tf.wrap(cat,tform2)
plt.subplot(133)
plt.subplot(133).set_title("Scaled")
plt.imshow(scaled, cmap=plt.cm.gray)

#tform3=tf.AffineTransform(shear=math.pi/180*10)
#shearing = tf.warp(cat,tform3)

#plt.subplot(2,4,4)
#plt.imshow(shearing, cmap=plt.cm.gray)