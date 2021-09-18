"""
import cv2
import numpy as np
img=cv2.imread('HappyFish.jpg')
layer=img.copy()
gp=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)

    cv2.imshow('layer'+str(i),layer)


cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# 
"""
import cv2
import numpy as np
img=cv2.imread('HappyFish.jpg')
layer=img.copy()
gp=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)

    #cv2.imshow('layer'+str(i),layer)

layer=gp[5]
cv2.imshow("upper level gaussian pyramid",layer)
lp=[layer]
for i in range(5,0,-1):
    gaus_extand=cv2.pyrUp(gp[i])
    laplac=cv2.subtract(gp[i-1],gaus_extand)
    cv2.imshow(str(i),laplac)

cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
