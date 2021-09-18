import cv2
print("hello ")
#there are 2 way : read an existant image, or create image and show it
#***************************read image :
#read image (put path of file )
img = cv2.imread('HappyFish.jpg')
#show you the pixel matrix
print(img)
#show image
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27 :
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('happyfish_copy.jpg',img)
    cv2.destroyAllWindows()

#*******************create image 
import numpy as np
img=np.zeros([512,512,3],np.uint8)
cv2.imshow('img',img)
k=cv2.waitKey(0)
if k==27 :
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('happyfish_copy.jpg',img)
    cv2.destroyAllWindows()