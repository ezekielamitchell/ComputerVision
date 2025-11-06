import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# Global variables for tracking mouse state
# ============================================================================
drawing = False  # True when mouse button is held down
ix = -1  # Initial x position
iy = -1  # Initial y position


# ============================================================================
# Mouse callback function for drawing rectangles and circles
# ============================================================================
def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing

    # Mouse button pressed - start drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # Mouse moving while button held - draw live rectangle
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)

    # Mouse button released - finish rectangle
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)

    # Right click draws magenta circle
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), 10, (255,0,255), 3)


# ============================================================================
# Setup and display
# ============================================================================
# Create blank 512x512 canvas
img = np.zeros(shape=(512,512,3))

# Connect mouse events to drawing function
cv.namedWindow('frame')
cv.setMouseCallback('frame', draw_rectangle)

while True:
    cv.imshow('frame', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        # Save before closing
        cv.imwrite('../test/data/test_img_03.jpg', img)
        break

cv.destroyAllWindows()