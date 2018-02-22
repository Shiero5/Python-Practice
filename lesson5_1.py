# coding:utf-8
import arrayUtil
import plot

def lg_rule(cur, neighbor):
# 1セルの挙動。0が空白、1が生命あり
# cur:現在の状況、neighbor: 隣接生命数
    if cur == 0:
    # 現在空白
        if neighbor == 3:
            return 1 # 誕生

        else:
            return 0
    else: # 現在生命有り
        if neighbor == 2 or neighbor == 3:
            return 1 # 生存
        else:
            return 0 # 過疎か過密で死滅

def count_neighbor(data,i,j):
    count = 0
    for k in range(i-1,i+2):
        for l in range(j-1, j+2):
            if 0 <= k < len(data) and 0 <= l < len(data[k]):
                 #lも適切な範囲にある
               count = count + data[k][l]
    final_count = count-data[i][j]
    return final_count
 #自分を引く


def lifegame_step(data): # ライフゲーム一世代分
    n = len(data)
    m = len(data[0])
    next = arrayUtil.make2d(n,m) #次世代のデータ
    for i in range(0,n):
        for j in range(0,m):
            c = count_neighbor(data,i,j)
            next[i][j] = lg_rule(data[i][j],c)
#各点でルールに従い次世代を計算
    return next


def lifegame(data,steps):
    results = arrayUtil.make1d(steps)
# アニメ用の画像の列を用意
    for i in range(0,steps):
        results[i] = data # 各ステップの結果を格納
        data = lifegame_step(data)
    return results

#動作確認

data = [[1,0,0,1,0,1],[0,0,0,0,0,0],[0,0,1,1,1,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,0,0]]

images = lifegame(data,20)
plot.animation_show(images)
