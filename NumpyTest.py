import numpy as np
import time
from PIL import ImageGrab
from PIL import Image
from mss.darwin import MSS as mss
from cv2 import cv2
from pynput.mouse import Button, Controller
from collections import deque

# Plays mouseaccuracy.com test
# Left side of screen
monitor = {"top": 250, "left": 15, "width": 1250, "height": 1235}

m = Controller()
avoid = deque()
click_count = 0


def should_avoid(x, y):
    for c in avoid:
        if abs(x - c[0]) < 10 and abs(y - c[1]) < 10:
            return True
    return False


def clicker_bot(screen):
    global click_count
    for y in range(0, 1249, 5):
        for x in range(0, 1234, 10):
            if 75 < screen[x][y][2] < 100 and 150 < screen[x][y][1] < 177 and screen[x][y][0] > 240 and not should_avoid(x, y):
                print(avoid, x, y)
                avoid.append([x, y, time.time()])
                m.position = (y + 15, x + 250)
                m.click(Button.left, 1)
                click_count += 1
                return


while True:
    mouse_pos = m.position
    if mouse_pos[0] <= 1280:
        break


with mss() as sct:
    while True:
        for c in avoid:
            if time.time() - c[2] > 0.5:
                avoid.remove(c)
                break
        mouse_pos = m.position
        if 15 <= mouse_pos[0] <= 1280:
            screen = np.array(sct.grab(monitor))
            clicker_bot(screen)
        else:
            break

print(click_count)
