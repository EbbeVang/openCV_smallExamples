# Exercise in facial recognition!

import cv2
faceCascade = cv2.CascadeClassifier('resources/haarcascade_frontalface.xml')


videoCapture  =cv2.VideoCapture(0)

#set withand height
videoCapture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
videoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
while True:
    succes, img = videoCapture.read()

    imageGreyScale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    humans = faceCascade.detectMultiScale(imageGreyScale, 1.05, 4)
    for (x,y,w,h) in humans:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)

    img[50:50, 0:0] = 255,255,255
    
    if len(humans) > 0:
        cv2.rectangle(img,(0,400),(300,300),(0,255,0),-1)
        cv2.putText(img, "Face detected!", (20,340), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,0),1)


    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break