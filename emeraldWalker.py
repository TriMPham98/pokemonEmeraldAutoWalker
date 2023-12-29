import pyautogui
import time

# Ensure the failsafe is enabled.
pyautogui.FAILSAFE = True

# Move the mouse to the specific coordinates and double click
pyautogui.moveTo(980, 420)
pyautogui.doubleClick()

while True:
    # Hold down the 'Up' arrow key
    pyautogui.keyDown('up')
    time.sleep(0.5)  # Keep the key pressed for half a second
    pyautogui.keyUp('up')  # Release the 'Up' arrow key

    # Hold down the 'Down' arrow key
    pyautogui.keyDown('down')
    time.sleep(0.5)  # Keep the key pressed for half a second
    pyautogui.keyUp('down')  # Release the 'Down' arrow key
