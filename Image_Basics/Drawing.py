# Direct drawing on images with opencv
# callbacks

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

###############
## FUNCTION ##
###############

def drawCircle(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),10,(0,255,0),-1)

    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),10,(0,0,255))

cv.namedWindow(winname='Drawing0')
cv.setMouseCallback('Drawing0', drawCircle)



#############################
## SHOWING IMAGE (OPENCV) ##
#############################

img = np.zeros(shape=(512,512,3), dtype=np.int8)

while True:
    cv.imshow('Drawing0', img)

    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()