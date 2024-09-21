# required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
import easyocr
import os

os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH", None)

image = cv2.imread('./data/images/image_8.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()

bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
edge = cv2.Canny(bfilter, 30, 200)
# plt.imshow(cv2.cvtColor(edge, cv2.COLOR_BGR2RGB))
# plt.show()

try:
    key_points = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(key_points)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    location = None

    for contour in contours:
        approximate = cv2.approxPolyDP(contour, 10, True)
        if len(approximate) == 4:
            location = approximate
            break

    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], -1, 255, -1)
    new_image = cv2.bitwise_and(image, image, mask=mask)
except:
    print(f"error .... failure to locate license plate")


plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()