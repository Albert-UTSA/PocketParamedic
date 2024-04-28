#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import serial
import time

# Setup serial connection
ser = serial.Serial('COM6', 115200, timeout=1)

def send_command(command, delay=0.2):
    """Send a command to the robot arm via serial and wait for it to complete."""
    print("Sending command:", command)
    ser.write((command + '\n').encode())
    time.sleep(delay)  # Delay to allow the command to be executed

def draw_diagonal_line(steps, step_size):
    """Draw a diagonal line by moving X positively and Y negatively."""
    for _ in range(steps):
        send_command(f"MOVE X {step_size}")   # Move positively on X axis
        send_command(f"MOVE Y {-step_size}")  # Move negatively on Y axis

if __name__ == "__main__":
    try:
        # Initial reset to home position
        send_command("RESET")
        
        # Commands extracted from the image and translated to serial commands
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
      

        # Assuming you end the sequence with a RESET command
        send_command("RESET")
      
    finally:
        ser.close()  # Ensure the serial port is closed regardless of errors

