# coding:utf-8
# NO:J5-170079 NAME:EGUCHI TAISHI（江口大志） FILE:kadai4_J5170079_Eguchi_Taishi.py CLASS:SCIENCE2-7
import arrayUtil
import bench
import random


def merge(a,b):
#整列済みの配列aとbを併合
    r = arrayUtil.make1d(len(a)+len(b)) #結果の格納先を用意
    ai = 0 #aは何番目まで処理したか?
    bi = 0 #bは何番目まで処理したか?
    for i in range(0, len(r)):
        if (bi >= len(b) or
            (ai < len(a) and a[ai] < b[bi])):
#aとbの先頭を比較(長さを超えないよう注意)
            r[i] = a[ai]
            ai = ai + 1
            # print("merge_a" + " : " + str(r))
        else:
            r[i] = b[bi]
            bi = bi + 1 #aとbの先頭の小さい方をrへ
            # print("merge_b" + " : " + str(r))
    return r

def mergesort(a): #配列aを整列
    n = len(a)
    if n <= 1: #短いときはそれでよし
        return a
    else:
        l = mergesort(a[0 : n//2])
        # print("l" + " : " + str(l))
        r = mergesort(a[n//2 : n])
        # print("r" + " : " + str(r))
#前半と後半をそれぞれ整列
        return merge(l,r)
#整列した結果を併合

def kadai4(a, k):
    n = len(a)
    if n <= 1:
        return a
    # elif n < k:
    #     print("第二引数は第一引数以下の値を取ってください")
    else:
        x = mergesort(a[0 : n//2])[0 : k-1]
        y = mergesort(a[n//2 : n])[0 : k-1]
        z = merge(x,y)
        return z[0 : k]


# ーーーーーーーーー動作確認用（コメントアウトしてあります）ーーーーーーーーー
#
# print("-- 動作確認 ーー")
#
# test_a = [7,1,2,43,10,12,13,4,5,6,12,42,765]
#
# print("kadai4 : " + str(kadai4(test_a,5)))
#
#
# ーーーーーーーーー実行時間計測用ーーーーーーーーー


def randomArray(n):
    # kadai4実行時間計測のためランダムな配列を生成する関数
    arr = arrayUtil.make1d(n)
    for i in range(0,n):
        arr[i] = random.random()
    return arr

def ss_test_a(n):
    return kadai4(randomArray(n),500)

def ss_test_k(k):
    return kadai4(randomArray(1000),k)

data = [1000,2000,4000,8000,10000]

result_a = bench.bench(ss_test_a,data)

result_k = bench.bench(ss_test_k,data)

bench.plot(result_a)
bench.plot(result_k)




''' プログラムについての説明・計算量についての議論
まず今回のプログラムでは授業で扱ったmerge、mergesort関数を用いて
長い配列を2つに分割し、それぞれの小さい方から順にk個抽出し、計2k個からk個抽出するのを分割統治法を利用して行う関数kadai4を定義した。
また計算量を可視化するために授業で用いたrandomArray、ss_test（授業で用いたss_testをss_test_aとしている）も使用した。

プログラムを実行すると計算量のグラフのみが出力されるように設定してあるが、
コメントアウトしてある動作確認の部分を再び有効化すればkadai4の関数を試せるようにした。
テスト用として配列test_a = [7,1,2,43,10,12,13,4,5,6,12,42,765]を用意したが他の配列でも成り立つことは
検証済みである。またkに当たる値はss_test_a内では100を初期値とした。

計算量についてだが今回の課題では併合整列法を用いており配列の長さをnとすると時間計算量はnlognとなるので単純整列法（n**2）よりも短くて済む
（グラフからもおおよそn**2よりはnlognよりになっているのがわかる）。
一方併合整列法は単純整列法よりもメモリを要するのでメモリが少ない時は単純整列法を用いるのが良い。
ss_test_a内のkに相当する値をいくつか設定してみてグラフを出力すると1000以下の範囲であればグラフの形は変わらないが、1000を超えた段階で
グラフが大きくゆがむのがわかる。そこでaを固定してkを変化させてグラフを書いてみた。そのための関数がss_test_kである。
初期値として生成する配列の長さを1000、kでdata配列を用いた。何度かresult_kのグラフを出力するとわかるが、計算量の範囲はおおよそ[0.030,0.040]であり、kと計算量に相関は取れない。
これはkの値よりもrandomArrayにより生成される配列の整列に要する計算量に起因すると考えられる。

'''
