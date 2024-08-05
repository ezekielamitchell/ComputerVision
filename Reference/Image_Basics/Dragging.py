import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

###############
## VARIABLES ##
###############

# true when button down; false when button up
drawing = False
ix, iy = -1, -1


###############
## FUNCTION ##
###############

def drawRect(event, x, y, flags, param):
    global ix, iy, drawing
    if event==cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event==cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.rectangle(img, (ix,iy), (x,y),(0,255,255),-1)

    elif event==cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img, (ix,iy), (0,255,255), -1)



#############################
## SHOWING IMAGE (OPENCV) ##
#############################

img = np.zeros(shape=(512,512,3))

cv.namedWindow(winname='Dragging')
cv.setMouseCallback('Dragging', drawRect)

while True:
    cv.imshow('Dragging', img)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()