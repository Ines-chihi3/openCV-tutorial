#draws points and connecting points using line 


import cv2
import numpy as np
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points)>1:
            cv2.line(img,points[-2],(x,y),(255,0,0),1)
        cv2.imshow('image',img)


img=np.zeros((512,512,3),np.uint8)
points=[]
cv2.imshow('image',img)
cv2.setMouseCallback('image',click)
cv2.waitKey(0)
cv2.destroyAllWindows()