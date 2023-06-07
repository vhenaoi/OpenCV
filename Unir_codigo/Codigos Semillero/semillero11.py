# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 22:00:47 2018

@author: lxMera
"""

import cv2
#import numpy as np


cv2.namedWindow("video",0)
cv2.namedWindow("ROI",0)

#ojosHaar = cv2.CascadeClassifier("haarcascade_eye.xml")
faceHaar = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video=cv2.VideoCapture('videoMJ.avi')

#Grabar video
col=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
row=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'WMV1')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (col,row))

while True:
    std, frame=video.read()
    
    if std==False:
        print ('Fin del video')
        break
    
    ImaGray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = faceHaar.detectMultiScale(
        ImaGray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize= (150,150),
        maxSize=(210,210),
        flags = cv2.CASCADE_SCALE_IMAGE)
    
    for (a, b, c, d) in face:
        cv2.rectangle(frame,(a, b),(a+c,b+d),(0,255,0),3) 
        cv2.circle(frame,(int((a+c)/2),int((b+d)/2)),5,255,2)
#        print ("Datos", a, b, c, d)
        ROI=ImaGray[b:b+d,a:a+c]
        cv2.imshow('ROI',ROI)
    
    out.write(frame)
    cv2.imshow("video",frame)
    k=cv2.waitKey(30)
    
    if k==27: break

video.release()
out.release()
cv2.destroyAllWindows()