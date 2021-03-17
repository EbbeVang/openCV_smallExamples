
import cv2
print("package imported")


#read image 
image = cv2.imread("resources/kitten.jpg")

# get the size of the image
print(image.shape) # (height. width, channels)

smallImage = cv2.resize(image, (900,600))

cv2.imshow("normal size", image)
cv2.imshow("small image", smallImage)

cv2.waitKey(0)