from time import sleep

from pynput.mouse import Controller
from win32gui import GetWindowText, GetForegroundWindow

import matplotlib.pyplot as plt
import numpy as np

mouse = Controller()
x,y=mouse.position
mouse.position=(x+500,y+500)

#定义X轴和Y轴
x = np.array([1,2,3])
y = np.array([1,2,3])
plt.plot(x,y)
plt.show()




while 1:
    print(GetWindowText(GetForegroundWindow()))
    sleep(1)




