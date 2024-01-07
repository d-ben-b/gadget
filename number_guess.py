import random

flag = True
Guess = 0
Rand = random.randrange(-100, 100)

while flag:
    Guess = input("Guess a number:")
    if int(Guess) == Rand:
        print("Correct Answer!", end="\n")
        flag = False

    else:
        print("Wrong Answer", end="\n")
        if int(Guess) > Rand:
            print("too large", end="\n")
        else:
            print("too small", end="\n")
