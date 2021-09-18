import cv2
image=cv2.imread('HappyFish.jpg',1)

image=cv2.line(image,(0,0),(100,100),(255,0,0),5)

image=cv2.arrowedLine(image,(20,0),(100,100),(0,0,255),5)
"""
pt1(x1,y1)  pt2(x2,y2)
x1,y1-------
-          -
-          -
-          -
-------x2,y2
"""
image=cv2.rectangle(image,(20,20),(100,150),(0,255,0),5)
#draw circle
cv2.circle(image,(150,150),15,(255,0,0),5)
#put text
font=cv2.FONT_HERSHEY_PLAIN
cv2.putText(image,'hi noussa',(10,100),font,2,(0,0,255),2,cv2.LINE_AA)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
