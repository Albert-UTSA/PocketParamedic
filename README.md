# Pocket Paramedic

Pocket Paramedic is a groundbreaking new piece of technology that detects a cut or scrape and uses a robotic arm to place a bandaid on the wound.

# Tools
- Pocket Paramedic placemat
- Robotic Arm (insert specific version here)

## Usage
- Download all files.
- To start the arm, run `AI_ARM_FINALv3.py` in `JUPYTER NOTEBOOK FOLDERS/ROBOT_ARM`.
- Then run `TEST4.py` in `JUPYTER NOTEBOOK FOLDERS/Kinect_and_ARM` to start the image sensor. Ensure to promptly place the wound in front of the camera. If having troubles detecting the cut, try adding more lighting. A flashlight nearby should suffice. After running, 5 images should be saved in a folder called `JUPYTER NOTEBOOK FOLDERS/FINAL_TEST1/KINECT`.
- Ensure that the wound is placed in the "wound box" on the placemat. Next, run `FINAL_TEST3.py` in `JUPYTER NOTEBOOK FOLDERS/FINAL_TEST1/yolo5` which runs the yolo model to detect cuts. If a cut is detected, the movement function will be triggered in AI_ARM_FINALv3.py.

## Demo Video
Click to be redirected to youtube. \\
[![Demo Vidoe](https://img.youtube.com/vi/kCZSegzI_90/0.jpg)](https://www.youtube.com/watch?v=kCZSegzI_90)
