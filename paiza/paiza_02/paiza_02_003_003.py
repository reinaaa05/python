# coding: utf-8
import random
age = random.randint(15, 25)    # ageに、何才かを15~25の範囲でランダムに代入
print(str(age) + "才", end="")
if age >= 20:
    print("成人です")	# 条件が成り立ったときの処理
else:
    print("未成年です")	# それ以外だったときの処理
