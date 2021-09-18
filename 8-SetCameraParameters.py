import cv2
#cv2.CAP_PROP_FRAME_WIDTH  : 3
#cv2.CAP_PROP_FRAME_HEIGHT  : 4
cap=cv2.VideoCapture(0)
#afficher la resolution par defaut
print(cap.get(3))
print(cap.get(4))
#set parameter
cap.set(3,352)
cap.set(4,288)
#afficher les nouveau parametre
print(cap.get(3))
print(cap.get(4))
while(True):
    ret,frame=cap.read()
    cv2.imshow('videoCam',frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
