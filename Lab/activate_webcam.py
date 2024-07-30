##### SETUP #####
import cv2 as cv
vid = cv.VideoCapture(0)
##### BUILD #####
while (True):
    ret, frame = vid.read() # read frame
    cv.imshow('frame', frame) # display frame

    if cv.waitKey(1) & 0xFF == ord('q'):
        break ## break once esc key is pressed

vid.release() # release cap object
cv.destroyAllWindows()