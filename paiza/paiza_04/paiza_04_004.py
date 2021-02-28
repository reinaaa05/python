# coding: utf-8
# リストの要素を操作する

team = ["勇者", "魔法使い"]
print(team)
print(team[0])
print(len(team))

team.append("戦士")
print(team)
print(len(team))

team[2] = "ドラゴン"
print(team)
print(len(team))

team.pop(2)
print(team)
print(len(team))
