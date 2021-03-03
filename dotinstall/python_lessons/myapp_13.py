# msg = "hello" #グローバル変数

# def say_hi():
#   msg = "hi" #ローカル変数
#   print(msg)

# say_hi()
# print(msg)

# msg = "hello" #グローバル変数

# def say_hi():
#   print(msg)

# say_hi()
# print(msg)

msg = "hello" #グローバル変数

def say_hi():
  global msg
  msg = "hello global"
  print(msg)

say_hi()
print(msg)