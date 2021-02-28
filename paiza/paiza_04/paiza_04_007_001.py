# coding: utf-8
# 読み込んだ複数行を出力する

import sys
for line in sys.stdin.readlines():
	msg = line.rstrip()
	print(msg + "が現れた")
