# coding: utf-8
# Your code here!

# 画像用ハッシュ
item_images = {
    "剣":"http://paiza.jp/learning/images/sword.png",
    "盾":"http://paiza.jp/learning/images/shield.png",
    "回復薬":"http://paiza.jp/learning/images/potion.png",
    "クリスタル":"http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順配列
items_orders = ["クリスタル", "盾", "剣", "回復薬", "回復薬", "回復薬"]

#print(item_images)
#print(items_order)

#アイテム名を取り出す
for item_name in items_orders:
#画像ファイルを取り出す
    print("<img src='" + item_images[item_name] +"'>")
    print(item_name)
