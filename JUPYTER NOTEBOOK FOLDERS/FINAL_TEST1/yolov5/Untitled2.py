#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os
import time
import subprocess
from IPython.display import display
from PIL import Image

# Create the directory if it does not exist
output_directory = 'C:\\Users\\(YOU)\\Documents\\AI_ML_CLASS\\FINAL_TEST1\\TEST'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Directory created at {output_directory}")
else:
    print(f"Directory already exists at {output_directory}")

def take_photos(output_directory, num_photos=9, delay=1):
    cap = cv2.VideoCapture(0)  # Open the default camera
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    try:
        for i in range(num_photos):
            ret, frame = cap.read()  # Capture frame-by-frame
            if ret:
                time.sleep(delay)  # Delay between photos
                image_path = f"{output_directory}\\image_{i + 1}.jpg"
                cv2.imwrite(image_path, frame)
                print(f"Saved image {i + 1} to {image_path}")
            else:
                print("Failed to capture image")
                break
    finally:
        cap.release()  # Release the camera
        print("Camera released")

# Take photos using the camera
take_photos(output_directory)

# Change the directory to the yolov5 directory
os.chdir('C:\\Users\\(YOU)\\Documents\\AI_ML_CLASS\\FINAL_TEST1\\yolov5')

# Build the command for detection

command = [
    'python', 'detect.py',
    '--weights', 'runs/train/yolov5s_results/weights/best.pt',
    '--img', '416',
    '--conf', '0.25',
    '--source', output_directory,
    '--project', 'C:\\Users\\(YOU)\\Documents\\AI_ML_CLASS\\FINAL_TEST1',
    '--name', 'PREDICT',
    '--exist-ok',
    '--device', 'cpu'  # Add this line to use CPU
]


# Execute the command using subprocess to capture output
result = subprocess.run(command, capture_output=True, text=True)
print("Standard Output:", result.stdout)
print("Error Output:", result.stderr)
if result.returncode != 0:
    print("Detection script failed with return code:", result.returncode)
else:
    print("Detection completed successfully.")

# Directory where the detected images are saved
output_directory = 'C:\\Users\\(YOU)\\Documents\\AI_ML_CLASS\\FINAL_TEST1\\PREDICT'

# Check for the presence of jpg images in the output directory
images = [os.path.join(output_directory, img) for img in os.listdir(output_directory) if img.endswith('.jpg')]

# Display images
if not images:
    print("No images found in the predict directory.")
else:
    for img_path in images:
        print(f"Displaying image {img_path}")
        img = Image.open(img_path)
        display(img)


# In[ ]:




