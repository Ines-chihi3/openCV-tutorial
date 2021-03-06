#image gradient is directional change in the intensity or color in image 
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("opencvLogo.png",cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=1)
lap=np.uint8(np.absolute(lap))
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)
sobelx=np.uint8(np.absolute(sobelx))
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1)
sobely=np.uint8(np.absolute(sobely))
canny= cv2.Canny(img,100,200)
sobelCombined=cv2.bitwise_or(sobelx,sobely)
titles=['image','laplacien','sobelx','sobely','sobelCombined','canny']
images=[img,lap,sobelx,sobely,sobelCombined,canny]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()



