import cv2
import easyocr
import matplotlib.pyplot as plt
import os

os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH", None)
image_path = './data/located_plates/cropped_image.png'

def get_text(image_path):
    
    image = cv2.imread(image_path)

    reader = easyocr.Reader(['en'], gpu=False)

    text_ = reader.readtext(image)
    message = ""

    for t in text_:
        bounding_box, text, score = t

        message += text + ' '

        top_left = tuple([int(val) for val in bounding_box[0]])
        bottom_right = tuple([int(val) for val in bounding_box[2]])
        
        if score > 0.25:
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
            cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_COMPLEX, 0.65, (0,0,255), 1)

    return message

message = get_text(image_path)
with open('./data/located_plates/license_plates.txt', 'w') as file:
    file.write(message + '\n')

