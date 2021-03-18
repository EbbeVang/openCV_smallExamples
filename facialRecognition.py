import cv2

videoCapture  =cv2.VideoCapture(0)

#set withand height
videoCapture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
videoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
videoCapture.set(bright)
while True:
    succes, img = videoCapture.read()
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break