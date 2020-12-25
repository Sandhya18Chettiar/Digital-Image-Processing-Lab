# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:05:09 2020

@author: sandhya chettiar
"""
#LAB - Gamma, Power, log

# Gamma

from skimage import data, exposure, img_as_float
import numpy as np
from matplotlib import pyplot as plt
from skimage import io

image = img_as_float(data.moon())
plt.gray()

gamma_corrected2 = exposure.adjust_gamma(image, 2)
plt.figure(1)
plt.subplot(131)
plt.subplot(131).set_title("Original image")
plt.imshow(image)
plt.subplot(132)
plt.subplot(132).set_title("Gamma=2")
plt.imshow(gamma_corrected2)
plt.subplot(133)
plt.imshow(exposure.adjust_gamma(image, 1/2))
plt.subplot(133).set_title("Gamma=1/2")
plt.show()


# log

from skimage import data, exposure, img_as_float
import numpy as np
from matplotlib import pyplot as plt
from skimage import io

image = img_as_float(data.moon()) 
plt.gray()

log_corrected2 = exposure.adjust_log(image, gain=1, inv=False)
plt.figure(1)
plt.subplot(131)
plt.subplot(131).set_title("Original image")
plt.imshow(image)
plt.subplot(132)
plt.subplot(132).set_title("log")
plt.imshow(gamma_corrected2)
plt.subplot(133)
plt.imshow(exposure.adjust_log(image, gain=1, inv=True))
plt.subplot(133).set_title("Antilog")
plt.show()