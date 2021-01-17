# https://pyautogui.readthedocs.io/en/latest/
#uu
import pyautogui
import time

import keyboard
import sys



MAX_TIME_M = 35

DOING_POINT_FINDING = False
USING_MOTO_X4 = True

# Replay, Next, Auto
MOTO_G7_POINTS = [(812, 846), (1146, 962), (1101, 117)]
MOTO_X4_POINTS =  [(789, 884), (1190, 958), (1127, 66)]

points = MOTO_G7_POINTS
if USING_MOTO_X4:
    points = MOTO_X4_POINTS

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print(screenHeight)
print(screenWidth)
start_time = time.time()
while True:
    time.sleep(0.5)
    if DOING_POINT_FINDING:
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        print("({:2}, {:2})".format(currentMouseX, currentMouseY))
        continue

    if keyboard.is_pressed(' '):
        print('Exit')
        sys.exit()

    pyautogui.moveTo(points[0][0], points[0][1], duration=.25, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.moveTo(points[1][0], points[1][1], duration=.25, tween=pyautogui.easeInOutQuad)
    pyautogui.click()

    # pyautogui.moveTo(1639, 678, duration=.25, tween=pyautogui.easeInOutQuad)
    # pyautogui.click()
    # time.sleep(0.5)
    # pyautogui.click()

    pyautogui.moveTo(points[2][0], points[2][1], duration=.25, tween=pyautogui.easeInOutQuad)
    pyautogui.click()

    elapsed_time_min = (time.time() - start_time) / 60
    print(elapsed_time_min)
    if elapsed_time_min > MAX_TIME_M:
        break
#
# pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.
#
# pyautogui.click()          # Click the mouse.
# pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
# pyautogui.click('button.png') # Find where button.png appears on the screen and click it.
#
# pyautogui.move(0, 10)      # Move mouse 10 pixels down from its current position.
# pyautogui.doubleClick()    # Double click the mouse.
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
#
# pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES
#
# pyautogui.keyDown('shift') # Press the Shift key down and hold it.
# pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key 4 times.
# pyautogui.keyUp('shift')   # Let go of the Shift key.
#
# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
#
# pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.
