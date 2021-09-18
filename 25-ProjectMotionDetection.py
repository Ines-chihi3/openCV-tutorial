import cv2          
import numpy as np   

cap=cv2.VideoCapture('vtest.avi')

ret,frame1=cap.read()
ret,frame2=cap.read()


while cap.isOpened():
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    blur=cv2.GaussianBlur(gray,(3,3),0)

    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

    dilated=cv2.dilate(thresh,None,iterations=3)

    contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour in contours :
        (x,y,w,h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour)<700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"status : movement",(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv2.imshow('feed',frame1)

    frame1=frame2
    ret,frame2=cap.read()

    k=cv2.waitKey(1)
    if k==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()