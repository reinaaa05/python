# coding: utf-8
# whileによるループ処理

import random
hp = 30# カウンタ変数を初期化
while hp >= 0:
    hit = random.randint(1,10)
    print("スライムに" +str(hit) + "のダメージを与えた！")# 繰り返し処理
    hp -= hit# カウンタ変数を更新
print("スライムをたおした")
