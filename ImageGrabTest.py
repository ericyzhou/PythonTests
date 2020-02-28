from PIL import ImageGrab as ig
from PIL import Image as image
from PIL import ImageOps as io
import numpy as np


parse_size = 6
# Image -> ASCII art
# Copy image to clipboard
im = ig.grabclipboard()
im = im.rotate(90, image.NEAREST, 1, None, None, None)
im = io.flip(im)

for x in range(0, im.size[0], parse_size):
    for y in range(0, im.size[1], parse_size):
        if im.getpixel((x, y))[0] < 25 and im.getpixel((x, y))[1] < 25 and im.getpixel((x, y))[2] < 25:
            print(" ", end=" ")
        elif im.getpixel((x, y))[0] < 50 and im.getpixel((x, y))[1] < 50 and im.getpixel((x, y))[2] < 50:
            print(".", end=" ")
        elif im.getpixel((x, y))[0] < 75 and im.getpixel((x, y))[1] < 75 and im.getpixel((x, y))[2] < 75:
            print(":", end=" ")
        elif im.getpixel((x, y))[0] < 100 and im.getpixel((x, y))[1] < 100 and im.getpixel((x, y))[2] < 100:
            print("-", end=" ")
        elif im.getpixel((x, y))[0] < 125 and im.getpixel((x, y))[1] < 125 and im.getpixel((x, y))[2] < 125:
            print("=", end=" ")
        elif im.getpixel((x, y))[0] < 150 and im.getpixel((x, y))[1] < 150 and im.getpixel((x, y))[2] < 150:
            print("+", end=" ")
        elif im.getpixel((x, y))[0] < 175 and im.getpixel((x, y))[1] < 175 and im.getpixel((x, y))[2] < 175:
            print("*", end=" ")
        elif im.getpixel((x, y))[0] < 200 and im.getpixel((x, y))[1] < 200 and im.getpixel((x, y))[2] < 200:
            print("#", end=" ")
        elif im.getpixel((x, y))[0] < 225 and im.getpixel((x, y))[1] < 225 and im.getpixel((x, y))[2] < 225:
            print("%", end=" ")
        else:
            print("@", end=" ")

        # if im.getpixel((x, y))[0] > im.getpixel((x, y))[1] and im.getpixel((x, y))[0] > im.getpixel((x, y))[2]:
        #     print("+", end=" ")
        # elif im.getpixel((x, y))[1] > im.getpixel((x, y))[0] and im.getpixel((x, y))[1] > im.getpixel((x, y))[2]:
        #     print("-", end=" ")
        # elif im.getpixel((x, y))[2] > im.getpixel((x, y))[1] and im.getpixel((x, y))[2] > im.getpixel((x, y))[0]:
        #     print("*", end=" ")
        # else:
        #     print(" ", end=" ")
    print()
