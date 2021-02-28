# coding: utf-8
# 西暦年と平成年の対応表を作る
# 1989年から2016年までをループで出力
# ループ内で、各西暦年を平成年に変換
for seireki in range(1989,2017):
    print("西暦" + str(seireki) + "年は、", end = "")
    heisei = seireki -1988
    print("平成" + str(heisei) + "年です。")
