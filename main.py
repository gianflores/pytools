from time import sleep
import math
from clicknium import clicknium as cc


def circle():
    a, b = cc.mouse.position()
    w = 20
    m = (2 * math.pi) / w
    r = 200

    while 1:
        for i in range(0, w + 1):
            x = int(a + r * math.sin(m * i))
            y = int(b + r * math.cos(m * i))
            cc.mouse.move(x, y)
            sleep(0.2)


if __name__ == "__main__":
    circle()

# import pyautogui
# import time

# while True:
#     pyautogui.click(x=100, y=100)
#     pyautogui.press("enter")
#     time.sleep(5)
#     pyautogui.click(x=200, y=200)
#     pyautogui.press("enter")
#     time.sleep(5)
