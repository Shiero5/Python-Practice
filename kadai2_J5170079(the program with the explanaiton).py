# coding:utf-8
#NO:J5-170079 NAME:EGUCHI TAISHI（江口大志） FILE:kadai2.py CLASS:SCIENCE2-7
import matplotlib.pyplot as plt
import numpy as np

#色については以下でまとめておく
white = [1.0, 1.0, 1.0]
red = [1.0,0.388,0.388]
yellow = [0.976,0.749,0.294]
green = [0.267,0.890,0.494]
purple = [0.584,0.451,1.0]

def image_show(data):
    picture = plt.imshow(data,interpolation='nearest')
    #デフォルトの設定で滑らかに表示されるようになっていたのでピクセル型に表示されるようinterpolation='nearest'と指定
    # print(data)
    plt.show()
    return picture

def background_color(y,x):
    #x * y の行列作る（全てyellow）
    #各要素はRGBを指定
    base_list = [[yellow for i in range(x)] for j in range(y)]
    return base_list

y = 300
x = 173
bg_list = background_color(y, x)
bg_list2 = background_color(y, x)


#基本要素の生成
for i in range(y):
    for j in range(x):
        if (i > np.tan(np.pi/6.)* j and i < np.tan(np.pi/6.)* j + 200):
            bg_list[i][j] = red


for i in range(y):
    for j in range(x):
        if (i > (-1) * np.tan(np.pi/6.)* j + 100 and i < (-1) * np.tan(np.pi/6.)* j + 300):
            bg_list2[i][j] = purple



#配列の連結
bg_list3 = np.r_[bg_list, bg_list2]
bg_list4 = np.r_[bg_list2, bg_list]

bg_list5 = np.hstack([bg_list3, bg_list4])

image = []

cb_list_v = []

image = np.r_[bg_list5,bg_list5,bg_list5]

for i in range(5):
    cb_list_v.append(image)

image = np.hstack(cb_list_v)


image_show(image)


"""
参考文献

・色の指定
https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.imshow.html
・配列の連結
https://deepage.net/features/numpy-stack.html

"""
"""
以下プログラムに関する簡単な説明

最初に300(y) * 173(x)の背景が全て黄色の行列を用意して、
そのあと不等式で領域を指定して部分的に赤色と紫色に変えたbg_list、bg_list2を作る。

それぞれの不等式は、（この領域を赤色、紫色にする）
bg_list：y > np.tan(np.pi/6.)* x and y < np.tan(np.pi/6.)* x + 200
bg_list２：y > (-1) * np.tan(np.pi/6.)* x + 100 and y < (-1) * np.tan(np.pi/6.)* x + 300

bg_list、bg_list2で同じものを対角線上に配置して４つで構成された要素を作る。
その要素を繰り返して縦に３つ、横に５つ繋げたものが画像となる。
"""
