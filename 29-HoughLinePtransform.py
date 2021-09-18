

import cv2
import numpy as np 

img=cv2.imread('sudoko.PNG')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges= cv2.Canny(gray,0,50,apertureSize=3)
lines=cv2.HoughLinesP(edges,1,np.pi/180,125,minLineLength=100,maxLineGap=20)
for line in lines :
    x1,y1,x2,y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()