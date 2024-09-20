import cv2
from ultralytics import YOLO

# load YOLOv8 model
model = YOLO('yolov8n.pt')

# load video
image_path ='./data/image0.jpg'
video_path = './data/video1.mp4'
cap = cv2.VideoCapture(video_path)

# read video frame
while True:
    ret, frame = cap.read()

    if ret:
        # apply object detection method & track detected objects
        results = model.track(frame, persist=True)

        frame_ = results[0].plot() # plot results

        cv2.imshow('Find Dog', frame_) # visualize

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break