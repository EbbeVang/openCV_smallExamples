import cv2

videoCapture  =cv2.VideoCapture('resources/kittens.mp4')

while True:
    succes, img = videoCapture.read()
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break