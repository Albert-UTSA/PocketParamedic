#!/usr/bin/env python
# coding: utf-8

# In[1]:


import serial
import time
import os  # Import the os module

# Setup serial connection
ser = serial.Serial('COM6', 115200, timeout=1)

def send_command(command, delay=0.2):
    """Send a command to the robot arm via serial and wait for it to complete."""
    print("Sending command:", command)
    ser.write((command + '\n').encode())
    time.sleep(delay)  # Delay to allow the command to be executed

def check_and_run_robot(file_path):
    """Check if a specific file exists and run robot commands if it does."""
    while(True):
        if os.path.exists(file_path):
            #print("File exists, running robot commands.")
            break
        #else:
            #print("File does not exist. Skipping robot commands.")
        time.sleep(1)
    run_robot_commands()

def run_robot_commands():
    """Container for robot commands to be executed."""
    try:
        # Initial reset to home position
        send_command("RESET")
        
        send_command("MOVE Z -20")
        send_command("MOVE Z -20")
        send_command("MOVE Z -20")
        send_command("MOVE Z -20")
        send_command("MOVE Z -20")
        send_command("MOVE Z -20")
        send_command("MOVE Z -20")
        send_command("MOVE Z -10")
        send_command("MOVE Z -5")
        send_command("MOVE Z -5")
        send_command("NOZZLE ON")
        send_command("MOVE Z 20")
        send_command("MOVE Z 20")
        send_command("MOVE Z 20")
        send_command("MOVE Z 20")
        send_command("MOVE Z 20")
        send_command("MOVE Z 20")
        send_command("MOVE Z 20")
        send_command("MOVE Z 10")
        send_command("MOVE Z -20")
        send_command("MOVE X 20")
        send_command("MOVE X 20")
        send_command("MOVE Z -20")
        send_command("MOVE X 20")
        send_command("MOVE X 20")
        send_command("MOVE Z -20")
        send_command("MOVE Z -20")
        send_command("MOVE X 20")
        send_command("MOVE X 20")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("MOVE Z -2")
        send_command("RESET")
    finally:
        ser.close()  # Ensure the serial port is closed regardless of errors

if __name__ == "__main__":
    file_path = r"C:\Users\Anti\Documents\AI_ML_CLASS\FINAL_TEST1\PREDICT\labels\color_image_0.txt"
    check_and_run_robot(file_path)


# In[ ]:




