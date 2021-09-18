#in this video we will learn how to perform object detection using HSV
#there are more then  150 convert color methodes
#one of there is colored image to HSV image
#so what is hsv color space
"""
HSV  : hue,saturation,value


so h,s,v can be used to pick any color just like  rgb
"""

import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow('tracking')
cv2.createTrackbar('LH','tracking',0,255,nothing)
cv2.createTrackbar('LS','tracking',0,255,nothing)
cv2.createTrackbar('LV','tracking',0,255,nothing)
cv2.createTrackbar('UH','tracking',255,255,nothing)
cv2.createTrackbar('US','tracking',255,255,nothing)
cv2.createTrackbar('UV','tracking',255,255,nothing)
while(1):
    frame=cv2.imread('smarties.PNG')

    hsv=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)

    LH=cv2.getTrackbarPos('LH','tracking')
    LS=cv2.getTrackbarPos('LS','tracking')
    LV=cv2.getTrackbarPos('LV','tracking')
    UH=cv2.getTrackbarPos('UH','tracking')
    US=cv2.getTrackbarPos('US','tracking')
    UV=cv2.getTrackbarPos('UV','tracking')
    lr=np.array([LH,LS,LV])
    ur=np.array([UH,US,UV])

    mask= cv2.inRange(hsv,lr,ur)

    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('image',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break
cv2.destroyAllWindows()
