import cv2
import numpy as np
import datetime
#import time
#4segundos
#7.5 Hz
#Paso de grosor 4segundos (descanso negro)
#Pantalla: alto 29cm  - ancho 46,5cm



row=256
col=256
channel=3
contador = 0
estado=0
#tiempo=time.clock()
#tiempo=time.sleep(0.6)  
Divisiones=input('Divisiones: ')
Contraste=input('Contraste: ')
#Velocidad=input('Velocidad: ')
Divisiones=int(Divisiones)
Contraste=int(Contraste)
D=int(256/Divisiones) 
print(D)
C=0
img=np.zeros((row,col,channel),dtype=np.uint8)
Hora_inicio = datetime.datetime.now().hour
Minuto_inicio = datetime.datetime.now().minute
Segundo_inicio = datetime.datetime.now().second
print("Inicio de la tarea(HH:MM:SS): ",Hora_inicio,":",Minuto_inicio,":",Segundo_inicio)
cv2.namedWindow('',0)
while True: 
    if (estado==0): 
        img[:,:D,0]=contador
        img[:,:D,1]=contador
        img[:,:D,2]=contador
        img[:,D:128,0]=255-contador
        img[:,D:128,1]=255-contador
        img[:,D:128,2]=255-contador

        img[:,128:192,0]=contador
        img[:,128:192,1]=contador
        img[:,128:192,2]=contador
        img[:,192:,0]=255-contador
        img[:,192:,1]=255-contador
        img[:,192:,2]=255-contador
#        contador+=1
        if(contador==255):
           estado=1
           cv2.imshow('',img)
    #           tiempo=time.sleep(0.6)  
    #           print(contador)
    if (estado==1):
       img[:,:D,0]=contador
       img[:,:D,1]=contador
       img[:,:D,2]=contador
       img[:,D:128,0]=255-contador
       img[:,D:128,1]=255-contador
       img[:,D:128,2]=255-contador

       img[:,128:192,0]=contador
       img[:,128:192,1]=contador
       img[:,128:192,2]=contador
       img[:,192:,0]=255-contador
       img[:,192:,1]=255-contador
       img[:,192:,2]=255-contador       
       C=C+D
    
#       contador-=1
    if(contador==0):
       estado=0
    cv2.imshow('',img)
    x=cv2.waitKey(Contraste);#modifico contraste
#Codigo ASCCI 27 es la tecla de escape
    if x==27:
       break
Hora_final = datetime.datetime.now().hour
Minuto_final = datetime.datetime.now().minute
Segundo_final = datetime.datetime.now().second
print("Final de la tarea(HH:MM:SS): ",Hora_final,":",Minuto_final,":",Segundo_final)
Hora_total=Hora_final-Hora_inicio
if(Minuto_final>Minuto_inicio):
    Minuto_total=Minuto_final-Minuto_inicio
else:
    Minuto_total=Minuto_inicio-Minuto_final
if(Segundo_final>Segundo_inicio):
    Segundo_total=Segundo_final-Segundo_inicio
else:
    Segundo_total=Segundo_inicio-Segundo_final
print("Duración(HH:MM:SS): ",Hora_total,":",Minuto_total,":",Segundo_total)

cv2.destroyAllWindows();    
    
