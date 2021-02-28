# coding: utf-8
# Your code here!

# キーワード引数
def say_hello(greeting = "hello", target = "world"):
    print(greeting + " " + target)
say_hello()
say_hello("こんにちは", "皆さん")
say_hello("good morning!")
say_hello(greeting="こんにちは", target = "みなさん")
say_hello(target = "猫", greeting = "おはようございます。")
say_hello(target = "猫")
say_hello(greeting = "おはようございます")
