# install openCV
# pip install opencv-python


import cv2
print("package imported")


#read image 
image = cv2.imread("resources/kitten.jpg")
# show image
cv2.imshow("image", image)
#wait
cv2.waitKey(0)