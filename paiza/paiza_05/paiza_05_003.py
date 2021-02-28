# coding: utf-8
# Your code here!

# 辞書の基本操作
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["ザコ"])
print(len(enemies))

enemies["ザコ2"] = "メタルモンスター"
print(enemies)
print(len(enemies))

enemies["中ボス"] = "レッドドラゴン"
print(enemies)
print(len(enemies))

del enemies["ザコ"]
print(enemies)
print(len(enemies))
