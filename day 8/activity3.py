print("select your ride \n")
print("1. bike\n")
print("2. car \n")
choice=int(input("enter youur choice either 1 or 2"))
if choice == 1:
    print("what type of bike\n")
    print("1 electric bike\n")
    print("2 scooter\n")
    choice2= int(input("enter ur choice"))
    if choice2 == 1:
        print("you have selected a electric bike")
    else:
        print("you have selected a scooter")
elif choice == 2:
    print("what type of car\n")
    print("1 electric car\n")
    print("2. luxury car\n")
    choice3=int(input("enter your choice"))
    if choice3 == 1:
        print("you have a electric car")
    else:
        print("you have selected a luxury car")
else:
    print("wrong choice")


