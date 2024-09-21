import os
import cv2
import numpy as np
from datasets import load_dataset

## ---> pull dataset
os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH", None)
data_set = load_dataset("keremberke/license-plate-object-detection", "full")

train_data = data_set["train"]

## ---> save the first 10 images from the dataset to the repo
if not os.path.exists('./data/images'):
    os.makedirs('./data/images')

for i, image in enumerate(train_data[:10]['image']):
    image_name = f'image_{i+1}.png'
    image_path = f'./data/images/{image_name}'
    image_np = np.array(image)  # Convert to numpy array
    cv2.imwrite(image_path, cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))  # Convert RGB to BGR for saving
    print(f'Saved {image_name}')
