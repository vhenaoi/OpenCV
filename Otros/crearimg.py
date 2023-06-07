import cv2
import numpy as np

row=256
col=256
channel=3

img=np.zeros((row,col,channel),dtype=np.uint8);
#img=cv2.imread('imagen.jpg');
for i in range(row):
    img[:,i,0]=255;
    img[:,i,1]=255;
    img[:,i,2]=255;
    
cv2.namedWindow('Ventana',0);
cv2.imshow('Ventana',img);
x=cv2.waitKey(0);
cv2.destroyAllWindows();
