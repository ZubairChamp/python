import random
playing=True
number=str(random.randint(10,20))
print("i will generate a randim number frim 0 to 9 and you have to guess the number 1 digit at a time")
print("the game end when you get 1 correct answer")
while playing:
    guess=input("give me your best guess! \n")
    if number==guess:
        print("u win the game and the number was ",number)
        break
    else:
        print("ur guess is not quite right try again \n")