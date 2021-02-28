# coding: utf-8
# 西暦年から平成年を求める
import datetime
seireki = datetime.date.today().year
print("西暦" + str(seireki) + "年は、",end="")

heisei = seireki - 1988
print("平成" + str(heisei) + "年です" )
