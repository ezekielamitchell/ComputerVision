## IMPORTS
import cv2
import numpy as np

# VARIABLES
## True when mouse button DOWN, False while mouse button UP
drawing = False
ix = -1 
iy = -1


# FUNCTION
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y # catch where mouse is located
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(image, (ix,iy), (x,y), (0,255,255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(image, (ix,iy), (x,y), (0,255,255), -1)

# SHOW IMAGE
image = np.zeros((512,512,3))
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_rectangle)

while True:
    cv2.imshow('my_drawing', image)
    if cv2.waitKey(1) & 0xFF==27:
        break

cv2.destroyAllWindows()