#Deteccion de rostros
#Detección de bordes de canny, detecta cambios de intensidad por medio de gradientes 
#Aplicar filtros Haar en esos cambios de intensidad elevadas
import cv2

Facehaar=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

fisicos=cv2.imread('fisicos1.png')
#original=cv2.imread('original.jpg')

#Cambiar a escala de grises
fisicosGray=cv2.cvtColor(fisicos,cv2.COLOR_BGR2GRAY)
#originalGray=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)

face=Facehaar.detectMultiScale(
        #original,
        fisicosGray,
        scaleFactor=1.1,
        minNeighbors=5,
#        minSize=(),
#        maxSize=(),
        flags=cv2.CASCADE_SCALE_IMAGE)

for (a,b,c,d) in face:
    cv2.rectangle(fisicos,(a,b),(a+c,b+d),(0,255,0),3)
#    cv2.rectangle(original,(a,b),(a+c,b+d),(0,255,0),3)


cv2.namedWindow('Imagen',0)
cv2.imshow('Imagen',fisicos)
#cv2.imshow('Imagen',original)
cv2.waitKey(0)