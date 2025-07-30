# Take a snapsot via default device camera

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cap = cv.VideoCapture(0)

cv.waitKey(1000)

if not cap.isOpened():
    print('error: failure captuing camera')
    exit()

ret, frame = cap.read()

if ret:

    # Display (flipped) snapshot
    flipped_frame = cv.flip(frame, 1)
    cv.imshow('Snapshot', flipped_frame)

    # Save snapshot
    cv.imwrite('snapshot.jpg', flipped_frame)
    print("snapshot saved as 'snapshot.jpg'")
else:
    print('error: failure to capture snapshot')

cv.waitKey(0)
cv.destroyAllWindows()
cap.release
