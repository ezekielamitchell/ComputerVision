import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def generate_image():
    data_set = '/home/ezekiel/Developer/ComputerVision/Lab/opencv/data/images/'
    img = cv.imread(data_set + 'image04.jpg')

    if img is None:
        print('Error: image not found')
    else:
        cv.cvtColor(img, cv.COLOR_BGR2RGB) # BGR -> RGB color mapping
        while True:
            cv.imshow('Image', img) # show image
            if cv.waitKey(1) & 0xFF==27: # close img using esc key
                break
        cv.destroyAllWindows() # destroy image windows

if __name__ == '__main__':
    generate_image()