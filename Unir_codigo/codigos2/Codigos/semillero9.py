# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 20:18:22 2018

@author: lxMera
"""

import cv2
import numpy as np

cv2.namedWindow('frame',0)
image=cv2.imread('Virus.png')

#imageB=image[:,:,0]
#imageG=image[:,:,1]

#image=imageG+255*imageB
#black=np.zeros((100,100,3), dtype="uint8")

ret, seg = cv2.threshold(image,125,255,cv2.THRESH_BINARY)

cv2.imshow('frame',seg)
cv2.waitKey(0)
cv2.destroyAllWindows()