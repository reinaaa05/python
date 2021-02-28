# 画像用辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# ここから下を記述しよう
num = int(input())
for i in range(num):
    line = input().rstrip()
    print("<img src='" + items_imges[line] + "'>")
