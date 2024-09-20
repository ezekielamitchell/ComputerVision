import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt') # load YOLOv8 model

class_names = model.names # model classes

dog_class_id = class_names.index('dog') if 'dog' in class_names else None

if dog_class_id is not None:
    image_path ='./data/image0.jpg' 
    video_path = './data/video0.mp4'
    cap = cv2.VideoCapture(video_path) # load video

    while True: # read video frame
        ret, frame = cap.read()

        if ret:
            # apply object detection method & track detected objects
            results = model.track(frame, persist=True)

            for result in results: # filter results to only include 'dog' detections
                result.boxes = result.boxes.cpu() # move boxes to CPU for filtering
                result.boxes = result.boxes[result.boxes.cls==dog_class_id]

            frame_ = results[0].plot()

            cv2.imshow('Find Dog', frame_) # visualize

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
else:
    print("error locating 'dog' class")