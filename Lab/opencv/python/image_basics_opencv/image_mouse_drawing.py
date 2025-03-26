# This program utilizes mouse callback to draw on images

# IMPORTS
import cv2
import numpy as np

# VARIABLES
## true when left button down
drawing = False
ix, iy = -1, -1

# FUNCTION
def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img,(ix,iy),(x,y), (256,256,256), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x, y), (256,256,256), -1)

# SHOW IMAGE

# BLACK
img = np.zeros(shape=(512,512,3))
winname = "mouse_drawing"
cv2.namedWindow(winname=winname)
cv2.setMouseCallback(winname, draw_rectangle)

while True:
    cv2.imshow(winname, img)
    if cv2.waitKey(1) & 0xFF==27: # esc key press
        break

cv2.destroyAllWindows()