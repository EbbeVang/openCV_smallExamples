### find edges in image


import cv2
import numpy as np


# read image 
image = cv2.imread("resources/kitten.jpg")

# find edges
canny = cv2.Canny(image, 150, 200)

# dilation = expanding shapes by stretching or enlarging
# erode = make lines thinner
kernel = np.ones((5,5,), np.uint8)
imageDilation = cv2.dilate(canny, kernel, iterations=1)
imageEroded = cv2.erode(imageDilation, kernel, iterations=1)
# show image
cv2.imshow("canny", canny)
cv2.imshow("dilation", imageDilation)
cv2.imshow("erode", imageEroded)
#wait
cv2.waitKey(0)
