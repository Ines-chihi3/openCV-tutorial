#trackbar is useful whenever you want to change some value in your image dynamically at runtime.

"""
goal: want to change the bgr value using trackbar
-trachbar name
-windows name
-value initial
-valeur final
-nothing """  

import numpy as np
import cv2 as cv
def nothing(x):
    print(x)

img=np.zeros((300,512,3),np.uint8)

cv.namedWindow('image')
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)
switch="0 : off , 1 : on "
cv.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv.imshow('image',img)
    k=cv.waitKey(1) & 0xFF
    if k==27:
        break

    b=cv.getTrackbarPos('B','image')
    g=cv.getTrackbarPos('G','image')
    r=cv.getTrackbarPos('R','image')
    s=cv.getTrackbarPos(switch,'image')
    if s==0 :
        img[:]=0
    else    :

        img[:]=[b,g,r]

cv.destroyAllWindows()





