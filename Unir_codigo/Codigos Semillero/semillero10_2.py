# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:44:03 2018

@author: lxMera
"""

import cv2
#import numpy as np


ojosHaar = cv2.CascadeClassifier("haarcascade_eye.xml")
#faceHaar = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cv2.namedWindow('imagen',0)
image=cv2.imread('ojos.jpg')

ImaGray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ojos = ojosHaar.detectMultiScale(
        ImaGray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        #minSize= (150,150),
        #maxSize=(210,210),
        flags = cv2.CASCADE_SCALE_IMAGE)
    
for (a, b, c, d) in ojos:
    cv2.rectangle(image,(a, b),(a+c,b+d),(0,255,0),3)              
    #cv2.circle(image, (a+c/2,b+d/2),20,255,4)
        

cv2.imshow("imagen",image)
cv2.waitKey(0)
    
cv2.destroyAllWindows()