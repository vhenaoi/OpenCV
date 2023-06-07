import cv2
#import numpy as np

#Leer la imagen
cimg = cv2.imread('monedas.jpg')

#Conversión del modelo de color- BGR a escala de grises (imagen de un solo )
img = cv2.cvtColor(cimg,cv2.COLOR_BGR2GRAY)


img = cv2.medianBlur(img,5)

#Parametro 1- umbral del detector de bordes canny (más grande menos sensible)
#Parametro 2 - valor de acumulador, acumulación de puntos que conforman los 
# x, y, radio