# coding: utf-8
# Your code here!

print(1)
try:
    num = 0
    answer = 100 / num
    print(answer)
except ZeroDivisionError as e:
    print(e)
finally:
    print(2)

#例外エラー
Traceback (most recent call last):
  File "Main.py", line 6, in <module>
    answer = 100 / num
ZeroDivisionError: division by zero

(Exit status: 1)
