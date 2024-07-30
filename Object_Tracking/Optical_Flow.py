import cv2
import numpy as np
import matplotlib.pyplot as plt

# Parameters for corner detection: detect up to 10 corners with a quality level of 0.3,
# a minimum distance of 7 pixels between corners, and a block size of 7 pixels
corner_tracking_params = dict(maxCorners=5, qualityLevel=0.3, minDistance=7, blockSize=7)

# Parameters for Lucas-Kanade optical flow: window size of 200x200 pixels, a maximum pyramid level of 2,
# and termination criteria of 10 iterations or an epsilon of 0.03
lk_params = dict(winSize=(200, 200), maxLevel=4, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Initialize video capture from the webcam
cap = cv2.VideoCapture(0)
ret, prev_frame = cap.read()
prev_frame = cv2.flip(prev_frame, 1)  # Flip the frame horizontally

# Convert the first frame to grayscale
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Detect the top 10 corners in the first frame
prevPts = cv2.goodFeaturesToTrack(prev_gray, mask=None, **corner_tracking_params)

# Create an empty mask image for drawing lines
mask = np.zeros_like(prev_frame)

while True:
    # Capture a new frame from the webcam
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale

    # Calculate the optical flow from the previous frame to the current frame
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, frame_gray, prevPts, None, **lk_params)

    # Select good points (where status is 1)
    good_new = nextPts[status == 1]
    good_prev = prevPts[status == 1]

    # Draw lines and circles to visualize the optical flow
    for i, (new, prev) in enumerate(zip(good_new, good_prev)):
        x_new, y_new = new.ravel()
        x_prev, y_prev = prev.ravel()

        # Draw a white line from the previous point to the new point
        cv2.line(mask, (int(x_new), int(y_new)), (int(x_prev), int(y_prev)), (255, 255, 255), 3)

        # Draw a white circle at the new point
        frame = cv2.circle(frame, (int(x_new), int(y_new)), 8, (255, 255, 255), -1)

    # Combine the frame with the mask to display the lines and circles on the frame
    img = cv2.add(frame, mask)
    cv2.imshow('Tracking', img)  # Show the frame with the optical flow visualization

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

    # Update the previous frame and points for the next iteration
    prev_gray = frame_gray.copy()
    prevPts = good_new.reshape(-1, 1, 2)

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
