import cv2
import numpy as np
image=cv2.imread('Virus.png')

ROI=image[:200,:200,:]
ROIB=image[:200,:200,0]
ret, seg=cv2.threshold(image,125,255,0)

cv2.namedWindow('Ventana',0)
cv2.namedWindow('Ventana2',0)

cv2.imshow('Ventana',image)
#cv2.imshow('Ventana2',seg)

cv2.waitKey(0)

cv2.destroyAllWindows()