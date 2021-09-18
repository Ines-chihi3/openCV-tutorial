
import cv2
img = cv2.imread('HappyFish.jpg')
#convert image  bgr 2 gray
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',img)
cv2.imshow('imggray',imggray)

k=cv2.waitKey(0)
if k==27 :
    cv2.destroyAllWindows()

