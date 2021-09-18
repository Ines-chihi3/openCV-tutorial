

import cv2
import numpy as np

img=cv2.imread('PlayerBall.jpg')
img=cv2.resize(img,(512,512))
img2=cv2.imread('HappyFish.jpg')
img2=cv2.resize(img2,(512,512))
dst=cv2.add(img,img2)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
import cv2
import numpy as np
#simple add lazem ykounou les 2 image ykoun 3andhom nafs e size
img=cv2.imread('PlayerBall.jpg')
img=cv2.resize(img,(512,512))
img2=cv2.imread('HappyFish.jpg')
img2=cv2.resize(img2,(512,512))
dst=cv2.addWeighted(img,.8,img2,.2,0)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""