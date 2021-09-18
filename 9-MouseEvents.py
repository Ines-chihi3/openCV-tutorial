
#how to llist all event in cv2
import cv2
""" 
how to get event list :

event=[i for i in dir(cv2) if "EVENT" in i]
print(event)
output :
['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
"""


def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        textXY=str(x)+','+str(y)
        cv2.putText(img,textXY,(x,y),font,.5,(0,255,255),1)
        cv2.imshow('image',img)
    elif event==cv2.EVENT_RBUTTONDOWN:
        blue=img[x,y,0] 
        green=img[x,y,1]
        red=img[x,y,2]  
        font=cv2.FONT_HERSHEY_SIMPLEX
        textBGR=str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,textBGR,(x,y),font,.5,(255,255,0),1)
        cv2.imshow('image',img)

img=cv2.imread('HappyFish.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click)
cv2.waitKey(0)
cv2.destroyAllWindows()