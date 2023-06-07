import cv2
import numpy as np
#import math
import time

row=10
col=10
channel=3
contador = 0
timer=0;
estado=0;
x=0;
stop=0;
Divisiones=100 #Estas son las divisiones iniciales que equivalen a un grosor de 4.35 mm
#tiempo=input('Tiempo(s): ');
#tiempo=int(tiempo)
#D=int(math.ceil(row/Divisiones)) #Aproxima al entero de arriba para reducir perdida de grosor
#t=math.floor(Divisiones/2); #Variable para rango del for
img=np.zeros((row,col,channel),dtype=np.uint8);
cv2.namedWindow('', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('', cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
time_on = time.time()

while True:
    for i in range(row):
        img[:,:i,0]=255-contador
        img[:,:i,1]=255-contador
        img[:,:i,2]=255-contador
        img[:,i:,0]=contador
        img[:,i:,1]=contador
        img[:,i:,2]=contador
    
        contador+=100
#        if(contador==255):
#            stop=1

               
    cv2.imshow('',img);
    k=cv2.waitKey(10)
    if k==27 or stop==1: 
       break

cv2.destroyAllWindows();        