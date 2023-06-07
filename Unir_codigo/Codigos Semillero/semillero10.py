# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:34:59 2018

@author: lxMera
"""

import cv2
#import numpy as np

Tiempo=24  #En milisegundos

cv2.namedWindow('Frame',0)
video=cv2.VideoCapture('Megamind.avi')

print ("Columnas", video.get(cv2.CAP_PROP_FRAME_WIDTH))
print ("Filas",  video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print ("Total de Fotogramas", video.get(cv2.CAP_PROP_FRAME_COUNT))
print ("Velocidad", video.get(cv2.CAP_PROP_FPS))

while True:
    state, frame=video.read()
    
    if state==False:
        print ('Fin del video')
        break
    
    #frame2=frame.copy()     
    #frame[:,:,0]=0
    #frame[:,:,1]=0    
    #frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      
    
    cv2.imshow('Frame',frame)
    k=cv2.waitKey(Tiempo)
    
    if k==27: break

#Liberar la variable para espacio de memoria
video.release()
cv2.destroyAllWindows()