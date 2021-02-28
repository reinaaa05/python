# coding: utf-8
# if文による条件分岐
import random
number = random.randint(1, 5)
print("あなたの順位は" + str(number) + "位です")
if number == 1:
	print("おめでとう")
elif number == 2:
	print("あと少し")
else:
	print("よくがんばったね")
