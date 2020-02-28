from mss.darwin import MSS as mss
import numpy as np

monitor = {"top": 250, "left": 15, "width": 1150, "height": 1235}

with mss() as sct:
    screen = np.array(sct.grab(monitor))
    for y in range(100):
        for x in range(100):
            print(x + 15, y + 250)
            print(screen[x][y][0], screen[x][y][1], screen[x][y][2])
