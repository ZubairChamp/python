def cube(number):
    total=number*number*number
    print(total)
def cube2(number):
    if number%3==0:
       cube(number)
    else:
        print(False)
cube2(9)
cube2(4)