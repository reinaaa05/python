# coding: utf-8
# Your code here!

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer2)
except ZeroDivisionError as e:
    print("0では割り算できません")
    print(e)
except NameError as e:
    print("未定義の変数を呼び出しています")
    print(e)
#スーパークラス ExceptionError
except Exception as e:
    print("予期せぬエラーが発生しました")
    print(e)
finally:
    print(2)
