#変数の応用

animal = 'dog'
動物 = 'cat'
print(動物)

#定数

LEGAL_AGE = 20
age = 22

if age < LEGAL_AGE:  #ageが20よりも小さいとき処理を実行
    print('未成年')
else:
    print('成人')


#format文
print(f'age = {age}')
print(f'{age = }')