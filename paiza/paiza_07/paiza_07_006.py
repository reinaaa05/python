# coding: utf-8
# Your code here!

# 引数のデフォルト値
'''
def introduce(greeting, name = "村人"):
    print("私は" + name + "です。" + greeting)

introduce("こんにちは", "勇者")
introduce("こんにちは")
'''

'''
def introduce(greeting, *names):
    for name in names:
        print("私は" + name + "です。" + greeting)

introduce("こんにちは", "勇者", "村人", "兵士")
'''
def introduce(**people):
    for name,greeting in people.items():
        print("私は" + name + "です。" + greeting)

introduce(hero="初めまして", villager="こんにちは",soldier="よろしくお願いします")
