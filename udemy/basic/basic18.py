#for

for i in range(10):
    print(i)

for _ in range(10):
    #print('A')
    pass

for i in range(2,20,3):
    print(i)

# sample = ['john','Paul','George','Rongo']
sample = ('john','Paul','George','Rongo')
for member in sample:
    print(member)

human = {
    'Name': 'Taro',
    'Age':20,
    'gender':'Man'
}

for h in human:
    print(h,human.get(h))