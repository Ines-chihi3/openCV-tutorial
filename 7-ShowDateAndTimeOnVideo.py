import cv2          
import datetime           
cap=cv2.VideoCapture(0)
while(cap.isOpened()): 
    ret,frame=cap.read()  
    if ret == True :
        font=cv2.FONT_HERSHEY_SIMPLEX
        TEXT =str(datetime.datetime.now())
        frame= cv2.putText(frame,TEXT,(20,100),font,1,(0,255,255),1,cv2.LINE_AA)
        cv2.imshow('videoCam',frame)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()