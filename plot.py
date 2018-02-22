# coding:utf-8
# 補助ライブラリ：データのプロット用

import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plotdata(data):
    plt.plot(data)
    plt.show()  # IDLEでは必要。Jupyterでは要らないと思われる。

def histgram_plot(data):
    plt.hist(data)
    plt.show()

def image_show(data):
    picture = plt.imshow(data)
    plt.show()
    return picture

def animation_show(data):
    fig = plt.figure()
    a = []
    for i in range(0,len(data)):
        a.append([plt.imshow(data[i], origin='lower')])
    ani = animation.ArtistAnimation(fig, a, interval=500)
    plt.show()
    return ani



def linear_fit(data):
    xdata = [i[0] for i in data]
    ydata = [i[1] for i in data]
    fitp = numpy.poly1d(numpy.polyfit(xdata, ydata, 1))
    ma = max(xdata)
    mi = min(xdata)
    xp = numpy.linspace(mi, ma, (ma - mi))
    plt.plot(xdata, ydata, '.', xp, fitp(xp), '-')
    plt.show()


import random as rnd

# 身長体重データ疑似生成用
def gen_hw_data():
    s = rnd.randint(0,1)
    h = int(rnd.gauss(155+s*18, 10))
    t = rnd.randint(0,1)
    wd = (h/100) ** 2 * (19+3*t)
    w = int(wd + rnd.betavariate(2,10) * 200 - 15)
    return (h,w)

# バネの延びデータ疑似生成用
def gen_spring_data():
    w = rnd.randint(0,200)
    l = int(2 * w * rnd.gauss(1, 0.1))
    return (w,l)
