import pyautogui
import time

# Ensure the failsafe is enabled.
pyautogui.FAILSAFE = True

# Move the mouse to the specific coordinates and double click
pyautogui.moveTo(1269, 775)
pyautogui.doubleClick()

while True:
    # Hold down the 'A' key
    pyautogui.keyDown('a')
    time.sleep(0.5)  # Keep the key pressed for half a second
    pyautogui.keyUp('a')  # Release the 'A' key

    # Hold down the 'D' key
    pyautogui.keyDown('d')
    time.sleep(0.5)  # Keep the key pressed for half a second
    pyautogui.keyUp('d')  # Release the 'D' key
