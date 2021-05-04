#if and or not

# msg = 'yellow'
# if msg == 'blue':
#     print('すすめ')
# elif msg == 'red':
#     print('止まれ')
# else:
#     print('それ以外の処理')

# age = 10
# if age < 20:
#     print('20未満')
# elif age <= 40:
#     print('20以上,40以下です')
# elif age >= 60:
#     print('60以上です')
# else:
#     print('それ以外の年齢')

#and or not
# gender = 'man'
# age = 10
# if gender == 'man' and age < 20:
#     print('未成年男性です')

gender = 'ma'
age = 30
if gender == 'man' or age < 20:
    print('男性もしくは20歳未満です')

if gender != 'man':
    print('男ではない')