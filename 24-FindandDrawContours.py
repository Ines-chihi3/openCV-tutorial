
import cv2
img=cv2.imread("opencvLogo.png")

imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,200,255,0)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print("nbr of contours is : ",str(len(contours)))
cv2.drawContours(img,contours,-1,(0,255,255),2)
cv2.imshow("img",img)
cv2.imshow("imgray",imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()