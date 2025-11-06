import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# Mouse callback function - triggered on mouse events
# ============================================================================
def draw_circle(event, x, y, flags, params):
    # Left click draws white circle
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 15, (255,255,255), -1)

    # Right click draws green circle
    if event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), 15, (0,255,0), -1)


# Create window and connect mouse callback
cv.namedWindow(winname='frame')
cv.setMouseCallback('frame', draw_circle)

# ============================================================================
# Create blank canvas and display
# ============================================================================
# Create 512x512 black image with 3 color channels (BGR)
img = np.zeros(shape=(512,512,3))

while True:
    cv.imshow('frame', img)
    # waitKey(1) checks for key every 1ms - allows drawing to update smoothly
    if cv.waitKey(1) & 0xFF == ord('q'):
        # Save drawing before closing
        cv.imwrite('../test/data/test_img_02.jpg', img)
        break

cv.destroyAllWindows()