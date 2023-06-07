# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 11:29:55 2018

@author: lxMera
"""

import cv2

cameraCapture = cv2.VideoCapture(0)

cv2.namedWindow('frame',0)

while True:
    
       
    success, frame = cameraCapture.read()
    
    if success!=True:
        break
    
    cv2.imshow('frame', frame)
    
    k=cv2.waitKey(30)
    
    if k==27: break

cameraCapture.release() #lib

cv2.destroyAllWindows()  

print ("end")