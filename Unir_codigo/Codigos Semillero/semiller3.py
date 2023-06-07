# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 22:41:04 2018

@author: lxMera
"""

import cv2
import numpy as np

row=256
col=256
channel=3

img=np.zeros((row, col, channel), dtype=np.uint8)

for i in range(256):
    img[:,i,0]=i
    img[i,:,1]=i
    img[255-i,:,2]=i

cv2.namedWindow('Ventana')

cv2.imshow('Ventana',img)

cv2.waitKey(0)

cv2.destroyAllWindows()