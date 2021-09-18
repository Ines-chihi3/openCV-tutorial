#ROI notion
"""
ROI : region of interrest  : when yyou wannt to work with specific part of image (face ..)

ma 3nhza f cas ili t7ib te5dem 3ala zone mou3ayna ..
il exercice bch ykoun 3andik une uimage feha player w koura bch t7awel il koura mil blasaa li blasa

"""
"""
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        textXY=str(x)+','+str(y)
        cv2.putText(img,textXY,(x,y),font,.5,(0,255,255),1)
        cv2.imshow('image',img)
"""
# bch n5arej bih il x,y de la ball
"""
#read the image
import cv2
import numpy as np
img=cv2.imread('PlayerBall.jpg')
#cv2.imshow('image',img)
#cv2.setMouseCallback('image',click)

#determiner les cordonnees de la ballle 
#sta3malt l event mouse click : cordonne de la ball (193,124)(222,146)
#nouvell pos 77,102   111,125
#tawa bch ndefini il ball bch ngoulou kif ngoulik ball ya3i il balsaa ili mawjouda f les cor hedhouma
ball=img[124:146,193:222]
#b3d bch naffecti l blasa mou3ana mil image il ball 
img[106:133,75:112]=ball
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
hedhe nal9eh f stackoverflow
-------------------------------------------
|                                         | 
|    (x1, y1)      w                      |
|      ------------------------           |
|      |                      |           |
|      |                      |           | 
|      |         ROI          | h         |  
|      |                      |           |   
|      |                      |           |   
|      |                      |           |       
|      ------------------------           |   
|                           (x2, y2)      |    
|                                         |             
|                                         |             
|                                         |             
-------------------------------------------
Consider (0,0) as the top-left corner of the image with left-to-right as the x-direction and top-to-bottom as the y-direction. If we have (x1,y1) as the top-left and (x2,y2) as the bottom-right vertex of a ROI, we can use Numpy slicing to crop the image with:

ROI = image[y1:y2, x1:x2]
"""

#mafhemthc alech mamchech zah e pourtant code shih..bn lawejt f google..taw nzid nlawej mch mochkil

