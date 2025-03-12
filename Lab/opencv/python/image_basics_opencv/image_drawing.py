import cv2
import numpy as np

# create a blank image
blank_image = np.zeros((512,512,3))
cv2.rectangle(blank_image, pt1=(150,150), pt2=(350,400), color=(255,255,255), thickness=-1)
cv2.imshow("Blank Image", blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()