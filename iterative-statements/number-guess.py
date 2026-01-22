import random
number = random.randint(10,50)

ctr = 0
while ctr < 5 :
    guess = int(input("Guess a number between 10 and 50: "))
    if guess == number:
        print("you win!! :) ")
        break
    elif guess > number:
        print("too high")
    else:
        print("too low")
    ctr += 1
if not ctr < 5:    # or if not ctr < 5:
    print("you lose :( \n The number was)", number)        