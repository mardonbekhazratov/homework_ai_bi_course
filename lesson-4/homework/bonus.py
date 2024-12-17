import random

a = ["rock","paper","scissors"]

x = 0
y = 0

while x < 5 and y < 5:
    c = random.choice(a)
    # print(c)
    p = input("choose one: rock, paper, scissors\n")
    if p not in a:
        print("wrong choice! try again!")
        continue
    if c == p:
        continue
    if (c=="rock" and p=="scissors") or (c=="paper" and p=="rock") or (c=="scissors" and p=="paper"):
        x += 1
    else:
        y += 1
    
if x>y:
    print(f"You lost with {x}:{y}")
else:
    print(f"You won with {y}:{x}")