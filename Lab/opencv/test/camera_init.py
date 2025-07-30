# Turns on the device default video camera -- press 'q' key for exit

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Initialize video capture
cap = cv.VideoCapture(0)

# Check if camera is opened
if not cap.isOpened():
    print("Error: failure to init camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failure to recieve frame")
        break

    # Display (flipped) frame
    cv.imshow("Test_Frame", cv.flip(frame, 1))

    # Press 'q' to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture and destroy window
cap.release()
cv.destroyAllWindows()