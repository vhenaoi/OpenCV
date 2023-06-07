# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 23:26:11 2018

@author: lxMera
"""

import cv2
import numpy as np

row=256
col=357
channel=3
z=0
pos=0
pix=[0, 0, 0]
img=np.zeros((row, col, channel), dtype=np.uint8)

cv2.namedWindow('Ventana')

while True:
    for b in range(51):
        pix[0]=b*5
        img[:,pos]=pix
        pos+=1
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for g in range(51):
        pix[1]=g*5
        img[:,pos]=pix
        pos+=1
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for b in range(51):
        pix[0]=255-(b*5)
        img[:,pos]=pix
        pos+=1
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for r in range(51):
        pix[2]=r*5
        img[:,pos]=pix
        pos+=1
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for g in range(51):
        pix[1]=255-(g*5)
        img[:,pos]=pix
        pos+=1
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for b in range(51):
        pix[0]=b*5
        img[:,pos]=pix
        pos+=1
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
        
    for g in range(51):
        pix[1]=g*5
        img[:,pos]=pix
        pos+=1
        cv2.imshow('Ventana',img)
        z=cv2.waitKey(10)
    
    cv2.waitKey(0)
        
    break

cv2.destroyAllWindows()