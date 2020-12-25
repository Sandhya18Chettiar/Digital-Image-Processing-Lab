# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 02:03:50 2020

@author: sandhya chettiar
"""
# This is L9-f1 : Histogram Equilaztion funtions

import numpy as np 

def flower_imagehist(flower_image):
  # calculates normalized histogram of an image
	m, n = flower_image.shape
	h = [0.0] * 256
	for i in range(m):
		for j in range(n):
			h[flower_image[i, j]]+=1
	return np.array(h)/(m*n)

def cumsum(h):
	# finds cumulative sum of a numpy array, list
	return [sum(h[:i+1]) for i in range(len(h))]

def histeq(flower_image):
	#calculate Histogram
	h = flower_imagehist(flower_image)
	cdf = np.array(cumsum(h)) #cumulative distribution function
	sk = np.uint8(255 * cdf) #finding transfer function values
	s1, s2 = flower_image.shape
	Y = np.zeros_like(flower_image)
	# applying transfered values for each pixels
	for i in range(0, s1):
		for j in range(0, s2):
			Y[i, j] = sk[flower_image[i, j]]
	H = flower_imagehist(Y)
	#return transformed image, original and new istogram, 
	# and transform function
	return Y , h, H, sk