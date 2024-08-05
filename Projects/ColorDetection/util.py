import numpy as np
import cv2


def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Handle red hue wrap-around
    if hue >= 170:    # Modified upper threshold
        lowerLimit = np.array([hue - 15, 100, 100], dtype=np.uint8)  # Increased tolerance
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 10:    # Modified lower threshold
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 15, 255, 255], dtype=np.uint8)  # Increased tolerance
    else:
        lowerLimit = np.array([120, 50, 50], dtype=np.uint8)
        upperLimit = np.array([160, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit
