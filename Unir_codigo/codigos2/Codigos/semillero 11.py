# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:52:45 2019

@author: lxMera
"""

import cv2
import numpy as np

#Leer la imagen
cimg = cv2.imread('monedas.jpg')

#conversión del modelo de color- BGR a escala de grises (imagen de un solo canal)
img = cv2.cvtColor(cimg,cv2.COLOR_BGR2GRAY)

#filtrar la imagen (imagen y tamaño del kernel)
img = cv2.medianBlur(img,5)

#parametro 1- umbral del detector de bordes canny (más grande menos sensible a falsos)
#parametro 2 - Valor de acumulador, acumulacion de puntos que conforman los circulos (más grande menos sensible).
# x, y, radio
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=90,minRadius=130,maxRadius=180)

#
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(cimg,(i[0],i[1]),6,(0,0,255),3)

cv2.namedWindow('detected circles',0)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()