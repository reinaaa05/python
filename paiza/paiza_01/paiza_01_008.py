# coding: utf-8
#値段を計算する
apple_price = 350	#リンゴの単価
apple_num = 5	#リンゴを買う数
print("リンゴの単価" + str(apple_price) + "円")
print("リンゴを買う数" + str(apple_num) + "個")
total = apple_price * apple_num
print("合計金額:" + str(total) + "円")


import random
apple_price = random.randint(1,3) * 100	#リンゴの単価
apple_num = random.randint(1,10) #リンゴを買う数
print("リンゴの単価" + str(apple_price) + "円")
print("リンゴを買う数" + str(apple_num) + "個")
total = apple_price * apple_num
print("合計金額:" + str(total) + "円")
