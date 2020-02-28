from pynput.mouse import Button, Controller
from pynput import mouse
import time

m = Controller()
print("Current mouse position {0}".format(m.position))

mouse.position = (10, 20)
print("Moved to {0}".format(m.position))

m.move(500, 500)


def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        listener.stop()


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
