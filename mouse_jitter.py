import pyautogui
import random
import time
import sys

# Configure PyAutoGUI
pyautogui.FAILSAFE = True  # Move mouse to top-left corner to abort
pyautogui.PAUSE = 0.1  # Small pause between actions

def mouse_jitter():
    print("Mouse jitter started. Press Ctrl+C to stop.")
    try:
        while True:
            # Get current mouse position
            x, y = pyautogui.position()
            
            # Generate small random movement (-5 to +5 pixels)
            delta_x = random.randint(-5, 5)
            delta_y = random.randint(-5, 5)
            
            # Move mouse to new position
            pyautogui.moveTo(x + delta_x, y + delta_y, duration=0.2)
            
            # Wait before next jitter (e.g., 5 seconds)
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nMouse jitter stopped.")
        sys.exit(0)

if __name__ == "__main__":
    # Delay start to give time to focus on the terminal
    print("Starting mouse jitter in 3 seconds...")
    time.sleep(3)
    mouse_jitter()