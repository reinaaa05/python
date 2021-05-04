n = 0
while(n := n + 1) < 101:
    if n%3==0 and n%5==0:
        print('{}: Fizz Buss'.format(n))
    elif n%3==0:
        print('{}: Fizz'.format(n))
    elif n%5==0:
        print('{}:Buzz'.format(n))
    else:
        print(n)