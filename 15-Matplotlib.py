#matplotlib
#2D ploting lib
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('HappyFish.jpg')
cv2.imshow('image',img)
#how to show image using matplotlib 

img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)

plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()