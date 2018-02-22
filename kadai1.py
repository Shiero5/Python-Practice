# coding:utf-8
import arrayUtil
import plot
def draw_circle(image, y, x, r, color):
# (x,y)を中心とする半径rの円
    for i in range(y-r, y+r+1):
        for j in range(x-r, x+r+1):
            if (y-i)**2 + (x-j)**2 < r**2:
        # 中心からの距離がr以下なら
                image[i][j] = color
        return image

def parabolic_motion_w_draw(y, x, vy, vx):
    res = parabolic_motion(y, x, vy, vx)
# シミュレーション結果を取得
    images = arrayUtil.make1d(len(result))
# 画像の配列を準備
    for i in range(0, len(result)):
        im = arrayUtil.make2d(100,100)
        draw_circle(5,res[i][0],res[i][1],1,im)
# 指定された座標に半径5の円を描画
        images[i] = im
# 画像の配列に格納
    return images


images = parabolic_motion_w_draw(5,5,20,20)
plot.animation_show(images)
