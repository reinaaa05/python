# coding: utf-8
# 西暦年と昭和年の対応表
# 1926年から1988年までをループで出力
# ループ内で、各西暦年を昭和年に変換
for seireki in range(1926,1989):
    print("西暦" + str(seireki) + "年は",end="")
    showa = seireki - 1925
    print("昭和" + str(showa) + "年です")
