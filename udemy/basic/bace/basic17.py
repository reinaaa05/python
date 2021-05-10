#all, any
if all((30 > 10, 10< 20, 'a' == 'a')): #allは全てTrue
    print('allの中の処理')

if any((False,False,True)): #anyは1つでもTrue
    print('anyの中の処理')

if any((30 < 10, 10< 20, 'a' == 'b')):
    print('anyの中の処理')

if not any((30 < 10, 10< 20, 'a' == 'b')):
    print('anyの中の処理')