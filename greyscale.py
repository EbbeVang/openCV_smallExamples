
import cv2
print("package imported")


#read image 
image = cv2.imread("resources/kitten.jpg")
greyscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
gaussianBlur = cv2.GaussianBlur(image, (15,15), 0)
canny = cv2.Canny(image, 150, 200)
# show image
cv2.imshow("image", greyscale)
cv2.imshow("canny", canny)
cv2.imshow("GaussianBlue", gaussianBlur)

#wait
cv2.waitKey(0)