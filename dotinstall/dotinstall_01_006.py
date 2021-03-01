answer = 6

print("Your guessr? ", end="")
guess = int(input())

if answer == guess:
    print("Bingo!")
else:
    print("Boo...")