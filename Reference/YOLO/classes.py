from ultralytics import YOLO
import time

model = YOLO('yolov8n.pt')
class_names = model.names

with open('classes.txt', 'w') as file:
    for class_id, class_name in class_names.items():
        file.write(f'{class_id}: {class_name}\n')

print("Possible class names and ids being added to classes.txt file")
time.sleep(1)
print("Possible class names and ids being added to classes.txt file..")
time.sleep(1)
print("Possible class names and ids being added to classes.txt file...")
time.sleep(2)
print("success... running program...")
time.sleep(2)
