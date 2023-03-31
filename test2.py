import numpy as np
import pyautogui
import cv2

from mss import mss

from PIL import Image

mon = {'top': 160, 'left': 160, 'width': 200, 'height': 200}

sct = mss()

import win32api,win32con

print(win32api.GetSystemMetrics(win32con.SM_CXSCREEN))#获得屏幕分辨率X轴

win32api.GetSystemMetrics(win32con.SM_CYSCREEN)   #获得屏幕分辨率Y轴

while 1:
    img = pyautogui.screenshot(region=[960 - 320, 540 - 320, 960 + 320, 540 + 320])  # x,y,w,h
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)  # cvtColor用于在图像中不同的色彩空间进行转换,用于后续处理。
    cv2.imshow('show',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()