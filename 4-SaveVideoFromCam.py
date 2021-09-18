#create VideoCapture object 
import cv2
cap=cv2.VideoCapture(0)
        
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('out.avi',fourcc,20.0,(640,480))

while(True):
    ret,frame=cap.read()
    if ret== True :
        out.write(frame)
        cv2.imshow('videoCam',frame)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
    else :
        break
cap.release()
out.release()
cv2.destroyAllWindows()
