# coding: utf-8
# Your code here!
import traceback,sys
print(1)
try:
    num = 0
    answer = 100 / num
    print(answer)
except ZeroDivisionError as e:
    print("0では割り算できません")
    #print(traceback.format_exc())
    sys.stderr.write(traceback.format_exc())
finally:
    print(2)
