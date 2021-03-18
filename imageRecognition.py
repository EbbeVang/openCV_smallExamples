import cv2

#detect the cats face
catCascade = cv2.CascadeClassifier('resources/haarcascade_frontalcatface.xml')

#detect the girls face
faceCascade = cv2.CascadeClassifier('resources/haarcascade_frontalface.xml')

catImage = cv2.imread('resources/manWithCat2.jpg')
imageGreyScale = cv2.cvtColor(catImage, cv2.COLOR_BGR2GRAY)


cats = catCascade.detectMultiScale(imageGreyScale)
for (x,y,w,h) in cats:
    cv2.rectangle(catImage, (x,y), (x+w,y+h), (255,255,255),2)

humans = faceCascade.detectMultiScale(imageGreyScale, 1.05, 4)
for (x,y,w,h) in humans:
    cv2.rectangle(catImage, (x,y), (x+w,y+h), (255,0,0),2)


cv2.imshow("cat detector", catImage)

cv2.waitKey(0)