import cv2

# Load an image
data_set = '/home/ezekiel/Developer/ComputerVision/Lab/opencv/data/images/'
image = cv2.imread(data_set + 'image01.jpg')

# Check if image was loaded successfully
if image is None:
    print('Error: image not found')
else:
    print('Image loaded successfully')

    # Display the image
    cv2.imshow('Image', image)

    # Wait for a key press to close the window and exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()