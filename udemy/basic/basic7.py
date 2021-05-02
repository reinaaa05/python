#文字列型

fruit = 'apple'
print(fruit)
print(type(fruit))
print(fruit * 10)
fruie_10 = fruit * 10
print(fruie_10)

new_fruit = fruit + 'banana'
print(new_fruit)

fruits = """apple
banana
grape
"""
print(fruits)

fruit = 'banana'
print(fruit[-1])

#encode,decode => bytes[]
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

#ccount

msg = 'ABCDABC'
print(msg.count('ABCD'))

#startswith, endwith

print(msg.startswith('ABCD'))
print(msg.startswith('ABCDE'))
print(msg.endswith('ABC'))
print(msg.endswith('CD'))

#strip, rstrip, lstrip

msg = ' ABC '
print(msg)
print(msg.strip())
print(msg.rstrip())
print(msg.lstrip())

msg = 'ABCDEFABC'
print(msg.strip('CBA'))
print(msg.rstrip('CBA'))
print(msg.lstrip('CBA'))

#upper,lower,awapcase,replace,captalize

msg = 'abcABC'
msg_u = msg.upper() #大文字
msg_l = msg.lower() #小文字
msg_s = msg.swapcase() #大文字と小文字の入れ替え
print(msg_u,msg_l,msg_s)

msg = 'ABCDABC'
msg_r = msg.replace('ABC', 'FFF',-1)
print(msg_r)

msg = 'hello WoRld'
print(msg.capitalize()) #頭だけ大文字

#文字列の一部取り出し、format, isloewr, isupper

msg = 'hello, my name is taro'
print(msg[:6])
print(msg[6:])
print(msg[1:10:3])
print('hello {}'.format('Taro'))
name = 'Jiro'
print(f'hello {name}')
print(f'{name=}') #3.8以上

msg = 'APPLE'
print(msg.islower())
print(msg.isupper())

#find, index, rfind,rindex

msg = 'ABCDEABC'
print(msg.find('ABC'))
print(msg.rfind('ABC'))
print(msg.index('ABC'))
print(msg.rindex('ABC'))

print(msg.find('ABCE')) #存在しないとき-1が表示
print(msg.index('ABCE')) #存在しないときerrorが表示
