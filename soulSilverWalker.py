import pyautogui
import time

# Ensure the failsafe is enabled.
pyautogui.FAILSAFE = True

# Move the mouse to the specific coordinates and double click
pyautogui.moveTo(1275, 420)
pyautogui.doubleClick()

while True:
    # Hold down the 'Up' arrow key
    pyautogui.keyDown('up')
    time.sleep(3)  # Keep the key pressed for 3 seconds
    pyautogui.keyUp('up')  # Release the 'Up' arrow key

    # Hold down the 'Down' arrow key
    pyautogui.keyDown('down')
    time.sleep(3)  # Keep the key pressed for 3 seconds
    pyautogui.keyUp('down')  # Release the 'Down' arrow key
