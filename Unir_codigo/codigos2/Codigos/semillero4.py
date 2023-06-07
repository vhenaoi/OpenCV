# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 22:53:05 2018

@author: lxMera
"""

import cv2
import numpy as np

row=256
col=256
channel=3
z=0

img=np.zeros((row, col, channel), dtype=np.uint8)

cv2.namedWindow('Ventana')

while True:
    for b in range(256):
        img[:,:,0]=b
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for g in range(256):
        img[:,:,1]=g
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for b in range(256):
        img[:,:,0]=255-b
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for r in range(256):
        img[:,:,2]=r
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for g in range(256):
        img[:,:,1]=255-g
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for b in range(256):
        img[:,:,0]=b
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for g in range(256):
        img[:,:,1]=g
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    break

cv2.destroyAllWindows()
                