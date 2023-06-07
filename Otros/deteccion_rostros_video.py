# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:01:21 2018

@author: DELL
"""
#import numpy
import cv2 
cv2.namedWindow('video',0)
cv2.namedWindow('ROI',0)
#w=video.get(cv2.CAP_PROP_FRAME_WIDTH)
#h=video.get(cv2.CAP_PROP_FRAME_HEIGHT)
#F=video.get(cv2.CAP_PROP_FRAME_COUNT)
#FPS=video.get(cv2.CAP_PROP_FPS)
Facehaar=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#video=cv2.VideoCapture('videoMJ.avi')
video=cv2.VideoCapture('videoMJ.avi')

while True:
    state,frame=video.read()
    if state==False:
        print('Fin de vídeo.')
        break
    ImaGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=Facehaar.detectMultiScale(
        ImaGray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(150,150),
        maxSize=(210,210),
        flags=cv2.CASCADE_SCALE_IMAGE)
    for (a,b,c,d) in face:
        cv2.rectangle(frame,(a,b),(a+c,b+d),(0,255,0),3)        ##################
        ROI=ImaGray[b:b+d,a:a+c]
        cv2.imshow('ROI',ROI)
        eyes = eye_cascade.detectMultiScale(ImaGray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(ROI,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('video',frame)
    k=cv2.waitKey(30)
    if k==27:
        break
    
video.release()
cv2.destroyAllWindows()