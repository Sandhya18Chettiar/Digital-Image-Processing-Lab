# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:32:22 2020

@author: sandhya chettiar
"""

import math
import numpy as np
from matplotlib import pyplot as plt
from skimage import data
from skimage import transform as tf
cat=data.chelsea()

#scale+rotation
tform=tf.SimilarityTransform(scale=(2,1),rotation=math.pi/20,translation=(2,2))
rotated=tf.warp(cat,tform)
plt.figure(1)
plt.subplot(1,3,1)

plt.imshow(cat,cmap=plt.cm.gray)
plt.subplot(1,3,2)
plt.imshow(rotated,cmap=plt.cm.gray)

#Shear
tform3=tf.AffineTransform(shear=math.pi/180*10)
shearing = tf.warp(cat,tform3)

plt.subplot(1,3,3)
plt.imshow(shearing, cmap=plt.cm.gray)