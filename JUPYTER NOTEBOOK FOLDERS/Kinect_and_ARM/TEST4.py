#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
from pykinect2 import PyKinectV2
from pykinect2 import PyKinectRuntime

# Initialize Kinect for color data
kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)

try:
    image_count = 0
    while image_count < 5:
        # Check for a new color frame
        if kinect.has_new_color_frame():
            color_frame = kinect.get_last_color_frame()
            color_image = color_frame.reshape((kinect.color_frame_desc.Height, kinect.color_frame_desc.Width, 4))
            color_image = cv2.cvtColor(color_image, cv2.COLOR_BGRA2RGB)

            # Manually swap red and blue channels
            color_image[:, :, [0, 2]] = color_image[:, :, [2, 0]]

            # Apply gamma correction to adjust brightness
            gamma = 0.7  # Adjust gamma value as needed (0.5 to 2.0)
            color_image_corrected = np.power(color_image / 255.0, gamma) * 255.0
            color_image_corrected = np.clip(color_image_corrected, 0, 255).astype(np.uint8)

            # Apply histogram equalization to adjust contrast
            color_image_equalized = cv2.cvtColor(color_image_corrected, cv2.COLOR_RGB2LAB)
            color_image_equalized[:, :, 0] = cv2.equalizeHist(color_image_equalized[:, :, 0])
            color_image_equalized = cv2.cvtColor(color_image_equalized, cv2.COLOR_LAB2RGB)

            # Save the color image
            image_filename = f"C:\\Users\\Anti\\Documents\\AI_ML_CLASS\\FINAL_TEST1\\KINECT\\color_image_{image_count}.jpg"
            cv2.imwrite(image_filename, color_image_equalized)
            print(f"Image {image_count + 1} saved.")

            # Increment the image count
            image_count += 1

except KeyboardInterrupt:
    print("Stream stopped.")

# Clean up
kinect.close()

