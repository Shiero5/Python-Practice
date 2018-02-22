# coding:utf-8
#NO:J5-170079 NAME:EGUCHI TAISHI（江口大志） FILE:kadai1.py CLASS:SCIENCE2-7
from pylab import *
import matplotlib.pyplot as plt

#軸を消す
plt.tick_params(labelbottom='off')
plt.tick_params(labelleft='off')



n = 501
X, Y = np.meshgrid(np.linspace(0, 1, n), np.linspace(0, 1, n))
Z = np.sin(X*30) + np.cos(Y*30)
print np.min(Z), np.max(Z)

cm = generate_cmap(['#00008B', '#aaaaab', '#FFFFFF', '#F4D793', '#F4A460'])

fig =plt.figure(figsize=(10,8))
im = plt.pcolor(X, Y, Z, cmap=cm)

fig.colorbar(im)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()


#以下参考文献
#http://www.tcom242242.site/entry/2017/08/21/190957
#http://web.sfc.keio.ac.jp/~yama/nos/?p=4091
