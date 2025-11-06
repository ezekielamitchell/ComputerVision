"""
Section 3: Image Basics with OpenCV

Topics covered:
- Introduction to Images and OpenCV Basics
- Opening Image files in a notebook
- Opening Image files with OpenCV
- Drawing on Images - Part One - Basic Shapes
- Drawing on Images Part Two - Text and Polygons
- Direct Drawing on Images with a mouse - Part One
- Direct Drawing on Images with a mouse - Part Two
- Direct Drawing on Images with a mouse - Part Three
- Image Basics Assessment
- Image Basics Assessment Solutions
"""

import cv2 as cv
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

# Load image from file path
img = cv.imread('../data/00-puppy.jpg')

print('image located')
sleep(1)
print('loading....')
sleep(1)

# Note: OpenCV loads images in BGR format by default
# Use cv.cvtColor(img, cv.COLOR_BGR2RGB) to convert for matplotlib
# fixed_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Single display method (waits for any key)
# cv.imshow('frame-0', img)
# cv.waitKey(0)

# Display image in window until 'q' is pressed
while True:
    cv.imshow('frame_00', img)
    # waitKey(0) waits indefinitely for key press
    # 0xFF masks to get last 8 bits for key comparison
    if cv.waitKey(0) & 0xFF == ord('q'):
        print('break')
        break

# Close all OpenCV windows
cv.destroyAllWindows()