import cv2
import time
import platform

# Callback Functions
def draw_circle(event, x, y, flags, params):
    global center, clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x,y)
        clicked = False
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

# Nothing drawn yet
center = (0,0)
clicked = False

# Capture video
cap = cv2.VideoCapture(2)
cv2.namedWindow('Frame')

# Binding
cv2.setMouseCallback('Frame', draw_circle)

while True:
    ret, frame = cap.read()
    if not ret: break

    if clicked:
        cv2.circle(frame, center, radius=50, color=(0,0,255), thickness=3)
    
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

