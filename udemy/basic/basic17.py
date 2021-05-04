#all, any
# if all((30 > 10, 10< 20, 'a' == 'a')):
#     print('allの中の処理')

# if any((False,False,True)):
#     print('anyの中の処理')

# if any((30 < 10, 10< 20, 'a' == 'b')):
#     print('anyの中の処理')

if not any((30 < 10, 10< 20, 'a' == 'b')):
    print('anyの中の処理')