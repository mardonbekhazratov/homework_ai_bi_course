from random import randint

while True:
    x = randint(1,100)
    for i in range(10):
        y = int(input())
        if y>x:
            print("Too high!")
        elif y<x:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
    else:
        print("You lost. Want to play again?")
        s = input()
        if s in ["Y","YES","y","yes","ok"]:
            continue
    break
