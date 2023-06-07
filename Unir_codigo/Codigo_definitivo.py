# In[Importar librerias]
import cv2
import numpy as np 
# In[Cargar filtros Haar]
faceHaar = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
ojosHaar = cv2.CascadeClassifier("haarcascade_eye.xml")
# In[Cargar video]
#video = cv2.VideoCapture('video.mp4')
video = cv2.VideoCapture(0) #//abrir camara
# In[Definir variables globales]
col=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
row=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# In[Guardar video]
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('nuevovideo.mp4',fourcc, 20.0, (col,row))
# In[Definir ventanas]
cv2.namedWindow("video",0)
cv2.namedWindow('deteccion',0)
cv2.imshow('video.mp4',video)
# In[While]
while True:
    std, frame=video.read()
    
    if std==False:
        print ('Fin del video')
        break
    
    ImaGray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = faceHaar.detectMultiScale(
        ImaGray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize= (150,150),
        maxSize=(210,210),
        flags = cv2.CASCADE_SCALE_IMAGE)
    ojos = ojosHaar.detectMultiScale(
        ImaGray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize= (150,150),
        maxSize=(210,210),
        flags = cv2.CASCADE_SCALE_IMAGE)
    
    for (a, b, c, d) in face:
        cv2.rectangle(frame,(a, b),(a+c,b+d),(0,255,0),3)              
        cv2.circle(frame, (a+c/2,b+d/2),5,255,2)
        print ("Datos", a, b, c, d)
        ROI=ImaGray[b:b+d,a:a+c]
        cv2.imshow('ROI',ROI)
        cv2.rectangle(image,(a, b),(a+c,b+d),(255,0,0),3)
        Roi=image[b:b+d,a:a+c]
        Roi = cv2.cvtColor(Roi,cv2.COLOR_BGR2GRAY)
        Roi = cv2.medianBlur(Roi,5)
        
        circles = cv2.HoughCircles(Roi,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=45,minRadius=0,maxRadius=0)    
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(image,(a+i[0],b+i[1]),i[2],(0,255,0),2)
            cv2.circle(image,(a+i[0],b+i[1]),6,(0,0,255),1)
            print(i[2])
    
    out.write(frame)
    cv2.imshow("video",frame)
    k=cv2.waitKey(30)
    
    if k==27: break

video.release()
out.release()
cv2.destroyAllWindows()

# In[for]


    
for (a, b, c, d) in ojos:
    cv2.rectangle(image,(a, b),(a+c,b+d),(255,0,0),3)
    Roi=image[b:b+d,a:a+c]
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
    
cv2.destroyAllWindows()

