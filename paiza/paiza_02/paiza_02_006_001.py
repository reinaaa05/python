# coding: utf-8
# 西暦を昭和年に変換
import random
seireki = random.randint(1926, 1988) #西暦年
print("西暦" + str(seireki) + "年は", end = "")

# 昭和年を計算
showa = seireki - 1925
# 昭和年を出力
print("昭和" + str(showa) + "年です")
