import cv2
import numpy as np


img=cv2.imread('Shape.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,240,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(len(contours))

for contour in contours:

    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

    cv2.drawContours(img, [approx],0,(0,255,255),5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    font=cv2.FONT_HERSHEY_SIMPLEX
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, .5, (0,0,0))
    elif len(approx) == 4:
        x,y,w,h=cv2.boundingRect(approx)

        wh=float(w/h)
        if wh >=0.9  and wh<= 1.1:
            cv2.putText(img, "square", (x, y), font, .5, (0,0,0))
        else :
            cv2.putText(img, "Rectangle", (x, y), font, .5, (0,0,0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font, .5, (0,0,0))
    elif 6 < len(approx) < 15:
        cv2.putText(img, "Ellipse", (x, y), font, .5, (0,0,0))
    else:
        cv2.putText(img, "Circle", (x, y), font, .5, (0,0,0))
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()