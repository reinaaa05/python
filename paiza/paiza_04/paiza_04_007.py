# coding: utf-8
# 複数行データをリストに格納する

import sys
array = []
for line in sys.stdin.readlines():
    array.append(line.rstrip())
    #print(line.rstrip())
print(array)
