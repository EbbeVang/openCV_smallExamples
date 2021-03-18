# drawing with opencv


import cv2
import numpy as np

#create image (matrix of pixels)
image = np.zeros((800,800,3), np.uint8)

image[:] =255,0,0


# draw some lines
cv2.line(image,(0,0), (800,800), (0,255,0),3)
cv2.line(image,(800,0), (0,800), (0,255,0),3)


for i in range(1,80):
    cv2.line(image,(i*10,0), (i*10,800), (0,255-(i*2),0),1)
    cv2.line(image,(0,i*10), (800, i*10), (0,250-(i*2),20),1)
    cv2.circle(image, (i*20,i*20), 60, (0,0,255), 2)
    
image[740:800,0:300] = 255,255,255
cv2.putText(image, "OpenCV Rocks!", (20,780), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),1)
    

cv2.imshow("drawing", image)

cv2.waitKey(0)
