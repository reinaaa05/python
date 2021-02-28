# coding: utf-8
import random
age = random.randint(18, 22)    # ageに、何才かを18~22の範囲でランダムに代入
text = "飲酒可能"
if age < 20:
    # 条件が成り立ったときの処理
    print(str(age) + "才は飲酒不可")
else:
    # それ以外だったときの処理
    print(str(age) + "才は" + text)
