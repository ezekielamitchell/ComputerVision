# required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from datasets import load_dataset
import os
import imutils
import easyocr

os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH", None)
data_set = load_dataset("charliexu07/license_plates_2")

train_data = data_set["train"]

first_image = train_data[0]['image']
first_label = train_data[0]['label']
second_image = train_data[1]['image']
second_label = train_data[1]['label']


