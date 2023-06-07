# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:49:52 2018

@author: lxMera
"""

import cv2

frame=cv2.imread('Virus.png')

frameR=frame[:,:,2]
frameG=frame[:,:,1]
frameB=frame[:,:,0]

cv2.namedWindow('WindowRGB',0)
cv2.namedWindow('WindowB',0)
cv2.namedWindow('WindowG',0)
cv2.namedWindow('WindowR',0)

cv2.imshow('WindowRGB',frame)
cv2.imshow('WindowB',frameR)
cv2.imshow('WindowG',frameG)
cv2.imshow('WindowR',frameB)

#cv2.imwrite('Imagen.png',frameR)
#img = np.zeros((col, row, 3), np.uint8)

cv2.waitKey(0)

cv2.destroyAllWindows()  