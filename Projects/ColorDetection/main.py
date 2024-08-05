import cv2
import numpy as np
from util import get_limits

cap = cv2.VideoCapture(0)

# BGR color values
orange = [0, 128, 255]
yellow = [0,0,0]
purple = [140,0,128]

while True:
    ret, frame = cap.read()
    if not ret:
        print('error accessing camera')
        quit

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_limit, upper_limit = get_limits(purple)

    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

    print("Number of white pixels in mask:", cv2.countNonZero(mask))
    # if cv2.countNonZero(mask) > 0:
    #     x, y = np.where(mask == 255)[1][0], np.where(mask == 255)[0][0]  # Find one white pixel
    #     print("HSV values at a orange pixel:", hsvImage[y, x])

    # Countours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y,),(x+w,y+h),(0,255,0),2)

    cv2.imshow('Color Detector', cv2.flip(frame,2)) # display with flipped POV
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()