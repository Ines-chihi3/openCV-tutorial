import cv2          
 
cap=cv2.VideoCapture('vtest.avi')

while cap.isOpened():
    ret,frame=cap.read()
    cv2.imshow('video',frame)
    k=cv2.waitKey(100)
    if k==ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
