# install openCV
# pip install opencv-python


import cv2
print("package imported")


#read image 
image = cv2.imread("resources/kitten.jpg")


#crop image
crop = image[200:400,300:600]

# show image
cv2.imshow("cropped image", crop)
#wait
cv2.waitKey(0)