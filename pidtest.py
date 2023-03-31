import os
import time

import pynput
from pynput.mouse import Button
from matplotlib import pyplot as plt
from simple_pid import PID
import ctypes
import os
import pynput
import winsound
from pynput.keyboard import Key, Listener,KeyCode

lock = False
try:
    root = os.path.abspath(os.path.dirname(__file__))+'\logitech.driver.dll'
    print(root)
    driver = ctypes.CDLL(root)
    ok = driver.device_open() == 1  # 该驱动每个进程可打开一个实例
    if not ok:
        print('Error, GHUB or LGS driver not found')
except FileNotFoundError:
    print(f'Error, DLL file not found')

def mouse(lock):

    def down(x, y, button, pressed):
        if button == Button.left:
            lock = pressed

    with pynput.mouse.Listener(on_click=down) as m:
        m.join()


def keyboard(lock):

    def press(key):

        if key == Key.shift:
            lock=True

    def release(key):

        if key == Key.shift:
            lock = False
    with Listener(on_release=release, on_press=press) as k:
        k.join()

def loop(lock):

    def move(x: int, y: int):
        if (x == 0) & (y == 0):
            return
        driver.moveR(x, y, True)

    a = point(500.0, 600.0)

    pidx = PID(120000000, 0, 0, setpoint=0)
    pid.output_limits = (0, None)
    while True:
        x=a.x-b.x
        y=b.y-b.y
        if lock:
            p = -pidx(x * x + y * y)
            px = p * x
            py = p * y
            move(px, py)

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


if __name__ == '__main__':
    # 将创建的模型写进主函数


    # 设置PID的三个参数，以及限制输出


    a = point(500.0,600.0)
    b = point(200.0,900.0)
    #print(a.x+b.x)
    jl = (b.x-a.x)*(b.x-a.x)+(b.y-a.y)*(b.y-a.y)
    #print(jl)
    pid = PID(120000000, 0, 0, setpoint=0)
    pid.output_limits = (0, None)
    # 用于设置时间参数
    start_time = time.time()
    last_time = start_time
    # 用于输出结果可视化
    setpoint, y, x = [], [], []
    i=5
    # 设置系统运行时间
    while i > 1:
        i=i-1
        # 设置时间变量dt
        current_time = time.time()
        dt = (current_time - last_time)

        # 变量temp在整个系统中作为输出，变量temp与理想值之差作为反馈回路中的输入，通过反馈回路调节变量power的变化。


        jl=(b.x-a.x)*(b.x-a.x)+(b.y-a.y)*(b.y-a.y)
        #print(jl)
        p = -pid(jl)
        #print(p)
        b.x+=(b.x-a.x)*p
        b.y+=(b.y-a.y)*p
        print(b.x,b.y)
        #print(b.x)
       # print(b.y)
        #print(p)
        #print("--")
        # 用于输出结果可视化
        x += [current_time - start_time]
        y += [jl]
        setpoint += [pid.setpoint]
        # 用于变量temp赋初值
        if current_time - start_time > 0:
            pid.setpoint = 0

        last_time = current_time
            # 输出结果可视化

    plt.plot(x, setpoint, label='target')
    plt.plot(x, y, label='PID')
    plt.xlabel('time')
    plt.ylabel('temperature')
    plt.legend()
    plt.show()
