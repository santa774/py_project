# coding:utf-8

import os
import PIL
import numpy
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
1.截取当前的屏幕
2.将截图写入坐标轴工具，方便计算2个点的坐标
3.分别点击起始坐标，结束坐标，得到2个坐标值
4.因为跳一跳的画面是斜着跳的，所以可以使用勾股定理计算出2点之间的距离
5.根据得到的距离计算出按压的时间
6.重新截图当前的屏幕
"""


def get_screen():
    """
    获取手机实时截图
    :return:
    """
    os.system('adb shell screencap -p /sdcard/jump1.png')
    os.system('adb pull /sdcard/jump1.png')
    return numpy.array(PIL.Image.open('jump1.png'))


def do_jump(point1, point2):
    """
    执行跳跃操作
    :param point1:
    :param point2:
    :return:
    """
    x1, y1 = point1
    x2, y2 = point2
    # 计算两点之间的长度
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    os.system('adb shell input swipe 320 410 320 410 %s' % str(int(distance * 2.13)))


def onclick(event, coor=[]):
    """
    在电脑上的坐标轴图片上执行点击操作
    :param event:
    :param coor:
    :return:
    """
    coor.append((event.xdata, event.ydata))
    print("x: " + str(event.xdata) + ", y: " + str(event.y))
    if len(coor) == 2:
        # 执行跳的动作
        do_jump(coor.pop(), coor.pop())
        global need_update
        need_update = True


def update_screen(frame):
    """
    刷新电脑上的坐标轴图片
    :param frame:
    :return:
    """
    print('update_screen' + str(update_count))
    global need_update
    if need_update:
        time.sleep(1)
        jump_show_image.set_array(get_screen())
        need_update = False
    return jump_show_image,


update_count = 0
need_update = False
jump_figure = plt.figure()
jump_show_image = plt.imshow(get_screen(), animated=True)
jump_figure.canvas.mpl_connect('button_press_event', onclick)
func_ani = FuncAnimation(jump_figure, update_screen, interval=1000, blit=True)
plt.show()
