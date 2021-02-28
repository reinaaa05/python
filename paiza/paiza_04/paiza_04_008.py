# coding: utf-8
# リストを使ったランダムくじ
# スライム,モンスター,ドラゴン,魔王
import random
line = input().rstrip().split(",")
for enemy in line:
	print(enemy + "が現れた！")

num = len(line)
print ("敵は" + str(num) + "匹")
attack = random.randrange(num)


print(line[attack] + "に会心の一撃！" + line[attack] + "を倒した！")
