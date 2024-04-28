#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import subprocess
from IPython.display import display
from PIL import Image

# Directory where the images are saved
input_directory = 'C:\\Users\\(YOU)\\Documents\\(YOUR DIR)\\FINAL_TEST1\\KINECT'

# Change the directory to the yolov5 directory
os.chdir('C:\\Users\\(YOU)\\Documents\\(YOUR DIR)\\FINAL_TEST1\\yolov5')

# Build the command for detection
command = [
    'python', 'detect.py',
    '--weights', 'runs/train/yolov5s_results/weights/best.pt',
    '--img', '416',
    '--conf', '0.25',
    '--source', input_directory,
    '--project', 'C:\\Users\\(YOU)\\Documents\\(YOUR DIR)\\FINAL_TEST1',
    '--name', 'PREDICT',
    '--exist-ok',
    '--device', 'cpu',  # Add this line to use CPU
    '--save-txt'
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
output_directory = 'C:\\Users\\(YOU)\\Documents\\(YOUR DIR)\\FINAL_TEST1\\PREDICT'

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


# In[5]:


get_ipython().system('python Untitled2.py')


# In[ ]:




