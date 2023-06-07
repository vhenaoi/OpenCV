#Video
import cv2

Facehaar=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#video=cv2.VideoCapture('videoMJ.avi')
video=cv2.VideoCapture('video2.avi')
F=video.get(cv2.CAP_PROP_FRAME_COUNT)#Cantidad de fotogramas
print('Fotogramas: ',F)
col=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
row=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'WMV1')
video=cv2.VideoWriter('video3.avi',fourcc,20.0,(col,row))
print('col: ',col)
print('fil: ',row)
while True:
    state, frame=video.read()#Funciona mientras las imagenes se muestran
    
    if state==False:#cuando se dejan de mostrar las imagenes state se vuelve falso
        print('Fin de video')
        break
    
    #Cambiar a escala de grises
    videoGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=Facehaar.detectMultiScale(videoGray,scaleFactor=1.1,minNeighbors=5,minSize=(150,150),maxSize=(210,210),flags=cv2.CASCADE_SCALE_IMAGE)
    
    for (a,b,c,d) in face:
        cv2.rectangle(frame,(a,b),(a+c,b+d),(0,255,0),3)
    
    if F==8000:
        video.write(frame)
#    cv2.namedWindow('Imagen',0)
    cv2.imshow('Imagen',frame)
    k=cv2.waitKey(24)
    #    cv2.VideoWriter('NuevoVideo.mp4')
    if k==27: break
    
video.release()
cv2.destroyAllWindows()