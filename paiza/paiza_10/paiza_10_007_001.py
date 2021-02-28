# coding: utf-8
# 呼び出し元へ例外を伝えよう

import sys
def calc():
    return 100 / 0

try:
    print(calc())
    raise(e)
except ZeroDivisionError as e:
    sys.stderr.write("0で割り算はできません")
