import cv2
import numpy as np

ojosHaar = cv2.CascadeClassifier("haarcascade_eye.xml")
cv2.namedWindow('imagen',0)
cv2.namedWindow('otra',0)
image=cv2.imread('ojos.jpg')

ImaGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ojos = ojosHaar.detectMultiScale(
        ImaGray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        #minSize=(150,150),
        #maxSize=(210,210),
        flags = cv2.CASCADE_SCALE_IMAGE)

for (a, b, c, d) in ojos:
    cv2.rectangle(image,(a,b),(a+c,b+d),(255,0,0),3)
    Roi = image[b:b+d,a:a+c]
    Roi = cv2.cvtColor(Roi,cv2.COLOR_BGR2GRAY)
    Roi = cv2.medianBlur(Roi,5)
    
    circles = cv2.HoughCircles(Roi,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=45,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(image,(a+i[0],b+i[1]),i[2],(0,255,0),2)
        cv2.circle(image,(a+i[0],b+i[1]),6,(0,0,255),1)
        print(i[2])
        
    cv2.imshow('otra',Roi)
    cv2.waitKey(0)
    
cv2.imshow("imagen",image)
cv2.waitKey(0)