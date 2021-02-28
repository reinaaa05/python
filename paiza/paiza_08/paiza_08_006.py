# coding: utf-8
# 文字列とリストのメソッドを使ってみよう

text = "pYthon"
print(text)
print(text.capitalize())
print(text.upper())

players = "勇者,戦士,魔法使い,忍者"
list = players.split(",")
print(list)
list.remove("忍者")
print(list)
list.append("霧島")
print(list)
