#サブジェネレーター

def sub_sub_generater():
    yield "Sub Subのyield"
    return "sub sub のreturn"

def sub_generater():
    yield "subのyield"
    res = yield from sub_sub_generater()
    print("sub res = {}".format(res))
    return "subのreturn"

def generator():
    yield "generatorのyield"
    res = yield from sub_generater()
    print('sub res = {}'.format(res))
    return "generatorのreturn"

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))