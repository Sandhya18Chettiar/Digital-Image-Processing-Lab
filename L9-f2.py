# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 02:03:09 2020

@author: sandhya chettiar
"""

import pylab as plt
import matplotlib.image as mpflower_img
import numpy as np


flower_img = np.uint8(mpflower_img.imread('C:/Users/sandhya chettiar/Desktop/flower.jpg')*255.0)
# convert to grayscale

# for individual channels R, G, B for nongrayscale images
flower_img = np.uint8((0.2126* flower_img[:,:,0]) + \
  		np.uint8(0.7152 * flower_img[:,:,1]) +\
			 np.uint8(0.0722 * flower_img[:,:,2]))
    #Every colour has different wavelength. If multiplied with same no. then one colour 
    # can over power other.

#First step - To count the total no. of pixels associated witheach pixel intensity.
#Second step - To calculate probability of each pixel intensity in the image matrix.
#Third step - To calculate cumulative probability.
#Fourth step - To multiply cumulative probability with total intensity range.
#Fifth step - To round off by taking floor.

def flower_imagehist(flower_image):
  # calculates normalized histogram of an image
	m, n = flower_image.shape
	h = [0.0] * 256 #instead of np.zeros(len[a], len(a[0]))
	for i in range(m): #Traversing pixels
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
	s1, s2 = flower_image.shape #Shape of image is accessed
	Y = np.zeros_like(flower_image) #transformed image
	# applying transfered values for each pixels
	for i in range(0, s1):
		for j in range(0, s2):
			Y[i, j] = sk[flower_image[i, j]]
	H = flower_imagehist(Y)
	#return transformed image, original and new histogram and transform function
	return Y , h, H, sk
    

new_flower_img, h, new_h, sk = histeq(flower_img)

#Histogram plotting - Pixel intensities VS pixel probabilities

# To display old and new image

# show original image
plt.subplot(121)
plt.imshow(flower_img)
plt.title('Original image')
plt.set_cmap('gray')
# show original image
plt.subplot(122)
plt.imshow(new_flower_img)
plt.title('Histogram eq. image')
plt.set_cmap('gray')
plt.show()

# plot histograms and transfer function
fig = plt.figure()
fig.add_subplot(221)
plt.plot(h)
plt.title('Original histogram') # original histogram

fig.add_subplot(222)
plt.plot(new_h)
plt.title('New histogram') #hist of eqlauized image

plt.show()