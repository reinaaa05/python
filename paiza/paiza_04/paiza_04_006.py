# coding: utf-8
# 取り込んだデータをリストに格納する

line = input().rstrip().split(",")
print(line)
print(len(line))

for enemy in line:
    print(enemy + "が現れた！")
