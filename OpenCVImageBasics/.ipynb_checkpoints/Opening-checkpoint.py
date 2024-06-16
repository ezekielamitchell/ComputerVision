import cv2 as cv
img = cv.imread('/OpenCVImageBasics/tester1.jpg')

while True:
    cv.imshow("Ezekiel's Puppy", img)

    # if waited at least (1) ms & pressed escape key
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()