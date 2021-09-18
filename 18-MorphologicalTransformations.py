



import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('J.PNG',0)
kernal = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernal,iterations = 1)
dilation=cv2.dilate(img,kernal,iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernal)
image=[img,erosion,dilation,opening,closing,mg,th]
titles=["img","erosion","dilation","opening","closing","mg","th"]

for i in range(7):
    plt.subplot(3,3,i+1),plt.imshow(image[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
